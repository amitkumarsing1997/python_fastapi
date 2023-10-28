from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
# from fastapi import FastAPI,Depends, HTTPException,Path
from fastapi import APIRouter,Depends, HTTPException,Path
import models
from models import Todos
# from database import engine,SessionLocal
from database import SessionLocal
# from routers import auth
import starlette.status as status
from .auth import get_current_user

# app=FastAPI()
router=APIRouter()

# models.Base.metadata.create_all(bind=engine)

# app.include_router(auth.router)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency=Annotated[Session,Depends(get_db)]

user_dependency=Annotated[dict,Depends(get_current_user)]

## for video 94
class TodoRequest(BaseModel):
    title:str=Field(min_length=3)
    description:str=Field(min_length=3,max_length=100)
    priority:int=Field(gt=0,lt=6)
    complete:bool



# video 92   get all todos from database
# @app.get("/",status_code=starlette.status.HTTP_200_OK)
# async def read_all(db: db_dependency):
#     return db.query(Todos).all()

@router.get("/",status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency,db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed') 
    return db.query(Todos).filter(Todos.owner_id==user.get('id')).all()

# video 93 get todo by id

# @app.get("/todo/{todo_id}",status_code=starlette.status.HTTP_200_OK)
# async def read_todo(db: db_dependency,todo_id:int=Path(gt=0)):
#     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
#     if todo_model is not None:
#         return todo_model
#     raise HTTPException(status_code=404,detail='Todo not found.')


@router.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(user:user_dependency,db: db_dependency,todo_id:int=Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model=db.query(Todos).filter(Todos.id==todo_id)\
        .filter(Todos.owner_id==user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail='Todo not found.')


#video 94 post request 

# @app.post("/todo",status_code=starlette.status.HTTP_201_CREATED)
# async def create_todo(db:db_dependency,todo_request:TodoRequest):
#     todo_model=Todos(**todo_request.model_dump())
#     db.add(todo_model)
#     db.commit()

@router.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(user:user_dependency,db:db_dependency,
                      todo_request:TodoRequest):
    
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model=Todos(**todo_request.model_dump(),owner_id=user.get('id'))
    db.add(todo_model)
    db.commit()


#video 95 put request 
# @app.put("/todo/{todo_id}",status_code=starlette.status.HTTP_204_NO_CONTENT)
# async def update_todo(db:db_dependency,
#                       todo_request:TodoRequest,
#                       todo_id:int=Path(gt=0)):
#     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404,detail='Todo not found.')
    
#     todo_model.title=todo_request.title
#     todo_model.description=todo_request.description
#     todo_model.priority=todo_request.priority
#     todo_model.complete=todo_request.complete
    
#     db.add(todo_model)
#     db.commit()


@router.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user:user_dependency,
                      db:db_dependency,
                      todo_request:TodoRequest,
                      todo_id:int=Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model=db.query(Todos).filter(Todos.id==todo_id)\
        .filter(Todos.owner_id==user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found.')
    
    todo_model.title=todo_request.title
    todo_model.description=todo_request.description
    todo_model.priority=todo_request.priority
    todo_model.complete=todo_request.complete
    
    db.add(todo_model)
    db.commit()


#video 96 delete request
# @app.delete("/todo/{todo_id}",status_code=starlette.status.HTTP_204_NO_CONTENT)
# async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
#     todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404,detail='Todo not foound.')
#     db.query(Todos).filter(Todos.id==todo_id).delete()
#     db.commit()


@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user:user_dependency,db:db_dependency,todo_id:int=Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model=db.query(Todos).filter(Todos.id==todo_id).\
    filter(Todos.owner_id==user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not foound.')
    db.query(Todos).filter(Todos.id==todo_id).filter(Todos.owner_id==user.get('id')).delete()
    db.commit()



    

1


