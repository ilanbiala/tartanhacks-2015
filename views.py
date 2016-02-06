from flask import *
import psycopg2
from server import *
from courses import *
from freetime import *
from sameclasses import *
import base64
import sys
import urllib.parse
app = Flask(__name__)
app.jinja_env.autoescape = False
urllib.parse.uses_netloc.append("postgres")
url = urllib.parse.urlparse('postgres://zqirlutztjyaov:ceb3bv_TL8S_9KjggKchociRsN@ec2-54-225-199-245.compute-1.amazonaws.com:5432/d7193dajm703tu')

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
sql = conn.cursor()
# sql.execute("CREATE TABLE andrewUsers(id VARCHAR(20) PRIMARY KEY, firstname VARCHAR(20), lastname VARCHAR(20), fullname VARCHAR(41), password VARCHAR(20), classes VARCHAR(100000))")
# conn.commit()

@app.route('/calendar', methods=['get','post'])
def calendar():
	if request.method == 'POST':
		user_id = (request.form['username'])
		user_pw = (request.form['password'])
		query = "SELECT * FROM andrewUsers where id = '%s'" % user_id
		sql.execute(query)
		user = sql.fetchall()

		if(not user):
			courses = get_courses(user_id, user_pw)

			encrypted_pw = base64.b64encode(bytes(user_pw, 'utf8')).decode('utf8')
			#print("Password Matching %s" %encrypted_pw, type(encrypted_pw), file=sys.stderr)
			query = "INSERT INTO andrewUsers (id,  firstname, lastname, fullname, password, classes) VALUES (%s,%s,%s,%s,%s,%s)"
			first = courses['user']['first_name']
			last = courses['user']['last_name']
			full = '{} {}'.format(first,last)
			data  = (user_id, first, last, full, encrypted_pw, str(courses['schedule']))
			sql.execute(query,data)
			conn.commit()
			query = "SELECT * FROM andrewUsers where id = '%s'" % user_id
			sql.execute(query)
			user = sql.fetchall()

		print(user, file=sys.stderr)
		stored_pw = user[0][4]
		encrypted_pw = base64.b64encode(bytes(user_pw, 'utf8')).decode('utf8')
		
		if stored_pw == encrypted_pw:
			#print("Correct Password", file=sys.stderr)

			query = "SELECT * FROM andrewUsers" 
			sql.execute(query)
			userlist = sql.fetchall()

			users_dict = {}
			for i in userlist:
				if i[0]!=user_id:
					users_dict[i[0]]=i[5]

			free_time=freetime(users_dict, user[0][5])

			same_classes=sameclasses(users_dict, user[0][5])

			query="UPDATE andrewUsers SET classes=%s WHERE id=%s"
			data=(str(same_classes),user_id)
			sql.execute(query,data)
			conn.commit()

			#print(user[0][5],file=sys.stderr)

			return render_template('calendar.html', freeSchedule = free_time, userInfo = user[0][5])
		else:
			return render_template('index.html', password_match = 'false')

	return render_template('calendar.html')

@app.route('/', methods = ['get','post'])
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.debug = True
	app.run()