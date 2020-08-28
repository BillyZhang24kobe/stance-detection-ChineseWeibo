#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: BillyZhang24kobe
@Date: 2020-07-13 20:16:37
@LastEditTime: 2020-07-18 17:28:41
@LastEditors: BillyZhang24kobe
@Description: Process a raw dataset into a sample file.
@FilePath: /stance-detection/data/process.py
'''

import sys
import os
import pathlib

import json
import jieba

abs_path = pathlib.Path(__file__).parent.absolute()
sys.path.append(sys.path.append(abs_path))
from data_utils import write_samples, partition


train_samples = set()
dev_samples = set()
# Read text file
train_file_path = os.path.join(abs_path, 'train-3000-raw.txt')
dev_file_path = os.path.join(abs_path, 'dev-1000-raw.txt')

# process train file
with open(train_file_path, 'r', encoding='utf8') as train:
    for line in train:
        if len(line.split("\t")) != 4: continue
        line = line.replace('\n', '').replace('\r', '')
        target = ' '.join(list(jieba.cut(line.split("\t")[1])))
        text = ' '.join(list(jieba.cut(line.split("\t")[2])))
        if line.split("\t")[3] == "FAVOR":
            stance = 1
        elif line.split("\t")[3] == "AGAINST":
            stance = -1
        else:
            stance = 0
        # stance = line.split("\t")[3]
        t_sample = text+'\n'+target+'\n'+str(stance)
        train_samples.add(t_sample)
train_write_path = os.path.join(abs_path, 'train-3000-seg.txt')
write_samples(train_samples, train_write_path)

# process test file
with open(dev_file_path, 'r', encoding='utf8') as dev:
    for line in dev:
        if len(line.split("\t")) != 4: continue
        line = line.replace('\n', '').replace('\r', '')
        target = ' '.join(list(jieba.cut(line.split("\t")[1])))
        text =' '.join(list(jieba.cut(line.split("\t")[2])))
        if line.split("\t")[3] == "FAVOR":
            stance = 1
        elif line.split("\t")[3] == "AGAINST":
            stance = -1
        else:
            stance = 0
        # stance = line.split("\t")[3]
        d_sample = text+'\n'+target+'\n'+str(stance)
        dev_samples.add(d_sample)
dev_write_path = os.path.join(abs_path, 'dev-1000-seg.txt')
write_samples(dev_samples, dev_write_path)


# # Read json file.
# json_path = os.path.join(abs_path, '../files/服饰_50k.json')
# with open(json_path, 'r', encoding='utf8') as file:
#     jsf = json.load(file)
#
# for jsobj in jsf.values():
#     title = jsobj['title'] + ' '  # Get title.
#     kb = dict(jsobj['kb']).items()  # Get attributes.
#     kb_merged = ''
#     for key, val in kb:
#         kb_merged += key+' '+val+' '  # Merge attributes.
#
#     ocr = ' '.join(list(jieba.cut(jsobj['ocr'])))  # Get OCR text.
#     texts = []
#     texts.append(title + ocr + kb_merged)  # Merge them.
#     reference = ' '.join(list(jieba.cut(jsobj['reference'])))
#     for text in texts:
#         sample = text+'<sep>'+reference  # Seperate source and reference.
#         samples.add(sample)
# write_path = os.path.join(abs_path, '../files/samples.txt')
# write_samples(samples, write_path)
# partition(samples)
