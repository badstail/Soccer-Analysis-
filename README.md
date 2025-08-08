# Soccer Video Analytics Automation

**A slick pipeline that lets you upload a match clip to auto-extract player & ball tracks, compute metrics like speed and distance, and produce CSVs, annotated videos, and heatmaps.**

##  Features
- Object tracking via YOLO + ByteTrack for stable player/ball IDs
- CSV outputs: per-frame tracking + summary stats
- Annotated video overlays and heatmap visuals

##  Getting Started

### Prerequisites
```bash
python3.12
pip install -r requirements.txt
