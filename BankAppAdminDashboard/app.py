from flask import Flask,render_template,request
from db import get_connection
app = Flask(__name__)

@app.route("/adminDashboard",methods=["GET","POST"])
def adminD():
     return render_template("adminDashboard.html")


@app.route("/insert",methods=["POST"])
def insertData():
     acc = request.form["Acc"]
     name = request.form["Name"]
     mobile = request.form["Mobile"]
     email = request.form["Email"]
     balance = request.form["balance"]
     password = name[0:3]+"@"+mobile[0:4]
     
     
     conn = get_connection()
     cmd = conn.cursor()
     cmd.execute('''
                 INSERT INTO customers(acc,name,mobile,email,balance,password)
                 VALUES(%s,%s,%s,%s,%s,%s)
                 ''',(int(acc),name,int(mobile),email,int(balance),password))
     conn.commit()
     conn.close()
     
     return "data inserted successfullyyyyyy"


if __name__ == "__main__":
     app.run(debug=True)