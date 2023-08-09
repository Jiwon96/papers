""" test 부분 아직 미완성

import argparse
from sklearn.metrics import classification_report
import torch
import numpy as np

def evaluation(true, predict, domain):
    true_label = []
    predict_label = []

    if domain == 'restaurant':

        for line in predict:
            predict_label.append(line.strip())

        for line in true:
            true_label.append(line.strip())
        print(len(true_label), len(predict_label))

        print(classification_report(true_label, predict_label))

def prediction(test_labels, aspect_probs, cluster_map, domain):
    print()
    label_ids = torch.argmax(aspect_probs, dim = 1)
    label_ids= label_ids.flatten().tolist()
    #label_ids = label_ids.tolist()
    print(label_ids)
    predict_labels=[]
    for label_id in label_ids:
        if label_id<=13:
            predict_labels.append(cluster_map[label_id])
        else:
            predict_labels.append(cluster_map[0])
    #predict_labels = [cluster_map[label_id] for label_id in label_ids]
    evaluation(test_labels, predict_labels, domain)



"""