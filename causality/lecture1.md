# A Brief Introduction to Causal Inference
* Simposon's paradox<br>![image](https://github.com/Jiwon96/papers/assets/65645796/2282e93e-bb9e-470b-95e3-909eeda06060)
  * 증상(Condition)에 따라서 치료(Treatment)를 다르게 했는데, 증상만을 고려해서 약을 고려하면 A가 사망률이 낮기에 치료하기 적절해 보인다. 하지만, 모든 Condition에서는 B가 치명률이 낮다.
  * 이럴 때는 어떤 약을 처방해야 하는가?
    * 이런 현상을 설명하기 위해서는 다양한 이유가 있겠지만(A약값이 B약값보다 싸거나 등등) 여기에는 모델에 따라 고려되어야 함.
    * ![image](https://github.com/Jiwon96/papers/assets/65645796/8f3822d3-28a3-4e9f-9f73-03541f9830c0)
      * Confounding(교란 변수 여기서는 Condtition임)이 다음과 같이 Treatment와 Result에 영향을 같이 미칠 때는 B를 주는게 효율적임
    * ![image](https://github.com/Jiwon96/papers/assets/65645796/b0977f0d-717a-47cc-b005-47f7fe5a09ec)
      * Treatment가 Confounding에 원인을 주는 경우에는 A를 처방하는게 효율적임
 
* Correlation은 causation이 아니다.
  * ex) 니콜라스 케이지 영화와 수영장 익사 상관관계
  * 만약 위 주장이 사실이라면 니콜라스 케이지는 영화 관계자들이 가장 기피하는 출연자가 되지 않을까...?<br>![image](https://github.com/Jiwon96/papers/assets/65645796/e48c36f0-6b29-4a35-8929-b5268ae53c63)

* 정의
  * $Y_i | _{do (T=0) } \triangleq Y_i {(0)}$
  * Indivisual Treatment effect: $Y_i {(1)} - Y_i {(0)}$

* Average Treatment Effect (이해가 안되는 부분)
  * $E[Y_i {(1)} - Y_i {(0)}] = E[Y {(1)}] - E [Y{(0)}] \neq E[Y | T=1] - E [Y | T = 0]$
  * 제일 우변에서 등호가 성립안하는 이유는 Confounder 때문이라고 함.
  * 이거 pill 예제에서 A, B를 대입해서 이해하면 될 거 같다.
