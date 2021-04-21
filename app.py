import os
from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route('/')
def index():
    contenido = os.listdir('templates')
    contenido.remove("index.html")
    contenido.remove("layout.html")
    return render_template("index.html", paginas = contenido)

@app.route('/<string:file>')
def getFile(file):

    if file == "index.html":
        return redirect("/")
    return render_template(file);   