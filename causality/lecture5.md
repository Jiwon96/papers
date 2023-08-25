![image](https://github.com/Jiwon96/papers/assets/65645796/8001f56e-f128-42cd-af08-51791008a5e0)# identification
* randomized experiments
    * Randomized control trial: Treatment를 random하게 설정해서 covariate에 대해 독립적으로 만듬
 
* 얻는 효과
  *  Covariate balance: covariate variable X가 treatment에 상관없이 같은 분포를 갖는것을 의미 즉, $P(X|T=1) =^d P(X|T=0) =^d P(X)$ T,X가 독립이 됨
  *  exchangeability: $E[Y(1)|T=0] = E[Y(1)|T=1] = E[Y(1)]$
 
# Frontdoor adjustment
* Step1: Identify the causal effect of T on M: $P(m|do(t)) = P(m|t)$
* Step2: Identify the causal effect of M on Y: $P(y |do(m)) = \sum P(y|m,t)P(t)$
* Step3: 스텝1, 스텝2 를 힙헤사 Y에 대한 T의 영향을 계산함<br>![image](https://github.com/Jiwon96/papers/assets/65645796/d460c6c0-c20d-4874-bc66-523cc5256847)![image](https://github.com/Jiwon96/papers/assets/65645796/da98cf61-bd6d-49c6-808f-af34aaf628a8)


# Do-calculus
*  causal estimand -> stat으로 바꾸는 룰임
*  개념
    *  $G_{\overline{T}}$: T로 incoming 하는 에지를 끊어버림
    *  $G_{\underline{Z}}$: Z에서 outgoing 하는 에지를 끊어버림
    *  $Z(W)$: 집합 Z가 W의 조상이 아닌 그래프 -> Z 자손 중에 W가 없는 그래프
 
*  Rules of do-calculus
    * 아래와 같은 룰을 사용하면 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/5601c2a3-0e41-4f4e-b603-c6d43193a109) 을 참고하자
 
    * Rule 1을 적용하면 아래와 같은 결과를 얻는다. <br>![image](https://github.com/Jiwon96/papers/assets/65645796/2d90cd3e-061b-42ef-b6c3-0c9d14530334)
    * Rule 2를 적용하면 아래와 같은 결과를 얻는다. <br>![image](https://github.com/Jiwon96/papers/assets/65645796/bc90a2cc-4ec6-4af8-8d31-acbd7191793b)
    * Rule 3을 적용->![image](https://github.com/Jiwon96/papers/assets/65645796/db2b46c8-3c12-4f61-99b1-7dbd32d9e5ae)
    * Rule 3에서 Z(W) 인 이유는 W가 Z의 child이면 편향 U에 의해 W가 conditioning되므로 colider가 되서 association이 만들어짐


* Completeness of do-calculus: Rule 1~3이 모든 idenfiable causal estimand를 만들 수 있음.

# Unconfounded children criteron
* Treatment에서 한 개의 conditioning을 가진 Y 변수를 조상 노드의 백도어 path를 막을 수 있음.
* Theorem: Treatment T, Outcome variable Y가 단일 변수일 때 Unconfounded children criteron과 positivity를 만족하면 P(Y=y | do(T=t))이면 identifiable임 but identifiable이라고 unconfounded children criteron은 성립하지 않음.
