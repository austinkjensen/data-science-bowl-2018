#!/usr/bin/env python

'''Let's go all Christopher Columbus on this dataset.

Without the carnage of Natives.
'''

from PIL import Image

DATA_DIR = 'data/'
TRAIN_DIR = 'stage1_train/'
IMAGE_SUB_DIR = 'images/'
MASKS_SUB_DIR = 'masks/'
TEST_DIR = 'stage1_test/'

def scrub_pics():
	'''Let's check out these dank pics.
	'''
	image_id = '7ba20aa731cc21af74a8d940254176cbad1bdc44f240b550341c6d9c27509daa'
	image = Image.open(DATA_DIR + TRAIN_DIR + image_id + '/images/' + image_id + '.png')
	image.show()

if __name__ == '__main__':
	print('Literally, Hello, World')
	scrub_pics()

