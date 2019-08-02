from flask import Flask,render_template
from flask import *
from i2p import i2pconverter
app = Flask(__name__)

@app.route('/Img2Pdf')
def index():
    return render_template('index.html')

@app.route('/converted',methods = ['GET', 'POST'])
def convert():
    global f1
    fi = request.files['img']
    f1 = fi.filename
    fi.save(f1)
    i2pconverter(f1)
    return render_template('converted.html')

@app.route('/download')
def download():
    filename = f1.split('.')[0]+'converted.pdf'
    return send_file(filename,as_attachment=True)

app.run(debug=True)