from flask import Flask,render_template,request,redirect,url_for,session,Response
#flask --app app.py --debug run

app = Flask(__name__)
app.secret_key="abhishekgordepatil"
# @app.route("/")
# @app.route("/home")
# def home_page():
#     return render_template('home.html')
# # @app.route("/about/<username>")
# # def about(username):
# #     return f"<h1>Hello, {username}</h1>" 

# @app.route("/submit",methods=["GET","POST"])
# def submit():
#     if request.method == "POST":
#         return "You Sent data"
#     else :
#         return "Youe are Just viewing form"

@app.route("/",methods=["GET","POST"])
def login() :
 if(request.method == "POST"):
  username = request.form.get("username")
  password = request.form.get("password") 
  if(username == "admin" and password == "123") :
    session["user"] = username 
    return redirect(url_for("welcome")) 
  else :
   return Response("Your Password and username is incorrect",mimetype="text/plain") # by default mimetype ="text/html" 
 return ''' 
     <h2>Login Page</h2>
     <form method="POST">
      username : <input type="text" name="username"> 
      Password : <input type="password" name="password">
      <input type="submit" value="Login" >
     </form>
  '''  
@app.route("/welcome") 
def welcome():
 if "user" in session :
   return f''' 
    <h2>Welcome , {session["user"]}! </h2>
    <a href={url_for('logout')}>Logout </a> 

 '''
 return redirect(url_for("login")) 

@app.route("/logout")
def logout():
 session.pop("user",None)
 return redirect(url_for("login"))