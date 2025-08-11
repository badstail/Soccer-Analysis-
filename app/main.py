from fastapi import FastAPI, UploadFile, File
from app.tracker import run_pipeline

app = FastAPI(title="Soccer Analysis")

@app.post("/analyze")
async def analyze_video(file: UploadFile = File(...)):
    # save upload
    import tempfile, shutil, os
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name
    result_dir = run_pipeline(tmp_path)
    return {"status": "ok", "outputs": result_dir}
