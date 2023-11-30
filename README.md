# Sugarcane-Leaf-Disease-Detection

This project allows the detection of abnormalities that maybe present on the leaves of the Sugarcane plant and classify/recognize the disease accordingly. 

### Dataset:
Link to Dataset: https://www.kaggle.com/datasets/roshitab/sugarcane-leaf-disease-dataset
* Created by visiting a local sugarcane farm and collecting on-ground images.
* It consists of **224 images** of healthy and diseased crop leaves
* The dataset has 3 classes - **Healthy**, **Red Rot**, **Red Rust**. 
  * **Healthy:** 75 Images
  * **Red Rot:** 74 Images
  * **Red Rust:** 75 Images

### Methodology:
Transfer Learning approach was implemented with the help of **DenseNet201** architecture. To improve the accuracy of the model, **Support Vector Machine (SVM)** was incorporated in the final layer of the model. An **Accuracy** of **98%** and a **Validation Accuracy** of **97.78%** was obtained.

### Results:
![Alt text](/media/output/home.png "Home Page")

![Alt text](/media/output/prediction.png "Prediction Page")
