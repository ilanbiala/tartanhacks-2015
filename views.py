from flask import *
import psycopg2
from server import *
import base64
import sys
app = Flask(__name__)

conn = psycopg2.connect(dbname = 'postgres', user = 'postgres', host = 'localhost', password='postgres')
sql = conn.cursor()
# sql.execute("CREATE TABLE andrewUsers(id VARCHAR(20) PRIMARY KEY, password VARCHAR(20))")
# conn.commit()

@app.route('/index', methods=['get','post'])
def index():
	return render_template('index.html')

@app.route('/login', methods = ['get','post'])
def login():
	if request.method == 'POST':
		user_id = (request.form['username'])
		user_pw = (request.form['password'])
		query = "SELECT * FROM andrewUsers where id = '%s'" % user_id
		sql.execute(query)
		user = sql.fetchall()
		encrypted_pw = user[0][1]
		decrypted_pw = (base64.b64decode(encrypted_pw).decode('utf8'))
		if user_pw == decrypted_pw:
			print("Correct Password", file=sys.stderr)
			#Aggregate_data()
			return render_template('index.html')

	return render_template('login.html')

@app.route('/register', methods = ['get','post'])
def register():
	if request.method == 'POST':
		user_id = (request.form['username'])
		user_pw = (request.form['password'])
		user_pw_re = (request.form['password_re'])

		if(user_pw == user_pw_re):
			encrypted_pw = base64.b64encode(bytes(user_pw, 'utf8')).decode('utf8')
			#print("Password Matching %s" %encrypted_pw, type(encrypted_pw), file=sys.stderr)
			query = "INSERT INTO andrewUsers (id, password) VALUES (%s,%s)"
			data  = (user_id, encrypted_pw)
			sql.execute(query,data)
			conn.commit()
			return render_template('login.html')

		else:
			return render_template('register.html', password_match = 'false')

	return render_template('register.html', password_match = 'null')


if __name__ == '__main__':
	app.debug = True
	app.run()