from flask import Flask, render_template

app = Flask(__name__)
# #home.html was profile.html 
# @app.route("/")
# def student_profile():
#     return render_template("profile.html",
#                            name="Arun",
#                            isTopper=True,
#                            subjects=["Maths", "Physics", "Chemistry"])

# if __name__ == '__main__':
#     app.run(debug=True)


@app.route('/')
def home():
  return render_template("home.html",name ="Abhishek",isTopper=True,subjects=['Maths','Physics','Chemistry'])

@app.route('/about')
def about():
  return render_template("about.html")

app.run(debug=True)