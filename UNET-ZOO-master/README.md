# UNET-ZOO
including unet,unet++,attention-unet,r2unet,cenet,segnet ,fcn.

# ENVIRONMENT
window10(Ubuntu is OK)+pycharm+python3.6+pytorch1.3.1  

## HOW TO RUN:
The only thing you should do is enter the dataset.py and correct the path of the datasets.
then run ~
example:
```
python main.py --action train&test --arch UNet --epoch 21 --batch_size 21 
```
## RESULTS
after train and test,3 folders will be created,they are "result","saved_model","saved_predict".

### saved_model folder:
After training,the saved model is in this folder.
