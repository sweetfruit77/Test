from flask import Flask,render_template,redirect,url_for,jsonify ,request
import pymysql , os
app = Flask(__name__)

@app.route('/')
def movieIndex():
    connection = pymysql.connect(host = '127.0.0.1',
        user = 'root',
        password = 'qwer1324',
        db = 'movie',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "select movieid,movieposterName,movietitle,moviegrade,moviegenre,movietime,moviedirector,moviestar,moviestart from movieinfo;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    return render_template('movieIndex.html' , list = result)
@app.route('/movieRegister')
def movieRegister():
    return render_template('movieRegister.html')
@app.route('/movieRegister', methods = ['POST'])
def movieRegister_Action():
    #영화포스터 이미지 저장
    f = request.files['movieposterName']
    #저장할 경로 +파일명
    dirname=os.path.dirname(__file__)+'/static/movieposter/'+f.filename
    #dirname = 'd:\pythonwork\movie_information\webapp/static/img/'+f.filename
    print(dirname)
    f.save(dirname)
    #영화정보등록
    movietitle = request.form.get('movietitle')
    moviegrade = request.form.get('moviegrade')
    moviegenre = request.form.get('moviegenre') 
    movietime = request.form.get('movietime')
    moviedirector = request.form.get('moviedirector')
    moviestar = request.form.get('moviestar')
    #날짜 넣을때는 하이푼+(년-월-일(두자리씩넣어라)) 
    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db = 'movie',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "insert into movieinfo(movieposterName,movietitle,moviegrade,moviegenre,movietime,moviedirector,moviestar,moviestart) values(%s,%s,%s,%s,%s,%s,%s,now());"
            cursor.execute(sql,(f.filename,movietitle,moviegrade,moviegenre,movietime,moviedirector,moviestar))
            connection.commit()
    
    finally:
        connection.close()
    return redirect('/')
@app.route('/movieContent/<movieid>' , methods = ['GET'])
def content(movieid):
    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db = 'movie',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "select movieid,movieposterName,movietitle,moviegrade,moviegenre,movietime,moviedirector,moviestar,moviestart from movieinfo where movieid = %s;"
            cursor.execute(sql,movieid)
            result = cursor.fetchone()
    finally:
        connection.close()
    return render_template('movieContent.html' , movie = result)
@app.route('/movieUpdate/<movieid>', methods = ['GET'])
def updateforget(movieid):
    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db = 'movie',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "select movieid,movieposterName,movietitle,moviegrade,moviegenre,movietime,moviedirector,moviestar,moviestart from movieinfo where movieid = %s;"
            cursor.execute(sql,movieid)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()
    return render_template('movieUpdate.html' , movie = result)
@app.route('/movieUpdate' , methods = ['POST'])
def update():
    #영화포스터 이미지 저장
    f = request.files['movieposterName']
    #저장할 경로 +파일명
    dirname=os.path.dirname(__file__)+'/static/movieposter/'+f.filename
    #dirname = 'd:\pythonwork\movie_information\webapp/static/img/'+f.filename
    print(dirname)
    f.save(dirname)
    #영화정보등록
    movieid = request.form.get('movieid')
    movietitle = request.form.get('movietitle')
    moviegrade = request.form.get('moviegrade')
    moviegenre = request.form.get('moviegenre')
    movietime = request.form.get('movietime')
    moviedirector = request.form.get('moviedirector')
    moviestar = request.form.get('moviestar')
    print(movieid,movietitle,moviegrade,moviegenre,movietime,moviedirector,moviestar)
    
    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db = 'movie',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "update movieinfo set movieposterName = %s , movietitle = %s, moviegrade = %s, moviegenre = %s , movietime = %s, moviedirector = %s , moviestar = %s , moviestart = now() where movieid = %s;"        
            cursor.execute(sql,(f.filename,movietitle,moviegrade,moviegenre,movietime,moviedirector,moviestar,movieid))
            connection.commit()
    finally:
        connection.close()
    return redirect('/')
@app.route('/movieDelete/<movieid>')
def deleformet(movieid):
    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db = 'movie',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "delete from movieinfo where movieid = %s;"
            cursor.execute(sql,movieid)
            connection.commit()
    finally:
        connection.close()
    return redirect('/')

@app.route('/movieSearch', methods=['GET'])
def movieSearch():
    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db = 'movie',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            sql = "select movieid,movieposterName,movietitle,moviegrade,moviegenre,movietime,moviedirector,moviestar,moviestart from movieinfo;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    return render_template('movieSearch.html', SearchList = result)
@app.route('/movieSearch' , methods=['POST'])
def movieSearchfinally():
    movietitle = request.form.get('movietitle')
    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db = 'movie',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql="select movieid,movieposterName,movietitle,moviegrade,moviegenre,movietime,moviedirector,moviestar,moviestart from movieinfo where movietitle like %s;"
            movietitle = movietitle + '%'
            cursor.execute(sql,movietitle)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True, port=80 , host='0.0.0.0')