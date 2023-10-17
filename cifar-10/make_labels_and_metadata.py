import random
import os

# get label list
data_path = r"CIFAR-10-images"
label_list = os.listdir(data_path + '/train')
label_list = sorted(label_list)

labels_and_metadata = []

# train client
image_id = list(range(0,50000))
random.shuffle(image_id)


for client_id in range(0, 1000):
    start_img = client_id * 50
    end_img = client_id * 50 + 50

    for image_index in range(start_img, end_img):
        image = image_id[image_index]
        label = label_list[image//5000]
        metadata = {
        "user_id": str(client_id),
        "image_id": "{:05d}".format(image),
        "labels": [
            label,
        ],
        "partition": "train",
        "fine_grained_labels": [
        ]
        }
        labels_and_metadata.append(metadata)

# test client
image_id = list(range(50000,60000))
random.shuffle(image_id)

for client_id in range(1000, 1200):
    start_img = (client_id - 1000) * 50
    end_img = (client_id - 1000) * 50 + 50

    val_or_test = "val" if random.random() > 0.5 else "test"

    for image_index in range(start_img, end_img):
        image = image_id[image_index]
        label = label_list[(image - 50000)//1000]
        metadata = {
        "user_id": str(client_id),
        "image_id": str(image),
        "labels": [
            label,
        ],
        "partition": val_or_test,
        "fine_grained_labels": [
        ]
        }
        labels_and_metadata.append(metadata)

# labels_and_metadata.json 
import json

with open(r"/home/work/seongbin/cifar-10/CIFAR-10-images/labels_and_metadata.json", 'w') as f:
    json.dump(labels_and_metadata, f, indent=4)
