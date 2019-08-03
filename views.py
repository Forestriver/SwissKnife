from flask import Flask, render_template, request
from application import summary

app=Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def counter():
    errors = ""
    if request.method=="POST":
        rate_e = None
        rate_d = None
        euros = None
        dollars = None
        try:
            rate_e = float(request.form["rate_e"])
        except:
            errors += "<p>{!r} is not a number. </p>\n".format(request.form["rate_e"])
        try:
            rate_d=float(request.form["rate_d"])
        except:
            errors += "<p>{!r} is not a number. </p>\n".format(request.form["rate_d"])
        try:
            euros = float(request.form["euros"])
        except:
            errors += "<p>{!r} is not a number. </p>\n".format(request.form["euros"])
        try:
            dollars = float(request.form["dollars"])
        except:
            errors += "<p>{!r} is not a number. </p>\n".format(request.form["dollars"])
        if rate_e is not None and rate_d is not None and euros is not None and dollars is not None:
            result = summary(rate_e, rate_d, euros, dollars)
            return render_template("counter2.html").format(result=result)

    return render_template("counter.html").format(errors=errors)

if __name__=="__main__":
    app.run(debug=True)
