from flask import Flask, render_template, redirect, request, flash, url_for


import mysql.connector as connector
db = connector.connect(host="localhost", user="root", passwd="root", database="python")

app = Flask(__name__)
app.secret_key='gfhsagagahahaagag'

@app.route('/main')
def Home():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/team')
def Team():
    return render_template('Team.html')

@app.route('/connect')
def Connect():
    return  render_template('Connect.html')
@app.route('/pass')
def pass_data():
    results =[34,56,4,2,7,8,4,2]
    name='ben peter'
    details=('mary',34, 1.77, 76)
    car={'make':'toyota', 'model':'premio','year':'2008','color':'white'}

    students = [{"names": "Cchaddie Grishaev", "age": 18, "gender": "Male"},
                {"names": "Gawen Sked", "age": 15, "gender": "Male"},
                {"names": "Arleyne Petofi", "age": 13, "gender": "Female"},
                {"names": "Laetitia Gounard", "age": 18, "gender": "Female"},
                {"names": "Alvinia Elven", "age": 15, "gender": "Female"},
                {"names": "Jocko Hinsch", "age": 16, "gender": "Male"},
                {"names": "Randa Laurenceau", "age": 16, "gender": "Female"},
                {"names": "Myranda Abrahmovici", "age": 18, "gender": "Female"},
                {"names": "Jackelyn Cusworth", "age": 13, "gender": "Female"},
                {"names": "Corenda Geeritz", "age": 19, "gender": "Female"},
                {"names": "Emmit Beals", "age": 15, "gender": "Male"}]
    return  render_template('data.html', results=results, name=name, details=details, car=car, students=students)

@app.route('/url/<int:age>')
def url_data(age):
    age=age+5
    return  str(age)

@app.route('/names/<majina>')
def x(majina):

    return  majina.upper()

# Newly introduced ones

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        # print(name, email, password)
        cursor = db.cursor()
        sql = "INSERT INTO `users`( `name`, `email`, `password`) VALUES (%s,%s,%s)"
        values =(name,email,password)
        cursor.execute(sql,values)
        db.commit()
        flash('Saved Successfully')
        return redirect(url_for('show'))


    return render_template("form.html")

@app.route('/show')
def show():
    cursor = db.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    return render_template('show.html', users=users)


@app.errorhandler(404)
def error_page(e):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
