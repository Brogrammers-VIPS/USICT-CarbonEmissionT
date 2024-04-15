from flask import Flask, render_template, request, redirect, send_file
#from model import label_encoders

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
