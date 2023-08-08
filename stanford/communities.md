![image](https://github.com/Jiwon96/papers/assets/65645796/df4536fd-4fac-43a6-bc4b-3d3782256231)# 그래프 clustering
* Definition:
  * Short link: 한 그룹내에서 정보를 전달하는 edge
  * long edge: 그룹 간 정보를 전달하는 edge 
* Network:
  * Structural: interpersonal이 아닌, 어떤 조직을 나타냄 예를 들면 2학년 7반
  * interpersonal: edge
* Triadic Closure: 삼각형 형태의 네트워크, 두명의 친구가 한 명의 공동 친구가 있으면 다른 두 친구는 친구가 될 확률이 높다
* Edge overlab: 구 그룹에서 공동 노드를 가지고 있는 성질을 수치화 시켜서 score 함( slide 10)
* strength of real graph(slide 11)
  * low to high(long edge가 먼저 끊어질 수록 그룹들이 더 빨리 쪼개진다. -> 그룹간 정보 전달이 끊긴다)(slide 14)
  * edge overlap 했을 때 low to high: 급격하게 그룹간 정보전달이 끊기는 것을 확인할 수 있음(slide15)
 
# Network Communities
* definition: Modulairty Q: 그래프에서 그룹이 쪼개져 있는 정도를 측정하는 값 -> 0.3~0.7되면 S가 중요한 그룹이라는 것 즉, G에서 S1, S2, 이렇게 있을 텐데 S가 얼마나 중요한지 값을 나타내느것이라 생각하면 됨<br>![image](https://github.com/Jiwon96/papers/assets/65645796/25dcaf0b-6e44-4058-8c47-f77cbc6f9e4c)
* 그래프의 그룹에 대한 Modulairy Q는 다음과 같이 정의되고 이를 optimize 하는게 목표임<br>![image](https://github.com/Jiwon96/papers/assets/65645796/565ef7bf-0380-40a5-8744-99110f1994d1)


# Louvain Algorithm
* Definition:
  * Sum in:: sum of link Weight between nodes in C
  * sum total out: sum of all link weights of nodes in C 여기서 ki는 그룹 밖에 있는 edge도 포함된다.<br>![image](https://github.com/Jiwon96/papers/assets/65645796/6175e242-23d5-404c-9da7-65a74ef0dde5)![image](https://github.com/Jiwon96/papers/assets/65645796/e29ecb68-3db6-4f23-b860-cd9ecd06b925)

* S에 대해서 Group에 대해 Modularity를 optimizer 하고(phase1), 슈퍼노드를 기준으로 다시 그래프를 재정의함(phase2) (p31)
* 두 가지 단계가 있음 노드 i가 D에서 C로 가도 되는지 판단하기 위해서는 Modularity의 변화량을 계산해야됨<br>![image](https://github.com/Jiwon96/papers/assets/65645796/b59c3be7-0689-4d0e-bd53-8845fc4b2f51)
* 따라서 Modulity의 변화량은 다음과 같이 계산한다.(slide 38참고)![image](https://github.com/Jiwon96/papers/assets/65645796/1b646c05-39ef-4613-aa66-1b67902e8c4c)

# BigCLAM 알고리즘
* 앞의 community는 non overlap이지만, 실제로는 고등학교 동창이면서 대학교 동창일 수 있는것처럼 community가 겹침 overlapping community를 detect 할 수 있는 방법 찾기.
* step 1: Node momunity affiliations을 활용한 Generative model을 만듬 (Affiliation Graph Model)
* G가 AGM을 통해 만들어졌을 때 G와 비교하면서 가장 적합한 AGM을 찾음 -> parameter가 node가 얼마나 community에 속하는지 알려줌, AGM에 만들어 지면 다음과 같은 모델이 완성되는데 빨간색 노드들이 같이 엮이는 것을 볼 수 있음-> overlap community 발생 P_c, <br>![image](https://github.com/Jiwon96/papers/assets/65645796/1e0ea640-cfba-41b1-8d70-e073bb1bfb5f)
* Generative model issue: 어떻게 edge를 design?![image](https://github.com/Jiwon96/papers/assets/65645796/8c882b92-a275-4b7e-b8da-df3ff8b7881c)

  * u,v가 연결될 확률 p(u,v)
  * pc: 노드 c가 공동 커뮤니티일 확률
  * 


[참고사항](https://velog.io/@tobigs-gnn1213/4.-Community-Structure-in-Networks)
