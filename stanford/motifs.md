![image](https://github.com/Jiwon96/papers/assets/65645796/7b5504e8-696c-4008-91df-a86e37a02484)# Motifs in Networks

* Definiton
  * Subgraphs: blocks of networks -> they have the power to characterize and discriminate networks
  * Node-induced subgraph: <br>![image](https://github.com/Jiwon96/papers/assets/65645796/431debe5-0139-4f7f-8d4b-bb3ac017992c)
  * Edge-induced subgraph: <br>![image](https://github.com/Jiwon96/papers/assets/65645796/f33e4afc-4dd9-42e7-9055-c2db9672e3c9)
  * Graph Isomorphism: <br>![image](https://github.com/Jiwon96/papers/assets/65645796/27c70c5d-90db-41e2-a601-e1a009f2f90f)

* Subgraphs and motifs
  * motifs: 그래프의 특징이라고 생각하면 됨(pattern, recurring, significant)로 정의됨
    * patterns: small subgraph
    * recurring: found many times with high frequency
    * significant: more frequent than expected, in randomly generated graph
    * Frequency definition(in grarph level): Target 그래프에서 subset 그래프가 얼마나 나타나는지 ex<br>![image](https://github.com/Jiwon96/papers/assets/65645796/9c2c90a9-a450-445d-b203-5853435796fc)
    * Frequency definition(in Node level): (anchored) 노드를 기준으로 그래프가 isomorphic 한 것(나중에 order property가 나오면서 embedding 값이 비슷하게 만들 수 있음)<br>![image](https://github.com/Jiwon96/papers/assets/65645796/5d2394aa-2bc2-4242-962e-82c948f9994f)
    * random graphs: $G_{n,p}$: edge가 확률 p에 대해서 랜덤 워크로 그래프를 만들어감(n개 노드)
    * Configuration Model (slide 22): 더보고 싶으면 슬라이드 참조

* Neural Subgraph Representations (graph isomophic 구하는 embedding)
  * Node anchod graph: k-hop neighborgood
  * Ordering Space: 아래와 같은 속성 만족(slid 42)
    * Transitivity: 
    * Anti-symmetry
    * closure under intersection<br>![image](https://github.com/Jiwon96/papers/assets/65645796/fc0aaba6-5b24-4820-8291-b42c55098dcb)
    * loss: ![image](https://github.com/Jiwon96/papers/assets/65645796/f0a098d7-44e6-43a8-a903-21d3bdec546b)

* Mining Frequent Motifs(slide 55)
  * subgraph isomorphism is NP-complete 문제 -> 계산이 지수적으로 증가 -> 3에서 7정도의 motif 크기만 알 수 있음
  * Enumerating 
  * Counting
  * SPMiner: 메시징을 통해서 anchor 노드의 임베딩값을 계산하고 목표 서브그래프와 거리를 구해 입실론보다 작게 만듬
 
오늘은 개인 사정으로 정리를 대충 함... 공부하고 싶으면 다시 보면서 정리 다시하자
