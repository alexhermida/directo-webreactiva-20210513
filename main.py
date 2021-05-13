from fastapi import FastAPI
import uvicorn
import malandriners


app = FastAPI()


@app.get("/")
def hello():
    return "Hello Malandriners"


@app.get("/happiest")
def happiest_endpoint():
    return malandriners.happiest()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")
