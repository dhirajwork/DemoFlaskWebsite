from flask import Flask,jsonify, render_template, request,send_file, send_from_directory,session,redirect,url_for
import os
app = Flask(__name__)
port = int(os.getenv('PORT', 8080))


@app.route('/')
def index():
    r1=[{'degree':'12','university':'WB','percentage':'82'},{'degree':'10','university':'WB','percentage':'85'}]
    return render_template('index.html',data=r1)#,data2=r2,data3=r3)


if __name__ == '__main__':
    app.secret_key = 'mysecret' 
    app.run(host='0.0.0.0', port=port,debug=True)