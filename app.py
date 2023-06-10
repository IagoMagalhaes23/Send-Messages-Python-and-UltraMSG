<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template
import json
import http.client
import ssl 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def sendMsg():
    telefone = request.form.get('telefone')
    mensagem = request.form.get('mensagem')

    print(telefone)
    print(mensagem)
    conn = http.client.HTTPSConnection("api.ultramsg.com",context = ssl._create_unverified_context())

    payload = "token={{seu token}&to={}&body={}".format(telefone,mensagem)
    print(payload)
    payload = payload.encode('utf8').decode('iso-8859-1') 

    headers = { 'content-type': "application/x-www-form-urlencoded" }

    conn.request("POST", "/{{sua intância}}/messages/chat", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    return render_template('sucess.html', telefone=telefone)

if(__name__) == '__main__':
=======
from flask import Flask, request, jsonify, render_template
import json
import http.client
import ssl 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def sendMsg():
    telefone = request.form.get('telefone')
    mensagem = request.form.get('mensagem')

    print(telefone)
    print(mensagem)
    conn = http.client.HTTPSConnection("api.ultramsg.com",context = ssl._create_unverified_context())

    payload = "token=mujx72m834xk5c35&to={}&body={}".format(telefone,mensagem)
    print(payload)
    payload = payload.encode('utf8').decode('iso-8859-1') 

    headers = { 'content-type': "application/x-www-form-urlencoded" }

    conn.request("POST", "/instance50300/messages/chat", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    return render_template('sucess.html', telefone=telefone)

if(__name__) == '__main__':
>>>>>>> f10dae69cb1f73ecbfb99fc3eb63b81861e3721f
    app.run()