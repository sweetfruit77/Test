from flask import Flask,render_template,url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def javascript():
    return render_template('jqtest_15.html')

if __name__ =="__main__":
    app.run(debug=True , host="0.0.0.0",port=80)