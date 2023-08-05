# 오늘 다룬 주제: knowledge Graph Task and Embedding
* Answer the path queries by traversing the KG: What proteins are **associated** with adverse events **caused** by Fulvestrant?
* Query: (entity: Fulvestrant,(r:Causes, r:Association)) -> Answer : traverse the graph
  * **BUT** Knowledge graphs are notoriously incomplete. <b> 지식그래프가 불완전 하기 때문에 쿼리 예측이 필수적임 근데 어떻게 할건데? 이게 오늘 핵심 질문임 </b> 
  * Completed KG is a dense graph -> Time Complexity of traversing a dense KG is $O(d{^L}_{max})$

# Traverse query
* Key idea: Embed Query <b>해결 아이디어</b>
* Generalize **TransE** (lecture 10 refer) to multi-hop reasoning. only TranE can handle composition relation.
* **Question** How can we use embeddings to implicitly inpute the missing. -> Traversing KG in Vector space (ex is on slide 31 page.)<b>해결 방법</b>

# Reasoning over KGs Using Box Embedding 베리베리 중요
* hyper-rectangles(box): query의 연산값이 됨<br>![image](https://github.com/Jiwon96/papers/assets/65645796/36b81908-57bc-427d-ace8-ced837c3aa27)
* 장점: intersection이 잘 정의됨
* 필요한 것(page 36)
  * Entity embedding: num of params: d $\times |V|$
  * relation embedding: num of params: $2 \times d \times |V|$
  * intersection operator f: box의 intersection area 구하는 방법
  * Projection Operator $P$: Box $\times$ Relation ex slide p38페이지 참고 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/ba8103d8-bb7a-484a-8398-077c84659390)
  * Geometric Intersection Operator(page 43): query의 intersection 이후의 임베딩 값 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/2dd1c3b2-4118-4872-a99c-d6e223ba5924)
  * 여기서 Center와 여백을 결정할 수 있는 offset 속성(가로, 세로 길이)이 있어야 됨 이 때 계산하기 위해서는 다음과 같음<br> 센터 계산<br>![image](https://github.com/Jiwon96/papers/assets/65645796/a0c5633f-b5f5-4352-ad8e-4d7ee29270f2)<br>오프셋계산<br>![image](https://github.com/Jiwon96/papers/assets/65645796/28055193-c62a-4159-b885-a21fb06c2a78)
  * 이 때 dist: $d_{box}{(q,v)} = d_{out}{(q,v)} + \alpha \cdot d_{in}{(q,v)}$ where 0< $\alpha$ <1
  * $f_q(v) = -d_{box}{(q,v)}$인데 이 때 $f_q(v) = -d_{box}{(q,v)}$ 겹치는 곳은 작아져야 하기 때문에 f의 연산은 음수의 값을 가져야 함.(page 47)
 
# and - or 연산
* and 연산은 intersection 이므로 표현이 가능하지만, or 연산은 연산이 복잡해짐 ex) [q2]={v2}, [q4]={v4} 일 때 q2 합집합 q4 박스는 v3에 걸림 무조건 slice 58 ex)<br>![image](https://github.com/Jiwon96/papers/assets/65645796/8f2a3ec7-7e95-4038-bcdf-6c254509a0e2)
* **따라서** M conjuctive queries 에서 all or query를 다루기 위해서는 dimenstionality of $\theta{(M)}$이 필요함
* **마지막에 or 쿼리를 넣는걸로 바꾸면 차원을 줄일 수 있음**

# Distance Betw q and An Entity (슬라이드 )
* dist: ![image](https://github.com/Jiwon96/papers/assets/65645796/ad2a8f4e-2044-4f3a-b601-9bb02ee6b274)
* trainable paras:
  * d $\times |V|$
  * $2 \times d \times |V|$
  * intersection operator f
 
* 과정![image](https://github.com/Jiwon96/papers/assets/65645796/9027a082-84ea-4e18-9f0f-fe41c8b56566)

# 초기화 할까?
* 먼저 변수부터 초기화 (node, edge)
* tail 노드 하나 잡고 -> intersect 된 관계 파악 -> forward 와 backward 함 (차례대로 약간 bfs 느낌으로)
