from fastapi import FastAPI
import uvicorn
from api.routes import case_router,order_router,product_router

app = FastAPI()

app.include_router(case_router)
app.include_router(order_router)
app.include_router(product_router)




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)