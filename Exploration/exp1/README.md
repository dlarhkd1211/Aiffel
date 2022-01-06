## 회고록

- 모델 생성 부분에서 MaxPool2D, MaxPooling2D를 혼동해서 사용하는데 이를 MaxPooling2D로 통일해서 진행
- 데이터 셋의 크기를 28 x 28로 진행하였기 때문에 이미지가 가지는 feature들이 많이 손실됨
- 위와 연결하여 나의 데이터셋, 상대의 데이터셋은 촬영 환경, 가위바위보 포즈 등 모든것이 다른 데이터셋이기 때문에 내 데이터로 학습을 진행하고 상대의 데이터로 검증하는 것은 맞지 않는 방법임.
- 위 문제를 해결하기 위해 본인의 데이터셋과 다른 분의 데이터셋을 50대 50의 비율로 섞어서 진행하였고, 모델의 Convolution layer 층을 하나 더 추가하고 Dense층 또한 추가하였다.
- 또한, 학습데이터 과적합을 방지하기 위해 Dropout을 0.3의 비율로 추가해주었고, 이를 통해 test accuracy 60을 달성할 수 있었다.