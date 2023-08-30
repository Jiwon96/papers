# Difference-in-Differences
* Motivation
  * how about time dimension to help with identification? treatment 효과를 보기 위해서 시간축을 도입해보자<br>![image](https://github.com/Jiwon96/papers/assets/65645796/b9759d8e-72be-4d08-bbf5-4a7e82761cd3)
* Average Treatment Effect on the Treated(ATT)
  * ATE = $E[Y(1) - Y(0)] = E[Y|T=1] - E[Y|T=0]$ , unconfoundedness: $(Y(0), Y(1)) \perp\kern-5pt\perp Y$
  * ATT = $E[Y(1) - Y(0)| T=1] = E[Y|T=1] - E[Y|T=0]$ weaker unconfoundedness $Y(0) \perp\kern-5pt\perp Y$
 
* Introducing Time이 됐을 때 청사진<br>![image](https://github.com/Jiwon96/papers/assets/65645796/8fad8c19-5430-4847-900f-c144d707d999)
  * <b>우리가 구하고자 함은 T=1일 떄 효과가 있는 그룹과 없는 그룹의 차이를 알고 싶은 것 </b>

* Assumption
  * consistency:
    * 임의 시간 $\tau$ 에서 $T=t => Y_{\tau} = Y_{tau}(t)$ 즉, 임의의 $\tau, Y_{\tau} = Y_{\tau}(T)$
   
  * Parallel Trends
    * $E[Y_i(0) - Y_0(0)|T=1] = E[Y_1(0) - Y_0(0) T=0]$ 즉, $Y_i(0) - Y_0(0)$는 T와 독립이다.
   
  * No Pretreatment Effect
    * $E[Y_0(1) - Y_0(0)|T=1] = 0$, 즉 초기에는 잠재결과 treatment(1) =  잠재결과 treatment(0) 이다. 즉 둘의 차이가 없다.
   
* Main Result and Proof
  * $E[Y_1(1) - Y_1(0) | T=1] = (E[Y_1 | T=1] - E[Y_0| T=1]) - (E[Y_1 | T=0] - E[Y_0 | T=0])$, 증명은 교재 97부터 참고, 핵심으론 parallel trends 가정, No pretreatment effect가 쓰였음

* Major Problem
  * Difference-in-Differences method에서 parallel trends assumption이 만족되지 않을 때가 많음. 따라서 대안으로
  * Controlled Parallel Trends
    * $E[Y_i(0) - Y_0(0)|T=1, W] = E[Y_1(0) - Y_0(0) T=0, W]$ 가정을 사용하기도 하는데, interaction term이 T와 time $\tau$에 있으면 이또한 만족하지 않음.
   
  * 추가적으로 parallel trends는 scale specific한 성질이 있음. 즉, $E[Y_i(0) - Y_0(0)|T=1] = E[Y_1(0) - Y_0(0) T=0]$ 을 만족할 때 $E[log Y_i(0) - log  Y_0(0)|T=1] = E[log Y_1(0) - log Y_0(0) T=0]$가 성립되지 않음.
