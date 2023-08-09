# Generative model for graph
* Degree Distribution
  * P(k): 임의의 노드가 k의 degree를 가질 확률
  * $N_k$를 degree가 $k$인 노드의 수라 할 떄 정규화된 히스토그램 $P{(k)}=N_k/N$으로 나타냄
 
* Clustering Coeff
  * $C$로 표기하고 노드 i가 이웃들과 어떻게 연결되어 있는지 나타냄
  * Degree가 $k_i$인 노드 i에 대해 $C_i = \frac{2e_i}{k_i(k_i-1)}$
  * $e_i$는 노드 i의 이웃노드들 간의 엣지의 수를 의미한다 -> i노드가 끝점이 아닌 에지의 개수를 세면 됨
  * $C = \frac{1}{N}\Sigma{_i}{^N}C_i$, 모든 노드에 대한 평균값으로 C를 정의
 
* Connectivity
  * $s$: 가장 큰 component의 크기
  * giant component: s가 매우 클 때 기준은?<b>숙제</b> -> 보통 노드의 절반이상이 component로 구성되어 있으면 giant component라고 하는듯
  * BFS를 통해 모든 노드를 방문했을 때 network가 연결되어 있다고 말하고, 방문하지 않은 노드가 있을 경우는 BFS를 반복한다.
 
* Path Length
  * 그래프 내 노드 쌍의 최대 거리를 Diameter라고 한다.
  * 평균 path length는 connected graph에 대해서만 계산하고, average h = $\frac{1}{2E_{max}\Sigma_{i,{j \neq i}}}h_{ij}$
  * $h_{ij}$는 노드 i,j의 거리를 $E_{max}$는 엣지의 최대 개수(노드 쌍의 개수)를 의미
  * graph Diameter를 구하기에는 시간이 많이 들 때가 있어서 평균 path 길이로 대체할 때가 많음

* null model:모델을 generating 시키는 것.(만들어낸 모델)
 
# Erodos-Renyi Random Graph
* $G_{np}$: 엣지가 독립 항등 분포(iid)의 확률 p를 가지는 노드 n에 대한 undirected graph => 얘만 집중
* $G_{nm}$: m개의 엣지가 균등한 확률로 랜덤하게 뽑히는 노드 n에 대한 undirected graph
* 파라미터가 n,p이지만, n,p의해 그래프가 unique하게 결정되지 않음 -> $G_np$는 properties로 degree dist $P{(k)}$, clustering coeff $C$, path length $h$를 가짐

* Degree Dist:
  * $G_{np}$는 P(k)는 이항분포 따름

* Clustering Coeff
  * E[$C_i$] = p = $\frac{kbar}{n-1}$ ~~ $\frac{kbar}{n}$
 
* Connected Component: 뭐에 쓰려나? <b>숙제</b>
  * Connected Component 는 그래프의 크기를 대충알 수 있음
  * 예를 들어 giant component가 p=1/(n-1) 일 때 avg_deg= 1임 이 때 이를 기준으로 degree k가 1보다 작으면 그래프 컴포넌트 크기는 $\Omega{(logn)}$임 즉 logn보다 모두 작음 반면 디그리가 1보다 크면 적어도 한 컴포넌트 크기는 $\Omega{(n)}$ 임 다른거는 $\Omega{(logn)}$ 이고
  * 이를 활용하면 expansion에서 그래프의 robustness를 알 수 있음
 
* Expansion :
  * Robustness의 척도가 되고 ?왜?, subset을 쉽게 만들 수 있는 구조면 low expansion, 어려운 구조: high expansion
  * Robustness는 그래프 G에서 서브셋 S를 만들기 위해서 끊어야 하는 에지 개수가 많을 수록 robust하다고 함 이 때 alpha는 G에서 끊어야 하는 에지의 비율임
 
* real network와 $G_{np}$비교
  * clustering coefficient, Degree dist가 다르다.
  * 실제 그래프의 giant componet는 phase transition 형태로 나타나지 않는다? (phase transition은 k=1을 기준으로 giant component가 등장하는 것을 의미)<br>![image](https://github.com/Jiwon96/papers/assets/65645796/dd764472-4ded-4d65-92bf-a0309102ac98)

<b>숙제</b> : edge와 node를 구성하는 방법? generation이니까 아이디어도 생각해볼 필요 있음, -><b> Erodos-Renyi Random Graph</b> 실제와 비교 지금 나온 아이디어는 현실을 반영 X 특히 현실 네트워크는 tringle 관계가 많이 성립하는데 랜덤으로 한 방법은 이 속성을 만족 X 그리고 주변에서 네트워크를 구성할 때 누가 랜덤으로 구성함? 그래서 대체 아이디어 필요함
 
# The Small-world model => Erodos-Renyi Random Graph가 제대로 그래프 반영 X 하기 때문에 나옴 보간법으로 만들어보자
* 높은 clusering coefficient와 큰 diameter를 가지는 regular lattice graph를 <b>interpolation(보간법)</b> 하여 그래프를 만든다. what is interpolation?
* 결과? or 효과?, 방법?
  * 숙제

# Kronecker Graph Model -> Erodos-Renyi Random Graph의 대체품 어떻게 만들지?
* Object는 자기 자신의 일부와 비슷하므로 네트워크를 재귀적으로 구성할 수 있다. (어떤 과정을 위함일까? 얻는 효과는?)
* Kronecker product를 통해 self-similar 행렬을 만든다. (왜?)
* <i>Kronecker graph</i>는 kronecker product를 초기 행렬 $K_1$에 반복적으로 행해 만들 수 있음
  * Stochastic Kronecker graph
  * Generation of Kronecker graph -><b>숙제</b> 실제 그래프와 유사해짐, 어떻게 만들까? 방법

