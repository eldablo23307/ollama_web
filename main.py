import flask
import model_chat
from flask import request

app =  flask.Flask("__init__")
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
    else:
        return "Only POST method allow"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

