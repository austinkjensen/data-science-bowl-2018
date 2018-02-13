#!/usr/bin/env python

'''...

Preferred process:
	1. Call main with parameters (which?)
	2. Wrangler: data parser as package (make general and extract to new project)
	3. Model: TensorFlow model is in module, interfaces tightly with data parser
	4. View/output/debug performance of model

Let's go all Christopher Columbus on this dataset.

Without the carnage of Natives.
'''

import os
import model
import wrangler

from PIL import Image
from PIL import ImageDraw

#import numpy as np
#import tensorflow as tf

DATA_DIR = 'data/'
TRAIN_DIR = 'stage1_train/'
TEST_DIR = 'stage1_test/'
IMAGES_SUB_DIR = 'images/'
MASKS_SUB_DIR = 'masks/'

def collect():
	'''Collect training data (x, y) image (PNG) locations.
	'''
	xs_locs = []
	ys_locs = []
	train_data_dir = DATA_DIR + TRAIN_DIR
	for el in os.listdir(train_data_dir):
		el_rel = os.path.join(train_data_dir, el)
		images_rel = os.path.join(el_rel, IMAGES_SUB_DIR)
		masks_rel = os.path.join(el_rel, MASKS_SUB_DIR)
		xs_locs.append([os.path.join(images_rel, x) for x in os.listdir(images_rel)])
		ys_locs.append([os.path.join(masks_rel, x) for x in os.listdir(masks_rel)])
	assert len(xs_locs) == len(ys_locs)
	return xs_locs, ys_locs


# NOTE: This takes too much memory on OS.
def actualize(xs_locs, ys_locs):
	'''Convert each image location to an actual image.
	'''
	xs, ys = ([], [])
	for i in range(len(xs_locs)):
		xs.append(Image.open(xs_locs[i][0]))
		y_i = []
		for j in range(len(ys_locs[i])):
			y_i.append(Image.open(ys_locs[i][j]))
		ys.append(y_i)
	return xs, ys

def view(loc):
	'''View pretty image.
	'''
	Image.open(loc).show()

def overlap(img_a, img_b):
	'''Overlap two image masks.
	'''
	print(img_a.size)
	w = (ima_a.size)
	pass

if __name__ == '__main__':
	print('Where my nuclei at?')
	xs_locs, ys_locs = collect()
	xs, ys = actualize(xs_locs, ys_locs)

	print(xs_locs[0])
	print(xs[0])
	xs[0].show()

	# Attempt very dangerous merge thing
	overlap(ys[0], ys[1])
















	pass
