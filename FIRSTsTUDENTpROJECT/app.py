from flask import Flask,request,render_template
from db import get_connection

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
     
     if request.method == "GET":
          return render_template("index.html")
     
     elif request.method == "POST":
          id = request.form["sid"]
          name = request.form["sname"]
          branch = request.form["sbranch"]
          marks = request.form["smarks"]
          
          conn = get_connection()
          cmd = conn.cursor()
          cmd.execute('''
                      INSERT INTO student(sId,sName,sBranch,sMarks)
                      VALUES (%s,%s,%s,%s)''',(int(id),name,branch,int(marks)))
          conn.commit()
          conn.close()
     
          return "Data inserted successfully"
          
@app.route("/view")
def viewAll():
     conn = get_connection()
     cmd = conn.cursor(dictionary=True)
     cmd.execute("SELECT * FROM student")
     data = cmd.fetchall()
     conn.close()   
     
     return render_template("view.html",students=data)

if __name__ == "__main__":
     app.run(debug=True)