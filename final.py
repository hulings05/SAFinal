from flask import Flask, redirect, url_for, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('welcome.htm')

@app.route('/bookroom')
def bookaroom():
	return render_template('bookroom.htm')

@app.route("/bookingrec", methods = ["POST", "GET"])
def bookingrec():
    if request.method == "POST":
        name = request.form["name"]
        checkin = request.form["checkin"]
        checkout = request.form["checkout"]
        roomtype = request.form["roomtype"]

        cmd = "INSERT INTO final (name, checkin, checkout, roomtype) VALUES ('{0}', '{1}', '{2}', '{3}')".format(name, checkin, checkout, roomtype)

        with sql.connect("final.db") as conn:
            cur = conn.cursor()
            cur.execute(cmd)
            conn.commit()
            return render_template("confirmationpage.htm", name=name, checkin=checkin, checkout=checkout) #, msg = msg

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pswd = request.form['password']
        if user == 'manager' and pswd == 'Panther$':
                conn = sql.connect("final.db")
                conn.row_factory = sql.Row

                cmd = "SELECT * FROM final"
                cur = conn.cursor()
                cur.execute(cmd)
                rows = cur.fetchall()
                conn.close()
                return render_template("roomlist.htm", rows = rows)
        else:
            return render_template('deniedlogin.htm', name=user)
    else:
        return render_template('login.htm')


if __name__ == "__main__":
	app.run()