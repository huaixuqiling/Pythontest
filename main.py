from fastapi import FastAPI

#创建fastapi实例
app = FastAPI()

#定义路由 async异步

@app.get("/")
async def root():
    return {"message": "Hello World"}

#定义路由，接收参数

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
