from flask import Flask,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)
data=pd.read_csv(r"C:\Users\ATHUL AKSHAY\Desktop\Cancer\breast-cancer_csv.csv")
model=pickle.load(open("cancer.pkl","rb"))

@app.route('/')
def data():
    return render_template('bc.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method =='POST':
        age=int(request.form['age'])
        menopause=request.form['menopause']
        breastquad=request.form['breastquad']
        breast=request.form['breast']
        nodecaps=request.form['nodecaps']
        degmalig=request.form['degmalig']
        irradiat=request.form['irradiat']
        tumorsize=request.form['tumorsize']
        invnodes=request.form['invnodes']

        prediction=model.predict([[age,menopause,breastquad,breast,nodecaps,degmalig,irradiat,tumorsize,invnodes]])
        prediction=prediction[0]
        if prediction==0:
            a='No recurrence events'
        elif prediction==1:
            a='recurrence events'
        
        return render_template('bc.html',predict=a)


if __name__=='__main__':
    app.run(debug=True)