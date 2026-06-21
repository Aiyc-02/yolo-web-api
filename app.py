import io
import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # 【新增这一行】
from ultralytics import YOLO

app = FastAPI(title="YOLO26 Web API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("正在加载 YOLO 模型...")
model = YOLO("yolo26n.pt")
print("模型加载完成！")


# 这里保留你原来的 /detect 接口
@app.post("/detect")
async def detect_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return {"error": "无效的图像文件"}

    results = model(img, verbose=False)
    annotated_frame = results[0].plot()

    _, encoded_img = cv2.imencode('.jpg', annotated_frame)
    image_bytes = encoded_img.tobytes()

    return Response(content=image_bytes, media_type="image/jpeg")


# 【重点新增这行】：把当前目录（包含 index.html）挂载到根路径
# 注意：这行代码必须放在所有接口的最下面！
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
