![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Tinkerhub BFH-Project
This is an image classifier for popular malayalam actors lalettan and mammookka.  
Uses [ageitgey|face_recognition](https://github.com/ageitgey/face_recognition) to detect faces and to build face encodings.  Classifier used is [SVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) classsifier.  
Pretrained model was trained using [this](https://drive.google.com/drive/folders/1cAXZYF77T110ewctVQMWZrXeffsQM1Zb?usp=sharing) dataset.
Works on images that has both the actors in it.  
[Live App](https://ettan-ikka-classifier.herokuapp.com/)
## Team members
1. [Mohammed Aslam](https://github.com/dpjr47)
2. [Sagar Krishna](https://github.com/sagarkrishna1729)
3. [Muhammed Sabah](https://github.com/mhdsabah)
## Team Id
BFH/recfJguBvrn88uh8W/2021



##  How it works
 Step 1: face_recognition library will extract faces from image and face encoding data.  
 Step 2. The training data would be all the face encodings from all the known images and the labels are their names.  
 Step 3: svm classifier is trained with known face encodings and labels   
 Step 4. During testing an unknown face encoding is provided to the model
 Step 5. Output is obtained 

## Libraries used
 [Face recognition](https://github.com/ageitgey/face_recognition)  
 sklearn  
 flask - for deployment
 dlib - for face_recognition




## How to configure

Using  [pip](https://pip.pypa.io/en/stable/)

```bash
pip install -r requirements.txt
```

or 
```bash
docker build .
```

## How to run
For flask run :-
```python
python app.py 
```

## To use this to train your own model for other persons images 
Make a directory containing images in the following order   :
```tree
--directory_name
    |-----Images of person 1
    |-----Images of person 2
     ....
    |-----Images of person N
```
and run 
```bash
python train.py directory_name
```
To test the model : First make a directory containing test images.
```bash
python test.py <modelname> <test_image_directory>
```




## References
[Face recognition](https://github.com/ageitgey/face_recognition)  
[ Develop a Face Recognition System](https://machinelearningmastery.com/how-to-develop-a-face-recognition-system-using-facenet-in-keras-and-an-svm-classifier/)
