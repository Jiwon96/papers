# Heterogeneous Graph
* 정의
  * $G = (V, E, R, T)$ $v_i \in V$ Edges with relation types $(v_i, r, v_j) \in E $
  * Relation type $r \in R$
  * example<br>![image](https://github.com/Jiwon96/papers/assets/65645796/8796591c-b5a5-4268-90a3-cffcd8c4354c)

* Relation GCN
  * heterogeneous graphs를 GCN을 활용해 모델링해보자.
  * Layer 구성
<br>![image](https://github.com/Jiwon96/papers/assets/65645796/878e805c-7fca-4c42-9623-9a5f2992e385)
<br>![image](https://github.com/Jiwon96/papers/assets/65645796/4e452738-0851-48a1-b818-b29f2572471f)

* transformation
  * ![image](https://github.com/Jiwon96/papers/assets/65645796/3c738833-aa3f-42ba-9d0b-5053f2827fd0)

* aggregation
  * ![image](https://github.com/Jiwon96/papers/assets/65645796/cf431b88-de85-44a7-9ef0-89d5a9221654)

* RGCN
  * $h^l_v$는 자신의 임베딩레이어로 자신의 이전 정보를 W를 통해 transform 해서 self loop를 돌림
  * ![image](https://github.com/Jiwon96/papers/assets/65645796/a7639952-4832-438e-ab5e-ab620a5ef140)

* 단점
  * relational graph가 많아지면 relation마다 연산을 해야하므로 파라미터 개수가 많아짐 -> 연산량이 많아짐
    * Block Diagonal Matrices: $W_r$의 매트릭스를 block diagonal matrices로 만들기 but 근처 1->2 노드처럼 근처 노드의 정보만 알 수 있는게 한계
      * ![image](https://github.com/Jiwon96/papers/assets/65645796/143c6c78-45a2-4716-a799-ea2215499d4a)

    * Basis Learning: share weights(요인 분석으로 이해하면 될듯)
      * ![image](https://github.com/Jiwon96/papers/assets/65645796/2953ca12-f09e-430a-9088-e5fbc04fcef0)

* Link Prediction
  * training
    * supervision edge로 훈련 시키고, negative edge를 고려해서 loss를 구함<br>![image](https://github.com/Jiwon96/papers/assets/65645796/eff50874-a6a3-48ea-b8f3-c485368cdd83)

  * Evaluation
    * 대상 relation i(edge)
    * 같은 relation 값을 기준(r3)으로 훈련 때 사용하지 않은 relation을 RK(E,r3,B) 잡고 RK가 예측값 k보다 보다 작으면 타당하다고 보고 hit을 늘린다. <br>![image](https://github.com/Jiwon96/papers/assets/65645796/593c357c-024b-4401-90b6-84174c7706c4)

# knowlege Graph Completion Task
* <b>Predicting Missing Tail</b>
* The concept of triples: (h, r, t) = Edge in KG
* <b>The Goal</b>: Given a true triple (h, r, t), the goal is that the embedding of (h,t) <b>should be close</b> to the embedding of t.
* Relation에 대한 속성(connection pattern between head and tail)
  * Symmetric relation: r(h,t) => r(t, h) ex) 룸메이트, Antisymmetric relation: r(h,t) => not r(t,h) -> ex r:엄마
  * Inverse relations: $r_2$(h,t) => $r_1$(t,h) ex) r2-교수, r1-학생
  * Composition relation:example이 이해가 안된다??? <br>![image](https://github.com/Jiwon96/papers/assets/65645796/2e306a02-7bae-4a68-94ca-729a9f03dac7)
  * 1 - to - N relation:<br>![image](https://github.com/Jiwon96/papers/assets/65645796/7634a903-cd41-45de-86fc-be485f3ec569)

* 여기에서는 KG를 임베딩하는 Method가 4가지를 소개한다.(알고리즘은 ppt 참고하시길 바람)
  * TransE : h+r $\approx$ t, h,r,t $\in R^d$ if the given fact is true else h+r $\neq$ t, relation $r$ score function $f_r$ (h,t) = $-||h+r-t||$
  * TransR : TransE + with $M_r$ $\in R^k$ $^\times$ $^d$
  * DistMul: <br>![image](https://github.com/Jiwon96/papers/assets/65645796/0fc71e37-0336-400a-b135-a5e14f88f63b)
  * ComplEx:<br>![image](https://github.com/Jiwon96/papers/assets/65645796/c36ce474-d407-4121-96c0-2410ed0d4672)
  ![image](https://github.com/Jiwon96/papers/assets/65645796/9596d2d9-ce47-4a09-819a-03d554ec5fac)

