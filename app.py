from flask import *
import sqlite3

app = Flask(__name__)
app.secret_key= "123"

@app.route('/')
@app.route('/index')
def index():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    else:
        return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "" or password == "":
            return render_template("index.html", error="Please fill in all fields")
        else:
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("SELECT * FROM User WHERE username=? AND password=?", (username, password))
            row = c.fetchone()
            conn.close()
            if row != None:
                session["username"] = username
            else:
                return render_template("index.html", error="Wrong username or password")
            return redirect(url_for('index'))
    else:
        return render_template("index.html")

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        fullname = request.form["fullname"]
        email = request.form["email"]
        telno = request.form["telephone"]
        # Check if username already exists
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM User WHERE username=?", (username,))
        row = c.fetchone()
        if row != None:
            return render_template("register.html", error="Username already exists")
        # If username does not exist, create new user
        c.execute("INSERT INTO User VALUES(?,?,?,?,?)", (username, password, fullname, email, telno))
        conn.commit()
        conn.close()
        return render_template("reg_success.html")
    else:
        return render_template("register.html")

@app.route('/advertisement' , methods=["GET", "POST"])
def advertisement():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        category_id = request.form["category"]
        username = session["username"]
        if title == "" or description == "" or category_id == "":
            return render_template("advertisements.html")
        else:
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("INSERT INTO Advertisement(title,description,username,cid) VALUES(?,?,?,?)", (title, description, username, category_id))
            conn.commit()
            conn.close()
            return redirect(url_for('advertisement'))
    else:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Category")
        categories = c.fetchall()
        category_dict = {category[0]: category[1] for category in categories}
        c.execute("SELECT * FROM Advertisement WHERE username=?", (session["username"],))
        ads = c.fetchall()
        return render_template("advertisements.html", categories_dict=category_dict, ads=ads, categories=categories)

@app.route('/advertisement/<int:ad_id>/toggle', methods=["GET"])
def toggle(ad_id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Advertisement WHERE aid=?", (ad_id,))
    ad = c.fetchone()
    if ad[3] == 1:
        c.execute("UPDATE Advertisement SET isactive=0 WHERE aid=?", (ad_id,))
    else:
        c.execute("UPDATE Advertisement SET isactive=1 WHERE aid=?", (ad_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('advertisement'))

@app.route('/profile', methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        username = request.form["username"]
        fullname = request.form["fullname"]
        email = request.form["email"]
        telno = request.form["telephone"]
        if username == "" or fullname == "" or email == "" or telno == "":
            return render_template("profile.html", error="Please fill in all fields")
        else:
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("UPDATE User SET username=?, fullname=?, email=?, telno=? WHERE username=?", (username, fullname, email, telno, session["username"]))
            conn.commit()
            conn.close()
            session["username"] = username
            return redirect(url_for('profile'))
    else:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM User WHERE username=?", (session["username"],))
        user = c.fetchone()
        return render_template("profile.html", user=user)



if __name__ == '__main__':
    app.run()
