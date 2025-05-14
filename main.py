# main.py
from ultralytics import YOLO
from PIL import Image
import sys
import os

def detect_objects(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    model = YOLO("yolov5s.pt")  # or use 'yolov8n.pt' if you're working with YOLOv8
    results = model(image_path)
    
    detections = []
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls_id]
            detections.append((label, conf))
    return detections

def generate_response(detections, prompt):
    objects = ', '.join([f"{label} ({conf:.2f})" for label, conf in detections])
    response = f"The image contains the following objects: {objects}. Based on your prompt: '{prompt}', here's an interpretation or continuation..."
    return response

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <image_path> \"<your_prompt>\"")
        return

    image_path = sys.argv[1]
    prompt = sys.argv[2]

    try:
        detections = detect_objects(image_path)
        response = generate_response(detections, prompt)
        print(response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
