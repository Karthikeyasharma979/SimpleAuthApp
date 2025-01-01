from flask import Flask,render_template,request,url_for,redirect,session
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def welecome():
    return render_template("index.html")

@app.route('/login',methods=["POST","GET"])
def login():
    return render_template("Login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/checkcreidts',methods=["POST","GET"])
def check():
    if(request.method=="POST"):
        uname = request.form["uname"]
        passw = request.form["passw"]
        check="0"
        if uname !="karthik" and passw!="1234567890":
            check="Enter the username and password"
            return render_template("Login.html",result=check)  
        elif uname=="karthik" and passw!="1234567890":
            check="Check your password "
            return render_template("Login.html",result=check)  
        else:
            session["uname"]=uname
            return redirect(url_for("dashboard"))
        
        
@app.route("/registration",methods=["POST","GET"])
def registration():
    if(request.method=="POST"):
        uname = request.form["username"]
        passw = request.form["password"]
        email = request.form["email"]
        check=checkUser(uname,passw,email)
        if check!="0":
            return render_template("signup.html",result=check)
        else:
            session["uname"]=uname
            return redirect(url_for("dashboard"))
    
def checkUser(uname,passw,email):
        return "0"



@app.route("/dashboard")
def dashboard():
    if "uname" in session:
        return render_template("dashboard.html",uname=session["uname"])
    else:
        return render_template("index.html")
    
    
@app.route("/logout")
def logout():
    session.pop('uname',None)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)