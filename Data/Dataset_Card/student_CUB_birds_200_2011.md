CUB200-2011数据集介绍：
        该数据集由加州理工学院再2010年提出的细粒度数据集，也是目前细粒度分类识别研究的基准图像数据集。

        该数据集共有11788张鸟类图像，包含200类鸟类子类，其中训练数据集有5994张图像，测试集有5794张图像，每张图像均提供了图像类标记信息，图像中鸟的bounding box，鸟的关键part信息，以及鸟类的属性信息，数据集如下图所示。



下载的数据集中，包含了如下文件：

bounding_boxes.txt；classes.txt；image_class_labels.txt； images.txt； train_test_split.txt.

其中，bounding_boxes.txt为图像中鸟类的边界框信息；classes.txt为鸟类的类别信息，共有200类； image_class_labels.txt为图像标签和所属类别标签信息；images.txt为图像的标签和图像路径信息；train_test_split.txt为训练集和测试集划分。

本博客主要是根据train_test_split.txt文件和images.txt文件将原始下载的CUB200-2011数据集划分为训练集和测试集。在深度学习Pytorch框架下采用ImageFolder和DataLoader读取数据集较为方便。相关的python代码如下：

(1) CUB200-2011训练集和测试集划分代码
 # *_*coding: utf-8 *_*
 # author --liming--
 
"""
读取images.txt文件,获得每个图像的标签
读取train_test_split.txt文件,获取每个图像的train, test标签.其中1为训练,0为测试.
"""
 
import os
import shutil
import numpy as np
import config
import time
 
time_start = time.time()
 
# 文件路径
path_images = config.path + 'images.txt'
path_split = config.path + 'train_test_split.txt'
trian_save_path = config.path + 'dataset/train/'
test_save_path = config.path + 'dataset/test/'
 
# 读取images.txt文件
images = []
with open(path_images,'r') as f:
    for line in f:
        images.append(list(line.strip('\n').split(',')))
 
# 读取train_test_split.txt文件
split = []
with open(path_split, 'r') as f_:
    for line in f_:
        split.append(list(line.strip('\n').split(',')))
 
# 划分
num = len(images) # 图像的总个数
for k in range(num):
    file_name = images[k][0].split(' ')[1].split('/')[0]
    aaa = int(split[k][0][-1])
    if int(split[k][0][-1]) == 1: # 划分到训练集
        #判断文件夹是否存在
        if os.path.isdir(trian_save_path + file_name):
            shutil.copy(config.path + 'images/' + images[k][0].split(' ')[1], trian_save_path+file_name+'/'+images[k][0].split(' ')[1].split('/')[1])
        else:
            os.makedirs(trian_save_path + file_name)
            shutil.copy(config.path + 'images/' + images[k][0].split(' ')[1], trian_save_path + file_name + '/' + images[k][0].split(' ')[1].split('/')[1])
        print('%s处理完毕!' % images[k][0].split(' ')[1].split('/')[1])
    else:
         #判断文件夹是否存在
         if os.path.isdir(test_save_path + file_name):
             aaaa = config.path + 'images/' + images[k][0].split(' ')[1]
             bbbb = test_save_path+file_name+'/'+images[k][0].split(' ')[1]
             shutil.copy(config.path + 'images/' + images[k][0].split(' ')[1], test_save_path+file_name+'/'+images[k][0].split(' ')[1].split('/')[1])
         else:
             os.makedirs(test_save_path + file_name)
             shutil.copy(config.path + 'images/' + images[k][0].split(' ')[1], test_save_path + file_name + '/' + images[k][0].split(' ')[1].split('/')[1])
         print('%s处理完毕!' % images[k][0].split(' ')[1].split('/')[1])
 
time_end = time.time()
print('CUB200训练集和测试集划分完毕, 耗时%s!!' % (time_end - time_start))
config文件
# *_*coding: utf-8 *_*
# author --liming--
 
path = '/media/lm/C3F680DFF08EB695/细粒度数据集/birds/CUB200/CUB_200_2011/'
 
ROOT_TRAIN = path + 'images/train/'
ROOT_TEST = path + 'images/test/'
BATCH_SIZE = 16
(2) 利用Pytorch方式读取数据
# *_*coding: utf-8 *_*
# author --liming--
 
"""
用于已下载数据集的转换,便于pytorch的读取
"""
 
import torch
import torchvision
import config
from torchvision import datasets, transforms
 
data_transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
 
def train_data_load():
    # 训练集
    root_train = config.ROOT_TRAIN
    train_dataset = torchvision.datasets.ImageFolder(root_train,
                                                     transform=data_transform)
    CLASS = train_dataset.class_to_idx
    print('训练数据label与文件名的关系:', CLASS)
    train_loader = torch.utils.data.DataLoader(train_dataset,
                                               batch_size=config.BATCH_SIZE,
                                               shuffle=True)
    return CLASS, train_loader
 
def test_data_load():
    # 测试集
    root_test = config.ROOT_TEST
    test_dataset = torchvision.datasets.ImageFolder(root_test,
                                                transform=data_transform)
 
    CLASS = test_dataset.class_to_idx
    print('测试数据label与文件名的关系：',CLASS)
    test_loader = torch.utils.data.DataLoader(test_dataset,
                                              batch_size=config.BATCH_SIZE,
                                              shuffle=True)
    return CLASS, test_loader
 
if __name__ == '__main___':
    train_data_load()
    test_data_load()