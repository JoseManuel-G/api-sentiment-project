from flask import Flask, request
import markdown.extensions.fenced_code
import random
import json
import getdata as get
import postdata as pos

app = Flask(__name__)



@app.route("/")
def index():
    readme_file = open("README.md","r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string







@app.route("/mensajes/")
def mensajes():
    return json.dumps(get.mensajes())







@app.route("/frases/<personaje>")
def frase_person(personaje):
    frases = get.mensaje_person(personaje)
    return json.dumps(frases)







@app.route("/nuevafrase/", methods=["POST"])
def insertamensaje():
    name_episode = request.form.get("episode name")
    name = request.form.get("name")
    frase = request.form.get("line")
    pos.insertamensaje(name_episode,name,frase)
    return "Mensaje introducido correctamente en la base de datos" 












app.run(debug=False)