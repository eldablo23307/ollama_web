import flask
from markupsafe import escape

app =  flask.Flask("__init__")

@app.route("/")
def home_page():
    return flask.render_template("home.html.jinja")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
