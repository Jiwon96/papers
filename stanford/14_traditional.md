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
  * giant component: s가 매우 클 때 기준은?
  * BFS를 통해 모든 노드를 방문했을 때 network가 연결되어 있다고 말하고, 방문하지 않은 노드가 있을 경우는 BFS를 반복한다.
 
* Path Length
  * 그래프 내 노드 쌍의 최대 거리를 Diameter라고 한다.
  * 평균 path length는 connected graph에 대해서만 계산하고, average h = $\frac{1}{2E_{max}\Sigma_{i,{j \neq i}}}h_{ij}$
  * $h_{ij}$는 노드 i,j의 거리를 $E_{max}$는 엣지의 최대 개수(노드 쌍의 개수)를 의미
 
# Erodos-Renyi Random Graph
* $G_{np}$: 엣지가 독립 항등 분포(iid)의 확률 p를 가지는 노드 n에 대한 undirected graph => 얘만 집중
* $G_{nm}$: m개의 엣지가 균등한 확률로 랜덤하게 뽑히는 노드 n에 대한 undirected graph
* 파라미터가 n,p이지만, n,p의해 그래프가 unique하게 결정되지 않음 -> $G_np$는 properties로 degree dist $P{(k)}$, clustering coeff $C$, path length $h$를 가짐

* Degree Dist:
  * $G_{np}$는 P(k)는 이항분포 따름

* Clustering Coeff
  * E[$C_i$] = p = $\frac{kbar}{n-1}$ ~~ $\frac{kbar}{n}$
 
* Connected Component: 뭐에 쓰려나?
  * ???
 
* Expansion :
  * Robustness의 척도가 되고 ?왜?, subset을 쉽게 만들 수 있는 구조면 low expansion, 어려운 구조: high expansion
 
* real network와 $G_{np}$비교
  * clustering coefficient, Degree dist가 다르다.
  * 실제 그래프의 giant componet는 phase transition 형태로 나타나지 않는다? (phase transition은 k=1을 기준으로 giant component가 등장하는 것을 의미)
 
# The Small-world model
* 높은 clusering coefficient와 큰 diameter를 가지는 regular lattice graph를 <b>interpolation(보간법)</b> 하여 그래프를 만든다. what is interpolation?
* 결과? or 효과?, 방법?
  * 숙제

# Kronecker Graph Model
* Object는 자기 자신의 일부와 비슷하므로 네트워크를 재귀적으로 구성할 수 있다. (어떤 과정을 위함일까? 얻는 효과는?)
* Kronecker product를 통해 self-similar 행렬을 만든다. (왜?)
* <i>Kronecker graph</i>는 kronecker product를 초기 행렬 $K_1$에 반복적으로 행해 만들 수 있음
  * Stochastic Kronecker graph
  * Generation of Kronecker graph -> 실제 그래프와 유사해짐, 어떻게 만들까? 방법

