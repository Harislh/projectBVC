from flask import Flask,render_template,request,redirect
import mysql.connector
app = Flask(__name__)

def get_connection():
      return  mysql.connector.connect(
               host = "localhost",
               user = "root",
               password = "root",
               database="practiceproject"
          )

@app.route("/")
def home():
     conn = get_connection()
     cmd = conn.cursor(dictionary=True)
     cmd.execute("SELECT * FROM employee")
     data = cmd.fetchall()
     conn.close()
     return render_template("index.html",employee=data)

@app.route("/insert",methods=["POST"])
def insertData():
    id = request.form["id"]
    name = request.form["name"]
    dept = request.form["dept"]
    salary = request.form["salary"]
    
    conn = get_connection()
    cmd = conn.cursor()
    cmd.execute('''INSERT INTO EMPLOYEE (id,name,dept,salary) VALUES(%s,%s,%s,%s)
                ''',(int(id),name,dept,float(salary)))
    conn.commit()
    conn.close()
    return redirect("/")
     


@app.route("/delete",methods=["POST"])
def deleteData():
     id = request.form["id"]
     
     conn = get_connection()
     cmd = conn.cursor()
     cmd.execute("DELETE FROM employee WHERE id=%s",(id,))
     conn.commit()
     conn.close()
     return redirect("/")


@app.route("/update",methods=["POST"])
def updateData():
     id = request.form["id"]
     
     conn = get_connection()
     cmd = conn.cursor(dictionary=True)
     cmd.execute("SELECT * FROM employee WHERE id=%s",(id,))
     person = cmd.fetchone()
     conn.close()
     
     return render_template("update.html",employee=person)


@app.route("/updateData",methods=["POST"])
def updateDataFromForm():
     id = request.form["id"]
     name = request.form["name"]
     dept = request.form["dept"]
     salary = request.form["salary"]
     print(name,dept,salary,id)
     conn = get_connection()
     cmd = conn.cursor()
     cmd.execute('''UPDATE employee SET name=%s,dept=%s,salary=%s WHERE id=%s
                 ''',(name,dept,float(salary),int(id)))
     conn.commit()
     conn.close()
     return redirect("/")


@app.route("/logout")
def logout():
     return redirect("/")

if __name__ == "__main__":
     app.run(debug=True)