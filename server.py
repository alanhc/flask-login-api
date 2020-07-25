from flask import Flask, request
from flask import render_template
from flask import jsonify
import requests
import urllib3
import urllib.parse
import json
urllib3.disable_warnings()

"""example
curl -X POST --data "input=haha"  http://127.0.0.1:5000/post
curl -X POST -H "Content-Type: application/json" -d '{"username" : "", "password" : ""}' "http://127.0.0.1:5000/school_login"
"""
app = Flask(__name__)

@app.route("/school_login", methods=['POST'])
def post_json():
    re = request.get_json()
    payload = {
        "t_tea_no":re['username'],
        "t_tea_pass": re['password']
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


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=6001)
    #app.run()

