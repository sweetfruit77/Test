from flask import Flask,render_template
import sqlite3,json 

app = Flask(__name__)

@app.route('/')
def movieIndex():
    conn = sqlite3.connect('d:/pythonwork/api_study/example.db')
    c = conn.cursor()
    c.execute('select * from movie')
    result = c.fetchall()
    #print(result)    
    return render_template('index.html', list = result)

if __name__ == "__main__":
    app.run(debug=True, port=80 , host='0.0.0.0')