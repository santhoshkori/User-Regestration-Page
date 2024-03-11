from flask import Flask,redirect,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")


@app.route("/submit",methods=["POST","GET"])
def submit():
    username = ""
    password = ""
    retypepassword = ""
    if request.method=="POST":
        username=request.form["personname"]
        password=request.form["personpassword"]
        retypepassword=request.form["personretypepassword"]
        print(username,password,retypepassword)
    return render_template("result.html", username=username, password=password, retypepassword=retypepassword)
    # Redirect to the homepage if accessed via GET method
    
if __name__=='__main__':
    app.run(debug=True)