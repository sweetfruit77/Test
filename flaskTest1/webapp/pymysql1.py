import pymysql

connection = pymysql.connect(host ='127.0.0.1', 
user='root',
password ='qwer1324',
db='member',
charset = 'utf8mb4',
cursorclass = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = '''
                insert into users values('111aegildong','1234','코코길동',23,'kkd468@naver.com','부산시북구 만덕2동','male',
                '010-1234-1444');
            '''
        cursor.execute(sql)
        connection.commit()
    with connection.cursor() as cursor:

        sql = '''
              SELECT * from users;
        
        '''
        cursor.execute(sql)
        result =cursor.fetchall()
        print(result)
finally:
    connection.close()
    