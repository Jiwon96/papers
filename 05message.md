# 출처
* Stanford CS224W: Machine Learning with Graphs | 2021

# 오늘의 주제: 노드 classification
* relation classification
* Iterative classification
* Correct & Smooth

# 개념 정의
* correlation: 주변 노드가 같은 클래스인 것
  * Homophily: 개인은 비슷한 개체와 무리를 이루는 것
    * ex) 무리의 새들
  * Influence: 사회가 개인의 특징에 영향을 미치는 것
    * 내가 좋아하는 음악장르를 남에게 추천하는 일 -> 친구들이 그 음악을 좋아하게 됨
* Guilt_by_association: 내가 레이블 X와 연결되어 있으면 나도 label X일 확률이 높음
* 

# relation classfication
* idea: V의 레이블은 주변 이웃의 확률 가중 평균으로 구해보자.
![image](https://github.com/Jiwon96/papers/assets/65645796/3ccfba88-8c83-4f09-af83-78d479acc2e6)
![image](https://github.com/Jiwon96/papers/assets/65645796/05a005df-f243-4c3f-b996-6f128e4261f0)![image](https://github.com/Jiwon96/papers/assets/65645796/a26c3291-9148-4e37-bd9a-22eacb348a92)
![image](https://github.com/Jiwon96/papers/assets/65645796/f13d41b8-1981-4c6e-a58b-ac55634852a2)

<b>3->4->5->8->9으로 한 epoch이 끝나고 수렴할 때 까지 쭉 쭉 이어가면</b>
![image](https://github.com/Jiwon96/papers/assets/65645796/13c4f4f1-11ca-46ee-bb64-eba8f3dc5981)
<b>모든 과정이 끝났다 하지만, 매 번 수렴하는 게 아니므로 주의가 필요하다</b>

# iterative Classfication
* Relation classfication은 노드의 attribute를 사용하지 않는 문제점이 있다.
* 대안으로 two classifier를 사용
* $\Phi(f_v):$ 노드 벡터 $f_v$이 주어졌을 때 노드 레이블을 예측하는 함수
* $\Phi(f_v, z_v):$ 노드 벡터 $f_v$, neighbor의 축약 정보 $z_v$ 이 주어졌을 때 노드 레이블을 예측하는 함수
* 여기서 z_v는 trainable 한 변수로 훈련을 통해 학습됨
* 레이블 크기에 따라 컬럼 수가 결정됨
* 여기서 I는 들어오는 edge에 대한 요약 정보
* O는 레이블이 나가는 edge에 대한 요약 정보<br><br>
<b> 예제!!!!!!!!! </b><br>
![image](https://github.com/Jiwon96/papers/assets/65645796/adaf8147-3a24-40f6-8147-383cb9763ba6)![image](https://github.com/Jiwon96/papers/assets/65645796/bea90e19-969b-42cd-984e-f1ca578a0690)
![image](https://github.com/Jiwon96/papers/assets/65645796/eb7b8232-9619-4fa4-8feb-ffed25289cc8)![image](https://github.com/Jiwon96/papers/assets/65645796/678fdb50-a321-468c-9775-0f603fceef29)
![image](https://github.com/Jiwon96/papers/assets/65645796/eb7f9c89-8073-4597-99f4-d20ee4904928)![image](https://github.com/Jiwon96/papers/assets/65645796/cdcda2f2-ba18-48c8-9c10-10c96b25b8bf)
![image](https://github.com/Jiwon96/papers/assets/65645796/160591c8-3fc0-41cc-8b2e-274a2eae62d8)![image](https://github.com/Jiwon96/papers/assets/65645796/e3f7b489-e4ee-48ef-a589-45b3359abf70)
![image](https://github.com/Jiwon96/papers/assets/65645796/42bb4abd-42f7-4c47-b036-dccf64b42762)

# Loopy BP Algorithm
![image](https://github.com/Jiwon96/papers/assets/65645796/ff2f10eb-ecd5-4e4b-bdaa-4d9f531a3422)







