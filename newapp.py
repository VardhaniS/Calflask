from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def welcomehome():
    return "Welcome home flask"

@app.route('/calculate',methodS=['GET'])
def calculate():
    operator=request.json['operators']
    n1=request.json['n1']
    n2=request.json['n2']
    if operator=='add':
        result=n1+n2
    elif operator=='multiply':
        result=n1*n2
    elif operator=='subtract':
        result=n1-n2
    else:
        result=n1/n2

if __name__=="__main__":
    app.run(debug==True)