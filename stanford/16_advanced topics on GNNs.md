# Limitations of GNN
* Problems & Solutions
  * 완벽한 GNN은 neighborhood struct(정의역)와 node embedding 사이에 1:1 함수를 갖는 것, 같은 구조라면 같은 노드 임베딩을, 다른 구조라면 다른 노드 임베딩을 가져야 됨
  * BUT 같은 구조 갖더라도 그래프 상에서 다른 위치에 있어 다른 임베딩을 가지길 원할 수 있음.
 
* Problem2:
  * 지금까지 배운 GNN은 완벽하지 않음. 예를 들어 emssage passing GNN은 cycle length 를 세지 못해 $v_1$과 $v_2$가 같은 구조임에도 불구하고 같은 computationial graph 가짐,(추가): 또한 expression power가 WL test보다 클수가 없음 즉 upper bound 임 (Lecture 9, WL test 참고)
 
* Solution: 위치를 고려한 Position-aware GNNs, WL test보다 표현력이 뛰어난 Identity-aware GNNs

* Naive Approach
  * 서로 다른 input(nodes, edges, graphs)에 대해 다르게 라벨링 되어야 한다.
  * 원핫 인코딩을 통해 각 노드를 다른 ID로 인코딩하는 방식을 생각해볼 수 있지만 O(N)의 feature dimension이 필요하며 새로운 노드/그래프에 대해 일반화할 수 없다는 문제가 있다. 추가: not inductive 한데 즉 기존 노드에서 노드가 추가되면 기존 그래프와 완전히 달라지기 때문에 어떻게 고려해야 할 지 어렵다.
 
# Position-aware Graph Neural Networks
* Two types of tasks
  * Structure-aware task
  * Position-aware task<br>![image](https://github.com/Jiwon96/papers/assets/65645796/627b2ef4-2578-4fd4-8a20-bd857717be97)

* 노드가 sturucture에 의해 라벨링 될 때 GNN은 서로 다른 computational graph를 만들어 $v_1$, $v_2$를 구분할 수 있다.
* 노드가 position에 의해 라벨링 될 때 GNN은 v_1과 v_2가 같은 computational graph를 가지도록 만들어 구분을 못한다.
* Position-aware task를 잘 수행하기 위해 anchor를 활용한다.

* Power of "Anchor"<br>![image](https://github.com/Jiwon96/papers/assets/65645796/55036efa-194f-49e6-90e9-711fef5fe50c)

  * 임의의 anchor를 정한 후 각 노드 $v_i$까지의 상대적 거리를 나타내 $s_i$가 좌표축으로써 역할을 하면 노드위 위치를 알 수 있다 -><b>추가부분</b> $s_i$가 x, y 축처럼 s_1부터 떨어진 거리를 기준으로 각 노드들을 표현) 예를 들어 v1= (1,2) 축은 $s_1 s_2$임 <- x, y 축 대신 $s_i$축이라고 생각하면 됨
  * Anchor는 많을수록 많은 좌표축이 생기는 것을 의미하므로 더 잘 characterize 할 수 있다. 
* ex2)<br>![image](https://github.com/Jiwon96/papers/assets/65645796/5982005a-f94a-46e2-82b3-423cbdc359f6)
  * v1 = (1,2,1) 축은 s1, s2, s3
 
* 여러 노드를 묶어서 anchor set으로 활용 가능
* Large achor set은 더 정확한 위치 추정 가능
* Anchor를 통해 position을 알면 potision encoding을 augmented node feature로 활용할 수 있다.
* <b>변경</b>축을 어떻게 표현하는지에 따라 Position encoding이 바뀔 수 있지만(s1, s2, s3 $\neq$ s1,s3,s2 의 임베딩) 각 차원에서의 값은 그대로이므로 의미가 변하지는 않는다. <b>추가</b> (모든 데이터가 이 순서로 들어올 것이므로 1:1 대응이 될 것이라 생각할 수 있음)

# Identity-Aware Graph Neural Networks <이 부분은 이해가 잘 안간다>
* Failure cases of structure-aware tasks
  * Node-level<br>![image](https://github.com/Jiwon96/papers/assets/65645796/c511ba9c-6df2-4434-8583-7384da2cd6b5)
  * $v_1$과 $v_2$는 다른 구조를 가지지만 같은 computational graph 가짐 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/bfe00c3f-b4e3-4c81-9976-5691de9d8947)
  * <b>숙제 이해가 안되는 부분</b>
    * 임베딩 하고 싶은 노드에 색을 지정하여 ordering/identities invariant한 inductive function을 만들 수 있다.
    * 같은 구조 상에서 $v_2, v_3$ 의 순서가 바뀌어도 동일한 임베딩을 가진다. 즉, 일반화 성능에 도움이 된다.
    * 다른 구조를 가지는 노드는 다른 computational graph를 만든다.
   
  * Edge-level<br>![image](https://github.com/Jiwon96/papers/assets/65645796/16eacd96-d270-426e-8aa9-f960b8a32795)
    * $v_0$가 엣지 $A, B$를 가지는지에 대한 link prediction을 하는 경우에도 $v_1, v_2$가 같은 임베딩을 가지기 때문에 문제가 생긴다. <b> <- 이 부분은 이해가 안가므로 잘 들어봐야 겠다</b> <br>![image](https://github.com/Jiwon96/papers/assets/65645796/c6d5aa1c-027d-463b-9c65-7337ad75abe3)

    * Coloring을 활용하면 $v_1, v_2$ 를 구별할 수 있다. <b> 이게 뭔말일까?</b>
    * $v_0와 v_1$ 혹은 $v_2$ 와의 노드 쌍이 다른 임베딩을 가지기 때문에 link prediction을 할 때 문제가 없다.
  * Graph-level<br>![image](https://github.com/Jiwon96/papers/assets/65645796/0169f2c1-9eb1-499f-a536-56996be56734)
    * 다른 그래프에서도 A,B가 동일한 compuational graph 가짐
    * coloring <b> 어떻게 coloring이 효과적인지 살펴볼 필요가 있다</b><br>
    
* Identity Aware GNN<br>![image](https://github.com/Jiwon96/papers/assets/65645796/5b4484fb-14fb-4138-8b34-d2300fa291ca)
  * Coloring을 위해 노드에 따라 다른 network(message/aggregation)를 적용하는 heterogenous message passing을 활용한다.
  * $v_1$과 $v_2$은 같은 computational graph를 가지지만 서로 다른 네트워크에 의해 다르게 임베딩 된다.<br>![image](https://github.com/Jiwon96/papers/assets/65645796/d9562171-4222-4532-8ec1-6c146133b93a)

  * GNN과 달리 ID-GNN은 cycle count를 계산할 수 있다.
  * ID-GNN-Fast에서는 각 레이어에서의 cycle count로 augmented node feature를 heterogenous message passing 없이 간단하게 identity 정보를 가질 수 있다.

# Robustness of Graph Neural Network <집중 필요>
* Robustness
  * 딥러닝 네트워크는 adversarial attack에 취약하다.
  * 모델이 real world에 적용되기 위해서는 robustness를 갖추는 것이 중요하다.
  * input 그래프나 GNN의 prediction이 조작되었을 때 robust해야 하므로 semi-supervised node classification을 한다. <b>semi-supervised node classification 뭐지? </b>

* Attack Possiblitieis
  * Target node $t \in V$는 label prediction을 바꾸고자 하는 노드이다.
  * Attacker nodes $S \in V$는 attacker가 수정할 수 있는 노드이다.
  * Direct attack은 $S =t$로 attacker node가 target node와 동일한 경우이다. 직접 target 노드의 feature를 바꾸거나 엣지를 추가 및 제거할 수 있다.
  * Indirect attack $t \notin S$로 target node가 attacker nodes에 속하는 않는 경우이다. Attacker node의 feature 변경 및 엣지의 추가/제거로 target node를 간접적으로 바꾼다.
 
* Mathmatical Formulatioin<br>![image](https://github.com/Jiwon96/papers/assets/65645796/f1707532-e35f-46c1-9e51-86f659719aac)
  * Attacker는 조작은 최소화하면서 target node label prediction의 변화는 최대가 되도록 해야 한다.
  * Original 그래프의 인접행렬을 $A$, feature 행렬을 $X$라 하고 manipulated 그래프의 행렬들을 A' X'이라 하자 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/855157f1-a99a-4dc2-97a6-287ccda62814) ![image](https://github.com/Jiwon96/papers/assets/65645796/57db2364-6f03-4cf8-9e71-061848c2093e)
  * GCN은 loss를 최소화하는 $\theta$를 찾고 target node에 대한 예측 확률이 최대인 클래스를 $c^*_v$라 한다.
  * 조작 후의 예측 클래스와 이전의 예측 클래스와 달라지기를 원한다.? <b>왜? 어떤것을 의미하는 걸까? 목적이 무엇일까?</b> <br>![image](https://github.com/Jiwon96/papers/assets/65645796/632d855d-c0b5-4964-8a7a-256c5b9a9cd0)
 
  * 새롭게 예측된 $c^*_v$의 예측 확률과 기존에 예측되었던 c^*_v의 확률의 차이가 (A', X') $\sim$(A,X)라는 가정 하에 최대가 되어야 한다 <b>여기서 잘 이해가 필요하다</b>
  * 하지만, 인접행력 A'가 이산적이기 때문에 gradient를 활용한 최적화가 불가능하고 모든 A', X' 에 대해 GCN이 retrain 되어야 한다는 문제가 있다. <b> 공부해야 한다

  



[글 참고, 여기서 의문이 드는건 강의 듣고 추가함](https://velog.io/@kimkj38/CS224W-Lecture-16.-Advanced-Topics-on-GNNs)
