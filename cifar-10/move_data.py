import os
import shutil

# cifar10
# for train dataset
data_path = r"CIFAR-10-images"
label_list = os.listdir(data_path + '/train')
label_list = sorted(label_list)

label_plus_index = dict()

for index, label in enumerate(label_list):
    label_plus_index[label] = index * 5000

for label in label_list:
    cur_path = data_path + '/train/' + label 
    dest_path = data_path + '/all_data'
    for i in range(0, 5000):
        shutil.copy(cur_path + '/{:04d}.jpg'.format(i), dest_path + '/{:05d}.jpg'.format(i + label_plus_index[label]))

# for test dataset
data_path = r"CIFAR-10-images"
label_list = os.listdir(data_path + '/test')
label_list = sorted(label_list)

label_plus_index = dict()

for index, label in enumerate(label_list):
    label_plus_index[label] = index * 1000

for label in label_list:
    cur_path = data_path + '/test/' + label 
    dest_path = data_path + '/all_data'
    for i in range(0, 1000):
        shutil.copy(cur_path + '/{:04d}.jpg'.format(i), dest_path + '/{:05d}.jpg'.format(i + label_plus_index[label] + 50000))