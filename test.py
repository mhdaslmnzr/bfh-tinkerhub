import face_recognition as fp
from sklearn import svm
import os
import sys
import pickle



mod_name = sys.argv[1]
dire = sys.argv[2]


model = pickle.load(open(mod_name,'rb'))

def main():

	for i in os.listdir(dire):
		img = fp.load_image_file(dire+"/"+i)
		face_loc = fp.face_locations(img)
		no_of_faces = len(face_loc)

		for j in range(no_of_faces):
			img_enc = fp.face_encodings(img)[j]
			name = model.predict([img_enc])
			pb = model.predict_proba([img_enc])
			if checkProb :
				print(i," = ",*name)
			else :
				print(i," I am confused, who is this?")	
			    
			   




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


main()