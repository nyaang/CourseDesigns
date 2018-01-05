from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/login',methods=['GET'])
def login_form():
    return render_template('form.html')

@app.route('/login',methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='密码错误',username=username)
if __name__ == '__main__':
    app.run()
