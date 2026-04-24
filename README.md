# YOLOv11 行人和车辆检测
深圳大学 人工智能实验 | 基于 YOLOv11 的轻量化目标检测

## 项目介绍
本项目使用 YOLOv11 模型实现行人与车辆的实时检测，
支持 CPU 环境训练与推理，适合入门学习与实验复现。

## 环境配置
conda create -n yolo11 python=3.10
conda activate yolo11
pip install -r requirements.txt

## 数据集
数据集来自 Roboflow 公开人车数据集，
使用前请将数据集放置于项目根目录，并确保 data.yaml 路径正确。

## 运行方式
### 训练模型
python train.py

### 推理测试
python infer.py

## 实验结果
• 训练轮数：20 epochs
• mAP@0.5：0.8406
• 检测类别：person（行人）、car（车辆）

## 项目结构
yolov11-person-car-detection/
├── README.md         # 项目说明文档
├── requirements.txt  # 依赖库清单
├── train-video.py    # 模型训练脚本
├── test-video.py     # 视频推理脚本
├── data.yaml         # 数据集配置文件
└── resulets/         # 推理结果文件夹
    └── predict-6/    # 模型输出结果
