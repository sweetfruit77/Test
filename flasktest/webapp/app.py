from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',name='김기덕님!')


@app.route('/PList/')
def plist():
    list = {'김기덕','김성령','김혜원','김남주','시호'}
    return render_template('PList.html', name = list)

@app.route('/ulist/')
def ulist():
    list = {"김기덕":"김성령","김남주":"시호","김혜원":"배소진","윤수진":"서우현"}
    return render_template('list.html', nlist = list)

@app.route('/sqlite')
def movieIndex():
    conn = sqlite3.connect('d:/pythonwork/api_study/example.db')
    c = conn.cursor()
    c.execute('select * from movie')
    result = c.fetchall()
    #print(result)    
    return render_template('sqlite.html', list = result)    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
