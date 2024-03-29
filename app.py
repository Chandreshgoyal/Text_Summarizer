from flask import Flask, render_template, request
from Text_Summarizer import summarizer

app=Flask(__name__)

@app.route('/')

def index():
    return  render_template('index.html')


@app.route('/analyse',methods=['GET','POST'])
def analyse():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary, original_txt, len_orig_txt, len_summary=  summarizer(rawtext)
    return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary )

if __name__  == "__main__":
    app.run(host='0.0.0.0',port=8080)
    app.run(debug=True)

