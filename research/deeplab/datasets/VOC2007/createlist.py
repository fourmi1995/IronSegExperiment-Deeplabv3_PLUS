import os
trainPath = '/home/fourmi/桌面/models/research/deeplab/VOC2007/JPEGImages/'
#testPath = '/home/fourmi/桌面/IronData_Camvid/testing/imgs/'

for root, dirs, files in os.walk(trainPath):
    for file in files:
        f = open('train.txt','a')
        f.write(file[:-4]+'\n')
        f.close()

#for root, dirs, files in os.walk(testPath):
#    for file in files:
#        f = open('test.txt','a')
#        f.write('./IronData_Camvid/testing/imgs/'+file+' '+'./IronData_Camvid/testing/labels/'+file+'\n')
f.close()
