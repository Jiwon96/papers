# The reason why Biological networks challenging
* Heterogeneous interaction that span from molecules to whole populations
* data from diverse source
* noisy due to inherent natural variation, limitation of measurement platforms

# Safe drugs and drug combinations -> Multi-relational link prediction on KGs
* 약물 혼합 복용을 했을 때 부작용을 예측할 수 있는 task임 즉 edge(relation) 예측 task임
* the problems: Patients take multiple drugs to treat complex or co-existing diseases. but drug combination 힘듬
  * drug combination 수가 너무 많음 <- 모든  set을 고려할 수 없음
  * interaction의 activation이 non-linear함
  * 환자들 군집이 너무 다양함.
 
* Polypharmacy Knowledge Graph<br>![image](https://github.com/Jiwon96/papers/assets/65645796/b7e7112b-7824-433c-8f5b-87a6e9cc32fe)
  * Decagon이란 방법으로 이를 해결 -> Encorder + Decoder<br>![image](https://github.com/Jiwon96/papers/assets/65645796/7e1472f8-69b5-4e8e-b312-813709f67c56)
    * Aggregate Neighbor
      * 1st: Multirelational Graph Encoder<br>![image](https://github.com/Jiwon96/papers/assets/65645796/9ce3eb78-2270-4a9d-bee1-d4e6f88be9c6)

      * 2nd: Heterogeneous Edge Decoder<br>![image](https://github.com/Jiwon96/papers/assets/65645796/551b6da3-f147-4520-b97e-a8595b67dd26)


# Patient outcomes & disease classification
* graph classification 문제임, 더 알고 싶으면 SubGNN 논문을 찾아볼 것.
* Disease Diagnosis: 환자 증상이 관측가능함 -> 증상에 따른 모델링을 해 환자를 진단할 것
  * graph: 증상 노드들로 구성되어 있다고 가정
  * Node: 증상
  * edge: 증상들끼리 관계성
  * Subset S: 환자가 나타난 증상들 즉 Node들 묶음
  * Goal: subgraph의 레이블을 붙이는 것(병을 진단하는 것) <- 임베딩을 활용
 
* Challeging
  * sub graph의 size가 다양함
  * sub graph는 다른 그래프와 internal node와 external node 와 연결되어 있으므로 상당히 복합함
    * Localized: S1 = {s1, s2, ..} 한 sub graph 내부
    * Distributed: sub graphS={ S1, S2 ....} 진단명 집합
      
* 아이디어:
  * sub graph의 neighborhood, structure, position 의 3 채널을 가지고 sub graph를 임베딩 한 후에 subgraph 끼리 4가지 지표를 활용해 비교할 것임(density, cut ratio, coreness, component)
 
* 이 문제는 Subgraph prediction learning Task로 아래에 언급되어 있는 task와는 조금 다름 왜냐하면 G에서 sub group을 나누고 그에 대한 비교이므로
  * Node Prediction: pred property of a node
  * Link Prediction: predict property of a node pair
  * Graph Prediction: ""             of an entire graph

* SubGNN<br>![image](https://github.com/Jiwon96/papers/assets/65645796/068c5d19-6a7e-447c-84b1-bcf5d3ccdfc7)
  * Subgraph Message Passing<br>![image](https://github.com/Jiwon96/papers/assets/65645796/471201d4-0b79-48f3-ae27-e72e836adb8d)
  * Property-aware routing<br>![image](https://github.com/Jiwon96/papers/assets/65645796/1e831ccf-89e0-41f4-b1c0-178607fad4fa)

# Effective disease treatments
* Drug 후보군을 진달하기 위함. link prediction 문제임 in bipartite graph
 
* Challenging
  * 진단이 충분하게 labeled 되어야됨 but label이 scarce함
  * 아직 모르는 병이 너무 많고, 실제에서 효과적으로 입증된 레이블이 부족함
 
* Meta Learning
  * 레이블이 부족할 때 사용하는 머신러닝 방법임
  * 잠재적으로 나올 데이터를 고려하여 optimize함 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/05882ab0-0e48-4c47-8671-6f6766e021e0)
  * one dataset이 one data sample로 고려됨
 
* Few-shot learning:
  * training task에서는 query set과 레이블은 같지만 feature가 조금은 다른 데이터를 학습시키고 label set에 feature가 다른 애들을 테스트함 또한 Test set에서도 training task에서 학습시킨 레이블과 다른 레이블을 테스트하는것 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/3fd0ec90-594a-41f8-90da-7c7f4ee6d697)

* Local Subgraph Power:
  * Label propagation:
    * label이 sparse하기 때문에 현실에서는 label propagation이 효과적이지 않을 수 있음 따라서 struct similiarity를 활용해 분포 학습하는게 굉장히 중요할 수 있음.
  * Struct similiarity: structural equivalence leverage를 하는게 굉장히 중요함
 
* 이론 2개<br>![image](https://github.com/Jiwon96/papers/assets/65645796/2d885092-97cb-482d-bc76-c6a74956d8b6)

* 효과적인 예시: 실제로 비교했을 때 embedding space를 보면 covid-19에 대해서 약물을 re-purpose하고 simulation했더니 다른 메서드에 비교해서 (바이러스가 인간 단백질에 붙거나 등등 예방 효과에 대해서) ROC score가 굉장히 높았고 실제로도 hit ratio가 굉장히 높았음

