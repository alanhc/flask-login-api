from flask import Flask, request
from flask import render_template
from flask import jsonify

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask import flash, redirect, url_for


import requests
import urllib3
import urllib.parse
import json
urllib3.disable_warnings()
"""example
curl -X POST --data "input=haha"  http://127.0.0.1:5000/post
curl -X POST -H "Content-Type: application/json" -d '{"username" : "", "password" : ""}' "http://127.0.0.1:5000/school_login"
"""

def login(username=None, password=None):
    payload = {
        "t_tea_no": username,
        "t_tea_pass": password
    }
    url = 'https://www.mcu.edu.tw/student/new-query/Chk_Pass_New_v1.asp'
    r = requests.post(url, data=payload, verify=False)
    r.encoding = 'big5'
    response = {
        "status":''
    }
    
    #print(data)
    try:
        data = {}
        for c in r.cookies:
            data[ c.name ] = urllib.parse.unquote(c.value)
        response['status'] = 'success'
        response['id'] = data['std%5Fno']
        response['name'] = data['std%5Fenm'].replace("+"," ")
        
    except:
        response['status'] = 'error'
    return response

app = Flask(__name__)
app.config['SECRET_KEY']="12345678"
Bootstrap(app)

@app.route("/school_login", methods=['POST'])
def school_login():
    re = request.get_json()
    

    response = login(username=re['username'], password=re['password'])
    
    return response
class NameForm(FlaskForm):
    id = StringField('學號',validators=[DataRequired()])
    password = PasswordField('密碼',validators=[DataRequired()])
    submit = SubmitField('submit')

@app.route("/", methods=['GET','POST'])
def index():
    form=NameForm()
    
    if form.submit.data:
        response = login(username=form.id.data, password=form.password.data)
        if response['status']=='error':
            flash("password error")
        else:
            return jsonify(response)

        
    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    #app.run()

"""
https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
"""