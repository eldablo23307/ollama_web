import ollama

def choose_model(auto_choosen, requested_model=""):
    modell = ollama.list()
    
    if len(modell["models"]) == 0:
        return "Unable to pull any model: Error 401"
    elif auto_choosen == "on":
        return modell["models"][0]["model"]
    else:
        for i in range(len(modell)):
            if modell["models"][i]["model"] == requested_model:
                return requested_model
    return "Choosen Model not Available: Error 402"

def chat(input: str, model="", auto_choosen="off"):
    model_choosen = choose_model(requested_model=model, auto_choosen=auto_choosen)
    try:
        result = ollama.generate(model=model_choosen, prompt=input)
        return result["response"]
    except:
        raise Exception(model_choosen)
