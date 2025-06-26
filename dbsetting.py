import pymysql
from database import MyDB

mydb = MyDB(
    _host='geuno.mysql.pythonanywhere-services.com',
    _port=3306,
    _user='geuno',
    _pw='dlrmsdh1',
    _db_name='geuno$ubion'
)

create_user = """
    create table
    if not exists
    user (
    id varchar(32) primary key,
    password varchar(64) not null,
    name varchar(32)
    )
"""

mydb.sql_query(create_user)
mydb.commit_db()