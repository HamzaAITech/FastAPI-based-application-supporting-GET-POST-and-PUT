from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI(title="Built FastAPI")


@app.get("/") #parth ope deco
def hey_golbe():
    return {"message": "Hiii"}

@app.get("/Hello/{name}")
def Hello_name(name: str):
    return {"message": f"Hello {name}"}

class Todo(BaseModel):  #Type we acpt
    title:str
    completed:bool = False
    #to use store it
    
    
todos =[]


@app.get("/todos") #path
def get_todos():
    return todos #not use pot methord
 


@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"meassage": "t Created","todo":todo}

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):
        return {"message":"not found"}
    return todos [todo_id]


@app.put("/todos/{todo_id}")
def updated_todo(todo_id:int,todo: Todo):
    if todo_id<0 or todo_id >=len(todos):
        return {"meassge":"not found"}
    todos [todo_id]=todo
    return {"message": "Todo Updated", "todo": todo}







if __name__== "__main__":
    uvicorn.run("fapi:app", host="0.0.0.0", port=8000, reload=True)