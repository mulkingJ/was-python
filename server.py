from flask import Flask,request,render_template

app : Flask = Flask(__name__)

# root end-point
@app.route('/')
def say_hello()-> str:
    return render_template('html/index.html')

@app.route('/upper',methods=['POST'])
def upper_string()-> str:
    if request.method == 'POST':
        word = request.form.get('word','')
        word = word.upper()
        return render_template('html/index.html',word=word)
    else:
        return "Error: missing parameter" , 404

@app.route('/lower',methods=['POST'])
def lower_string()-> str:
    if request.method == 'POST':
        word = request.form.get('word','')
        word = word.lower()
        return render_template('html/index.html',word=word)
    else:
        return "Error: missing parameter" , 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)