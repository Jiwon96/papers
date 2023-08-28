# Estimation
estimation이란 Statistical Estimand 에서 estimation하는 과정을 말함

# 사전지식
* Conditional average treatment effects(CATEs): $\gamma(x) \triangleq E[Y(1) - Y(0) | X=x] = E_W[E[Y | X=x,T=1, W] - E[Y | X=x,T=0, W]]$ <- 평균에 대한 treament effect임
    * assuming unconfoundedness and positivity
 
* ITEs: $\tau_i = \hat{\tau}{(x_i)} = \hat{\mu}{(1, w_i, x_i)} - \hat{\mu}{(0, w_i, x_i)}$ 
* conditional outcome estimator: is usually called G-computation estimators, parametric G-formula, Standardization, S-learner
# Modeling
* $\gamma = E_W[E[Y |T=1, W] - E[Y | T=0, W]]$ <- $E[Y |T=1, W] = {\mu} (1,W)$,  $E[Y | T=0, W] =  {\mu}(0, W)$로 모델링 가능
  * 따라서 ${\mu} (1,W)$, ${\mu}(0, W)$를 모델링 하고자 함.(추정하는 함수를 만들거임)

# 한계 of COM
* W가 high dimension이면 T가 보통 1-dim이므로 T의 영향력이 계산이 안되는 경우가 있음

# Grouped Conditional Outcome Estimator
* COM의 T를 고려하는 모델을 만들기 위해 생각한 모델, 하지만 각 네트워크가 데이터 전체를 고려하지 못하기 때문에 variance가 커짐
   *  T=1 network와 T=0 network를 나눠서 모델링함 ex)<br>![image](https://github.com/Jiwon96/papers/assets/65645796/d68c6b48-366f-4864-b455-1d3c902245e1)

* TARNet<br>![image](https://github.com/Jiwon96/papers/assets/65645796/9c3382c0-ae48-4368-98e3-c374a7e308d5)
   * T=1으로 갈 때도 여전히 일부 데이터만 사용 문제점
 
* X-learner:
   * path에서 T->Y, X->T까지 효과를 계산한 후 차이를 계산함<br>![image](https://github.com/Jiwon96/papers/assets/65645796/45be921b-f1dc-4b34-bcbf-c355df4c5f0f)

# Propensity scores
* $e(W) \triangleq P(T=1 |W)$
* W가 high-dim 이어도 $e(W)$는 1dim이로 줄일 수 있다.

* Propenseity score Theorem
   * T|W 를 T|(e(W))로 줄일 수 있음, 즉 1dim으로 줄일 수 있음.
   * 위 문제는 unconfoundedness와 positivity를 dim이 커질수록 unconfoundedness를 만족하는 영역이 작아지고 그에 따른 positivity tradeoff 문제를 해결할 수 있는 솔루션이 될 수 있음.
   * Given positivity, unconfoundedness given W implies unconfoundedness given the propensity score $e(W)$ <br>![image](https://github.com/Jiwon96/papers/assets/65645796/e66750c8-257f-4813-8c85-ac114eb3e67e)![image](https://github.com/Jiwon96/papers/assets/65645796/b63abb78-1c1e-4a60-9ca2-c51e16a1c12d)
   
# pseudo-populations
* W-T와의 영향력을 무시하는 가정을 가진 Pseudo-population을 만들고 IPW를 활용해 이를 계산함
* IPW CATE estimation: ![image](https://github.com/Jiwon96/papers/assets/65645796/17f65197-2ffc-436a-bce5-03ee340dfda7)<br>

![image](https://github.com/Jiwon96/papers/assets/65645796/c2679187-378a-4c33-9ddc-d64537fedccc) ![image](https://github.com/Jiwon96/papers/assets/65645796/77ffeaef-25d6-4408-a9b5-4743bb82d83c)

