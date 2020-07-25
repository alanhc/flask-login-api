from flask import Flask, request
from flask import render_template
from flask import jsonify
import requests
import urllib3
import urllib.parse
urllib3.disable_warnings()

"""example
curl -X POST --data "input=haha"  http://127.0.0.1:5000/post
curl -X POST -H "Content-Type: application/json" -d '{"username" : "", "password" : ""}' "http://127.0.0.1:5000/school_login"
"""
app = Flask(__name__)





@app.route("/school_login", methods=['POST'])
def post_json():
    data = request.get_json()
    payload = {
        "t_tea_no":data['username'],
        "t_tea_pass": data['password']
    }
    
    url = 'https://www.mcu.edu.tw/student/new-query/Chk_Pass_New_v1.asp'
    r = requests.post(url, data=payload, verify=False)
    r.encoding = 'big5'
    msg = ""
    try:
        name = r.cookies['std%5Fno']
        name = urllib.parse.unquote(name)
        msg = name
    except:
        msg = 'password error'
    return msg


if __name__ == '__main__':
    app.debug = True
    app.run()

