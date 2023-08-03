# GNN Aug and Training
* Augmentation이 필요한 이유
  * input_graph가 feature가 부족할 경우 多 -> feature augmentation
  * 그래프가 sparse함 -> message passing이 효과적이지 않음 -> 가상 노드/엣지 만들기
  * 그래프가 dense함 -> message passing이 costly함 -> Sample neighbor을 활용
  * 그래프가 large함 -> 계산량이 많아짐 -> Sample Subgraph를 만들어 embedding 계산

* inductive setting과 transductive setting 비교
  * inductive settings = ex) [1,1,1,1,1,1,1] 노드를 이렇게 표현
![image](https://github.com/Jiwon96/papers/assets/65645796/47b1b33a-b783-4734-934d-cfaac6017320)

* feature argumentation 방법들
--------------
  * Node degree
  * Clustering Coeff
  * PageRank
  * Centrality
--------------
  * <b>Add virtual edge ex adj = A +</b> $A^2$  in bipartite graph                ![image](https://github.com/Jiwon96/papers/assets/65645796/c4738d62-8624-42cc-9637-0c62dd6015fc)

  * <b>Neighborhood Sampling</b>                                                        ![image](https://github.com/Jiwon96/papers/assets/65645796/86706ecb-7c72-44b1-812d-e2e556c5212c)



# Training
* <b>해야할일</b>
![image](https://github.com/Jiwon96/papers/assets/65645796/febd8948-728a-4eda-814d-b6fa47976819)
* <b>방법(edge level)</b>
  * Concat + Linear
  * Dot Product
* <b>방법 (graph level)</b>
  * Global mean Pooling
  * Global max pooling
  * Global sum pooling
  * hierarchical Global pooling
    * there are two pooling in hierarchical pool
    * first, GNN A: calcul node embed
    * second, compute the cluster that a node belong to
  ![image](https://github.com/Jiwon96/papers/assets/65645796/34493a25-f066-461b-a786-161f8bacb9d2)

# Data Split
* Random Split: 데이터 셋을 train/valid/test로 여러번 랜덤하게 나눈 후 결과를 평균으로 구함
* <b>그래프는 사진 데이터와 달리 노드끼리 연결되어 있기 때문에 부분 데이터끼리 dependent함</b>
* (Transductive setting): training: 전체 임베딩 학습 -> valid: label만 분리한 후에 테스트 -> node / edge prediction tast
* (Inductive setting): training: graph를 multiple 하게 쪼갠 후 (independent 성질 만족 but 중요노드면 문제가 생길수도)-> 각 subgraph로 training, valid, test를 함 -> node / edge / graph task 
![image](https://github.com/Jiwon96/papers/assets/65645796/4c82bc61-6370-4c8a-84bb-36b8f62199f6)


# 이해가 안가는 부분
* Link Prediction 부분에서 inductive 부분과 transductive 부분 예시가 잘 이해가 안됨...
* 예시를 보면 이해가 될 듯
