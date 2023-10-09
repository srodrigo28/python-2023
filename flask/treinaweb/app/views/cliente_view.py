from app import app

@app.route('/')
def home():
    return "Olá mundo em Flask"