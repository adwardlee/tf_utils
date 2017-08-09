import argparse
import os
import sys
import math
import cv2
import numpy as np
import multiprocessing
import tensorflow as tf
from inception_resnet_v2 import *
import urllib2

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
slim = tf.contrib.slim

model_path = './res_models'

video_path = '/media/llj/storage/microsoft-corpus/youtube_frame_flow'

#video_train_feature_file = '/media/llj/storage/all_sentences/msvd_inception_globalpool_train_origin.txt'

#video_test_feature_file = '/media/llj/storage/all_sentences/msvd_inception_globalpool_test_origin.txt'

video_train_sent_file = '/media/llj/storage/all_sentences/msvd_sents_train_lc_nopunc.txt'

video_test_sent_file = '/media/llj/storage/all_sentences/msvd_sents_test_lc_nopunc.txt'

vocabulary_file = '/media/llj/storage/all_sentences/coco_msvd_allvocab.txt'

dim_image = 1536
lstm_dim = 1000
word_dim = 500

n_lstm_step = 60
n_caption_lstm_step = 35
n_video_lstm_step = 25

n_epochs = 20
batch_size = 4
start_learning_rate = 0.01
width = 299
height = 299


def read_source_file(data_file):
	vid = []
	image_dirs = {}
	with open(data_file,'r') as files:
		for x in files:
			vid_name = x.strip().split(',')[0]
			if vid_name not in vid:
				vid.append(vid_name)
			if vid_name not in image_dirs:
				image_dirs[vid_name] = []
			image_dirs[vid_name].append(x.strip().split(',')[1])
	assert len(vid) == len(image_dirs)
	return vid,image_dirs

def image_reading_processing(path):
    video_batch = []
    for j in xrange(n_video_lstm_step):
        #image_string = urllib2.read()
            #filename_queue = tf.train.string_input_producer([path[j]])
            #reader = tf.WholeFileReader()
            #key, value = reader.read(filename_queue)
            #with tf.gfile.FastGFile(path[j], 'rb') as f:
            #    image_data = f.read()
            #image = tf.image.decode_jpeg(image_data, channels=3)
            #if image.dtype != tf.float32:
            #    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
            #image = tf.expand_dims(image, 0)
            #image = tf.image.resize_bilinear(image, [299,299], align_corners=False)
            #image = tf.subtract(image, 0.5)
            #image = tf.multiply(image, 2.0)
            image = cv2.imread(path[j], cv2.IMREAD_COLOR)### height,width,channels
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (299, 299))
            image = 2 * (image/255.0) - 1

            video_batch.append(image)
    return video_batch

def build_model():
    video_frames = tf.placeholder(tf.float32,[n_video_lstm_step, 299, 299, 3])
    all_frames = video_frames

    with slim.arg_scope(inception_resnet_v2_arg_scope()):
        with tf.variable_scope('InceptionResnetV2', 'InceptionResnetV2',
                               reuse=None) as scope:
            with slim.arg_scope([slim.batch_norm, slim.dropout],
                                is_training=False):
                net, endpoints = inception_resnet_v2_base(all_frames, scope=scope)
                net = slim.avg_pool2d(net, net.get_shape()[1:3], padding='VALID', scope = 'AvgPool_1a_8x8')
                net = slim.flatten(net)
    video = tf.reshape(net, [n_video_lstm_step, 1536])
    return video, video_frames

vid, image_dirs = read_source_file('/media/llj/storage/processed-data-ms/train_25frame_list.txt')
output_file = open('tf_inceptionres_v2_train_feature2.txt','w')
features, frames = build_model()
config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
sess = tf.InteractiveSession(config=config)
saver = tf.train.Saver(max_to_keep=100, write_version=1)
############## clipping every gradient####
#train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(tf_loss, global_step=global_step)
tf.global_variables_initializer().run()
#tf.summary.scalar('lr',learning_rate)
saver.restore(sess,'inception_resnet_v2_2016_08_30.ckpt')
for index in vid:
    frame_num = 1
    one_video = image_reading_processing(image_dirs[index])
    one_videos = sess.run(one_video)
    out_feature = sess.run(features, feed_dict = {frames: one_videos})
    for num in xrange(len(out_feature)):
        output_fea = out_feature[num,:]
        output_file.write(index + '_frame_' + str(frame_num) + ',' +\
							  ','.join(str(x) for x in output_fea.tolist()) + '\n')
        frame_num += 1


