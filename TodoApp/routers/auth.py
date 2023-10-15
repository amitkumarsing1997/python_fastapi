# from fastapi import FastAPI,APIRouter

# app=FastAPI()




from fastapi import APIRouter

router=APIRouter()

@router.get("/auth/")
async def get_user():
    return {'user':'authenticated'}


