from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', title="Home Page")

@app.route('/galeria')
def getGalery():
    listaObrazkow = [
        "https://whatnext.pl/wp-content/uploads/2015/11/1507494017271166356.jpg",
        "https://i.wpimg.pl/730x0/m.gadzetomania.pl/miecz-14c6db073794e671ea51daed97.jpg",



    ]
    return render_template('galeria.html', listaObrazkow=listaObrazkow, title="Galeria")

