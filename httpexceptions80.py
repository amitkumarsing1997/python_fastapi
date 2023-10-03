#FastAPI Project: http Exceptions

#FastApi Project: data validation with query parameter




# Assignment Problem
# Assignment

# Here is your opportunity to keep learning!

# Add a new field to Book and BookRequest called published_date: int (for example, published_date: int = 2012). So, this book as published on the year of 2012.

# Enhance each Book to now have a published_date

# Then create a new GET Request method to filter by published_date

# Solution in next video


#FastAPI Project:delete book with delete request

from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field
from typing import Optional
app=FastAPI()
class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int
    published_date: int

    def __init__(self,id,title,author,description,rating,published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date


BOOKS=[
    Book(1,'Computer Science Pro','codingwithroby','A very nice book!',5,2030),
    Book(2,'Be Fast with FastAPI','codingwithroby','A great book!',5,2030),
    Book(3,'Master Endpoints','codingwithroby','A awesome book!',5,2029),
    Book(4,'HP1','Author 1','Book Description',2,2028),
    Book(5,'HP2','Author 2','Book Description',3,2027),
    Book(6,'HP3','Author 3','Book Description',1,2026)

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
    published_date:int=Field(gt=1999,lt=2031)
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
                'rating':5,
                'published_date':2020
            }


        }







@app.get("/books")
async def read_all_books():
    return BOOKS


#78 query parameter data validation with query parameter
## by using Query(gt=0,lt=6)
#80 for httpexceptions
@app.get("/books/{book_id}")
async def read_book(book_id: int=Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book
    raise HTTPException(status_code=404,detail='Item not found')




@app.get("/books/rating/")
async def read_book_by_rating(book_rating:int= Query(gt=0,lt=6)):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==book_rating:
            books_to_return.append(book)
    return books_to_return



#75 FastapiProject:Fetch book by date

#78 query parameter data validation with query parameter
## by using Query(gt=1999,lt=2031)
@app.get("/books/")
async def read_book_by_published_date(book_date:int = Query(gt=1999,lt=2031)):
    books_to_return=[]
    for book in BOOKS:
        if book.published_date==book_date:
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




#75 FastAPI Project: Fields-Data Validation
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


#73 FastAPI Project:update book by put request
## but if we put new data than it did not show any error but it shows the 200 status code to handle it we add further logic like exception handling in next videos.

#80 httpExceptions
@app.put("/books/update_book")
async def update_book(book:BookRequest):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book.id:
            BOOKS[i]=book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404,detail='Item not found')


#80 httpExceptions
@app.delete("/books/{book_id}")
async def delete_book(book_id:int=Path(gt=0)):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            book_changed=True
            break
    if not book_changed:
        raise HTTPException(status_code=404,detail='the item which i want to deleted is not found')




