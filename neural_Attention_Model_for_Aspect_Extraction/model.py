# -*- coding: utf-8 -*-
import numpy as np
import torch
from torch.nn import init
from torch.nn.parameter import Parameter

## return ai
class SelfAttention(torch.nn.Module):
    def __init__(self, wv_dim: int, maxlen: int):
        super(SelfAttention, self).__init__()
        self.wv_dim = wv_dim

        # max sentence length -- batch 2nd dim size
        self.maxlen = maxlen
        self.M = Parameter(torch.empty(size=(wv_dim, wv_dim)))
        init.kaiming_uniform_(self.M.data)

        # softmax for attending to wod vectors
        self.attention_softmax = torch.nn.Softmax(dim=1)

    def forward(self, input_embeddings):

        # (3dim: batch, 데이터 개수: 60, 200 wv dim) 
        #print(input_embeddings.shape)
        mean_embedding = torch.mean(input_embeddings, dim = 1, keepdim=True) # 50 x 1 x 200
        out = torch.einsum('bij, jj-> bij', input_embeddings, self.M) # 50 x 60 x 200 , 200 200 -> 50 60 200
        out = torch.einsum('bij, bkj->bij', out, mean_embedding) # 50 60 200,  50 1 200
        out = self.attention_softmax(out)
        #print('mean_emb',mean_embedding.shape)
        #print(out.shape) # 50 60 200이어야 하는데
        return out
    # def forward(self, input_embeddings):
    #     # (b, wv, 1)
        

    #     # (wv, wv) x (b, wv, 1) -> (b, wv, 1)
    #     product_1 = torch.matmul(self.M, mean_embedding)

    #     # (b, maxlen, wv) x (b, wv, 1) -> (b, maxlen, 1)
    #     product_2 = torch.matmul(input_embeddings, product_1).squeeze(2)

    #     results = self.attention_softmax(product_2)

    #     return results

    # def extra_repr(self):
    #     return 'wv_dim={}, maxlen={}'.format(self.wv_dim, self.maxlen)

class ABAE(torch.nn.Module):
    """
        The model described in the paper ``An Unsupervised Neural Attention Model for Aspect Extraction''
        by He, Ruidan and  Lee, Wee Sun  and  Ng, Hwee Tou  and  Dahlmeier, Daniel, ACL2017
        https://aclweb.org/anthology/papers/P/P17/P17-1036/

    """

    def __init__(self, wv_dim: int = 200, asp_count: int = 30,
                 ortho_reg: float = 0.1, maxlen: int = 201, init_aspects_matrix=None, vocab_size: int=None, vocab_index=None):
        """
        Initializing the model

        :param wv_dim: word vector size
        :param asp_count: number of aspects
        :param ortho_reg: coefficient for tuning the ortho-regularizer's influence
        :param maxlen: sentence max length taken into account
        :param init_aspects_matrix: None or init. matrix for aspects
        """
        super(ABAE, self).__init__()
        ## 추가
        self.vocab_size = vocab_size
        self.emb = torch.nn.Embedding(vocab_size, embedding_dim=wv_dim)
        self.vocab_index = vocab_index
        ## 추가 끝
        self.wv_dim = wv_dim
        self.asp_count = asp_count
        self.ortho = ortho_reg
        self.maxlen = maxlen
        self.attention = SelfAttention(wv_dim, maxlen)
        self.linear_transform = torch.nn.Linear(self.wv_dim, self.asp_count) # W matrix
        self.softmax_aspects = torch.nn.Softmax(dim=1) # pt 만들기 위함
        self.aspects_embeddings = Parameter(torch.empty(size=(wv_dim, asp_count))) # T matrix # 200 x 15
        if init_aspects_matrix is None:
            torch.nn.init.xavier_uniform_(self.aspects_embeddings) # T matrix
        else:
            self.aspects_embeddings.data = torch.from_numpy(init_aspects_matrix.T)
        self.zero = torch.FloatTensor([[[0]]])
        self.one = torch.FloatTensor([[[1]]])
        self.z=None # zi # 50 60 200
        self.r=None #ri # 50, 1 200
        self.emb1=None

    def cal_loss(self, negative_embeddings):
        ni = self.emb(negative_embeddings) # 50 x 60 x 200
        ni = torch.reshape(ni, (ni.shape[0], -1, ni.shape[3])) # 50 300 200
        ni = torch.mean(ni, dim = 1, keepdim=True) # 50 x 1 x 200
        #print(ni.shape)
        J = torch.max(self.zero, self.one - torch.matmul(self.r, torch.transpose(self.z, 1,2)) + torch.matmul(self.r, torch.transpose(ni,1,2))).sum(axis=1).mean().squeeze()
        U = torch.norm((torch.matmul(torch.transpose(self.aspects_embeddings,0,1), self.aspects_embeddings) - torch.eye(self.asp_count)).mean())
        Loss = J+ U # regularization constant = 1 일 때
        return Loss

    def forward(self, text_embeddings):
        out = self.emb(text_embeddings) # 50 60 200
        self.emb1 = out
        ai = self.attention(out) # 50 60 200
        #print(out.shape) 
        self.z = torch.sum(ai * self.emb1, dim=1, keepdim=True) # 50 1 200
        out = self.linear_transform(self.z) # 50 1 15
        #print(out.shape) # 50 1 15
        
        pt = self.softmax_aspects(out) # 50 x 1 x 15 이어야 하는데 pt-> 50 15 200
        #print(pt.shape)
        self.r = torch.einsum('bij,kj -> bik', pt,self.aspects_embeddings) # 50 1 15, 200 15
        #print(self.r.shape) # 50 1 200
        return self.r
        #print(r.shape) # 50 200 60
    
    def test(self, text_embeddings):
        out = self.emb(text_embeddings)# 50 60 200
        print(out.shape)
        out = torch.einsum('bij, jk->bik', out, self.aspects_embeddings) # 50 60 15
        out = torch.einsum('bij, bkl -> bjl', out, out)
        return out

        # print()
    # def get_aspects_importances(self, text_embeddings):
    #     """
    #         Takes embeddings of a sentence as input, returns attention weights
    #     """

    #     # compute attention scores, looking at text embeddings average
    #     attention_weights = self.attention(text_embeddings)

    #     # multiplying text embeddings by attention scores -- and summing
    #     # (matmul: we sum every word embedding's coordinate with attention weights)
    #     weighted_text_emb = torch.matmul(attention_weights.unsqueeze(1),  # (batch, 1, sentence)
    #                                      text_embeddings  # (batch, sentence, wv_dim)
    #                                      ).squeeze()

    #     # encoding with a simple feed-forward layer (wv_dim) -> (aspects_count)
    #     raw_importances = self.linear_transform(weighted_text_emb)

    #     # computing 'aspects distribution in a sentence'
    #     aspects_importances = self.softmax_aspects(raw_importances)

    #     return attention_weights, aspects_importances, weighted_text_emb

    # def forward(self, text_embeddings, negative_samples_texts): # text 형태로 입력
        
    #     ## added by jiwon
    #     text_embeddings = self.emb(text_embeddings)
    #     negative_samples_texts = self.emb(negative_samples_texts) 
    #     # after input text and convert to Embeded value
    #     # print(text_embeddings)
    #     # negative samples are averaged
    #     averaged_negative_samples = torch.mean(negative_samples_texts, dim=2)

    #     # encoding: words embeddings -> sentence embedding, aspects importances
    #     _, aspects_importances, weighted_text_emb = self.get_aspects_importances(text_embeddings)

    #     # decoding: aspects embeddings matrix, aspects_importances -> recovered sentence embedding
    #     recovered_emb = torch.matmul(self.aspects_embeddings, aspects_importances.unsqueeze(2)).squeeze()

    #     # loss
    #     reconstruction_triplet_loss = ABAE._reconstruction_loss(weighted_text_emb,
    #                                                             recovered_emb,
    #                                                             averaged_negative_samples)
    #     max_margin = torch \
    #         .max(reconstruction_triplet_loss, torch.zeros_like(reconstruction_triplet_loss)) \
    #         .unsqueeze(dim=-1)

    #     return self.ortho * self._ortho_regularizer() + max_margin

    # @staticmethod
    # def _reconstruction_loss(text_emb, recovered_emb, averaged_negative_emb):

    #     positive_dot_products = torch.matmul(text_emb.unsqueeze(1), recovered_emb.unsqueeze(2)).squeeze()
    #     negative_dot_products = torch.matmul(averaged_negative_emb, recovered_emb.unsqueeze(2)).squeeze()
    #     reconstruction_triplet_loss = torch.sum(1 - positive_dot_products.unsqueeze(1) + negative_dot_products, dim=1)

    #     return reconstruction_triplet_loss

    # def _ortho_regularizer(self):
    #     return torch.norm(
    #         torch.matmul(self.aspects_embeddings.t(), self.aspects_embeddings) \
    #         - torch.eye(self.asp_count))

    def get_aspect_words(self, logger, topn=15):
        words = []
        w2v_model = self.emb.weight.detach().numpy()
        # getting aspects embeddings
        aspects = self.aspects_embeddings.detach().numpy()

        # getting scalar products of word embeddings and aspect embeddings;
        # to obtain the ``probabilities'', one should also apply softmax
        # words_scores = w2v_model.wv.syn0.dot(aspects)
        words_scores = w2v_model.dot(aspects)

        for row in range(aspects.shape[1]):
            argmax_scalar_products = np.argsort(- words_scores[:, row])[:topn]
            #print([w for w, dist in w2v_model.similar_by_vector(aspects.T[row])[:topn]])
            #words.append([self.vocab.index_to_key[i] for i in argmax_scalar_products])
            words.append([self.vocab_index[i] for i in argmax_scalar_products])
            #print(words[row])
            

        return words