from flask import Flask, render_template, request, escape

app = Flask(__name__)


@app.route("/")
def login():
    return render_template('login.html', the_title = "LOGIN")




@app.route("/admin", methods=["GET", "POST"])
def admin():
    return render_template("admin.html")

@app.route("/quizzee", methods=["GET", "POST"])
def quizzee():
    return render_template("quizzee.html")


if __name__ == "__main__":
    app.run()
