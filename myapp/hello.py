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
    success_list=[]
    for f in flist.getlist('file1'):
        file_name=f.filename.encode('utf-8')
        if os.path.exists(UPLOAD_FOLDER+file_name):
            exist_list.append(file_name.decode('utf-8'))
            continue
        f.save(UPLOAD_FOLDER+file_name)
        success_list.append(file_name.decode('utf-8'))
    return render_template('upload_return.html',exist_list=exist_list,success_list=success_list)
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
