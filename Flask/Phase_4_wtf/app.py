from flask import Flask,render_template,request,flash,url_for,redirect 

from form import RegistrationForm
#Form handling
app = Flask(__name__) 
app.secret_key = "abhishek"

@app.route("/",methods=["GET","POST"]) 
def register():
  form = RegistrationForm() 
  if form.validate_on_submit():
    name = form.name.data 
    email = form.email.data 
    flash(f"Welcome {name} , Your Registered Successfully","success")
    return redirect(url_for("success"))
  return render_template("register.html",form=form) 
@app.route("/success")
def success():
  return render_template("success.html")