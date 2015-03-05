from flask import Flask, url_for, render_template_string, render_template
from flask.ext.admin import Admin
import sqlalchemy

app = Flask(__name__)
admin = Admin(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    