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
import numpy as np

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


def actualize(img_loc):
	'''Convert each image location to an actual image.
	'''
	return Image.open(img_loc)

def view(loc):
	'''View pretty image.
	'''
	Image.open(loc).show()

# TODO: Vectorize this function across m inputs
def overlap(img_locs):
	'''Overlap two image masks by merging together their pixel values.
	'''
	img = Image.open(img_locs[0])
	w, h = img.size
	merged = np.zeros((w, h))
	for img_loc in img_locs[1:]:
		img = Image.open(img_loc)
		assert img.size == (w, h)
		merged += np.asarray(img)
	merged_img = Image.fromarray(merged)
	merged_img.show()

if __name__ == '__main__':
	print('Where my nuclei at?')
	xs_locs, ys_locs = collect()
	# Attempt very dangerous merge thing
	sample_index = 150
	Image.open(xs_locs[sample_index][0]).show()
	overlap(ys_locs[sample_index])
















	pass
