# an_unsupervised_neural_Attention_Model_for_Aspect_Extraction 논문 정리
* 목표: 우리가 가진 문장에서 가장 잘 대표할 수 있는 토픽 메트릭스를 구해보자
  * 이 때 각 토픽끼리 겹치지 않게 하는게 굉장히 중요하다
 
# 구조
* ABAE의 구조는 다음과 같다<br>
![image](https://github.com/Jiwon96/papers/assets/65645796/4332aa21-4a94-4a85-bc58-6735e1384abb)


# 단계
* 워드 전처리를 하는데 재밌던 부분은 embedding 층을 넣을 때 train set을 먼저 전처리 해놓고 test set에만 있는 단어는 <unk> 로 링크한다는 점이다.
* 워드 임베딩 층을 넣어 같은 단어들이 같은 인덱스로 맵핑되어 임베딩을 진행했다
  * 궁금점으로는 워드 임베딩 층을 넣지 않고 바로 word2vec 노드를 이용하여 단어를 바로 넣었으면 어떻게 될까 궁금하다.
* $z_s = \Sigma^n_{i=1}a_ie_{w_i}$
* $a_i = \frac{exp(d_i)}{\Sigma^n_{j=1}exp(d_i)}$ di를 구한후 softmax 함수를 활용하자 이 때 dim=1 인지 dim=-1인지 잘 생각해야 한다.
* $d_i = e^T_{w_i} \times M \times y_s$
* $y_s = \frac{1}{n} \Sigma^n_{i=1}e_{w_i}$
* $J{(\theta)} = \Sigma_{s \in D} \Sigma^m_{i=1}max(0, 1-r_sz_s + r_sn_i)$ 여기서 주변 관계를 고려하기 위해서 negative score가 높을수록 loss에 패널티를 부과해서 근접한 단어와 근접하지 않은 단어를 참고해 목적함수 $J{(\theta)}$를 설정한다.
* 또한 각 주제(단어)는 주변과 인접하면 안되기 때문에 $U( \theta)$와 regulation term $\lambda$ 를 활용해 loss function을 설정한다
  * $U(\theta) = || T_n \times T^T_n - I ||$ 여기서 $U(\theta)$가 $I$에 근접하도록 하는 것인데 이는 각 $I$는 orthogonal 하고, 다른 축과 수직이기 때문에 토픽(단어)을 겹치지 않게 만들어내는 효과를 낸다. 이 때 1은 단어 노드를 의미한다.
* Loss = $J({\theta}) + \lambda U({\theta})$
![image](https://github.com/Jiwon96/papers/assets/65645796/e03412b2-27df-4783-8268-c078d4c239a8)

# 한계
* 논문에는 Coherence Score와 다양한 방법을 통해 aspects를 평가하는 지표가 있었다. 하지만, 나는 아직 이 부분은 이해를 못해서 여기 부분은 숙제로 남아있다.
