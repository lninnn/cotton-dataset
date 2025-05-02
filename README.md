# Event Camera Object Detection: Cotton Boll Dataset

**Team Members**  
- Joseph Salas  
- Linh Nguyen  

---

## 📋 Project Overview

Conventional RGB cameras suffer from motion blur, latency, and challenging lighting. Event‑based cameras record per‑pixel changes (“events”), offering low latency, low power, and robustness to motion blur and lighting extremes.

**This experiment** compares YOLOv5 object detection on:
- **RGB frames** (in `obj_Train_data/`)  
- **Event‑camera frames** (in `event_Train_data/`)  

We fine‑tune on a cotton‑boll dataset captured from both modalities and evaluate performance side‑by‑side.

---

## 🗂 Dataset Structure

Dataset Structure:

project/

    obj.names             # class names
    
    obj.data              # metadata for train/val lists
    
    data.yaml             # YOLOv5 config
    
    obj_Train_data/       # RGB images + .txt labels
    
        frame_0001.png
        
        frame_0001.txt
        
        ...
        
    event_Train_data/     # Event‑camera images + .txt labels
    
        frame_0001.png
        
        frame_0001.txt
        
        ...
        
    yolov5/               # Ultralytics YOLOv5 repo
    

Setup & Installation
Create & activate a Python venv (PowerShell):
py -3 -m venv venv
.\venv\Scripts\Activate.ps1

Install dependencies and clone YOLOv5:

pip install torch torchvision pyyaml

git clone https://github.com/ultralytics/yolov5.git

cd yolov5

pip install -r requirements.txt

cd ..

🚅 Training Commands
Run from project root (with venv activated):

# RGB experiment:
python .\yolov5\train.py `

  --img 320 --batch 8 --epochs 10 `
  
  --data data.yaml `
  
  --weights yolov5s.pt `
  
  --name rgb_experiment
  

# Event experiment
//ADD HERE
