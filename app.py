from flask import Flask, render_template, request

app=Flask(__name__)

import numpy as np
import pickle
model1 = pickle.load(open('model1.pkl','rb')) 

@app.route('/')
def BreastGuard():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit(): 
  ##  data=request.form(Current id)
    rm=request.form["rm"]
    tm=request.form["tm"]
    pm=request.form["pm"]
    am=request.form["am"]
    sm=request.form["sm"]
    com=request.form["com"]
    cvm=request.form["cvm"]
    cpm=request.form["cpm"]
    sym=request.form["sym"]
    fdm=request.form["fdm"]
    
    rs=request.form["rs"]
    ts=request.form["ts"]
    ps=request.form["ps"]
    ars=request.form["as"]
    ss=request.form["ss"]
    cos=request.form["cos"]
    cvs=request.form["cvs"]
    cps=request.form["cps"]
    sys=request.form["sys"]
    fds=request.form["fds"]
    
    rw=request.form["rw"]
    tw=request.form["tw"]
    pw=request.form["pw"]
    aw=request.form["aw"]
    sw=request.form["sw"]
    cow=request.form["cow"]
    cvw=request.form["cvw"]
    cpw=request.form["cpw"]
    syw=request.form["syw"]
    fdw=request.form["fdw"]
    
    
    t=[[float(rm),float(tm),float(pm),float(am),float(sm),float(com),float(cvm),float(cpm),float(sym),float(fdm),
        float(rs),float(ts),float(ps),float(ars),float(ss),float(cos),float(cvs),float(cps),float(sys),float(fds),
        float(rw),float(tw),float(pw),float(aw),float(sw),float(cow),float(cvw),float(cpw),float(syw),float(fdw)]]
    
    prediction=model1.predict(t)
    
    if(prediction[0]==1):
        output="the tumor is cancerous"
    else:
        output="the tumor is non-cancerous"
    
    
    return render_template("index.html",y="The predicted result is that {} ".format(output))



if __name__ == '__main__' :
    app.run(debug=True) 