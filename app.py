from flask import Flask
from flask_wtf.csrf import CSRFProject

app = Flask(__name__)

csrf = CSRFProject(app)

@app.route("/")
def pagina_inicial():
    return "Laboratório PipeLine DevOps"

if __name__ == '__main__':
    app.run(debug=True)
