from flask import render_template
from tartanhacks import tartanhacks

@tartanhacks.route('/')
def index():
    return render_template('index.html')
