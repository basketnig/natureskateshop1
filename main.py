from flask import Flask, render_template

import db_methods

app = Flask(__name__)


app.secret_key = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/clothes")
def clothes():
    clothes = db_methods.Thing.get_all()
    return render_template("clothes.html",
                           clothes_list=clothes)


@app.route("/thing/<int:id>")
def thing(id):
    clothes = db_methods.Thing.get_by_id(id)
    return render_template("details.html",
                           thing=clothes)


if __name__ == "__main__":
    app.run(debug=True)
