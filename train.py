
import numpy
from numpy import load
from numpy import expand_dims
import os
from sklearn import svm
import sys
import face_recognition



print(os.getcwd())
train_dir = os.listdir(sys.argv[1])

encodings = []
names = []

llll = 0
for person in train_dir:
    pix = os.listdir(sys.argv[1]+"/" + person)

    # Loop through each training image for the current person
    for person_img in pix:
        llll+=1
        # Get the face encodings for the face in each image file
        face = face_recognition.load_image_file(sys.argv[1]+"/"+person+"/" +person_img)
        face_bounding_boxes = face_recognition.face_locations(face)

        #If training image contains exactly one face
        if len(face_bounding_boxes) == 1:
            face_enc = face_recognition.face_encodings(face)[0]
            # Add face encoding for current image with corresponding label (name) to the training data
            encodings.append(face_enc)
            names.append(person)
        else:
            print(person + "/" + person_img + " was skipped and can't be used for training")

        print(llll)    

### Uncomment the below if you need to save the face encodings
####Incase to refit the model in another machine you can save the face encoding if you are training on same data set 
### Or to add add another face data later save the current face encoding to save time
# trainx = numpy.asarray(encodings)
# trainy = numpy.asarray(names)
# numpy.savez_compressed('face_reg_encodings.npz', trainx,trainy)
####

## using support vector classifier

clf = svm.SVC(gamma = 'scale',probability=True)

clf.fit(encodings,names)


import pickle
filename = 'model.sav'
pickle.dump(clf, open(filename, 'wb'))





"""
If you need colab file go to the below link


Original file is located at
    https://colab.research.google.com/drive/1FIAvDhOEfKTQsAijHIvmJmHzu-Zd63aV
"""
