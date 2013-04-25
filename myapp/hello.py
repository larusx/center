import os
import re
from flask import Flask,render_template,request,send_from_directory,redirect,url_for,flash
from werkzeug import secure_filename
app = Flask(__name__) 
app.secret_key=os.urandom(24)
UPLOAD_FOLDER='/usr/upload/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.debug=True
@app.route('/')
def hello():
    #return_list=[]
    #for root,dirs,files in os.walk(UPLOAD_FOLDER):
    #    for fn in files:
    #        return_list.append(fn.decode('utf-8'))
    #return render_template('a.html',return_list=return_list)
    return render_template('index.html')

@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        flist = request.files
	exist_list=[]
	for f in flist.getlist('file1'):
	    if os.path.exists(UPLOAD_FOLDER+f.filename.encode('utf-8')):
		exist_list.append(f.filename.encode('utf-8'))
    	        return render_template('a.html',status='''<div class="row"><div class="span4 offset6"><div class="alert alert-success">%s exists!!!</div></div></div>''' % f.filename)
            f.save(UPLOAD_FOLDER+f.filename.encode('utf-8'))
	    
    return render_template('a.html',status='''<div class="row"><div class="span4 offset6"><div class="alert alert-success">Upload Success!!!</div></div></div>''')
@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/search',methods=['POST','GET'])
def search_result():
    return_list=[] 
    if request.method == 'POST':
        search_content=request.form['search_content'].encode('utf-8')
        for root,dirs,files in os.walk(UPLOAD_FOLDER):
            for fn in files:
                if re.search(search_content,fn,re.IGNORECASE):
                    return_list.append(fn.decode('utf-8'))
    return render_template('a.html',return_list=return_list)
if __name__ == '__main__': 
    app.run()
