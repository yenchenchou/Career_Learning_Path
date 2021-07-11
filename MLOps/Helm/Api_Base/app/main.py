from fastapi import FastAPI
# import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World YC"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=6008)
