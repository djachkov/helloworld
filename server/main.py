from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("about")
async def about():
    return {"name": "Dmitrii"}

@app.get("blog")
async def blog():
    return {}