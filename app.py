from flask import Flask, render_template, request, session, url_for, redirect
app=Flask(__name__)
app.secret_key = "knon"
def init_session() :
    if "visits" not in session :
        session['visits']=0
    if "counter" not in session :
        session['counter'] = 0
@app.route('/')
def hello() :
    init_session()
    session["visits"] +=1
    return render_template('index.html', visits=session["visits"], counter=session["counter"])
@app.route('/increment' , methods=['post']) 
def increment ():
    init_session()
    step_row=request.form.get("step","1").strip()
    try :
        step=int(step_row)
    except :
        step = 1
    session["counter"] +=step
    return redirect(url_for("hello"))
@app.route("/plus2", methods=["POST"])
def plus2() :
    init_session()
    session["counter"] +=2
    return redirect(url_for("hello"))
@app.route("/reset_counter", methods=["POST"]) 
def reset_counter() :
    init_session()
    session["counter"] = 0
    return redirect(url_for("hello"))
@app.route("/destroy_session") 
def destroy_session() :
    session.clear()
    return redirect(url_for("hello"))
if __name__=='__main__' :
    app.run(debug=True)