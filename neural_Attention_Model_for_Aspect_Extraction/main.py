# -*- coding: utf-8 -*-
import logging
import re

import hydra
import numpy as np
import pandas as pd
import torch
import os
#from evaluation import prediction

from model import ABAE
from reader import get_centroids, get_w2v, read_data_tensors
from omegaconf import DictConfig, OmegaConf
import create_vocab
import gensim
logger = logging.getLogger(__name__)

class Emb(torch.nn.Module):
    def __init__(self, wv_dim, vocab):
        super(Emb, self).__init__()
        self.wv_dim = wv_dim
        self.embedding_layer = torch.nn.Embedding(num_embeddings= len(vocab), embedding_dim=wv_dim)
        self.vocab = vocab
    
    def forward(self, x):
        out = self.embedding_layer(x)
        return out
    
@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg):

    #w2v_model = get_w2v(cfg.embeddings.path)
    wv_dim = cfg.w2v_vector_size

    y = torch.zeros(cfg.batch_size, 1)

    vocab, train_x, test_x, max_len = create_vocab.get_data(domain = 'restaurant')
    
    train_padding = create_vocab.word_padding(train_x, 60)
    test_padding = create_vocab.word_padding(test_x, 60)
    sen_gen = sentence_batch_generator(train_padding, cfg.batch_size)
    neg_gen = negative_batch_generator(train_padding, cfg.batch_size, cfg.negative_samples)
    #w2v_model = Emb(cfg.w2v_vector_size ,vocab)(torch.LongTensor(train_padding))

    #print(train_padding[:5, :])

    model = ABAE(wv_dim=wv_dim,
                  asp_count=cfg.aspects_number, vocab_size = len(vocab), vocab_index= dic_to_list(vocab))

    logger.debug(str(model))

    criterion = torch.nn.MSELoss(reduction="sum")

    if cfg.optimizer.name == "adam":
        optimizer = torch.optim.Adam(model.parameters())
    elif cfg.optimizer.name == "sgd":
        optimizer = torch.optim.SGD(model.parameters(), lr=cfg.optimizer.learning_rate)
    elif cfg.optimizer.name == "adagrad":
        optimizer = torch.optim.Adagrad(model.parameters())
    elif cfg.optimizer.name == "asgd":
        optimizer = torch.optim.ASGD(model.parameters(), lr=cfg.optimizer.learning_rate)
    else:
        raise Exception("Optimizer '%s' is not supported" % cfg.optimizer.name)

    for t in range(cfg.epochs):

        logger.debug("Epoch %d/%d" % (t + 1, cfg.epochs))

        for item_number in range((len(train_padding)//cfg.batch_size)):

            # prediction
            y_pred = model(torch.LongTensor(next(sen_gen)))

            # error computation
            loss = criterion(y_pred, y)
            #Loss = model.cal_loss(torch.LongTensor(next(neg_gen)))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if item_number % cfg.log_progress_steps == 0:

                logger.info("%d batches, and LR: %.5f" % (item_number, optimizer.param_groups[0]['lr']))

                for i, aspect in enumerate(model.get_aspect_words(logger)):
                    logger.info("[%d] %s" % (i + 1, " ".join([wa for wa in aspect])))

                logger.info("Loss: %.4f" % loss.item())

                try:
                    torch.save(model, f"abae_%.2f_%06d.bin" % (loss.item(), item_number))
                except Exception as e:
                    logger.exception("Model saving failed.")

    #text_label = pd.read_table('./preprocessed_data/restaurant/test_label.txt', sep='\t')


    """ evaluation 부분인데 아직 미완성
    m = torch.load('./abae_0.00_005000.bin')
    with torch.no_grad():

        cluster_map = {0: 'Food', 1: 'Miscellaneous', 2: 'Miscellaneous', 3: 'Food',
           4: 'Miscellaneous', 5: 'Food', 6:'Price',  7: 'Miscellaneous', 8: 'Staff', 
           9: 'Food', 10: 'Food', 11: 'Anecdotes', 
           12: 'Ambience', 13: 'Staff'}
        y=open('./preprocessed_data/restaurant/test_label.txt').readlines()
        y=[l.strip() for l in y]
        #print(y)
        test = CustomDataset(test_padding, y)
        MyDataLoader = DataLoader(test, batch_size = 50, shuffle = True)
        text = next(iter(MyDataLoader))
        pred = m.test(text['text'])
        prediction(text['class'], pred , cluster_map, domain='restaurant')

from torch.utils.data import Dataset,DataLoader
class CustomDataset(Dataset):
    def __init__(self, text, labels):
        self.labels = labels
        self.data = text

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
				# index 값을 주었을 때 반환되는 데이터 형태 (X,y)
        label = self.labels[idx]
        text = self.data[idx]
        sample = {'text' : text, 'class' : label}
        return sample
    
"""

def sentence_batch_generator(data, batch_size):
    n_batch = len(data) / batch_size
    batch_count = 0
    np.random.shuffle(data)

    while True:
        if batch_count == n_batch:
            np.random.shuffle(data)
            batch_count = 0

        batch = data[batch_count*batch_size: (batch_count+1)*batch_size]
        batch_count += 1
        yield batch

def negative_batch_generator(data, batch_size, neg_size):
    data_len = data.shape[0]
    dim = data.shape[1]

    while True:
        indices = np.random.choice(data_len, batch_size * neg_size)
        samples = data[indices].reshape(batch_size, neg_size, dim)
        yield samples

def dic_to_list(vocab):
    temp=[]
    for key in vocab.keys():
        temp.append(key)
    return temp

if __name__ == "__main__":
    main()