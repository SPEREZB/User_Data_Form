 
from flask import Flask, render_template,request
from flask_mysqldb import MySQL 
import pickle
app = Flask(__name__) 
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123'
app.config['MYSQL_DB']='contacts_flask'
mysql=MySQL(app)
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':  
        name= request.form['name']
        phone= request.form['phone']
        email= request.form['email']  
        print(name,phone,email)
        cur= mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (name,phone,email) values (%s,%s,%s)', 
        (name,phone,email))
        mysql.connection.commit()
        return 'LOS DATOS SE INGRESARON CORRECTAMENTE' 
 
if __name__=='__main__':
    app.run(port=3000,debug=True)  
    
 