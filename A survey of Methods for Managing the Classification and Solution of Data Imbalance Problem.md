# A survey of Methods for Managing the Classification and Solution of Data Imbalance Problem
데이터 imbalance에 대한 방법론들을 조사한 논문<br>
데이터 관점과 알고리즘 관점이 있음<br>

* 데이터 관점:
  * Over sampling 방법론:
    * SMOTE 방법: Minority 클래스를 over-sampling 하는 방법임
    * Cluster-based Over-sampling: cluster을 활용한 후 그룹에서 오버샘플링
    * ADASYN:
  * 오버 샘플링 장점:
    * 기존 데이터에 대해 정보의 손실량이 없다.

  * Under sampling 방법론:
    * RUS(radnom under sampling): 랜덤으로 다수 클레서에서 제거하는 방법
    * Tomek Link(T-Link): Neiborhood를 이용해서 거리가 먼 그룹은 삭제하는 방법
  * 언더 샘플링 장덤:
    * 시간 reduction이 좋음
   
* 알고리즘 기법:
  * SVM, KNN, Naive Bayes, Decision Tree, 등등 우리가 알고리즘으로 데이터를 classification 하는 방법등은 모두 알고리즘적인 데이터 imbalance solution임
 
* Conclusion
  * 퍼포먼스에 영향을 미치는 feature engineeing이 굉장히 중요함
  * Feature selection이 중요한 역할할 것
  * 퍼포먼스 중심으로는 hybird or ensemble classifier가 훨씬 효과적임
