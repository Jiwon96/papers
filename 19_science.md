# Pre-training
* 동기:
  * graph classification 할 때 graph를 임베딩 해서 분류 문제를 처리함... but? 그래프를 구조를 잘 표현하는 노드인데 이도 임베딩을 하면 더 그래프를 더 잘 표현할 수 있지 않을까?
 
* 현재 ML의 한계
  * labeled data가 부족함
  * train set A, B    test set C가 있을 때 실험 set을 (A, C), 와 (B, C)의 결과는 다르다
 
* 아이디어:
  * 도메인 지식을 훈련전에 도입시키자. 곰을 훈련시킬 때 강아지, 고양이 들판 위에 곰, 북극 곰 등등을 다 넣어서 훈련
    * pre-training 모델의 아이디어
   
* ex) molecule classification
  * downstream task가 아닌 엄청 많은 분자를 전처리 했을 때 score(slide 14)
    * 이 때 전처리 하지 않은 GNN모델이 score가 더 좋게 나올 때가 있었음...
      * 노드들도 전처리를 진행하자.(C, O 등등)
  * Attribution Masking(C, O 등을 마스킹 후 임베딩하는것)
    * 주어진 원소를 마스킹 시키고, 주어진 분자에서 해당 원소를 예측하는 업무를 진행함(원소를 임베딩함)
   
  * Context prediction
    * Masked Node 를 Center node로 잡고 이를 분류 문제로 치환함.
    * 이때 Masked node K-hop neighborhood와 context graph의 K hop neigh를 concat 시켜서 임베딩을 구함 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/da35688c-a5d3-4706-81cc-b1b666067a22)

# Hyperbolic Graph Embedding
* Tree 구조에서 사용할 수 있는 아이디어임
  * 이진 트리에서는 child가 exponentially 증가하고, 그 leaves들끼리 다르지만 굉장히 유사할텐데 euclidean space 에서는 이 leaves 들을 구별하면서도 비슷하게 임베딩하기에는 표현력이 부족함.
    * <b>Hyperbolic Space 탄생</b>
* 정의
  * curvature 절대값이 클수록 더욱 곡면이라는 것을 알 수 있음, hyperbolic 모양를 나타낸다 생각하면 됨
    * positive일 때: 사이클을 이룸 O 모양
    * 0일 때 평면
    * negative 값일 때: ) ( 이런 형태를 가짐<br>![image](https://github.com/Jiwon96/papers/assets/65645796/79600234-f669-4b86-814e-109350f3ae46) ![image](https://github.com/Jiwon96/papers/assets/65645796/29d84fa3-927a-407a-a038-69a3f286bd83)
  * Manifoid: High-dimensional surface
  * Riemannian Manifold: Manifold에서 특정 성질을 만족시키는 Manifold <br>![image](https://github.com/Jiwon96/papers/assets/65645796/f06cef85-4787-44d0-81bd-37ba582c70fa)
  * Geodesic: shortest path in manifold: manifold에서의 직선이라고 생각하면 됨
  * Hyperbolic space: Riemannian Manifold인데 curvature = ${-}\frac{1}{K^{'}}$ 으로 정의됨 K>0
  * $$\sqrt{K}$$ 는 radius of the Poincare ball
  * 다음 정의 3가지는 쓰기 어려워 사진으로 대체함 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/2b27b597-2227-4969-aa73-0fbd03612de0)<br>![image](https://github.com/Jiwon96/papers/assets/65645796/38c60dd9-63da-4ed8-989f-a820b405591b)<br>![image](https://github.com/Jiwon96/papers/assets/65645796/7637bce3-ab9c-4cca-a246-56030e45da7b)
    * <b>여기서 Tangent space는 hyperboloid model을 정사영 시킨 모델(euclidean space로 approximate)이라 생각하면 됨 </b>


* euclidean space 와 hyperbolic space (parallel postulate ($5^{th}$ axiom)) 기하학 개념이므로 찾아보삼 뭐라하지 그 평행선 동위각? 이라 하나 그 개념임
  * 직선: 직선과 직선을 지나지 않는 점이 주어졌을 때 
    * euclidean space 에서는 점이 직선과 평행한 선이 1개임
    * hyperbolicc space 에서는 무수히 많은 직선이 지날 수 있음 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/fd698d4f-dbec-432f-9191-1fd9dbef35f5)
   
* hyperbolic space를 나타내는 2가지 방법
  * Poincare Model
    * 간단한 visualization <br>![image](https://github.com/Jiwon96/papers/assets/65645796/27b23ecf-27d9-465b-8801-c406e7c886ff)
  * Hyperboloid Model <br>![image](https://github.com/Jiwon96/papers/assets/65645796/258b59e9-48ce-4e5f-b2fa-4e2fdc8ce28d)

* Geodesic Distance
  * curvature의 절대값이 커질수록 곡선의 정도가 굽음. 즉, 같은 좌표에서 x와 y사이의 거리가 멀어짐
 
* 새로운 정의
  * Exponential map: 유클리디안에서 manifold 로 mapping 하는 것
  * Logarithmic map: inverse operation of exponential map<br>![image](https://github.com/Jiwon96/papers/assets/65645796/6f224655-2374-4988-8a71-66b2922ff33a)

* 레이어 구성
* ![image](https://github.com/Jiwon96/papers/assets/65645796/a5b46eeb-b299-4f67-a05c-d2a123889691) ![image](https://github.com/Jiwon96/papers/assets/65645796/a5b57db0-b375-48f6-9dbb-92baba9d39ec)


# Design Space of Graph Neural Network
* 이 문제를 조명한 이유: 특정 task(노드 분류, 에지 회귀 등) 마다 사용되는 모델이 달라짐 즉 domain이 달라질 때마다 어떤 모델이 좋을지 궁금함
* 아이디어: task 들을 분류해서 특정 task에 적용되는 모델을 사용하자
* 실험 방법은
  * 1st task similarity metric을 정의하는데 anchor model set(M1, M2, ..)(GNN 모델 셋이라 생각하면 됨) 을 먼저 정한후에 이를 각각의 task 별로 돌리고 그거에 대한 score에 따라 model set을 정렬하고 순서가 비슷한 정도로 similarity를 정함(corr) 사용
  * 실험하고 싶은 specification 만을 다르게 해서 점수가 높으면 rank 1, 낮으면 rank 2를 줘서 rank 들을 서로 비교함<br>![image](https://github.com/Jiwon96/papers/assets/65645796/a10c75c4-9bbc-4ef6-aab7-7b6a0e18d23a)


예시 



  
