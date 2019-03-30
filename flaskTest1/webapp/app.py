from flask import Flask,request,render_template,redirect,jsonify
import pymysql , os
app = Flask(__name__)   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bootstrap')
def boot():
    return render_template('bootstraptest.html')

@app.route('/form')
def formTest():
    return render_template('form.html')

@app.route('/formresult', methods=['POST'])
def formresult():
    username = request.form['username']
    userpass = request.form['userpass']
    useremail = request.form.get('email')
    joblist = request.form.getlist('joblist')
    hobbylist = request.form.getlist('hobby')
    it = request.form.getlist('chk')
    Major = request.form.get('rad')
    resume = request.form['resume']
    return render_template('formresult.html' , name = username , password =userpass , email = useremail , joblist = joblist ,
                            hobbylist = hobbylist , it = it , major = Major , resume=resume)
@app.route('/table',methods=['POST','GET'])
def table():
    #if request.method =='POST':
        #userid = request.form['userid']
        #username = request.form['username']
        #userpw = request.form['userpw']
        #userage = request.form['userage']
        #useremail = request.form['useremail']
        #useradd = request.form['useradd']
        #usergender = request.form['usergender']
        #usertel = request.form['usertel']

        return render_template('list.html') #userid = userid, userpw = userpw , username = username, userage = userage,
        #useremail = useremail , useradd = useradd , usergender = usergender , usertel = usertel
        #)
    #else: 
        #return render_template('table.html')
@app.route('/usersform', methods=['POST','GET'])
def usersform():
    if request.method =='GET':
        return render_template('usersform.html')
    else:
        #print(type(request.values))
        #for key in request.values:
            #informationall =  request.values[key]
            #print(informationall)
            #information[key] = request.values[key]
            #print(key,":",request.values[key])
        #userid = request.form.get('userid')
        #print('userid :',userid)
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        username = request.form.get('username')
        userage = request.form.get('userage')
        usermail = request.form.get('usermail')
        useradd = request.form.get('useradd')
        usergender = request.form.get('usergender')
        usertel = request.form.get('usertel')

        connection = pymysql.connect(host = '127.0.0.1',
        user = 'root',
        password = 'qwer1324',
        db = 'member',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = "insert into users values(%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(sql,(userid,userpw,username,userage,usermail,useradd,usergender,usertel))
                connection.commit()

            #with connection.cursor() as cursor:
                #sql = '''
                    #SELECT 'userid','username','userage','useremail','useradd','usergender','usertel' from users; 
                    #'''
                #cursor.execute(sql)
                #result = cursor.fetchall()
                #print(result)
        finally:
                connection.close()
        return redirect('/list')
@app.route('/list')
def list():
    connection = pymysql.connect(host = '127.0.0.1',
        user = 'root',
        password = 'qwer1324',
        db = 'member',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql="select * from users;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    return render_template('list.html' , list = result)

@app.route('/updateform/<userid>', methods =['GET'])
def updateforget(userid):
    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db = 'member',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "select * from users where userid = %s;"
            cursor.execute(sql,userid)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()
    return render_template('updateform.html' , list = result)
@app.route('/updateform',methods=['POST'])
def update():
    userid = request.form.get('userid')
    userpw = request.form.get('userpw')
    username = request.form.get('username')
    userage = request.form.get('userage')
    useremail = request.form.get('useremail')
    useradd = request.form.get('useradd')
    usergender = request.form.get('usergender')
    usertel = request.form.get('usertel')

    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db ='member',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "update users set userpw = %s , username = %s, userage = %s, useremail = %s ,useradd =%s ,usergender = %s,usertel = %s where userid = %s;"
            cursor.execute(sql,(userpw,username,userage,useremail,useradd,usergender,usertel,userid))
            connection.commit()
    finally:
        connection.close()
    return redirect('/list')
@app.route('/content/<userid>',methods =['GET'])
def content(userid):
    connection = pymysql.connect(host = '127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db = 'member',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "select * from users where userid = %s"
            cursor.execute(sql,userid)
            result = cursor.fetchone()
    finally:
        connection.close()
    return render_template('content.html' , list = result)
@app.route('/deleteform/<userid>')
def deleteformget(userid):
    connection = pymysql.connect(host='127.0.0.1',
    user = 'root',
    password = 'qwer1324',
    db='member',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "delete from users where userid = %s;"
            cursor.execute(sql,userid)
            connection.commit()
    finally:
        connection.close()
    return redirect('/list')
@app.route('/imglist')
def imglist():
    print(os.path.dirname(__file__))
    dirname = os.path.dirname(__file__) + '/static/img/'
    filenames = os.listdir(dirname)
    print(filenames)
    #for filename in filenames:
        #full_filename = os.path.join(dirname , filename)
        #print(full_filename)
    return render_template('imglist.html' , full_filename = filenames)
@app.route('/ajaxlist',methods=['GET'])
def ajaxlistget():
    connection = pymysql.connect(host='127.0.0.1',
                                 user = 'root',
                                 password ='qwer1324',
                                 db = 'member',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql="select * from users;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    return render_template('ajaxlist.html',list = result)
#공통으로 뽑아내기
@app.route('/ajaxlist',methods=['POST'])
def ajaxlistPost():
    userid = request.form.get('userid')
    connection = pymysql.connect(host='127.0.0.1',
                                 user = 'root',
                                 password ='qwer1324',
                                 db = 'member',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql="select * from users where userid like %s;"
            userid = userid +'%'
            cursor.execute(sql,userid)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
    return jsonify(result)

@app.route('/upload')
def uploadget():
    return render_template('uploadform.html')

#파일 업로드 처리
@app.route('/upload' , methods = ['POST'])
def uploadpost():
    f = request.files['uploadfile']
    #저장할 경로 +파일명
    dirname=os.path.dirname(__file__)+'/uploads/'+f.filename
    print(dirname)
    f.save(dirname)
    return 'uploads 디렉토리 -> 파일업로드 성공!' 
if __name__ =='__main__':
    app.run(host='0.0.0.0', port=80 , debug=True)
    