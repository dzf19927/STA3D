import io
import os
import sys
import math
import random
import numpy as np
from scipy.misc import imread, imresize


def load_video_list(path):
  f = open(path, 'r')
  f_lines = f.readlines()
  f.close()
  video_data = {} 
  video_label = []
  for idx, line in enumerate(f_lines):
    video_key = '%06d' % idx
    video_data[video_key] = {} 
    videopath  = line.split(' ')[0]
    if '\xef\xbb\xbf' in videopath:
      videopath=videopath.replace('\xef\xbb\xbf','')
    framecnt   = int(line.split(' ')[1])
    videolabel = int(line.split(' ')[2])
    video_data[video_key]['videopath'] = videopath
    video_data[video_key]['framecnt'] = framecnt
    video_label.append(videolabel)
  return video_data,video_label

def prepare_isogr_rgb_data(image_info):
  video_path = image_info[0]
  video_frame_cnt = image_info[1]
  output_frame_cnt = image_info[2]
  is_training = image_info[3]
  rand_frames = np.zeros(output_frame_cnt)
  div = float(video_frame_cnt)/float(output_frame_cnt)
  scale = math.floor(div)
  if is_training:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(0, video_frame_cnt)
      rand_frames[video_frame_cnt::] = video_frame_cnt-1
    elif scale == 1:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt) + \
                        float(scale)/2*(np.random.random(size=output_frame_cnt)-0.5)
  else:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(0, video_frame_cnt)
      rand_frames[video_frame_cnt::] = video_frame_cnt-1
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
  rand_frames[0] = max(rand_frames[0], 0)
  rand_frames[output_frame_cnt-1] = min(rand_frames[output_frame_cnt-1], video_frame_cnt-1)
  rand_frames = np.floor(rand_frames)+1

  average_values = [105,108,112]
  processed_images = np.empty((output_frame_cnt, 224, 224, 3), dtype=np.float32)
  crop_random = random.random()
  for idx in xrange(0, output_frame_cnt):
    image_file = '%s%06d.jpg' %(video_path, rand_frames[idx])
    image = imread(image_file)
    image_h, image_w, image_c = np.shape(image)
    square_sz = min(image_h, image_w)
    if is_training:
      crop_h = int((image_h - square_sz)*crop_random)
      crop_w = int((image_w - square_sz)*crop_random)
    else:
      crop_h = int((image_h - square_sz)/2)
      crop_w = int((image_w - square_sz)/2)
    image_crop = image[crop_h:crop_h+square_sz,crop_w:crop_w+square_sz,::]
    processed_images[idx] = imresize(image_crop, (224,224)) - average_values
  return processed_images

def prepare_isogr_depth_data(image_info):
  video_path = image_info[0]
  video_frame_cnt = image_info[1]
  output_frame_cnt = image_info[2]
  is_training = image_info[3]
  rand_frames = np.zeros(output_frame_cnt)
  div = float(video_frame_cnt)/float(output_frame_cnt)
  scale = math.floor(div)
  if is_training:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(0, video_frame_cnt)
      rand_frames[video_frame_cnt::] = video_frame_cnt-1
    elif scale == 1:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt) + \
                        float(scale)/2*(np.random.random(size=output_frame_cnt)-0.5)
  else:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(0, video_frame_cnt)
      rand_frames[video_frame_cnt::] = video_frame_cnt-1
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
  rand_frames[0] = max(rand_frames[0], 0)
  rand_frames[output_frame_cnt-1] = min(rand_frames[output_frame_cnt-1], video_frame_cnt-1)
  rand_frames = np.floor(rand_frames)+1

  average_values = [169,171,169] 
  processed_images = np.empty((output_frame_cnt, 224, 224, 3), dtype=np.float32)
  crop_random = random.random()
  for idx in xrange(0, output_frame_cnt):
    image_file = '%s%06d.jpg' %(video_path, rand_frames[idx])
    image = imread(image_file)
    image_h, image_w, image_c = np.shape(image)
    square_sz = min(image_h, image_w)
    if is_training:
      crop_h = int((image_h - square_sz)*crop_random)
      crop_w = int((image_w - square_sz)*crop_random)
    else:
      crop_h = int((image_h - square_sz)/2)
      crop_w = int((image_w - square_sz)/2)
    image_crop = image[crop_h:crop_h+square_sz,crop_w:crop_w+square_sz,::]
    processed_images[idx] = imresize(image_crop, (224,224)) - average_values
  return processed_images

def prepare_isogr_flow_data(image_info):
  video_path = image_info[0]
  video_frame_cnt = image_info[1]
  output_frame_cnt = image_info[2]
  is_training = image_info[3]
  rand_frames = np.zeros(output_frame_cnt)
  div = float(video_frame_cnt)/float(output_frame_cnt)
  scale = math.floor(div)
  if is_training:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(0, video_frame_cnt)
      rand_frames[video_frame_cnt::] = video_frame_cnt-1
    elif scale == 1:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt) + \
                        float(scale)/2*(np.random.random(size=output_frame_cnt)-0.5)
  else:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(0, video_frame_cnt)
      rand_frames[video_frame_cnt::] = video_frame_cnt-1
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
  rand_frames[0] = max(rand_frames[0], 0)
  rand_frames[output_frame_cnt-1] = min(rand_frames[output_frame_cnt-1], video_frame_cnt-1)
  rand_frames = np.floor(rand_frames)+1

  average_values = [248,246,248] 
  processed_images = np.empty((output_frame_cnt, 224, 224, 3), dtype=np.float32)
  crop_random = random.random()
  for idx in xrange(0, output_frame_cnt):
    image_file = '%s%06d.jpg' %(video_path, rand_frames[idx])
    #assert os.path.exists(image_file)
    image = imread(image_file)
    image_h, image_w, image_c = np.shape(image)
    square_sz = min(image_h, image_w)
    if is_training:
      crop_h = int((image_h - square_sz)*crop_random)
      crop_w = int((image_w - square_sz)*crop_random)
    else:
      crop_h = int((image_h - square_sz)/2)
      crop_w = int((image_w - square_sz)/2)
    image_crop = image[crop_h:crop_h+square_sz,crop_w:crop_w+square_sz,::]
    processed_images[idx] = imresize(image_crop, (224,224)) - average_values
  return processed_images

def prepare_skig_rgb_data(image_info):
  video_path = image_info[0]
  video_frame_cnt = image_info[1]
  output_frame_cnt = image_info[2]
  is_training = image_info[3]
  rand_frames = np.zeros(output_frame_cnt)
  div = float(video_frame_cnt)/float(output_frame_cnt)
  scale = math.floor(div)
  if is_training:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(1, video_frame_cnt+1)
      rand_frames[video_frame_cnt::] = video_frame_cnt
    elif scale == 1:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt) + \
                        float(scale)/2*(np.random.random(size=output_frame_cnt)-0.5)
  else:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(1, video_frame_cnt+1)
      rand_frames[video_frame_cnt::] = video_frame_cnt
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
  rand_frames[0] = max(rand_frames[0], 1)
  rand_frames[output_frame_cnt-1] = min(rand_frames[output_frame_cnt-1], video_frame_cnt)
  rand_frames = np.floor(rand_frames)

  average_values = [132,112,96]
  processed_images = np.empty((output_frame_cnt, 112, 112, 3), dtype=np.float32)
  crop_random = random.random()
  for idx in xrange(0,output_frame_cnt):
    image_file = '%s/%04d.jpg' %(video_path, rand_frames[idx])
    image = imread(image_file)
    image_h, image_w, image_c = np.shape(image)
    square_sz = min(image_h, image_w)
    if is_training:
      crop_h = int((image_h - square_sz)*crop_random)
      crop_w = int((image_w - square_sz)*crop_random)
    else:
      crop_h = int((image_h - square_sz)/2)
      crop_w = int((image_w - square_sz)/2)
    image_crop = image[crop_h:crop_h+square_sz,crop_w:crop_w+square_sz,::]
    processed_images[idx] = imresize(image_crop, (112,112)) - average_values
  return processed_images

def prepare_skig_depth_data(image_info):
  video_path = image_info[0]
  video_frame_cnt = image_info[1]
  output_frame_cnt = image_info[2]
  is_training = image_info[3]
  rand_frames = np.zeros(output_frame_cnt)
  div = float(video_frame_cnt)/float(output_frame_cnt)
  scale = math.floor(div)
  if is_training:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(1, video_frame_cnt+1)
      rand_frames[video_frame_cnt::] = video_frame_cnt
    elif scale == 1:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt) + \
                        float(scale)/2*(np.random.random(size=output_frame_cnt)-0.5)
  else:
    if scale == 0:
      rand_frames[0:video_frame_cnt] = np.arange(1, video_frame_cnt+1)
      rand_frames[video_frame_cnt::] = video_frame_cnt
    else:
      rand_frames[::] = div*np.arange(0, output_frame_cnt)
  rand_frames[0] = max(rand_frames[0], 1)
  rand_frames[output_frame_cnt-1] = min(rand_frames[output_frame_cnt-1], video_frame_cnt)
  rand_frames = np.floor(rand_frames)

  average_values = [237,237,237]
  processed_images = np.empty((output_frame_cnt, 112, 112, 3), dtype=np.float32)
  crop_random = random.random()
  for idx in xrange(0,output_frame_cnt):
    image_file = '%s/%04d.jpg' %(video_path, rand_frames[idx])
    image = imread(image_file)
    image_h, image_w, image_c = np.shape(image)
    square_sz = min(image_h, image_w)
    if is_training:
      crop_h = int((image_h - square_sz)*crop_random)
      crop_w = int((image_w - square_sz)*crop_random)
    else:
      crop_h = int((image_h - square_sz)/2)
      crop_w = int((image_w - square_sz)/2)
    image_crop = image[crop_h:crop_h+square_sz,crop_w:crop_w+square_sz,::]
    processed_images[idx] = imresize(image_crop, (112,112)) - average_values
  return processed_images

