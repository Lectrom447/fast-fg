from fastapi import FastAPI



app =  FastAPI()

@app.get('/')
async def home():
    return "Hola Mundo"


@app.get('/rt2')
async def home_2():
    return "Hola Mundo2"