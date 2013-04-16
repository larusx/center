from flask import Flask,render_template
from werkzeug import secure_filename
app = Flask(__name__) 

@app.route('/') 
def hello(): 
	return render_template('a.html')

@app.route('/storage',methods=['GET','POST'])
def upload_file():
	if request.method== 'POST':
		f = request.files['file1']
		f.save('/usr/upload/'+secure_filename(f.filename))
	return render_template('a.html')
if __name__ == '__main__': 
	app.run(debug=True)
