from flask import Flask,jsonify, render_template, request,send_file, send_from_directory,session,redirect,url_for
from query import query_id,query_id2
import os


app = Flask(__name__)
port = int(os.getenv('PORT', 8080))


@app.route('/')
def index():
    r1=query_id('1')
    # r2=query_id('2')
    # r3=query_id('3')
    #print(r1,r2,r3)
    return render_template('index.html',data=r1)#,data2=r2,data3=r3)

@app.route('/id', methods=['GET'])
def id():
    r1=query_id2(request.args.get('id'))
    return render_template('index.html',data=r1)


if __name__ == '__main__':
    app.secret_key = 'mysecret' 
    app.run(host='0.0.0.0', port=port,debug=True)