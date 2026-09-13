import os, random, shutil

# Define the path containing the collected images 
SRC = 'Tensorflow/workspace/images/collectedimages'

#Define  folders for training and testing datasets 
TRAIN = 'Tensorflow/workspace/images/train'
TEST = 'Tensorflow/workspace/images/test'

#ratio of images to be used for training 
SPLIT = 0.8

os.makedirs(TRAIN, exist_ok=True)
os.makedirs(TEST, exist_ok=True)

for label in os.listdir(SRC):
    label_dir = os.path.join(SRC, label)
    if not os.path.isdir(label_dir):
        continue
    images = [f for f in os.listdir(label_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)
    split_idx = int(len(images) * SPLIT)
    train_imgs, test_imgs = images[:split_idx], images[split_idx:]

    for img_set, dest in [(train_imgs, TRAIN), (test_imgs, TEST)]:
        for img in img_set:
            base, orig_ext = os.path.splitext(img)
            for ext in [orig_ext, '.xml']:
                src_file = os.path.join(label_dir, base + ext)

                #Copy the file if it exits
                if os.path.exists(src_file):
                    shutil.copy(src_file, os.path.join(dest, base + ext))

print("Split complete.")
