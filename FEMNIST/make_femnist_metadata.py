from PIL import Image
import json
import os
from tqdm import tqdm
path_dir_list = ["train", "test", "val"]
labels_and_metadata = []
for partition in path_dir_list:
    file_list = os.listdir("/home/work/seongbin/leaf/data/femnist/data/{}".format(partition))
    for file in tqdm(file_list):

        with open("/home/work/seongbin/leaf/data/femnist/data/{}/{}".format(partition, file)) as f:
            data = json.load(f)

        user_list = data["users"]
        num_samples_list = data["num_samples"]
        print(user_list)
        print(num_samples_list)
        print(len(user_list))
        for index, user in enumerate(user_list):
            for sample in range(num_samples_list[index]):
                x = num_list = data["user_data"][user]["x"][sample]
                y = data["user_data"][user]["y"][sample]
                # make image from number list
                pixels = [int(pixel * 255) for pixel in x]
                image_out = Image.new("L", (28, 28))
                image_out.putdata(pixels)
                image_out.save("picture.png", "PNG")
                image_out.save("/home/work/seongbin/FEMNIST/small_images/{}_{}.png".format(user, sample), "PNG")
                # make metadata
                metadata = {
                    "user_id": user + "_val" if partition=="val" else user,
                    "image_id": "{}_{}".format(user, sample),
                    "labels": [
                        str(y),
                    ],
                    "partition": partition,
                    "fine_grained_labels": [
                    ]
                }
                labels_and_metadata.append(metadata)
# labels_and_metadata.json
import json
with open("/home/work/seongbin/FEMNIST/labels_and_metadata.json", 'w') as f:
    json.dump(labels_and_metadata, f, indent=4)