from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def main():

    return render_template('main.html')

@app.route('/User_sign')
def user_Sign():
    return render_template('User_sign.html')

    
if __name__ == "__main__":
    app.run(debug=True , port=80 , host='0.0.0.0')

