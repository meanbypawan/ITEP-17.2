from fastapi import FastAPI, Body,Request
from data import product_list

app = FastAPI()

# @app.post("/product")
# async def create_product(request:Request):
#     data = await request.json()
#     data["id"] = len(product_list)+1
#     product_list.append(data)
#     return {"message":"Product created successfully","product":data}

@app.get("/product/{product_id}")
async def get_product_by_id(product_id:int):
    product = filter(lambda product: product.id == id,product_list)
    return product

@app.post("/product")
async def create_product(title:str=Body(...),
                         price:int=Body(...),
                         brand:str=Body(...)):
    id = len(product_list)+1
    product = {"id":id,"title":title,"price":price,"brand":brand}
    product_list.append(product)
    return product


@app.get("/product")
async def get_product():
    return product_list

@app.get("/")
async def welcome():
    return {"message": "Welcome to FastAPI!"}

@app.get("/home")
async def home():
    return {"message": "It is home page"}

@app.get("/about")
async def about():
    return {"message":"It is about page"}
