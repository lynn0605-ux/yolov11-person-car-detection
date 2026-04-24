from ultralytics import YOLO
import warnings

warnings.filterwarnings("ignore")

# 加载模型
model = YOLO("yolo11s.pt")

# 开始训练
model.train(
    # 数据集路径
    data=r"D:\人工智能\teacher-penson-vehicle-database\data.yaml",

    # 训练基础参数
    epochs=20,
    imgsz=640,
    batch=2,
    device="cpu",
    workers=0,
    cache=False,

    # 优化增强（夜间、小目标、漏车）
    augment=True,
    mosaic=0.8,
    fliplr=0.5,
    scale=0.6,
    hsv_h=0.02,
    hsv_s=0.5,
    hsv_v=0.4,

    # 训练策略
    patience=7,
    cos_lr=True,
    lr0=0.0018,
    lrf=0.015,
    save=True,
    seed=42,

    project=r"D:\人工智能\4月份\实验\检测结果保存处",
    name="person_car_final"
)

print("模型训练完成！")