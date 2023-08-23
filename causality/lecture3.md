# The Flow of Association and Causation in Graphs
* Local Markov assumption: Given its parents in the DAG, a node X is independent of all of its non-descendants. ex)![image](https://github.com/Jiwon96/papers/assets/65645796/0025edae-b539-4696-96fd-875eaecafa3d)
* Minimality assumption:
  * local Markov assumption
  * Adjacent nodes in the DAG are dependent. <br>![image](https://github.com/Jiwon96/papers/assets/65645796/936af42b-8478-4cab-8f72-0dcfb7bfefd7)![image](https://github.com/Jiwon96/papers/assets/65645796/7a80d342-78e6-433d-80f5-b721daaf5448)

* Assumptions flowchart<br>![image](https://github.com/Jiwon96/papers/assets/65645796/d868c334-0761-4f90-b5db-49705cfe5125)

* Graphical building blocks<br>![image](https://github.com/Jiwon96/papers/assets/65645796/1397e4c4-e934-4924-89a4-86ac6f066d7d)
    * chains and forks: chain 구조나 fork 구조는 X1과 X3의 관게는 X2에 의해 association 관계임 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/422998bb-ee7a-4bbe-a729-948251bb78a9)
        * X2가 conditioning 되면 이 X1->X3는 조건부 독립이 성립할 수 있음(증명은 슬라이드 참고 매우 쉬움, markov network 이용하면 됨)
    * immoralities구조<br>![image](https://github.com/Jiwon96/papers/assets/65645796/bfb53016-df46-4129-8c34-feea7f33a6a9)
        * 이런 모양에서 X2를 colider라고 하는데 이 때는 X2가 conditioning이 안되어 있을 때(blocked path일 때) X1, X3가 independent함
        * 위 구조에서 X1을 (1:good-looking, 0: otherwise), X3를 성격이라 할 때 (1 kind, 0: jerk) X2 = X1 & X3라고 하자, 이 때 X2가 0일 때를 보면 음의 두 변수가 음의 상관관계를 갖는것을 알 수 있음 <- association임을 알 수 있음<br>![image](https://github.com/Jiwon96/papers/assets/65645796/bbdc3dd3-500e-41d3-b396-0362ad581d2d)
        * Conditioning on descendants of collider구조여도 다음과 같음<br>![image](https://github.com/Jiwon96/papers/assets/65645796/619aac27-439c-46a9-9b45-108c59a4e4b1)

* blocked path definition: A path between nodes X and Y is blocked by a conditioning set Z if either of the follwing is true: <- X, Y가 독립이라는 뜻임
  * Chain 구조나 fork 구조에서 어떤 노드 W가 주어졌는데 이 때 W는 chain 구조에서는 중간에, fork 구조에는 다자녀의 첫 부모여야됨
  * immorality 구조에서는 colider W가  컨디션닝이 없어야됨, 혹은 colider의 자손이 컨디셔닝이 없어야됨<br>![image](https://github.com/Jiwon96/papers/assets/65645796/7496b102-c508-4813-b0f8-3d4e797d305e)

* d-separtaion: path (X,Y)가 Z에 의해 block되면 X, Y가 Z에 의해 d-separated 된다고 함, <br>![image](https://github.com/Jiwon96/papers/assets/65645796/1b722d06-df0d-466d-85d9-fc85899f754a)

* 전체 그림<br>![image](https://github.com/Jiwon96/papers/assets/65645796/c548d96b-36b2-4c48-b3eb-c8b28c675ab1)

    * T에 대해서 Y의 effect를 알고 싶을 때 T->Y를 causal assocation,이라 한다.
