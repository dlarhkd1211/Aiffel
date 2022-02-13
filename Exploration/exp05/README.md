## 회고록

- 데이터 사이언스 직무를 준비하는 입장에서 가장 열심히 했던 노드가 아니였나 싶다.
- ADP 시험과 Kaggle 코드 리뷰를 하면서 데이터에 대한 통찰이 상당히 중요하다는 것을 많이 생각하게 되었다. 그 부분을 처음 실습할 수 있는 기회여서 최대한 많이 데이터에 대해 고민해볼 수 있었다.
- 일반적인 경진대회에서 성능이 좋다고 알려진 XGBoost 알고리즘을 사용하려 했으나, GridSearchCV를 사용하는 과정에서 시간이 상당히 소요되어 제거하였다. 다행이 LightGBM 모델로 루브릭 지표를 맞출 수 있었다.
- 데이터중 Zipcode, 위경도에 관련된 부분을 처리하는 것이 가장 애매했다. 위 변수들은 일반적인 데이터 처리 방식보다 지리적인 요소를 추가하여 처리하는 것이 훨씬 좋은 성능을 보일 것으로 생각된다.