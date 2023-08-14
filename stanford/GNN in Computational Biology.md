# The reason why Biological networks challenging
* Heterogeneous interaction that span from molecules to whole populations
* data from diverse source
* noisy due to inherent natural variation, limitation of measurement platforms

# Safe drugs and drug combinations -> Multi-relational link prediction on KGs
* the problems: Patients take multiple drugs to treat complex or co-existing diseases. but durg combination 힘듬
  * combination 수가 너무 많음
  * interaction의 activation이 non-linear함
  * 환자들 군집이 너무 다양함.
 
* Polypharmacy Knowledge Graph<br>![image](https://github.com/Jiwon96/papers/assets/65645796/b7e7112b-7824-433c-8f5b-87a6e9cc32fe)
  * Decagon이란 방법으로 이를 해결 -> Encorder + Decoder<br>![image](https://github.com/Jiwon96/papers/assets/65645796/7e1472f8-69b5-4e8e-b312-813709f67c56)
    * Aggregate Neighbor
      * 1st: Multirelational Graph Encoder<br>![image](https://github.com/Jiwon96/papers/assets/65645796/9ce3eb78-2270-4a9d-bee1-d4e6f88be9c6)

      * 2nd: Heterogeneous Edge Decoder<br>![image](https://github.com/Jiwon96/papers/assets/65645796/551b6da3-f147-4520-b97e-a8595b67dd26)


# Patient outcomes & disease classification
* Disease Diagnosis: 환자 증상이 관측가능함 -> 증상에 따른 모델링을 해 환자를 진단할 것
  * graph: 증상 노드들로 구성되어 있다고 가정
  * Node: 증상
  * edge: 증상들끼리 관계성
  * Subset S: 환자가 나타난 증상들 즉 Node들 묶음
  * Goal: subgraph의 레이블을 붙이는 것(병을 진단하는 것) <- 임베딩을 활용
 
* Challeging
  * sub graph의 size가 다양함
  * internal node와 external node 어떻게? 관계?
    * Localized: S1 = {s1, s2, ..} 한 sub graph 내부
    * Distributed: sub graphS={ S1, S2 ....} 진단명 집합
   
* Task
  * Node Prediction: pred property of a node
  * Link Prediction: predict property of a node pair
  * Graph Prediction: ""             of an entire graph

* SubGNN<br>![image](https://github.com/Jiwon96/papers/assets/65645796/068c5d19-6a7e-447c-84b1-bcf5d3ccdfc7)
  * Subgraph Message Passing<br>![image](https://github.com/Jiwon96/papers/assets/65645796/471201d4-0b79-48f3-ae27-e72e836adb8d)
  * Property-aware routing<br>![image](https://github.com/Jiwon96/papers/assets/65645796/1e831ccf-89e0-41f4-b1c0-178607fad4fa)

# Effective disease treatments
* Challenging
  * 진단이 충분하게 labeled 되어야됨 but label이 scarce함
 
* Meta Learning
  * 잠재적으로 나올 데이터를 고려하여 optimize함 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/05882ab0-0e48-4c47-8671-6f6766e021e0)
  * one dataset이 one data sample로 고려됨
 
* Few-shot learning: ????? <b>여기서 집중해서 봐야됨 잘 이해가 안되네</b>
  * K-shot N-calss classfication
 
* G-Meta: given 데이터로 학습한 후에 unseen 진단으로 test를 진행함, 즉 y-label이 train에서와 test에서가 다름.

* Local Subgraph Power:
  * Label propagation:
    * label이 sparse하면 효과적이지 않음
  * Struct similiarity: structural equivalence leverage를 하는게 굉장히 중요함
 
* 이론 2개<br>![image](https://github.com/Jiwon96/papers/assets/65645796/2d885092-97cb-482d-bc76-c6a74956d8b6)


