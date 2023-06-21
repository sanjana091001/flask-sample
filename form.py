from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def getname():
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        age = request.form.get("age")
        return ("Your name is "+first_name+" "+last_name+" and your age is "+age)
    return render_template("form.html")

if __name__=='__main__':
    app.run()
