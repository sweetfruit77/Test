from flask import render_template,redirect,Flask,url_for

app = Flask(__name__)

@app.route('/')
def jsTest():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0' , port = 80)