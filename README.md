# Tinkerhub BFH-Project
This is an image classifier for popular malayalam actors lalettan and mammookka.  
Uses [ageitgey|face_recognition](https://github.com/ageitgey/face_recognition) to detect faces and to build face encodings.  Classifier used is [SVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) classsifier.  
Pretrained model was trained using [this](https://drive.google.com/drive/folders/1cAXZYF77T110ewctVQMWZrXeffsQM1Zb?usp=sharing) dataset.  



## Installation

Using  [pip](https://pip.pypa.io/en/stable/)

```bash
pip install -r requirements.txt
```

or 
```bash
docker build .
```

## Usage
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
