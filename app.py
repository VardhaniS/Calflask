from flask import Flask,render_template,request,redirect,url_for
#creating the app
app=Flask(__name__)

#Creating home page '/' declares home
@app.route('/')
def home():
    return '<p>Hello Varu</p>'

@app.route('/Dashboard')
def Dashboard():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "Success with the score of:"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Fail with a score of"+str(score)
    
@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['Maths'])
        physics=float(request.form['Physics'])
        history=float(request.form['History'])

        average_marks=(maths+physics+history)/3
        result=''
        if average_marks>50:
            result='success'
        else:
            result='fail'
        #return redirect(url_for(result,score=average_marks))
        return render_template('result.html',results=average_marks)

if __name__=='__main__': #starting point 
    #app.run() #run to create the flask application
    app.run(debug=True)