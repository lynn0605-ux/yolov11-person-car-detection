cfrom ultralytics import YOLO

# 加载模型
model = YOLO(r"D:\人工智能\4月份\实验\检测结果保存处\person_car_final-6\weights\best.pt")

# 视频推理（自动播放 + 自动保存）
model.predict(
    source=r"D:\人工智能\4月份\实验\视频2.mp4",
    conf=0.28,
    device="cpu",
    show=True,       # 自动播放视频
    save=True,       # 自动保存带检测框的视频
    max_det=300
)