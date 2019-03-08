from flask import Flask,request,render_template
from mysqlconnetctor import showtickets,jugelogin,signup,addorder,showorders,tuipiao_order
import json
app = Flask(__name__)
@app.route('/')
def hello_world():
    tickets=showtickets()
    return render_template('home.html', tickets=tickets)
@app.route('/login',methods=['GET'])
def login_form():
    return render_template('form.html')
@app.route('/register',methods=['GET'])
def register_form():
    return render_template('form.html')

@app.route('/login',methods=['POST'])
def login():
    username=request.form['usernamelogin']
    password=request.form['passwordlogin']
    if jugelogin(username,password)==True:
        tickets = showtickets()
        return render_template('signin-ok.html',username=username,tickets=tickets)
    return render_template('form.html',loginmessage='密码错误',loginusername=username)

@app.route('/register',methods=['POST'])
def register():
    username=request.form['usernameregister']
    password=request.form['passwordregister']
    if signup(username,password)==True:
        return render_template('form.html',registermessage='注册成功')
    elif signup(username,password)=='keyerror':
        return render_template('form.html',registermessage='该用户名已被注册，请换一个用户名',registerusername=username,registerpassword=password)
    elif signup(username,password)=='nameerror':
        return render_template('form.html', registermessage='用户名过长，请输入不超过10个字符',registerusername=username,registerpassword=password)
    elif signup(username,password)=='passerror':
        return render_template('form.html', registermessage='密码过长，请输入不超过20个字符',registerusername=username,registerpassword=password)
    else:
        return render_template('form.html', registermessage='未知错误')

@app.route('/orderticket',methods=['POST'])
def orderticket():
    order_info=json.loads(request.form['ticket'])
    ticket_num=order_info[0]
    username=order_info[1]
    orderid=addorder(ticket_num,username)
    tickets = showtickets()
    return render_template('signin-ok.html', orderid=orderid,tickets=tickets,username=username)

@app.route('/myorder',methods=['GET'])
def myorderlogin():
    return render_template('myorder.html')

@app.route('/myorder',methods=['POST'])
def getmyorder():
    username=request.form['usernamelogin']
    password=request.form['passwordlogin']
    if jugelogin(username,password)==True:
        orders=showorders(username)
        return render_template('myorder.html', showorder=True,loginusername=username,orders=orders)
    return render_template('myorder.html' ,loginmessage='密码错误',loginusername=username)

@app.route('/tuipiao',methods=['POST'])
def tuipiao():
    order_info=json.loads(request.form['order'])
    orderid=order_info[0]
    username=order_info[1]
    tuipiao_order(orderid)
    orders = showorders(username)
    return render_template('myorder.html',showorder=True, loginusername=username,orders=orders,orderid=orderid)
@app.errorhandler(400)
def Bad_Request(e):
    return render_template('404.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html')
@app.errorhandler(405)
def Method_Not_Allowed(e):
    return render_template('404.html')
if __name__ == '__main__':
    app.run()