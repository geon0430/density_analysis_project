## density_analysis_project
---
detection : yolov8
BBX 기준 Euclidean Distance으로 밀집도 분석하여 단계별로 표시

## fastapi로 웹 표시
-----
# 실행

### density_analysis model using
```
python density_analysis.py
```

### requirements.txt 설치
### web 실행
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

```

