import sqlite3
class database:
    def createDatabase(self, dbname):
        conn = sqlite3.connect(dbname)
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS User("
              "username TEXT PRIMARY KEY,"
              "password TEXT,"
              "fullname TEXT,"
              "email TEXT,"
              "telno TEXT)")

        c.execute("CREATE TABLE IF NOT EXISTS Category("
                  "cid INTEGER PRIMARY KEY AUTOINCREMENT,"
                  "cname TEXT)")

        c.execute("CREATE TABLE IF NOT EXISTS Advertisement("
                  "aid INTEGER PRIMARY KEY AUTOINCREMENT,"
                  "title TEXT,"
                  "description TEXT,"
                  "isactive INTEGER DEFAULT 1,"
                  "username TEXT,"
                  "cid INTEGER,"
                  "FOREIGN KEY(username) REFERENCES User(username),"
                  "FOREIGN KEY(cid) REFERENCES Category(cid))")

        c.execute("INSERT INTO Category(cname) VALUES(?)", ("Clothes",))
        c.execute("INSERT INTO Category(cname) VALUES(?)", ("Technology",))
        c.execute("INSERT INTO Category(cname) VALUES(?)", ("Cars",))
        c.execute("INSERT INTO Category(cname) VALUES(?)", ("Food",))
        c.execute("INSERT INTO Category(cname) VALUES(?)", ("Drink",))

        conn.commit()
        conn.close()


db = database()
db.createDatabase("database.db")
