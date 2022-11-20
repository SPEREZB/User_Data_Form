
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'contacts_flask'
mysql = MySQL(app)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contacts')
        data = cur.fetchall()
        return render_template('index.html', contacts=data)
    else:
        print(request.method)
        search = request.form['search']
        print(search)

        if search == '1':
            print('iss')
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM contacts where id=' + search)
            data = cur.fetchall()
        else:
            print('a')
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
            return 'DEBE LLENAR TODOS LOS PARAMETROS DEL FORMULARIO'
        else:
            if phone.__len__() != 10:
                return 'EL NUMERO INGRESADO DEBE TENER 10 DIGITOS'
            else:
                print(name, phone, email)
                cur = mysql.connection.cursor()
                cur.execute('INSERT INTO contacts (name,phone,email) values (%s,%s,%s)',
                            (name, phone, email))
                mysql.connection.commit()
                return 'LOS DATOS SE INGRESARON CORRECTAMENTE'


if __name__ == '__main__':
    app.run(port=3000, debug=True)
