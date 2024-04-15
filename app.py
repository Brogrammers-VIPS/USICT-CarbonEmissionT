from flask import Flask, render_template, request, redirect, send_file
import pickle
import geocoder
from model import label_encoders

with open('xgb_model_6mse.pkl', 'rb') as f:
    model = pickle.load(f)


app=Flask(__name__)

@app.route('/')
def main():
    return  render_template('index.html')


@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method=='POST':
        comp = request.form.get('Comp_name')
        v_class = request.form.get('v_class')
        eng_size = int(request.form.get('eng_size'))
        cyl = int(request.form.get('cyl'))
        trans = request.form.get('trans')
        f_type = request.form.get('f_type')
        city = int(request.form.get('city'))
        hwy = int(request.form.get('hwy'))
        comb = int(request.form.get('comb'))
        cons=int(request.form.get('consump'))
        start = request.form.get('start')
        end= request.form.get('end')


        comp_en=label_encoders['Make'].transform(comp)
        v_class_en=label_encoders['Vehicle Class'].transform(v_class)
        trans_en=label_encoders['Transmission'].transform(trans)
        f_type_en=label_encoders['Fuel Type'].transform(f_type)

        input=[[comp_en,v_class_en,eng_size,cyl,trans_en,f_type_en,city,hwy,comb,cons]]
        
        emmision_output=model.predict(input)
        dist=geocoder.distance(start,end)

        emmision=dist*emmision_output

    return render_template('input.html', result=emmision)

if __name__=='__main__':
    app.run(,host="127.0.0.1",port=8080,debug=True)

