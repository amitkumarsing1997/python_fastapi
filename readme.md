pip install -r requirements.txt

to run program
uvicorn main:app --reload

uvicorn books:app --reload

http://127.0.0.1:8000

for swagger ui use following command

http://127.0.0.1:8000/docs


pip install "passlib[bcrypt]"