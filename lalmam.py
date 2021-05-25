import os 
import face_recognition as fp
from sklearn import svm
import numpy as np
import pickle
from PIL import Image







def mainFunction(ipFile):

	img = fp.load_image_file(ipFile)
	face_loc = fp.face_locations(img)
	#print(ipFile.filename)
	file_name = ipFile.filename
	no_of_faces = len(face_loc)

	model = pickle.load(open("model.sav", "rb"))
	ret = []

	if no_of_faces != 0: 
	
		for j in range(no_of_faces):
			img_enc = fp.face_encodings(img)[j]
			name = str(model.predict([img_enc]))
			name = name.replace("['","").replace("']","")
		
			pb = model.predict_proba([img_enc])
			
			printImage(face_loc[j], img,j)

			if checkProb :
				ret.append(name)
			else :
				ret.append( "I am confused! Who is this")

		
		
	else :

		ret.append("Sorry no faces found in the image!")	

	return ret			





def printImage(inputloc , image, it):
	
	top, right, bottom, left = inputloc
	
	    
	face_image = image[top:bottom, left:right]
	new_image = Image.fromarray(face_image)
	new_image = new_image.resize((160,160))
	new_image.save("static/images/process/{}.jpg".format(it))
	

	


		    








def checkProb(name , prob):
	
	if name == 'lalettan':
		val = round(prob[0,0]*100 ,2)

		if val > 96:
			return True
		else:
			return False	
	elif name  == 'mammookka':
		val =val = round(prob[0,1]*100 ,2)

		if val > 96:
			return True
		else:
			return False
	else :
		
		return True