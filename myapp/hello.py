import os
from flask import Flask,render_template,request,send_from_directory
from werkzeug import secure_filename
app = Flask(__name__) 

UPLOAD_FOLDER='/usr/upload'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/') 
def hello():
	return_list=[] 
	for root,dirs,files in os.walk(UPLOAD_FOLDER):
		for fn in files:
			return_list.append(fn)
	return render_template('a.html',return_list=return_list)

@app.route('/upload',methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file1']
		f.save('usr/upload'+secure_filename(f.filename))
	return 'OK'

@app.route('/upload/<filename>')
def uploaded_file():
	return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__': 
	app.run(debug=True)
