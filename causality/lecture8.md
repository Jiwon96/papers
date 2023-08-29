# Instrumental Variables
* Instrumental Variables: 다음과 같은 가정을 만족하는 변수
  * Relevance: Z has a causal effect on T
  * Exclusion Restriction: The causal effect of Z on Y is fully mediated by T
  * Instrumental Unconfoundedness: Z is unconfounded(no unblockable backdoor path to Y)
  * 세가지 조건을 만족하면 다음과 같은 그래프를 그릴 수 있음<br>![image](https://github.com/Jiwon96/papers/assets/65645796/b3f049e7-09e6-4489-b311-51b83c779f4a)
  * Conditional Instruments: assumption 3에 대해 살짝 어기지만, conditional instruments라고 함 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/bb307f4d-9781-4299-be93-1cd1ab78d647)

* No Nonparametric Identification of the ATE:
  * Let's think about parametric identification. What if $Y:= {\delta}T + {\alpha_u}U$. it's linear relation of Y with T, U.
  * ATE = $E[Y | Z=1] - E[Y|Z=0]$ <br>= $E[{\delta}T + {\alpha_u}U | Z=1] - E[{\delta}T + {\alpha_u}U | Z=0]$ 여기서 instumental unconfoundedness assumption이 들어감<br>= $\delta (E[T |Z =1] - E[T |Z =0]) +{\alpha}_u (E[U] - E[U])$
  * $\delta = \frac{E[Y|Z=1] - E[Y|Z=0]}{E[T|Z=1] - E[T|Z=0}$
  * 여기서 ${\alpha}_z {\delta} = E[Y|Z=1] - E[Y|Z=0]$이므로 분자가 $E[Y|Z=1] - E[Y|Z=0] =$ $\alpha_z \delta$ 가 된다. 그리고 Wald estimand (Z->Y 를 Z->T로 causal을 나눠줌) = $\delta = \frac{E[Y|Z=1] - E[Y|Z=0]}{E[T|Z=1] - E[T|Z=0]}$ 이다.
  * ![image](https://github.com/Jiwon96/papers/assets/65645796/c7f3eb43-8544-49f2-81b2-22c0b428e14f) <br><br>

  * <b>Continuous Linear Setting</b>에서 자세한 증명은 slide 17 page 참고
    * $Cov(Y, Z) = \delta Cov(T,Z)$, $\delta = \frac{Cov(Y, Z)}{Cov(T, Z)}$
   
  * Nonparametric identifiaction of local ATE (T, Z가 binary라고 생각하자)
    * linear outcome assumption:를 가정하기 위해선 U가 T와 homogeneous 해야됨, -> nonparametric에선 어떤 가정을 만족해야 할까?
    * Principal Strata: Instrument에서 나올 수 있는 구조는 4가지가 있음<br> Always-takers, never-takers는 Z에 상관없이 1, 0값을 가지므로 Z와 T는 독립임 ![image](https://github.com/Jiwon96/papers/assets/65645796/155e8abd-fd00-4bb2-a9d7-2d09ab26ddd8)
    * Monotonicity Assumption(No Defiers) ![image](https://github.com/Jiwon96/papers/assets/65645796/1a125455-4c79-4f7f-8b06-926d819b936a)<br><br>
    * Deriving Local ATE Identifiaction: 세번째줄은 Y(Z=1) = Y(Z=0) since T(Z=1) = T(Z=0) = 1이므로 Y(1) - Y(1)이 됨
    * ![image](https://github.com/Jiwon96/papers/assets/65645796/58080c96-421f-4422-b536-08218a6e2f39)<br><br>
   
    * 결과 <br>![image](https://github.com/Jiwon96/papers/assets/65645796/e01f9652-1576-41f6-adb4-b3e8e8b6d9c5)

  * 하지만 항상 monotonicity가 만족하지 않음... 다른 방법들..
    * Set Identifiaction of ATE -> ATE를 bound로 나타냄 peral's causality book에 있음
    * Y := f(T,U)를 만들어서 범위를 만들어냄
    


