from fastapi import FastAPI
import uvicorn


from api.routes import case_router


app = FastAPI()


@app.get('/healthcheck')
async def healthcheck():
    return "Hello, world"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
