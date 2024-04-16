from flask import Flask, render_template, request, redirect, url_for
import pickle
import geocoder
from model import label_encoders
import numpy as np

with open('xgb_model_6mse.pkl', 'rb') as f:
    model = pickle.load(f)


app=Flask(__name__)

@app.route('/')
def main():
    return  render_template('index.html')

@app.route('/redirect-input', methods=['POST'])
def redirect_input():
    # Redirect to the /input route
    return redirect(url_for('input'))

@app.route('/input', methods=['GET', 'POST'])
def input():
    emmision=0
    if request.method=='POST':
        comp = request.form.get('Comp_name')
        print(comp)
        v_class = request.form.get('v_class')
        eng_size = float(request.form.get('eng_size'))
        cyl = int(request.form.get('cyl'))
        trans = request.form.get('trans')
        f_type = request.form.get('f_type')
        city = int(request.form.get('city'))
        hwy = int(request.form.get('hwy'))
        comb = int(request.form.get('comb'))
        cons=int(request.form.get('consump'))
        # start = request.form.get('start')
        # end= request.form.get('end')


        comp_en=label_encoders['Make'].transform([comp.upper()])
        v_class_en=label_encoders['Vehicle Class'].transform([v_class.upper()])
        trans_en=label_encoders['Transmission'].transform([trans])
        f_type_en=label_encoders['Fuel Type'].transform([f_type.upper()])

        input=np.array([comp_en[0],v_class_en[0],eng_size,cyl,trans_en[0],f_type_en[0],city,hwy,comb,cons])
        input=input.reshape(1,10)
        emmision_output=model.predict(input)
        dist=10

        emmision=dist*emmision_output
        return render_template('hello.html', result=emmision[0])
    return render_template('hello.html', result=emmision)

if __name__=='__main__':
    app.run(host="127.0.0.1",port=8080,debug=True)

