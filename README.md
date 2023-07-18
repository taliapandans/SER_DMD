# Decouple Multimodal Distilling for Speech Emotion Recognition
This is one of the model that we proposed for Advanced Projects at the Quality and Usability Lab at TU Berlin. We refer to this [paper](https://arxiv.org/pdf/2303.13802.pdf) and follow this approach from [Github/DMD](https://github.com/mdswyz/DMD/tree/main).

Data files consist of MOSI and MOSEI datasets can be found [here](https://drive.google.com/drive/folders/17eayDmZSljt3Sf-V1qPr_c-UlC3rJ9gE?usp=drive_link).

The datasets are placed into the folder `./dataset`. 

By default, the trained model will be saved in folder `./pt`. Our trained model can be download from [pt folder](https://drive.google.com/drive/folders/1gul8V-dBdH9LkALqPouIqJ3j4R7Dn6l4?usp=drive_link)

If there is no difference in validation loss during, the last model contains layers and weights will be additionally saved in `./dmd.pth`.
Before testing the model we set the path of trained model in run.py (line 174). The results are saved into folder `./result`

We run the codes on google colab, implemented under the .ipynb file `Unimse_Submission`. 

### Current result:
- `Acc_2: 0.8430  F1_score: 0.8437  Acc_7: 0.4548  MAE: 0.7334  Loss: 0.7334`

### Goals:
- Create IEMOCAP or EMODB datasets and train these datasets
- Fine tune the model
