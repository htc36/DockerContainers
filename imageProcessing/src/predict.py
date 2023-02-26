'''
    Script for single prediction on an image. It puts result in the folder.
'''
import argparse
import os
import random
import time
from os import walk

import matplotlib.pyplot as plt
import numpy as np
import torch
from model import Net
from PIL import Image
from utils import ConfigL, ConfigS, download_weights

parser = argparse.ArgumentParser()

parser.add_argument(
    '-C',
    '--checkpoint-name',
    type=str,
    default='model.pt',
    help='Checkpoint name'
)

parser.add_argument(
    '-S',
    '--size',
    type=str,
    default='S',
    help='Model size [S, L]',
    choices=['S', 'L', 's', 'l']
)

parser.add_argument(
    '-I',
    '--img-path',
    type=str,
    default='',
    help='Path to the image'
)

parser.add_argument(
    '-R',
    '--res-path',
    type=str,
    default='./data/result/prediction',
    help='Path to the results folder'
)

parser.add_argument(
    '-T',
    '--temperature',
    type=float,
    default=1.0,
    help='Temperature for sampling'
)

args = parser.parse_args()

config = ConfigL() if args.size.upper() == 'L' else ConfigS()

# set seed
random.seed(config.seed)
np.random.seed(config.seed)
torch.manual_seed(config.seed)
torch.cuda.manual_seed(config.seed)
torch.backends.cudnn.deterministic = True

is_cuda = torch.cuda.is_available()
device = 'cuda' if is_cuda else 'cpu'

if __name__ == '__main__':
    ckp_path = os.path.join(config.weights_dir, args.checkpoint_name)
    print("CKP_PATH: ", ckp_path)
    print("image path: ", args.img_path)

    if not os.path.exists(args.res_path):
        os.makedirs(args.res_path)

    print("before logs")
    model = Net(
        clip_model=config.clip_model,
        text_model=config.text_model,
        ep_len=config.ep_len,
        num_layers=config.num_layers,
        n_heads=config.n_heads,
        forward_expansion=config.forward_expansion,
        dropout=config.dropout,
        max_len=config.max_len,
        device=device
    )
    print("afer logs")

    if not os.path.exists(config.weights_dir):
        os.makedirs(config.weights_dir)

    # if not os.path.isfile(ckp_path):
    if args.img_path != '':
        print("Downloading weights...")
        download_weights(ckp_path)

    # download_weights(ckp_path, args.size)

    checkpoint = torch.load(ckp_path, map_location=device)
    model.load_state_dict(checkpoint)

    model.eval()

    if args.img_path == '':
        filenames = next(walk('./input'), (None, None, []))[2]
        print(filenames)
        for filename in filenames:
            imageType = filename.split(".")[-1]
            img = Image.open('./input/' + filename)
            with torch.no_grad():
                caption, _ = model(img, args.temperature)

            plt.imshow(img)
            plt.title(caption)
            plt.axis('off')

            shorted_caption = caption.replace(" ", "_").replace(".", "")
            img.save("./output/" + shorted_caption + "." + imageType)
            plt.clf()
            plt.close()

            print('Generated Caption2: "{}"'.format(caption))
