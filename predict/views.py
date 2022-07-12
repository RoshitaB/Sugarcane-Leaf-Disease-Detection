from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import numpy as np
import keras
from keras.models import load_model

model=load_model('models/Final_DenseNetSVM_Model.h5')

def index(request):
    context={'a':1}
    return render(request,'index.html',context)

img_height, img_width=224,224

def predictImage(request):
    # print (request)
    # print (request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName

    img = keras.utils.load_img(testimage, target_size=(img_height, img_width))
    x = keras.utils.img_to_array(img)
    x=x/255
    x=x.reshape(img_height, img_width,3)
    x = np.expand_dims(x, axis=0)

    predi=model.predict(x)
    # print(predi)

    classes=["Healthy","Red Rot", "Red Rust"]      
    MaxPosition=np.argmax(predi)  

    global prediction_label
    prediction_label=prediction_label=classes[MaxPosition]
    print(prediction_label)

    if(prediction_label=="Healthy"):
        pred_flag=True
    else:
        pred_flag=False

    context={'filePathName':filePathName,'predictedLabel':prediction_label,'pred_flag':pred_flag}
    return render(request,'result.html',context) 



