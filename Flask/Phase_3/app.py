from flask import Flask,render_template,request,flash,url_for,redirect
#Form handling
app = Flask(__name__) 
app.secret_key = "abhishek"
@app.route("/feedback",methods=["POST","GET"])
def feedback():
  if request.method =="POST":
    name = request.form.get("username")#return none if username is absent 
    # second way request.form["Key"]-->throw error if absent
    if not name :
      flash("Name cannot be empty")
      return redirect(url_for("feedback"))
    message = request.form.get("message")
    flash(f"Thanks {name}, your feedback saved")
    return render_template("thankyou.html",user=name,message = message) 
 
  return render_template("feedback.html")
