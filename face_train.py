import torch
from ultralytics import YOLO

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

model = YOLO('yolov8l-face.pt').to(device)

results = model.train(data="my_data.yaml", imgsz=640, epochs=100, batch=8)

