## 회고록

- tokenize가 되어있는 데이터로 공부를 하고 실습에서는 tokenize부터 진행하려니 이 부분에 대한 설명이 없는게 아쉽다.
- 기존에 감성분석은 주로 머신러닝을 이용해서 많이 진행을 했는데, 이 부분을 딥러닝으로 진행하는 부분이 새로운 경험이였다.
- 루브릭 지표인 정확도 85를 맞추기 위해 기존에 진행한 모델 중 가장 잘 나온 모델에 Word2Vec를 적용했으나, 오히려 정확도는 저하되었다.
- 아예 새로운 모델을 정의하여 정확도를 맞추려 했으나, 83% 이상 올라가지 않았다. 
- 기존 모델보다 오히려 안좋은 성능을 보이는데, 이에 관해서는 데이터 처리 과정의 문제인지 모델 정의에서의 문제인지 다시한번 확인해볼 필요가 있을것 같다.
