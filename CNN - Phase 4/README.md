# CNN - Phase 4

The purpose of building the CNN was to train it on fMRI files and attempt to classify depression based on this data. We used the [VGG-16](https://arxiv.org/pdf/1409.1556.pdf) classifier to solve this problem. 

The model was tested and trained on fMRI images of patients that were listening to various types of music. There were 21 "normal" patients and 20 patients marked with depression. 

The images given were a .nii format, a NIfTI-1 Data Format used to store 3D and 4D MRI images. The [med2image](https://github.com/FNNDSC/med2image) python utility was used to convert the .nii files to .jpgs. 

The Caffe Deep Learning Framework (see below) was used to train the data. Due to the extraordinary time constraints, Caffe was used for its speed. An AWS Server with a NVIDIA Tesla K80 GPU was used to train the data. The Caffe Model can be seen above. No modifications were made to the model (upcoming?). 



NVIDIA Digits was used to visualize and train the data.

## Dependencies
This project has special Dependencies.
### Installation
* [Caffe](http://caffe.berkeleyvision.org/)
* [Digits](https://developer.nvidia.com/digits)
