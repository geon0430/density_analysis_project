##연구 진행 상황

# 얼굴 detect model search ( retinaface, deepface)

# 비교 결과 얼굴 탐지에 있어 yolo,retinaface,deepface는 큰 차이는 없다. retinaface,deepface에선 bbx 외에도 랜드마크를 사용해 얼굴 detect 하는 방식 // yolo는 랜드마크가 있긴하지만 없이 해도 큰 성능차이가 없는걸 확인

# 얼굴뿐 아닌 뒷통수 윗통수 옆동수 모자 마스크등 많은 변수 데이터셋을 새로 넣고 구축하기로 함

# model train 시키고 video detect 하는거 까지 확인   -- 여기서 widerface_datasets

# detect는 해도 BBX의 좌표를 받아오는 코드는 아직 YOLOV8에서는 없음

# 알고리즘 코드가 작동되는지 확인하기 위해 YOLOv7에서 epochs 30으로 train 시킨 후 알고리즘 코드가 작동되는지 확인 완료

# yolov8는 yolov7보다 휠씬 가볍고 물론 epochs가 70회 적게 했지만 결과는 yolov8가 확실히 좋음

# yolov8에서  bbx 좌표를 받아오는 코드 작성

# 바운더리박스 표시하는 코드 위치 : ./ yolo/engine/predictor.py

# 바운더리박스 표시하는 코드에 좌표를 넣어주는 코드 작성중 

# 현재 작성 완료된 순수 코드 : widerface_dataset_fomat_changgeon, 유클리드 거리 계산 알고리즘

# 학회 논문 제출 완료 | 학회 디지털콘턴츠 학회도 존재 넣을까 고민중 




#muilt-yolov8-face_detect

# yolov8 - ultralytics-yoloc8 사용

git clone 
