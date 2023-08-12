# Scaling Up Graph Neural Networks to Large Graphs
* 기존 그래프 방식의 문제점
  * 이웃노드에서 message를 전달받는 GNN의 미니배치를 활용해 일부 노드만 샘플링 하는게 어려움
  * FULL batch 또한 GPU 병렬 연산을 효과적으로 활용할 수 없음.

# GraphSAGE Neighbor Sampling: Scaling up GNNs
* Stochastic Training<br>![image](https://github.com/Jiwon96/papers/assets/65645796/43bce341-4fd0-42b7-8092-19b1b955addc)
  * K-layer의 GNN은 K-hop 이웃노드들의 feature를 전달 받은 노드의 임베딩을 만듬 <b>?????</b> 한 레이어에 한 호프? 한 hop에 k layer?
  * M 개 노드는 <b>M개의 computational graph</b>로 나타낼 수 있으므로 mini_batch 구성 가능
  * M개의 노드에 대한 평균 loss $l_{sub}( \theta )$ SGD를 통해 학습
 
  * <b>But 문제점 </b> Computational graph에 대한 SGD</b> 는 모든 노드에 대한 k-hop neighbor를 aggregation 하는 과정 과정에서 연산량이 지수적으로 증가
  * High degree를 가진 hub node가 있을 때도 연산량 증가
 
* <b>Neighbor Sampling</b><br>![image](https://github.com/Jiwon96/papers/assets/65645796/d9581937-b8f3-4337-a207-c4249fedd261)

  * 각 hop에서 <b>H개의 이웃 노드를 샘플링</b>하여 computational graph를 구성하면 연산량을 줄일 수 있음 <b>추가</b> upper bound $H^k$
  * <b>but </b> H가 줄어듬에 따라 연산량이 줄지만, variance가 크기 때문에 학습이 불안정(underestimate 할 수 있음)
  * 샘플링을 랜덤하게 할 경우 빠르지만 optimal 하지 못함
  * 해결법 Random Walk with Restarts score $R_i$를 구해 중요한 노드들을 샘플링(랜덤이 아니라)하면 더 효과적일 수 있다. (연산량의 문제는 괜찮나? 어떻게 구하지)

  * <b> (*************************)추가********************</b>
  * degree가 굉장히 높다면 batch_size는 굉장히 작아질 수 밖에 없음... batch_size가 작으면,,, variance가 굉장히 커지기 때문에 정확하지 않을 수가 있음.
  * 현재까지 neighbor sampling 을 어떻게 할 것인지에 대해서 많은 연구가 진행되고 있음.

 <b>Issues with Neighbor Sampling</b>![image](https://github.com/Jiwon96/papers/assets/65645796/a7f0d838-5caa-4ce4-a19e-592cdcac6dda)
  * Neighbor Sampling은 <b>GNN layer 수에 따라 computational graph의 크기가 지수적으로 증가</b>한다. <b>?????왜지? Random walk with restart score와 관련이 있을까?</b>
  * 또한, 미니배치의 노드들이 공유 이웃이 많으면 연산이 중복되기 때문에 연산 효율이 떨어짐. (C D를 두번 계산해야됨)

 # Cluster-GCN: Scaling up GNNs<br>![image](https://github.com/Jiwon96/papers/assets/65645796/adfa3fc9-572b-497a-b385-ff40dc1bc8d3)
  * <b>Layer-wise node embedding update는 이전 레이어에서의 임베딩을 재사용</b>하기 때문에 neighbor sampling의 불필요한 연산을 줄여준다.
  * <b> but</b> large graph에서 <b>GPU 메모리 한계</b>가 있음
  * subgraph 샘플링을 활용하면 메모리 한계 문제를 극복할 수 있음<br>![image](https://github.com/Jiwon96/papers/assets/65645796/3e3e429f-6009-48d1-b3a4-529b1be6191f)
  * edge들이 많이 사라져서 노드들이 고립되지 않게 모델링 해야한다. <b> 왜?</b> <br>![image](https://github.com/Jiwon96/papers/assets/65645796/7f1331bf-fd56-44a1-86fb-d9c2c3534476)
  * Real-world graph는 <b>community structure</b>를 가지기에 community를 샘플링 할 수 있는 <b>Cluster-GCN</b>을 활용한다.
  * Cluster-GCN은 larget graph를 그룹화하는 <b>pre-processing</b> 과정과 샘플링한 그룹 내에서 message passing을 하는 <b>mini-batch training</b> 과정으로 나뉜다.
 
  * <b>Pre-process</b>
    * Pre-processing 과정에서는 Louvain, METIS, BigCLAM 등 <b>community detection 알고리즘</b>을 활용해 $G=(V, E)$를 노드에 대해서만, <b>V1, V2, ... , Vc</b>로 그룹화 함 <b>엣지 포함 X</b>
  * <b>Mini batch training</b> <br>![image](https://github.com/Jiwon96/papers/assets/65645796/760290ef-bcdb-4c47-9b56-c30b5d88c2d3)
    * 샘플링한 노드 그룹 $V_c$ 로부터 엣지가 있는 <b>induced subgraph</b> $G_c = (V_c, E_c)$를 만듬
    * <b>Layer-wise node update</b>를 적용 -> $v \in V_c$에 대한 임베딩 $h_v$를 얻고 loss 통해 업데이트 함 <b> ???????????Layer-wise node update</b>
  
* <b>Issue with Cluster-GCN</b><br>![image](https://github.com/Jiwon96/papers/assets/65645796/2639b614-3ff4-4bcb-a264-6734c72103d8)
  * Induced subgraph는 그룹 간의 엣지를 제거하여 message를 잃는다.
  * Community detection 알고리즘은 유사한 노드들끼리 하나의 그룹으로 묶어 샘플링된 그룹은 전체 데이터의 <b>작은 부분</b>만을 커버할 수 있다.
  * 샘플링된 노드가 전체 구조를 표현하기에 <b>충분히 다양하지 못하다</b>. <--- 단점
 
* <b>Advanced Cluster-GCN</b><br>![image](https://github.com/Jiwon96/papers/assets/65645796/fb38ca9c-6b15-4eea-9322-8867335bf964)
  * community를 만들고 여러 개의 communities 을 미니배치 단위로 합친다.
  * Vanila cluster-GCN과 동일하게 pre-processing 과정에서는 그룹화하되 상대적으로 적은 수의 그룹으로 나눈다. (community 만들기)
  * Mini-batch training에서는 q개의 노드 그룹을 랜덤하게 골라 합치고 induced subgraph를 만들어 학습한다. (미니배치 단위로 합치기)

* <b>Comparison of Time Complexity</b><br>![image](https://github.com/Jiwon96/papers/assets/65645796/eb6700bc-ae3f-4708-b885-1a4ed19dd9bd)
  * H개의 이웃노드를 샘플링 하기에 하나의 노드는 $H_k$ 만큼 걸린다고 가정하면 M개의 메시지를 받기 위해서는 $M\times H^K$ 의 시간 복잡도를 가짐
  * Cluster-GCN은 M개 노드에 대해 induced subgraph 만들고, $D_{avg}$는 평균 node degree, K는 레이어 수라고 할 때 시간 복잡도는 $K\times M \times D_{abg}$가 된다.
  * Cluster-GCN의 시간복잡도는 <b>선형적으로 증가</b>하므로 효율적이지만 K가 크지 않다면 <b>neighbor sampling을 주로</b> 쓴다.
  * <b>(************************************ 추가**********************************)</b> 왜 Cluster GCN은 선형 복잡도를 갖는것이라 말하는거지? 이해가 안된다.
  * inductive graph가 굉장히 많이 쓰이므로 이를 복습할 때 잘 이해하고 넘어가자.

# Sacling up by Simplifying GNNs
* <b>Recall </b> <br>![image](https://github.com/Jiwon96/papers/assets/65645796/0acb024b-0c9f-4723-b4a0-7e2a05165e19)
  * Self-loop를 포함하는 $E$와 $V$로 이루어진 그래프의 node feature가 $X_v$라 할 때 input node embedding은 $h^{(0)}_v = X_v$이다.
  * Mean-pooling을 활용하면 $h^{(k+1)}_v는 이웃노드들의 정보를 평균낸 것을 학습되는 파라미터 $W_k$에 곱한 후 ReLU를 거쳐 얻을 수 있음 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/8a987e89-cfc1-4653-8008-9cf8dd7ee9df)
  * $H^{(k)}$ = [ $h^{(1}_1, .... , h^{(k)}_V$ ]
  * $\Sigma_{u\in N{(v)}}h^{(k)}_u = A_vH^{(k)}$
  * D는 노드 v의 degree가 담긴 대각행렬
  * A는 인접행렬
 
* <b> Simplifying GCN</b><br>![image](https://github.com/Jiwon96/papers/assets/65645796/f1b8ee10-66c5-4c76-af6f-672273c27c7c)
  * GCN에서 <b>non-linear activation을 제거</b>하여 simplify 할 수 있다.
  * $A^{\sim K}X$ 에는 학습되는 파라미터가 없으므로 <b>미리 계산</b>할 수 있다.
  * $A^{\sim K}X$가 미리 계산되므로 M개의 노드 임베딩은 M에 linear한 시간복잡도 가짐.
    * $h^{(K)} _{v_1} = WX _{v_1} ^{\sim}$
    * 
    * ....
    * $h^{(K)} _{v_M}$ = $WX^{\sim} _{v_M}$
  * Pre-grocessing 에서는 $A^{\sim k}X$ 를 미리 계산하면 됨
  * min-batch training 과정에선 <b>M개의 노드가 랜덤하게 샘플링 되어</b> 임베딩 $h{(K)} _{v_i}가 계산됨. 임베딩을 통해 예측한 값과의 loss로 parameter를 업데이트 한다.
 
# Comparison with other methods
* Neighbor sampling에 비해 <b>노드 임베딩을 더 효율적</b>으로 만들며 Cluster-GCN처럼 그룹을 활용하지 않기 때문에 전체 노드로부터 완전히 랜덤하게 샘플링하여 <b>variance를 줄일</b> 수 있다.
* 하지만, non-linearity가 없어 기존 GNN 모델에 비해 <b>표현력이 떨어진다는 한계</b>가 있다. <br>![image](https://github.com/Jiwon96/papers/assets/65645796/789fc597-8a4a-4abe-a525-a19b7fbd246e)
* 그럼에도 불구하고 많은 node classification task에서 연결된 노드들이 동일한 target label을 가지는 <b>homophily structure</b>를 보이기 때문에 original GNN과 유사한 성능을 보인다.
  * (ex. Social network에서 두 사람이 친구인 경우 같은 영화를 좋아하는 경향이 있다) <b>추가</b> 사회에서 비슷한 사람끼리 어울리는 느낌, 즉 비슷한 사람이면 노드 임베딩이 비슷함
* Pre-processing 과정에서 feature는 반복적으로 이웃 노드의 feature를 평균내 얻으므로 연결된 노드들이 유사한 feature를 가지고 이는 <b>homophily structure 하에서 잘 작동</b>한다.




  
