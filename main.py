import flask
from markupsafe import escape

app =  flask.Flask("__init__")

@app.route("/")
def home_page():
    return flask.render_template("chosse_mode.html.jinjia")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
