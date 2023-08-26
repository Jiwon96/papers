# Estimation
estimation이란 Statistical Estimand 에서 estimation하는 과정을 말함

# 사전지식
* Conditional average treatment effects(CATEs): $\gamma(x) \triangleq E[Y(1) - Y(0) | X=x] = E_W[E[Y | X=x,T=1, W] - E[Y | X=x,T=0, W]]$ <- 평균에 대한 treament effect임
    * assuming unconfoundedness and positivity 

# Modeling
* $\gamma = E_W[E[Y |T=1, W] - E[Y | T=0, W]]$ <- $E[Y |T=1, W] = {\mu} (1,W)$,  $E[Y | T=0, W] =  {\mu}(0, W)$로 모델링 가능
  * 따라서 ${\mu} (1,W)$, ${\mu}(0, W)$를 모델링 하고자 함.(추정하는 함수를 만들거임)
