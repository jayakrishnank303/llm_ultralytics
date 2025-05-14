import torch

def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model

def detect_objects(model, image_path):
    results = model(image_path)
    df = results.pandas().xyxy[0]
    return [{"label": row["name"], "confidence": round(row["confidence"], 2)} for _, row in df.iterrows()]
