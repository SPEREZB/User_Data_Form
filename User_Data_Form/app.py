
from flask import Flask, render_template, request,flash,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#options
app.secret_key='mysecretkey'

#mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'contacts_flask'
mysql = MySQL(app)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        print('aaa')
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contacts')
        data = cur.fetchall()
        return render_template('index.html', contacts=data)
    else:
        print(request.method)
        search = request.form['search']
        print(search)

        if search >= '1':
        
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM contacts where id=' + search)
            data = cur.fetchall()
        else:
         
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM contacts where name = "'+search +
                        '" or phone = "'+search+'" or email = "'+search+'"')
            data = cur.fetchall()

        return render_template('index.html', contacts=data)
 

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        if name == '' or phone =='' or email=='':
            flash('DEBE LLENAR TODOS LOS PARAMETROS DEL FORMULARIO')
            return redirect(url_for('home'))
        else:
            if phone.__len__() != 10:
                flash('EL NUMERO INGRESADO DEBE TENER 10 DIGITOS')
                return redirect(url_for('home'))
            else:
                print(name, phone, email)
                cur = mysql.connection.cursor()
                cur.execute('INSERT INTO contacts (name,phone,email) values (%s,%s,%s)',
                            (name, phone, email))
                mysql.connection.commit()
                flash('LOS DATOS SE INGRESARON CORRECTAMENTE')
                return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)
