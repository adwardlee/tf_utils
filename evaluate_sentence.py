import tensorflow as tf
import pandas as pd
import numpy as np
import os
import sys
import time
import argparse
import matplotlib.pyplot as plt
import random
import math
#from evaluation import *
import operator
from multiprocessing import Pool

sys.path.append('/home/llj/caffe/examples/spice/coco-caption-master')
from pycocoevalcap.bleu.bleu import Bleu
from pycocoevalcap.rouge.rouge import Rouge
from pycocoevalcap.cider.cider import Cider
from pycocoevalcap.meteor.meteor import Meteor
from pycocoevalcap.spice.spice import Spice
from collections import defaultdict


batch_size = 32
video_test_sent_file = '/home/llj/caffe/examples/spice/coco-caption-master/msrvtt/_test.txt'
video_ref_sent_file = '/home/llj/caffe/examples/spice/coco-caption-master/msrvtt/sent_test_file'

def score_all(ref, hypo):
    scorers = [
        (Bleu(4), ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),
        (Meteor(), "METEOR"),
        (Rouge(), "ROUGE_L"),
        (Cider(), "CIDEr"),
        (Spice(), "SPICE")
    ]
    final_scores = {}
    for scorer, method in scorers:
        score, scores = scorer.compute_score(ref, hypo)
        if type(score) == list:
            for m, s in zip(method, score):
                final_scores[m] = s
        else:
            final_scores[method] = score

    return final_scores

def evaluate_for_particular_captions(cand, ref_captions):
    ref = ref_captions
    # with open(candidate_path, 'rb') as f:
    #     cand = pickle.load(f)

    # make dictionary
    hypo = {}
    refe = {}
    for key, caption in cand.iteritems():
        hypo[key] = cand[key]
        refe[key] = ref[key]
    # compute bleu score
    final_scores = score_all(refe, hypo)

    # print out scores

    return final_scores

def get_video_feature_caption_pair(sent_file):
    sents = []
    features = {}
    with open(sent_file, 'r') as video_sent_file:
        for line in video_sent_file:
            line = line.strip()
            id_sent = line.split('\t')
            sents.append((id_sent[0], id_sent[1]))
    sents = np.array(sents)
    return sents

all_decoded_for_eval = {}
ref_decoded = {}
test_captions = get_video_feature_caption_pair(video_test_sent_file)
ref_captions = get_video_feature_caption_pair(video_ref_sent_file)

for num in xrange(0, len(test_captions), batch_size):
            videoid = test_captions[num:num + batch_size, 0]
            for id in videoid:
                if id not in all_decoded_for_eval:
                    all_decoded_for_eval[id] = []
            [all_decoded_for_eval[x].append(y) for x, y in zip(videoid, test_captions[num:num + batch_size, 1])]

for num in xrange(0, len(ref_captions), batch_size):
            videoid = ref_captions[num:num + batch_size, 0]
            for id in videoid:
                if id not in ref_decoded:
                    ref_decoded[id] = []
            [ref_decoded[x].append(y) for x, y in zip(videoid, ref_captions[num:num + batch_size, 1])]


scores = evaluate_for_particular_captions(all_decoded_for_eval, ref_decoded)
print 'finished'
