from flask import *
import psycopg2
from server import *
from courses import *
import freetime
import base64
import sys
import urllib.parse
app = Flask(__name__)

my_id= 'ildook'
my_pw= 'Jin03002!'
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

#sql.execute("CREATE TABLE andrewUsers(id VARCHAR(20) PRIMARY KEY, firstname VARCHAR(20), lastname VARCHAR(20), fullname VARCHAR(41), password VARCHAR(20), classes VARCHAR(100000))")
#conn.commit()

@app.route('/calendar', methods=['get','post'])
def calendar():
	if request.method == 'POST':
		user_id = (request.form['username'])
		user_pw = (request.form['password'])
		query = "SELECT * FROM andrewUsers where id = '%s'" % user_id
		sql.execute(query)
		user = sql.fetchall()
		encrypted_pw = user[0][4]
		decrypted_pw = (base64.b64decode(encrypted_pw).decode('utf8'))
		if user_pw == decrypted_pw:
			#print("Correct Password", file=sys.stderr)
			query = "SELECT * FROM andrewUsers"
			sql.execute(query)
			users_all = sql.fetchall()
			
			user_dict={}
			for cuser in users_all:
				user_dict[cuser[3]]=cuser[5]

			free_time=freetime(user_dict, user[0][5])

			return render_template('calendar.html', freetime=free_time)
			
		else:
			return render_template('index.html', password_match = 'false')

	return render_template('calendar.html')

@app.route('/', methods = ['get','post'])
def index():
	if request.method == 'POST':
		user_id = (request.form['username'])
		user_pw = (request.form['password'])
		user_pw_re = (request.form['password_re'])
		if(user_pw == user_pw_re):
			courses = get_courses(my_id, my_pw)
			print(courses, file=sys.stderr)
			if(courses!=None):
				encrypted_pw = base64.b64encode(bytes(user_pw, 'utf8')).decode('utf8')
				#print("Password Matching %s" %encrypted_pw, type(encrypted_pw), file=sys.stderr)
				query = "INSERT INTO andrewUsers (id, password, classes) VALUES (%s,%s,%s)"
				data  = (user_id, encrypted_pw, courses)
				sql.execute(query,data)
				conn.commit()
				return render_template('index.html', password_match = 'true')

		return render_template('index.html', password_match = 'false')

	return render_template('index.html')


if __name__ == '__main__':
	app.debug = True
	app.run()