from ultralytics import YOLO
import cv2, os, pandas as pd
from pathlib import Path

# If you prefer, plug in a ByteTrack/Norfair/Supervision tracker here.
def run_pipeline(video_path: str, out_dir: str = "data/outputs"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    model = YOLO("yolov8n.pt")  # start small; later swap for soccer-tuned weights

    cap = cv2.VideoCapture(video_path)
    frame_idx, rows = 0, []
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        results = model(frame, verbose=False)[0]
        for b in results.boxes:
            cls = int(b.cls.item())
            conf = float(b.conf.item())
            x1, y1, x2, y2 = b.xyxy[0].tolist()
            rows.append([frame_idx, cls, conf, x1, y1, x2, y2])
        frame_idx += 1

    df = pd.DataFrame(rows, columns=["frame","class","conf","x1","y1","x2","y2"])
    csv_path = os.path.join(out_dir, "detections.csv")
    df.to_csv(csv_path, index=False)
    cap.release()
    return out_dir
