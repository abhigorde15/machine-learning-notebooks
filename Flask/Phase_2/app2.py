from flask import Flask,render_template,request,redirect,url_for,session,Response

app = Flask(__name__)
app.secret_key="abhishekgordepatil"
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('form.html')

@app.route("/submit",methods=["POST"])
def login():
    username = request.form.get("username") 
    password = request.form.get("password")
    if username=="Abhishek" and password=="pass":
        return render_template("welcome.html",username=username)
    else :
        return "Invalid cradentials"