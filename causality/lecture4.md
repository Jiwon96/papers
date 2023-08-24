# causal Models
* The Identification-Estimation Flowchart<br>![image](https://github.com/Jiwon96/papers/assets/65645796/dce9c807-294c-4104-a08c-c71018307834)

* Do operator
    * Conditioning, intervening: Conditioning은 그냥 모집단에서 조건에 맞는 sample을 뜯어내는것, but intervening은 전체 모집단에 인위적으로 조건을 넣어주는 것 ex) 아래에서는 sodium 변수에 intervening을 가함 (참고1)
    * Interventional distributions: $P{(Y(t) = y )} \triangleq P(Y=y | do(T=t)) \triangleq P(y|do(t))$
    * Average treatment effect(ATE): $E[Y | do(T=1)] - E[Y| do(T=0)]$
    * Observational: P(Y, T, X), P(Y | T=t) Interventional: P(Y | do(T=t)), P(Y | do(T=t), X=x)
    * identifiability: causal Estimand를 Statistical Estimand로 바꿀 수 있으면 identifiability라고 한다.

* Modulaity assumption $\sim$ independent mechanisims, $\sim$ autonomy $\sim$ invariance. etc
    * modularity: $X_i$에 intervene을 가할 때 $P(X_i | pa_j)$만 영향을 받는다. 즉, 부분적 independent이다.
        * 조금 더 엄밀하게 말하면, intervene을 가했을 때와 동일한 값을 가지면 $P(x_i | pa_a) =1$ otherwise =0임 ex) 참고1에서 sodium이 1이었으면 1임
    * modularity가 violated 됐다는 것은 intervene을 가헀을 때 다른 노드가 영향을 받았다는 소리임
 
* Association $\neq$ causation
    * $P(y|do(t)) = \sum_x P(y|t,x)P(x)$ , $P(y|t) = \sum_x P(y,x| t) = \sum_x P(y|t,x)P(x|t)$ 따라서 $P(x) \neq P(x|t)$

* Backdoor criterion and backdoor adjustment(backdoor 막는거 causal-> stat 만드는거)
    * A set of variables W satisfies the backdoor criterion relative to T and Y if the following are true:
        * W blocks all backdoor paths from T to Y
        * W does not contain any descendants of T
     
    * 즉 W set이 immorrality이거나, Chain, fork가 아니어야 됨 <- 즉 lecture3에 나왔던 d-separation 기능을 할 수 있으면 됨
 
* Structural equations
    * causal infromation은 asymmetric이기 때문에 'B가 A의 결과이다'를 정의하려면 $ B:= f(A)$ or $B:= f(A, U)$라고 한다. 여기서 U는 데이터에 대한 편이이다. 
* Structural causal models <br>![image](https://github.com/Jiwon96/papers/assets/65645796/559b8623-9e6b-4d08-81a3-4d2a03d473e8)
* Modularity assumption for SCM
    * Treatment가 가해진 부분만 변하고 나머지는 똑같다는 말 scm에서도
![image](https://github.com/Jiwon96/papers/assets/65645796/5d398513-fc55-4dc8-ae34-9585155fa86d)

* 재밌는 association들,
    * collider bias: 편이 $U_M$에 의해서 M은 immorality가 되고 이는 M이 blocked 된 효과를 줘서 association이 생김 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/910b12c3-f62f-4d29-b032-50265a9fb466)
    * M 편이: <br>![image](https://github.com/Jiwon96/papers/assets/65645796/676e042f-6987-4b01-9fa3-334d022b38ca)

    
<b>참고1</b>
```python
Xt1=pd.DataFrame.copy(xt)
Xt1['sodium']=1
Xt2=pd.DataFrame.copy(xt)
Xt0['sodium']=0
```
