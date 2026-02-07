import flask
from flask import request

from . import model_chat

app = flask.Flask(__name__)
current_chat = ""

@app.route("/")
def home_page():
    return flask.render_template("home.html.jinja", current_chat=current_chat)

@app.route("/input", methods=["GET", "POST"])
def chat_return():
    if request.method == "POST":
        input_data = request.form.get("chat_input")
        input_model = request.form.get("model_name")
        auto_choose = request.form.get("auto_choose", "off")
        global current_chat
        current_chat = model_chat.chat(input_data, input_model, auto_choose)
        return "<script>window.location.href ='/'</script>"
    return "Only POST method allow"
