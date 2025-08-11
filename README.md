# Soccer Video Analytics Automation

**A slick pipeline that lets you upload a match clip to auto-extract player & ball tracks, compute metrics like speed and distance, and produce CSVs, annotated videos, and heatmaps.**

##  Features
- Object tracking via YOLO + ByteTrack for stable player/ball IDs
- CSV outputs: per-frame tracking + summary stats
- Annotated video overlays and heatmap visuals

##  Getting Started

### Prerequisites
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# POST a video to http://127.0.0.1:8000/analyze

