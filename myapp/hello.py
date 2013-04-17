import os
<<<<<<< HEAD
from flask import Flask,render_template,request,send_from_directory,url_for,redirect
=======
from flask import Flask,render_template,request,send_from_directory,redirect,url_for,flash
>>>>>>> 55467ae78c1e4031d6b3a52290135268fbc1e404
from werkzeug import secure_filename
app = Flask(__name__) 
app.secret_key=os.urandom(24)
UPLOAD_FOLDER='/usr/upload/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.debug=True
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
		f.save(UPLOAD_FOLDER+secure_filename(f.filename))
		flash('OK')
	return redirect(url_for('hello'))
@app.route('/upload/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__': 
	app.run()
