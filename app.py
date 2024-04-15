from flask import Flask, render_template, request, redirect, send_file
import pickle
#from model import label_encoders

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


app=Flask(__name__)

@app.route('/')
def main():
    return  render_template('index.html')


@app.route('/input', methods=['POST'])
def input():
    if request.method=='POST':
        comp = request.form.get('Comp_name')
        v_class = request.form.get('v_class')
        eng_size = request.form.get('eng_size')
        cyl = request.form.get('cyl')
        trans = request.form.get('trans')
        f_type = request.form.get('f_type')
        city = request.form.get('city')
        hwy = request.form.get('hwy')
        comb = request.form.get('comb')
        start = request.form.get('start')
        end= request.form.get('end')


        comp_en=label_encoders['Make'].transform(comp)
        v_class_en=label_encoders['Vehicle Class'].transform(v_class)
        trans_en=label_encoders['Transmission'].transform(trans)
        f_type_en=label_encoders['Fuel Type'].transform(f_type)

        input=[[comp_en,v_class_en,eng_size,cyl,trans_en,f_type_en,city,hwy,comb]]
        emmison_output=model.predict(input)

        
