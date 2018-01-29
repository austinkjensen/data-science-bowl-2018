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

# from PIL import Image
import os
import model
import wrangler

DATA_DIR = 'data/'
TRAIN_DIR = 'stage1_train/'
TEST_DIR = 'stage1_test/'
IMAGES_SUB_DIR = 'images/'
MASKS_SUB_DIR = 'masks/'

def scrub_pics():
	'''Let's check out these dank pics.
	'''
	# Grab locations of PNG training data (not raw data)
	train_in = []
	train_out = []
	train_data_dir = DATA_DIR + TRAIN_DIR
	for el in os.listdir(train_data_dir):
		el_rel = os.path.join(train_data_dir, el)
		images_rel = os.path.join(el_rel, IMAGES_SUB_DIR)
		masks_rel = os.path.join(el_rel, MASKS_SUB_DIR)
		train_in.append([os.path.join(images_rel, x) for x in os.listdir(images_rel)])
		train_out.append([os.path.join(masks_rel, x) for x in os.listdir(masks_rel)])

	print(train_in)
	image_id = '7ba20aa731cc21af74a8d940254176cbad1bdc44f240b550341c6d9c27509daa'
	image = Image.open(DATA_DIR + TRAIN_DIR + image_id + '/images/' + image_id + '.png')
	image.show()

if __name__ == '__main__':
	print('Literally, Hello, World')
	scrub_pics()
