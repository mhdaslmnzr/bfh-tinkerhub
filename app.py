from flask import Flask, redirect, url_for, render_template, request,send_from_directory,flash,send_file,after_this_request
import os
import pickle
import lalmam
import itertools 

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
UPLOAD_FOLDER = 'test'



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/" , methods = ["GET", "POST"])
def main_page():


	

	if request.method == "POST":		


		
		


		# try :
			img = request.files["file_uploaded"]
			#img.save(os.path.join(app.config['UPLOAD_FOLDER'],img.filename))
			
			
			if img.filename.lower().endswith(('.jpg','.jpeg','.png')):
				

				msg_ret = lalmam.mainFunction(img) 
				if (msg_ret[0] == "Sorry no faces found in the image!"):

					imges = list('static/images/nop/images.jpg')

					return render_template("home.html", msg = msg_ret[0] , cont_imr= zip(msg_ret, imges))
				else :
					
					imges = os.listdir('static/images/process')
					for i in range(len(imges)):
						j = 'static/images/process/'+ imges[i]
						imges[i] = j
						
					return render_template("home.html" , cont_imgr = zip(msg_ret,imges))
					 
			else :
				return render_template("home.html" , msg = "Upload an image file")

				

		# except :
			
		# 	return	render_template("home.html" , msg = "Please upload a file and try again")	




	return render_template("home.html" , msg = "Upload a file")


























if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=port)


