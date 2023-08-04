# theory(노드 관점)
* GNN이란?
  * 이웃 노드 정보를 이용해 노드 임베딩을 생성 후 메시지 패싱 -> aggregation을 진행함

* 노드 임베딩?
  * 노드 임베딩을 할 때 인접 노드의 정보를 이용함, 그렇다면 노드를 잘 표현하기 위해선 임베딩 함수가 injective property를 가져야함. 서로 다른 노드가 다른 값을 갖는 성질?, 퍼포먼스?(express power)

* computational graph(root 계산하는 방법)
  * computation graph가 필요한 이유는 컴퓨터는 노드들을 구분하지 못하기 때문, 즉 우리는 편의상 그림으로 id를 부여하지만, 컴퓨터는 처음에 모두 같은 노드라고 인식함. 쉽게 예를 들면 처음에 모두 0으로 init된다고 생각하기
  * 노드 1에 대한 computational graph(rooted tree 구조)<br> ![image](https://github.com/Jiwon96/papers/assets/65645796/4451f2a0-966d-4d52-a330-d9d2ceb71d56)
  * 이 때 왼쪽 그래프에서 1,2의 computational graph는 같고, 나머지는 모두 다른 구조를 가지고 있음.

* multi set
  * {2,3} $\neq$ {2,2,3} 즉, 원소의 중복을 인정함

* 기존의 레이어들의 문제점(aggr에서)
  * GCN: computational graph에서 mean pooling 사용해서 aggr을 함. 하지만, 이는 단사함수가 될 수 없음<br>반례<br>![image](https://github.com/Jiwon96/papers/assets/65645796/0e5f09e2-c6e8-45da-a1f8-0ecfdf7a6f9d)
  * GraphSAGE: max pooling 사용해서 aggr 함 하지만, 단사가 안됨<br>반례<br>![image](https://github.com/Jiwon96/papers/assets/65645796/026b9189-09cb-4221-b307-0f91f82288ec)
 
* <b>GIN</b>
  * Theorem 1: <br>
  ![image](https://github.com/Jiwon96/papers/assets/65645796/f39d6a3d-184f-4019-9c1e-45f9d748694f)
  * Theorem 2: In pracice, MLP hidden dimensionality of 100 to 500 is sufficient <br>
  ![image](https://github.com/Jiwon96/papers/assets/65645796/786cc339-802b-4d25-a1f9-6fc3b2e42e2f)
  * <b>GIN 구조</b><br>
  ![image](https://github.com/Jiwon96/papers/assets/65645796/72090fd0-a6b3-42f3-87f9-043d4375b10c)<br><br><br><br>
  ![image](https://github.com/Jiwon96/papers/assets/65645796/5e643705-08cf-4cae-ac9f-2e35da3a786a)

  * 부모 노드를 embedding 하는 방법:<br>![image](https://github.com/Jiwon96/papers/assets/65645796/701ec56d-f67f-493c-ab01-e600b260de9e)




* 참고자료
  * GIN에서 $c^(k) (v)$를 구하는 방법은 lecture 2에 나왔던 WL Graph Kernel을 이용함.
  * 임베딩할 때 GIN이 사용될 것 같다.(node classification)
