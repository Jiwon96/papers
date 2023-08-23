# Potential Outcome
* potential outcome: 우리가 Treatment를 제공했을 때 기대되는 효과
* causal effect: $Y_i{(1)} - Y_i{(0)}$


# Average treatment effect(ATE)
* $E[ Y(1) - Y(0) ] = E[ Y(1) ] - E[ Y(0) ] \neq E[ Y| T=1 ] - E[ Y | T=0 ] $
* 우변이 성립안하는 이유는 confounding 변수가 Treatment에도 영향을 미치고 Y에도 영향을 미치기 때문임

# 가정들
* Ignorability $\sim$ exchangeability: (Y(1), Y(0))와 treatment는 independent하다.
    * causal quantity를 statistical quantity로 바꿀 수 있으면 causal quantity를 identifiable이라 한다.
    * unconfoundedness = conditional ignorability = conditional exchangeability =  (Y(1), Y(0))와 T|X는 independent하다.
    * 하지만, unconfoundedness는 untestable assumption임 왜냐하면 다른 숨어있는 변수 W가 또 confounding으로 숨어있을 수 있기 때문
* positivity:
    * $ 0 < P(T=1 | X=x) < 1$
      * division by zero를 막기 위한 조건임
      * 이는 group X에서 단일한 모든 treatment가 고르게 분포되어 있어야 한다는 것을 의미한다.

  * ignoability와 positivity는 tradeoff가 있음 covariate variable이 많아질 수록 변수끼리 overlab되는 영역이 작아지기 때문에 positivity를 가질 수 있는 영역이 줄어듬 -> 정의역에서 treatment에 대한 extrapolation이 발생
* No interference
    * $Y_i {(t_1,... ,t_{i-1}, t_i, t_{i+1}, ...., t_n)} = Y_i{(t_i)}$
* Consistency: T=t => Y=Y(t), 즉 treatment가 관측되면 potential outcome은 real outcome과 같다.

# 핵심 결론
* E[Y(1) - Y(0)] = $E[ Y(1) ] - E[ Y(0) ]$ (linearity of expectation)<br>
                  = $E_x[E[ Y(1)|X ] - E[ Y(0) |X]]$ (law of iterated expectation)<br>
                  = $E_x[E[ Y(1)|X, T=1 ] - E[ Y(0) |X, T=0]]$ (unconfoundedness and positivity)<br>
                  = $E_x[E[ Y|X, T=1 ] - E[ Y |X, T=0]]$ (consistency)
