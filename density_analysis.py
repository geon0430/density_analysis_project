from ultralytics import YOLO
import numpy as np
import cv2
import os

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "1"


class YOLOConverter:
    def __init__(self, yolo_path, yolo_conf=0.30, yolo_iou=0.7):
        self.yolo_path = yolo_path
        self.yolo_conf = yolo_conf
        self.yolo_iou = yolo_iou
        self.yolo_load()

    def yolo_load(self):
        self.yolo_model = YOLO(self.yolo_path)

    def calculate_density(self, boxes):
        centroids = [(int((box[0] + box[2]) / 2), int((box[1] + box[3]) / 2)) for box in boxes]
        total_distances = 0
        count = 0
        for i, cent in enumerate(centroids):
            for next_cent in centroids[i+1:]:
                distance = np.sqrt((cent[0] - next_cent[0]) ** 2 + (cent[1] - next_cent[1]) ** 2)
                total_distances += distance
                count += 1

        if count == 0:
            return 0

        average_distance = total_distances / count
        max_possible_distance = np.sqrt(1920**2 + 1080**2)
        density_ratio = average_distance / max_possible_distance
        if density_ratio < 0.1:
            return 4
        elif density_ratio < 0.3:
            return 3
        elif density_ratio < 0.6:
            return 2
        else:
            return 1
        
    def yolo_eval(self, input_frame):
        output = self.yolo_model.predict(
            input_frame,
            conf=self.yolo_conf,
            iou=self.yolo_iou,
            show_conf=False,
        )
        boxes = output[0].boxes.xyxy
        density_level = self.calculate_density(boxes)

        output_frame = output[0].plot(conf=False,names=False)
    
        # 밀집도를 나타내는 텍스트 설정
        text = f"Density Level: {density_level}"
    
        # 텍스트 위치와 스타일 설정
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1.5
        font_thickness = 3
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        text_x = output_frame.shape[1] - text_size[0] - 20  # 오른쪽 위 모서리에서 20픽셀 내려옴
        text_y = 40  # 상단에서 40픽셀 내려옴

        # 텍스트 그리기
        cv2.putText(output_frame, text, (text_x, text_y), font, font_scale, (0, 0, 255), font_thickness, cv2.LINE_AA)

        return output_frame


    def process_video(self, video_input, video_output):
        cap = cv2.VideoCapture(video_input)
        org_fps = cap.get(cv2.CAP_PROP_FPS)
        org_w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        org_h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_out = cv2.VideoWriter(video_output, fourcc, org_fps, (org_w, org_h))

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                output_frame = self.yolo_eval(frame)
                video_out.write(output_frame)
        finally:
            cap.release()
            video_out.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    yolo_path = "./yolov8n-face.pt"  
    video_input_path = "./1.mp4"
    video_output_path = "./result_1.mp4" 

    converter = YOLOConverter(yolo_path)
    converter.process_video(video_input_path, video_output_path)

