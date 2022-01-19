from flask import Flask, render_template, redirect, request, session
import os
from web import *

app = Flask(__name__)
app.secret_key = os.urandom(69).hex()

#основа
@app.route("/")
def hello_world():
    res = ["login, role"]
    return render_template("index.html", res=res)


@app.route('/')
def index():
    if session.get('user') == None:
        return redirect('/reg')
    return redirect('/lk')

#регистрация
@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if session.get('user') == None:
        if request.method == "POST":
            acc = request.form.get('acc')
            key = request.form.get('key')
            login = request.form.get('login')
            password = request.form.get('passw')
            fio = [request.form.get('f'), request.form.get('i'), request.form.get('o')]
            res = registr( acc, key, login, password, fio)
            if type(res) == str: 
                return f"error: {res}"
            session['account'] = acc
            return redirect('/auth')
        else:
            return render_template('reg.html')
    else:
        return redirect('/lk')

#авторизация
@app.route('/auth', methods=['POST', 'GET'])
def authg():
    if session.get('user') == None:
        if request.method == "POST":
            acc = request.form.get('acc')
            login = request.form.get('login')
            password = request.form.get('passw')
            res = auth(acc, login, password)
            if type(res) == str: 
                return f"error: {res}"
            session['user'] = res
            return redirect('/lk')
        else:
            return render_template('auth.html')
    else:
        return redirect('/')

#личный кабинет
@app.route('/lk')
def lk():
    if session.get('user') != None:
        return render_template('lk.html', res=session.get('user'))
    return redirect('/')    


if __name__ == "__main__":
    app.run(debug=True)


