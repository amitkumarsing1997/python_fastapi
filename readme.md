pip install -r requirements.txt

to run program
uvicorn main:app --reload

uvicorn books:app --reload

http://127.0.0.1:8000

for swagger ui use following command

http://127.0.0.1:8000/docs



//for crypt purpose
pip install "passlib[bcrypt]"


// for authentication purpos
pip install python-multipart

//for json web token
pip install "python-jose[cryptoraphy]"

//for secret key go for cmd 
// and type below code
//openssl rand -hex 32


// for pgadmin(doubt) for better understanding search it

pip install psycopg2-binary

//for mysql install 
pip install pymysql

//for installation of alembic
pip install alembic

//to setup alembic in our project type following command on terminal
alembic init alembic

