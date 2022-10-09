from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template('/home.html')

@app.route("/Contato")
def Contato():
    return render_template('/Contato.html')

@app.route("/Quem_Somos")
def Quem_Somos():
    return render_template('/Quem_Somos.html')
    