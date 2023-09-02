# SMOTE: Synthetic Minority Over-sampling Technique (2002 Journal of Artificial Intelligence Research, Nitesh V. Chawla 외 3명)
* SMOTE 는 보통 분류문제에서 Imbalanced dataset에서의 데이터 평향에 의해 학습이 불균형 하게 될 수 있는 문제를 해결하기 위해 synthetic 하게 데이터를 만들어 내어 해결하고자 한 방법론이다.
* 데이터 편향 문제에서는 데이터 적인 문제를 (over-sampling 기법과 under-sampling 기법) 으로 해결하거나, 알고리즘적인 기법으로 해결하곤 함.
* 데이터 측면으로 해결하는 방법론에 대해 다루고자 함
  * over-sampling이란 데이터가 부족한 클래스에 대해 데이터를 증량하는 방법으로 해결하고자 함
    * 신뢰성 문제가 큼
  * under-sampling에서는 데이터가
    * 이 때는 데이터가 부분적으로만 보기 때문에 부분 데이터에 대해서 오버피팅이 나거나 등등 문제가 발생할 가능성 있음.

* Smote에서는 클러스터와 랜덤 기법을 활용해서 데이터를 증량함
  * 데이터가 적은 그룹에서 k개의 클러스터를 만들고 클러스터 안에서 노드의 차이를 계산한 후에 그 값에 uniform 랜덤 변수를 곱해서 값을 설정하는 방식으로 data argumentation을 함
  * 

# Borderline-Smote: A New Over-sampling Method in Imbalanced Data Sets Learning()
* SMOTE 기법에 진화해서 Borderline에서 데이터를 구분하기 힘들기 때문에 경계부분을 잘 학습할 수 있는 방법을 제안
* SMOTE 기법과 방법론은 비슷하지만, synthetic 하는 방법이 다름, 그냥 SMOTE는 그룹간 차이에 대해서 Random 하게 generate했지만, 여기는 경계 부근 근처에서 클러스터를 만들 때 다수 클레스의 집단과 소수 클레스 집단의 차이를 계산하고 그 경계를 채워주는 방법론임<br>![image](https://github.com/Jiwon96/papers/assets/65645796/7c71c1c7-dfaa-4755-aac9-e2edbbd0d9e3)
![image](https://github.com/Jiwon96/papers/assets/65645796/60ec4648-7fa2-438e-ac46-b00f24d42336)

* 느낀 점: binary data에서는 꽤 효과가 좋은 듯 하지만, 4개의 클레스에서는 글쎄??? 확실히 편향 데이터도 복잡해지면 성능이 떨어지는 것 같다.<br> ![image](https://github.com/Jiwon96/papers/assets/65645796/663dc350-11f0-4da9-b99c-5d305f277d0f)![image](https://github.com/Jiwon96/papers/assets/65645796/388a5556-83dc-4ac3-a9b0-bfec4208b822)

