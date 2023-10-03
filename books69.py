from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional
app=FastAPI()
class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating


BOOKS=[
    Book(1,'Computer Science Pro','codingwithroby','A very nice book!',5),
    Book(2,'Be Fast with FastAPI','codingwithroby','A great book!',5),
    Book(3,'Master Endpoints','codingwithroby','A awesome book!',5),
    Book(4,'HP1','Author 1','Book Description',2),
    Book(5,'HP2','Author 2','Book Description',3),
    Book(6,'HP3','Author 3','Book Description',1)

]

class BookRequest(BaseModel):
    id:Optional[int]=None
    # id:int
    # id:Optional[int]=Field(title='id is not needed') ## this create error
    title:str =Field(min_length=3)
    author:str = Field(min_length=1)
    description:str=Field(min_length=1,max_length=100)
    rating:int=Field(gt=0,lt=6)
  



@app.get("/books")
async def read_all_books():
    return BOOKS



#66 FastAPI Project:Post Request before Validation
# @app.post("/create-book")
# async def create_book(book_request=Body()):
#     BOOKS.append(book_request)




# 67 FastAPI Project: Pydantics and Data Validation
# @app.post("/create-book")
# async def create_book(book_request:BookRequest):
#     print(type(book_request))
#     BOOKS.append(book_request)




#69 FastAPI Project: Fields-Data Validation
@app.post("/create-book")
async def create_book(book_request: BookRequest):
    # new_book=Book(**book_request.dict())
    ### Book(**book_request.dict())=converting the request to Book object
    ## but as of right now,Fast API supports two versions of pedantic version one and version two
    ### so here i face some error due to version two 
    ### so i use modern thing which is 
    ### Book(**book_request.model_dump()) in place of (**book_request.dict())
    new_book=Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))


## method to autoincrement id
def find_book_id(book:Book):
    # if len(BOOKS)>0:
    #         book.id=BOOKS[-1].id+1
    # else:
    #      book.id=1
    # return book

    #another way is
    book.id=1 if len(BOOKS)==0 else BOOKS[-1].id+1
    return book




