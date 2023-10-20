from fastapi import FastAPI

app = FastAPI();

@app.get("/")
def index():
    return "Hello API"

@app.post("/users/")
def añadir_personas(id):
    return {"message": 2123}

@app.route('users', methods=['POST'])
def xdd():
    return "xd";