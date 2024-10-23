#bibliotecas
from flask import Flask, render_template

#iniciando
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


#rodar app
app.run()