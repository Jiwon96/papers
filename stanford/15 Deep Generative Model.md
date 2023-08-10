# Graph Generation
* given : Graphs sampled from $p_{data}(G)$ 
* Goal:
  * Learn the dist $p_{model}(G)$
  * sample from $P_{model}(G)$
* 실제 그래프 분포 샘플들을 이용해 $P_{model}(G)$ 을 학습하고, 학습된 $P_{model}(G)$에서 샘플링하여 그래프 생성

* <b>의문:</b> $p_{data}(G)$ 와 $p_{model}(G)$의 차이점은 무엇이지? -> 우리의 목표는 그래프를 generate할 것임. 이 때 generate를 할 때는 kernel 함수를 이용해서 generate를 하는데 이 때 필요한게 parameter와 그 액션이 무엇이 나왔는지가 있어야 됨 이 때 $p_{data}(G)$는 우리가 여태까지 모은 데이터로 현실을 반영하는 예를 들면 $H_2O$ 같은 데이터들이고, parameter는 이제 우리가 이걸 학습해야 하는 값임. 그래서 어찌저찌해서 $\theta$에 대한 학습이 끝났으면 첫 번째 목표 달성임 이제 새로운 물질을 만들어 내기 위해서는 H에서 add edge를 하든 add node를 해야 하는데 이를 하는게$P_{model}(G)$임
  * $p_{data}(G)$  is the data distribution, which is never known to us, but we have sampled $x_i$ ~ $P_{data}(x)$
  * $P_{model}(x; \theta )$ is the model, parametrized by $\theta $, that we use to approximate $p_{data}(G)$
  * <b>의문:</b> $P_{model}(x; \theta )$ 와 $p_{data}(G)$ 의 차이는? given에서 goal 되는 과정이 어떻게 되는지? $P_{model}(x; \theta )$  -> appoxim $p_{data}(G)$ -> Goal 2가지 -> 후자 먼저 설명하면 $H_2O$처럼 실생활에서 얻은 데이터임 전자는 이제 실생활 데이터를 잘 학습하기 위한 확률적 모델일까나?
 
* <b> Density Esimation</b>
  * make $P_{model}(x; \theta )$ <b> close to</b> $p_{data}(G)$ <b>질문: 이것이 무엇을 의미하지? 다음 입력의 x인가? 아니면 다른 x와 edge가 연결될 것인가를 의미하나?</b> -> 이건 위에서도 잘 설명함. 파라미터 학습임 우리가 가진 데이터 잘 설명하는
    * $\theta^*$ = $argmax_{\theta}E_{x\sim p_{data}}logp_{model}(x|\theta)$
   
  * Maximum Likelihood Estimation을 이용한다. 즉, 표본들을 이용해 $p_{model}$의 likelihood를 최대로 하는 최적의 likelihood를 최대로 하는 최적의 parameter θ를 찾는다.
 
* <b> Sampling</b>
  * Smaple from $P_{model}(x; \theta )$
    * Sample from a simple noise distribution (e.g. standard normal distribution), $z_i \sim N(0,1)$
    * Transform the noise $z_i$ via $f({\centerdot})$, $x_i = f(z_i;\theta )$
      * $f({\centerdot})$ 를 deep neural network로 구성하고, 갖고 있는 데이터들을 이용해 학습시킨다.
   
* <b> 의문</b>: 그러면 $z_i$를 들을 linear나 그런 레이어로 transform 해서 $x_i$를 구하는 건가? <b>예시가 집중해서 보자</b> -> ㄴㄴ auto-regressive model을 사용함 여기서는
* <b> Auto-regressive models</b> -> 위에서 f라는 커널함수를 사용할 때 사용되는 함수임 이 때 variation auto encoder 등을 사용해도 됨
  * $P_{model} (x; \theta)$ 는 density estimation과 sampling에 사용되고, 이를 위해 auto-regressive model을 사용한다.
    * $P_{model}(x; \theta )$ = $\Pi^n_{t=1}P_{model}(x_t|x_1, \cdots , x_{t_1};\theta )$
     * (강의 후 추가) 이 때 $x_i$는 t-th 액션이므로 add node나 add edge를 값으로 가짐 따라서 sequence는 add edge, add node .... 이런식으로 sequence를 구성
   
  * Idea: Joint distribution이 conditional distribution들의 곱으로 표현될 수 있는 Chain rule을 이용한다.
  * 이를 위해 $X = (x_1, x_2, \cdots, x_t)$를 sequence로 보고, $x_t$는 t번째 행동이 된다. 여기서 행동은 node 또는 edge를 추가하는 것이다.
 
  * <b>질문</b> sequence로 본다는 것은 뭘까? <b>예시</b>를 볼 수 있을까? 전 액션이 현재 결정할 액션에 영향을 미친다는 것 같은데 주의 깊게 볼 필요가 있다.


# GraphRNN: Generating Realistic Graphs
* <b> Model Graph as Sequences</b>
 * node와 edge를 추가하면서 그래프를 만들어감
  * node ordering $\pi$에 따라 Graph $G$는 node와 edge들의 sequence인 $S^{\pi}$에 유일하게 매핑된다
  * $S^{\pi} = f_S(G, \pi) = (S^{\pi}_1, \cdots , S^{\pi}_n)$
* <b>Node-level</b>
  * Node를 추가
* <b>Edge-level</b>
  * edge를 추가 in adj


# Background: RNN
* RNN은 sequencial data 위해 고안됨
  * RNN은 순차적으로 input sequence를 받아 hidden states를 update함
  * hidden states 는 RNN 입력의 모든 정보를 요약한다 ? -><b> 어떻게 요약하지?</b>
  * update는 다음과 같이 RNN cells를 통해 수행된다

# Graph RNN
* <b> 종류</b>
  * Node-level RNN generates the initial state for edge-level RNN
  * Edge-level RNN sequentially predict if the new node will connect to each of the previous node <b> ???? 예제</b> 그래프 G에서 adjaency matrix로 변환된 것을 보면 h1에서 h2로 갈 때 노드가 생김 이걸 node level graph net임 그리고 이를 다시 h3에서 반복한 후 노드 2가 추가되는데 2번 째 노드가 [1,0]이 되는 것을 볼 수 있다. 이것을 2번 노드에 대해서 edge 그래프를 만들어 내는 것을 볼 수 있다. ![image](https://github.com/Jiwon96/papers/assets/65645796/ab9b8b33-1a11-4c3b-bb49-a822c6f2fd37) ![image](https://github.com/Jiwon96/papers/assets/65645796/d1b724d3-2b22-411a-899b-1a38f50839fd)



* <b>구조</b>
  * 이전 출력을 입력으로 사용해 sequence를 생성
    * Start of sequence token(SOS)를 초기(initial) 입력으로 사용
    * End of sequence token(EOS)를 RNN의 추가 출력으로 사용해서 생성을 멈춤
  * -> 결정론적인 모델이 된다.
* Use $\Pi^n_{k=1}P_{model}(x_t|x_1, \cdots , x_{t_1};\theta )$
* $y_t = P_{model}(x_t|x_1, \cdots , x_{t_1};\theta )$라 하자. 그러면 $x_{t+1}$를 $y_t$에서 샘플링 해야 됨. 즉, $x_{t+1} \sim y_t$
  * RNN은 각 단계에서 확률 출력
  * 확률 분포에서 샘플링하고, 다음 단계의 입력으로 사용
 
* <b> Test Time</b>
  * $y_t$의 확률에 따라 $x_{t+1}을 샘플링해서 다음 단계 입력으로 사용 -> $y_1$= 0.9이면 $x_2 = 0.9 \sim 1$??? 여기 부분 이해 X <br>![image](https://github.com/Jiwon96/papers/assets/65645796/7cc54103-cf46-4eea-9050-d5c9349b5c7f)
 
* <b> Training Time </b> 질문: 왜 test time -> Training time 이지? 상관없음
  * ground truth $y^*$와 prediction $y$를 비교해 loss를 계산하고, [teacher forcing](https://wikidocs.net/24996)을 이용해(다음 값에 정확한 값을 넣어서 훈련을 잘 시키기 위함 학습 데이터 활용하는 것) 다음 단계 입력으로 ground truth를 사용 <b>질문: ground truth는 뭐지 어떻게 구하지?</b>
  * $L = -y^{*}_1log{(y_1)} + (1-y^*_1)log{(1-y_1)}$ binary cross entropy (사진 넣자) -> 사진을 넣기보다는 태블릿 슬라이드 27부터 천천히 보면 됨


* <b> 훈련과 테스트 타임을 같이 (Testime, Training time) </b>
  * Add a new node: Node RNN을 실행하고, Node RNN의 출력을 Edge RNN의 초기치로 사용 <b>질문: Node RNN은 Node level이고 Edge RNN은 Edge 레벨인가?</b>
  * Add new edges for the new node: Edge RNN을 실행하여 새로운 node가 이전의 node 각각과 연결되는지 예측 
  * Add another new node: Edge RNN의 마지막 hiddent state를 사용해서 Node RNN을 실행
  * Stop graph generation: Edge RNN이 EOS를 출력하면 그래프 생성을 종료

* Traning
 * 사진 예제 대체 -> 사진을 넣기보다는 태블릿 슬라이드 27부터 천천히 보면 됨

# Tractability
* Random node ordering의 경우 edge generation시 이전의 모든 노드들을 고려해야해서 복잡도가 증가하고, long-term dependency 문제가 발생한다. 이를 해결하기 위해 BFS(Breadth-First Search) node ordering을 사용한다.
 * BFS node ordering 이란?
   * 이점 1: Reduce possible node orderings: Random ordering은 $O(n!)$이지만, BFS는 이보다 적음
   * 이점 2: Reduce steps for edge generation: edge 생성시 인접 노드들과의 관계만 고려할 수 있어 long-term dependency 문제를 해결한다. <b>질문: edge generation을 줄일 수 있다는게 무엇일까?</b>

# Evaluating Generated Graph
* 실제와 비교했을 때 얼마나 유사할까?
 * visual similarity -> plot 그림
 * Graph stat similarity
   * Degree Dist
   * Clustring coeff dist
   * orbit count stat
 * Training graph statistics 집합과 generated graph statistics를 비교하기 위해 EMD(Earth Mover Distance)와 MMD(Maximum Mean Discrepancy)를 사용한다.
  * EMD(p,q) = $inf_{\gamma \in \Pi (p,q)} E_{(x, y) \sim \gamma }(||x-y||)  $
    * p, q: two joint distribution
    * $\Pi(p,q)$: the set of all distributions whose marginals are p and q respectively
    * $\gamma$: valid transport plan <b> ?????? </b>
    * <b> 숙제: EMD 의미가 무엇인지</b>
   
  * $MMD^2(p||q) = E_{x,y \sim p} {[k(x,y)]} + E_{x,y \sim q} {[k(x,y)]} - 2E_{x \sim p , y \sim q} {[k(x,y)]}$
    * $k$: kernel function
    * <b> 숙제: MMD가 의미하는바는 무엇인지</b>

<b> EMD와 MMD를 잘 찾아보는게 필요할 것 같다. </b>


# application of Deep Graph Generative Models
* 그래프 생성 모델을 사용해 신약 개발(drug discovery)에 활용할 수 있다. 이를 위해서는 다음 조건을 만족해야 한다.
  * Optimize a given objective (high scores): 약과 같은 특성을 갖게 최적화 되어야 한다.
  * Obey underlying rules (valid): 타당한 화학적 규칙을 따라야 한다.
  * Are learned from examples (Realistic): 실제 분자 그래프를 모방해야 한다.
* <b>강화학습</b> ML agent는 Environment를 관찰(파악)하고, action을 취해 Environment와 상호작용을 하고, Reward를 받는다.


# GCPN 
* Graph Convolutional Policy Network = Graph representation(graph convolution) + Reinforcement Learning(policy)
  * <b>graph Neural Network</b>가 그래프 구조적 정보를 포착한다.
  * <b>Reinforcement learning</b>으로 desired objectives를 따르게 생성한다.
  * <b>supervised training</b>으로 주어진 데이터셋을 모방한다. <b>숙제:</b> 이 3개가 왜 중요하지?
 
* <b>GCPN vs GraphRNN</b> GCPN 논문을 나중에 참고해야 할 듯 아직 잘 모르겠음.
  * 공통점: Sequentially 그래프를 생성, 주어진 그래프 데이터셋 모방
  * 차이점:
   * GCPN은 generation action을 예측하기 위해 GNN을 사용한다. <b>질문</b> generation action?
     * 장점: GNN이 RNN보다 expressive함
     * 단점: GNN이 RNN보다 연산량이 많아 오랜 시간 걸림
    
   * GCPN은 RL을 사용해 goal-directed graph generation을 한다. <b>질문:</b> goal directive이면 아마 만들어가는데도 규칙이 있는거 같음
  * 두 모델 모두 순차적으로(sequentially) node를 추가하면서 그래프를 생성하는데, edge를 연결하는 방법에 있어 차이가 존재한다. <b>GraphRNN</b>은 hidden states를 이용해 action(edge)을 예측한다. 반면에 GCPN의 경우 각각의 node embedding을 GNN을 통해 구한 후 prediction head를 통해 action(edge)을 예측한다.
    * <b>질문:</b> hidden states와 node embedding, <b>pedction head???</b> 임베딩으로 prediciton head를 통한다는게 뭔말일까? * graph에서 head가 노드 u일 확률이라고 생각하면 된다. 즉 v가 tail일 때 u가 헤드일 확률 -> 둘이 연결될 확률
   
* <b>train</b>
  * reward 정의: reward = final reward + step reward
    *  step reward: 각 단계마다 타당한 action을 했을 때 얻는 보상. 타당한 action은 타당하게 edge를 연결시킨 것
    *  final reward: 최종 단계에서 desired properties를 갖을 때 얻는 보상.
  * Training은 2가지 부분으로 나뉨
    * Supervised: Gradient를 사용해서 모델이 그래프 샘플들을 모방하게 학습
    * RL: Policy gradient algorithm을 사용해서 보상이 최적화 되게 학습
   
* <b> example</b>

    
[참고 자료](https://velog.io/@skhim520/15.-Deep-Generative-Models-for-Graphs)
