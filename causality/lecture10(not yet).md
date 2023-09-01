# Causal Discovery from Observational Data
* 여태까지 우리가 관심있던 것은 causal graph -> estimation을 하는 과정이었음, 하지만 causal graph가 없다면? , data만 있을 때 causal graph를 만들어야 한다면 어떻게 해야할까? 의 아이디어에서 시작

* Assumption
  * Faithfulness Assumuption: $X indep_G Y |Z <= X indep_P Y |Z$ 즉, X,Y가 conditional independent이면 z가 conditioning 됐을 때 X, Y 독립이다.
    * but faithfulness Assumption은 반례를 굉장히 쉽게 만들 수 있다. 
  * Causal Sufficiency: Unobserved한 confounders는 그래프에 없다.
  * Acyclicity: cycle이 없는 그래프
  * Markov assumption

* Q. 왜 마르코프 가정만으로는 causal graph를 learning하는게 어려울까?
  * ans?
 
* Markov Equivalence and Main Theorem
  * Markov Equivalence class1: $X_1 indep X_3 | X_2 and X_1 not indep X_3$ 성질을 만족하는 그룹들<br>![image](https://github.com/Jiwon96/papers/assets/65645796/7e560c0e-e978-4958-a367-2a6ae776d1f9)
  * Markov Equivalence class2(immoralities): $X_1 indep X_3 and X_1 not indep X_3 | X_2$ <br>![image](https://github.com/Jiwon96/papers/assets/65645796/b814bdb1-9e99-49b8-886c-e96f5939b02e)
  * Skeletons: 두 Markov Equivalence class에서 $X1 indep X_3 | X_2$ 인지 아닌지를 이용해서 구조를 정의한 것 immorality는 X1과 X3가 연결된 형태 등등으로 되어 있다. <br>![image](https://github.com/Jiwon96/papers/assets/65645796/f6ead6b1-20d3-463a-a355-658969bac8c2)
  * <b>Theorem</b>: 두 그래프가 Markov equivanlent iff they have the same skeleton and same immoralities
  * slide 18page 의 연습문제 풀어보자
 
* The PC Algorithm(아직 이해를 못함 복습 해자)
  * PC 알고리즘이란 independent causal discover algorithm임 즉, causal structure를 찾는 과정이다.
  1. Identify the skeleton
  2. identify immoralities and orient them
    * 두 가지 가정이 만족되면 X-Z-Y가 immortality임
      *  there is no edge between X and Y in our previous step.
      *  Z was not in the conditioning set that makes X and Y conditionally independent.
  3. Orient qualifying edges that are incident on colliders
  * (예시는 이해가 안되서 다시 공부한 후에 올리자)
 
* Hardness of Conditional Independence Testing
  * 조건부에서 독립성을 밝히는게 굉장히 어려움 데이터가 굉장히 많아야 됨
 
# Semi-Parametric Causal Discovery
* 이 부분은 다시 한 번 보자.
