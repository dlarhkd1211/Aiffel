## 회고록

sticker로 사용했던 사진들이 png 형식이라 기존 사진으로는 배경이 존재하지 않는 사진이나, 이를 opencv로 불러오면서 배경이 생기게 된다. 이를 처리하는 방식이 새로운 접근이였다.

addWeighted로 투명도를 추가하는 작업은 sticker의 배경이 존재하는 상황에서 그냥 두개의 사진을 합쳐버리면 배경까지 같이 합성이 된다. 이를 처리하기 위해 투명도를 우선 준 뒤 배경을 제거하며 합치는 방식으로 진행했다.

다양한 각도에서 촬영한 사진으로 프로젝트를 진행하면서, dlib.get_frontal_face_detector() 라이브러리의 한계점을 파악할 수 있었다. 정면 사진의 경우 쉽게 이용이 가능하나, 추가적인 얼굴 형태에 대한 작업은 새로운 모델이 필요할 것이다.
