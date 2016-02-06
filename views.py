from flask import *
from server import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['get','post'])
def register():
    if request.method=='POST':
    	user_id=(request.form['username'])
    	user_pw=(request.form['password'])
    	user_pw_re=(request.form['password_re'])
    	do_something_with_register()
    	
    return render_template('register.html')

if __name__=='__main__':
	app.debug = True
	app.run()