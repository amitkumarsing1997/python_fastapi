#FastapiProject:Fetch Book by rating
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
    print("58589")
    id:Optional[int]=3555
    # id:int
    # id:Optional[int]=None
    title:str =Field(min_length=3)
    author:str = Field(min_length=1)
    description:str=Field(min_length=1,max_length=100)
    rating:int=Field(gt=0,lt=6)
    ##this will show example at bottom in swagger ui as Example Value| Schema
    print("585846")

    class Config:
        #schema_extra={}
        ##but in pydantic2 use json_schema_extra={} not use schema_extra={} because it is part of pydantic version 1
        json_schema_extra={
            'example':{
                'title':'A new book',
                'author':'codingwithroby',
                'description':'A new description of a book',
                'rating':5
            }


        }







@app.get("/books")
async def read_all_books():
    return BOOKS

#71 FastapiProject:Fetch Book
@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id==book_id:
            return book

#72 FastapiProject:Fetch book by rating
@app.get("/books/")
async def read_book_by_rating(book_rating:int):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==book_rating:
            books_to_return.append(book)
    return books_to_return









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
    
    print("5858")
    
    new_book=Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Book):
    # if len(BOOKS)>0:
    #         book.id=BOOKS[-1].id+1
    # else:
    #      book.id=1
    # return book

    #another way is
    book.id=1 if len(BOOKS)==0 else BOOKS[-1].id+1
    return book





