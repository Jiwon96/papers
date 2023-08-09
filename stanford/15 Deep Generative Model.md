# Graph Generation
* given : Graphs sampled from $p_{data}(G)$ 
* Goal:
  * Lean the dist $p_{model}(G)$
  * sample from $P_{model}(G)$
* 실제 그래프 분포 샘플들을 이용해 $P_{model}(G)$ 을 학습하고, 학습된 $P_{model}(G)$에서 샘플링하여 그래프 생성

* <b>의문:</b> $p_{data}(G)$ 와 $p_{model}(G)$의 차이점은 무엇이지?
  * $p_{data}(G)$  is the data distribution, which is never known to us, but we have sampled $x_i$ ~ $P_{data}(x)$
  * $P_{model}(x; \theta )$ is the model, parametrized by $\theta $, that we use to approximate $p_{data}(G)$
  * <b>의문:</b> $P_{model}(x; \theta )$ 와 $p_{data}(G)$ 의 차이는? given에서 goal 되는 과정이 어떻게 되는지? $P_{model}(x; \theta )$  -> appoxim $p_{data}(G)$ -> Goal 2가지
 
* <b> Density Esimation</b>
  * make $P_{model}(x; \theta )$ <b> close to</b> $p_{data}(G)$
    * $\theta^*$ = $argmax_{\theta}E_{x\sim p_{data}}logp_{model}(x|\theta)$
   
  * Maximum Likelihood Estimation을 이용한다. 즉, 표본들을 이용해 $p_{model}의 likelihood를 최대로 하는 최적의 likelihood를 최대로 하는 최적의 parameter θ를 찾는다.
 
* <b> Sampling</b>
  * Smaple from $P_{model}(x; \theta )$
    * Sample from a simple noise distribution (e.g. standard normal distribution), $z_i \sim N(0,1)$
    * Transform the noise $z_i$ via $f({\centerdot})$, $x_i = f(z_i;\theta )$
      * $f({\centerdot})$ 를 deep neural network로 구성하고, 갖고 있는 데이터들을 이용해 학습시킨다.
     
* <b> 의문</b>: 그러면 $z_i$를 들을 linear나 그런 레이어로 transform 해서 $x_i$를 구하는 건가? <b>예시가 집중해서 보자</b>
* <b> Auto-regressive models</b>
  * $P_{model} (x; \theta)$ 는 density estimation과 sampling에 사용되고, 이를 위해 auto-regressive model을 사용한다.
    * $P_{model}(x; \theta )$ = $\Pi^n_{t=1}P_{model}(x_t|x_1, \cdots , x_{t_1};\theta )$
   
  * Idea: Joint distribution이 conditional distribution들의 곱으로 표현될 수 있는 Chain rule을 이용한다.
  * 이를 위해 $X = (x_1, x_2, \cdots, x_t)$를 sequence로 보고, $x_t$는 t번째 행동이 된다. 여기서 행동은 node 또는 edge를 추가하는 것이다.
 
  * <b>질문</b> sequence로 본다는 것은 뭘까? <b>예시</b>를 볼 수 있을까? 전 액션이 현재 결정할 액션에 영향을 미친다는 것 같은데 주의 깊게 볼 필요가 있다.






[참고 자료](https://velog.io/@skhim520/15.-Deep-Generative-Models-for-Graphs)
