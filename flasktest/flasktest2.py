from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/cakes')
def cakes():
    return "yummy cakes!"

@app.route('/method/',methods=['GET','POST'])
def login():
    if request.method =='POST':
        return "Post"
    else:
        return "Get"
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User {}'.format(username)
    
@app.route('/user/<username>/<int:age>')
def show_user_profile_age(username,age):
    return 'User {}이고 나이는{}입니다.'.format(username,age)

if __name__ == "__main__":
    #debug = false = >  소스가 바뀔때 재접속을해야 적용됨
    #debug = True = > 소스가 바뀔때 자동접속
    app.run(debug = True,host = '0.0.0.0',port=80)