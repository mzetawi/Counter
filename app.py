from flask import Flask, render_template, session, redirect, url_for, request
app = Flask(__name__)
app.secret_key = "mustafazetawi"  
def init_session():
    if "counter" not in session:
        session["counter"] = 0
    if "visits" not in session:
        session["visits"] = 0
@app.route("/")
def home():
    init_session()
    session["visits"] += 1            
    return render_template(
        "index.html",
        counter=session["counter"],
        visits=session["visits"]
    )
@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect(url_for("home"))
@app.route("/plus2", methods=["POST"])
def plus2():
    init_session()
    session["counter"] += 2
    return redirect(url_for("home"))
@app.route("/reset", methods=["POST"])
def reset():
    init_session()
    session["counter"] = 0
    return redirect(url_for("home"))
@app.route("/increment", methods=["POST"])
def increment():
    init_session()
    step_raw = request.form.get("step", "1").strip()
    try:
        step = int(step_raw)
    except ValueError:
        step = 1
    session["counter"] += step
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)
