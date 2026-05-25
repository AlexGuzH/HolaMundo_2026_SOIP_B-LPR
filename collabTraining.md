PASO 1
import torch
if torch.cuda.is_available():
    print(f"✅ ¡GPU detectada! Usando: {torch.cuda.get_device_name(0)}")
else:
    print("❌ Seguimos en CPU. Revisa el paso 1 de nuevo.")
PASO 2
import zipfile
import os

def descomprimir(archivo, destino):
    with zipfile.ZipFile(archivo, 'r') as zip_ref:
        zip_ref.extractall(destino)

# Creamos la carpeta del dataset
os.makedirs('dataset', exist_ok=True)

# Descomprimimos cada parte
descomprimir('/content/License Plate Recognition.v1-raw-images.yolov8.zip', 'dataset/train')
PASO 3
import os
# Verificamos si la carpeta de entrenamiento tiene imágenes
ruta_imgs = "/content/dataset/train/train/images"
if os.path.exists(ruta_imgs):
    print(f"✅ ¡Éxito! Encontradas {len(os.listdir(ruta_imgs))} imágenes para entrenar.")
else:
    print("❌ Error: La ruta no es correcta. Verifica el nombre de las carpetas.")
PASO 4
!pip install ultralytics
PASO 5
from ultralytics import YOLO

# 1. Cargamos un modelo base (el "estudiante" que va a aprender)
# Usamos el 'n' (nano) porque es el más rápido para pruebas
model = YOLO('yolov8n.pt')

# 2. Comenzamos el entrenamiento
# data: la ruta al archivo yaml que se ve en tu foto
# epochs: cuántas veces el modelo repasará las fotos (50-100 es bueno para empezar)
# imgsz: resolución de las fotos (640 es el estándar de alta fidelidad)
results = model.train(
    data='/content/dataset/train/data.yaml',
    epochs=50,
    imgsz=640,
    device=0  # Esto le dice que use la GPU de Colab
)
SALIDA DE PROCESAMIENTO
Creating new Ultralytics Settings v0.0.6 file ✅ 
View Ultralytics Settings with 'yolo settings' or at '/root/.config/Ultralytics/settings.json'
Update Settings with 'yolo settings key=value', i.e. 'yolo settings runs_dir=path/to/dir'. For help see https://docs.ultralytics.com/quickstart/#ultralytics-settings.
Downloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolov8n.pt to 'yolov8n.pt': 100% ━━━━━━━━━━━━ 6.2MB 103.0MB/s 0.1s
Ultralytics 8.4.41 🚀 Python-3.12.13 torch-2.10.0+cu128 CUDA:0 (Tesla T4, 14913MiB)
engine/trainer: agnostic_nms=False, amp=True, angle=1.0, augment=False, auto_augment=randaugment, batch=16, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, cls_pw=0.0, compile=False, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=/content/dataset/train/data.yaml, degrees=0.0, deterministic=True, device=0, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, end2end=None, epochs=50, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.01, lrf=0.01, mask_ratio=4, max_det=300, mixup=0.0, mode=train, model=yolov8n.pt, momentum=0.937, mosaic=1.0, multi_scale=0.0, name=train, nbs=64, nms=False, opset=None, optimize=False, optimizer=auto, overlap_mask=True, patience=100, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=None, rect=False, resume=False, retina_masks=False, rle=1.0, save=True, save_conf=False, save_crop=False, save_dir=/content/runs/detect/train, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3.0, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
Downloading https://ultralytics.com/assets/Arial.ttf to '/root/.config/Ultralytics/Arial.ttf': 100% ━━━━━━━━━━━━ 755.1KB 25.9MB/s 0.0s
Overriding model.yaml nc=80 with nc=1

                   from  n    params  module                                       arguments                     
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                
  2                  -1  1      7360  ultralytics.nn.modules.block.C2f             [32, 32, 1, True]             
  3                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                
  4                  -1  2     49664  ultralytics.nn.modules.block.C2f             [64, 64, 2, True]             
  5                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]               
  6                  -1  2    197632  ultralytics.nn.modules.block.C2f             [128, 128, 2, True]           
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  8                  -1  1    460288  ultralytics.nn.modules.block.C2f             [256, 256, 1, True]           
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 
 10                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 11             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 12                  -1  1    148224  ultralytics.nn.modules.block.C2f             [384, 128, 1]                 
 13                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 14             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 15                  -1  1     37248  ultralytics.nn.modules.block.C2f             [192, 64, 1]                  
 16                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 17            [-1, 12]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 18                  -1  1    123648  ultralytics.nn.modules.block.C2f             [192, 128, 1]                 
 19                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 20             [-1, 9]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 21                  -1  1    493056  ultralytics.nn.modules.block.C2f             [384, 256, 1]                 
 22        [15, 18, 21]  1    751507  ultralytics.nn.modules.head.Detect           [1, 16, None, [64, 128, 256]] 
Model summary: 130 layers, 3,011,043 parameters, 3,011,027 gradients, 8.2 GFLOPs

Transferred 319/355 items from pretrained weights
Freezing layer 'model.22.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks...
Downloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt to 'yolo26n.pt': 100% ━━━━━━━━━━━━ 5.3MB 104.0MB/s 0.1s
AMP: checks passed ✅
train: Fast image access ✅ (ping: 0.0±0.0 ms, read: 973.4±526.6 MB/s, size: 288.1 KB)
train: Scanning /content/dataset/train/train/labels... 7058 images, 5 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 7058/7058 2.4Kit/s 3.0s
train: New cache created: /content/dataset/train/train/labels.cache
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))
val: Fast image access ✅ (ping: 0.0±0.0 ms, read: 597.8±390.1 MB/s, size: 21.9 KB)
val: Scanning /content/dataset/train/valid/labels... 2048 images, 3 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 2048/2048 1.1Kit/s 1.9s
val: New cache created: /content/dataset/train/valid/labels.cache
optimizer: 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically... 
optimizer: AdamW(lr=0.002, momentum=0.9) with parameter groups 57 weight(decay=0.0), 64 weight(decay=0.0005), 63 bias(decay=0.0)
Plotting labels to /content/runs/detect/train/labels.jpg... 
Image sizes 640 train, 640 val
Using 2 dataloader workers
Logging results to /content/runs/detect/train
Starting training for 50 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       1/50      2.03G      1.248      1.428      1.137          5        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:04
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.2it/s 15.2s
                   all       2048       2134      0.889      0.871      0.904      0.585

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       2/50      2.89G      1.273     0.8566      1.157          3        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 2:01
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.1s
                   all       2048       2134      0.936      0.885      0.941      0.613

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       3/50      2.89G      1.267     0.7819       1.15          7        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:03
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.2it/s 15.2s
                   all       2048       2134      0.935      0.896      0.934      0.605

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       4/50      2.89G      1.252     0.7423      1.145          2        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:02
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.6s
                   all       2048       2134      0.933      0.917      0.939      0.597

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       5/50      2.89G      1.214     0.6984      1.126          5        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:59
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.3s
                   all       2048       2134      0.951      0.919      0.955      0.627

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       6/50      2.89G      1.204     0.6655      1.114          4        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:59
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.4s
                   all       2048       2134      0.975      0.918      0.956      0.631

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       7/50      2.89G      1.188     0.6416       1.11          3        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 2:01
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.3it/s 14.8s
                   all       2048       2134       0.97      0.928      0.962      0.649

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       8/50      2.89G      1.176     0.6242      1.102          4        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:04
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.3it/s 14.7s
                   all       2048       2134      0.969      0.937      0.963      0.639

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       9/50      2.89G      1.173     0.6164      1.102          6        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:03
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.0it/s 15.9s
                   all       2048       2134      0.971      0.938      0.969      0.657

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      10/50      2.89G      1.162     0.6001      1.094          6        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 2:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.3it/s 15.0s
                   all       2048       2134      0.962      0.944      0.967      0.663

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      11/50      2.89G      1.154     0.5872      1.087          3        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:02
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.2it/s 15.3s
                   all       2048       2134      0.972      0.939       0.97      0.666

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      12/50      2.89G      1.131     0.5663      1.079          4        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:04
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.3s
                   all       2048       2134      0.967       0.94      0.969      0.662

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      13/50      2.89G      1.141     0.5646      1.082          4        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:03
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.6s
                   all       2048       2134      0.969      0.943      0.972       0.66

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      14/50      2.89G      1.139     0.5629      1.081          3        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:04
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.3it/s 15.0s
                   all       2048       2134      0.977       0.94      0.972      0.663

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      15/50      2.89G      1.136     0.5614      1.073          3        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:04
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.3it/s 15.0s
                   all       2048       2134      0.967      0.953      0.978      0.664

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      16/50      2.89G      1.123     0.5499      1.074          3        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:04
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.2it/s 15.1s
                   all       2048       2134      0.976      0.953      0.976      0.673

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      17/50      2.89G       1.12     0.5392      1.072          2        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:04
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.2it/s 15.4s
                   all       2048       2134      0.979       0.94      0.975      0.677

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      18/50      2.89G      1.113     0.5369      1.072          7        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:03
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.5s
                   all       2048       2134      0.978      0.948      0.976      0.676

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      19/50      2.89G      1.109     0.5282      1.065          1        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:03
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.4s
                   all       2048       2134      0.976      0.948      0.976      0.673

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      20/50      2.89G      1.099     0.5259      1.064          4        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:03
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.1it/s 15.5s
                   all       2048       2134      0.962      0.949      0.973      0.677

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      21/50      2.89G      1.099     0.5212      1.063          6        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:02
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.5s
                   all       2048       2134      0.976       0.94      0.976      0.681

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      22/50      2.89G      1.098     0.5141      1.059         10        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:02
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.5s
                   all       2048       2134       0.98      0.952      0.978      0.682

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      23/50      2.89G      1.088     0.5054      1.058          2        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:01
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.1s
                   all       2048       2134      0.977      0.958       0.98      0.685

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      24/50      2.89G      1.085     0.5027      1.049          2        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 2:01
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.4s
                   all       2048       2134      0.966      0.955      0.975      0.691

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      25/50      2.89G      1.081     0.5017      1.051          3        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:58
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.6it/s 14.0s
                   all       2048       2134      0.973      0.955       0.98      0.688

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      26/50      2.89G       1.08     0.4942      1.046          5        640: 100% ━━━━━━━━━━━━ 442/442 3.8it/s 1:56
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.6s
                   all       2048       2134      0.982      0.953       0.98      0.685

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      27/50      2.89G      1.071     0.4899       1.05          3        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:03
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.2s
                   all       2048       2134       0.98      0.948      0.978      0.687

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      28/50      2.89G      1.075     0.4919       1.05          2        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:59
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.5s
                   all       2048       2134      0.978      0.953      0.981      0.688

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      29/50      2.89G      1.061     0.4828      1.045          3        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:59
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.7it/s 13.7s
                   all       2048       2134      0.975      0.955       0.98      0.688

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      30/50      2.89G      1.057     0.4733       1.04          6        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:60
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.6it/s 14.0s
                   all       2048       2134      0.979      0.956      0.981      0.693

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      31/50      2.89G       1.06      0.478      1.045          5        640: 100% ━━━━━━━━━━━━ 442/442 3.8it/s 1:58
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.5s
                   all       2048       2134      0.979      0.958      0.979       0.69

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      32/50      2.89G      1.041     0.4645      1.037          2        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:58
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.3s
                   all       2048       2134      0.977       0.96       0.98      0.695

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      33/50      2.89G      1.045     0.4656      1.036          5        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:60
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.2s
                   all       2048       2134      0.974      0.965      0.981      0.698

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      34/50      2.89G      1.041     0.4608      1.035          5        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 2:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.5s
                   all       2048       2134      0.981      0.961       0.98      0.696

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      35/50      2.89G      1.038     0.4622       1.03          5        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 2:00
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.5s
                   all       2048       2134      0.979      0.957      0.981      0.698

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      36/50      2.89G      1.025     0.4522      1.027          4        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:02
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.4s
                   all       2048       2134      0.979      0.962       0.98      0.698

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      37/50      2.89G      1.022     0.4474      1.025          5        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:59
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.7it/s 13.6s
                   all       2048       2134      0.977      0.965      0.981        0.7

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      38/50      2.89G      1.027     0.4434      1.027          5        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:59
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.1s
                   all       2048       2134       0.98      0.963      0.981      0.701

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      39/50      2.89G      1.021     0.4412      1.024          2        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:58
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.6it/s 14.1s
                   all       2048       2134      0.974      0.966      0.981      0.701

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      40/50      2.89G      1.016     0.4357      1.025          3        640: 100% ━━━━━━━━━━━━ 442/442 3.7it/s 1:58
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.6it/s 14.0s
                   all       2048       2134      0.982      0.959       0.98        0.7
Closing dataloader mosaic
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, method='weighted_average', num_output_channels=3), CLAHE(p=0.01, clip_limit=(1.0, 4.0), tile_grid_size=(8, 8))

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      41/50      2.89G      1.005     0.3998      1.029          2        640: 100% ━━━━━━━━━━━━ 442/442 3.8it/s 1:55
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.2it/s 15.1s
                   all       2048       2134      0.979      0.966      0.982      0.697

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      42/50      2.89G      0.997     0.3875      1.027          2        640: 100% ━━━━━━━━━━━━ 442/442 3.6it/s 2:02
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.1it/s 15.8s
                   all       2048       2134      0.982      0.959      0.982      0.702

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      43/50      2.89G      0.988     0.3824      1.019          2        640: 100% ━━━━━━━━━━━━ 442/442 3.8it/s 1:57
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.3it/s 14.9s
                   all       2048       2134       0.98      0.965      0.982      0.702

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      44/50      2.89G     0.9797     0.3764      1.015          2        640: 100% ━━━━━━━━━━━━ 442/442 3.8it/s 1:55
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.4s
                   all       2048       2134      0.985       0.96      0.982      0.704

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      45/50      2.89G     0.9749     0.3764      1.018          2        640: 100% ━━━━━━━━━━━━ 442/442 3.9it/s 1:54
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.5s
                   all       2048       2134      0.975      0.963      0.982      0.704

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      46/50      2.89G     0.9697      0.371      1.017          2        640: 100% ━━━━━━━━━━━━ 442/442 4.0it/s 1:51
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.6it/s 13.9s
                   all       2048       2134      0.973      0.969      0.982      0.703

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      47/50      2.89G     0.9672     0.3678      1.012          2        640: 100% ━━━━━━━━━━━━ 442/442 3.9it/s 1:54
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.6s
                   all       2048       2134       0.98      0.966      0.982      0.706

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      48/50      2.89G     0.9592     0.3626      1.011          2        640: 100% ━━━━━━━━━━━━ 442/442 3.9it/s 1:54
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.4it/s 14.5s
                   all       2048       2134      0.979      0.968      0.982      0.705

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      49/50      2.89G     0.9538     0.3583      1.014          2        640: 100% ━━━━━━━━━━━━ 442/442 3.9it/s 1:52
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.2s
                   all       2048       2134      0.984      0.966      0.983      0.708

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      50/50      2.89G     0.9466     0.3532      1.006          2        640: 100% ━━━━━━━━━━━━ 442/442 3.9it/s 1:54
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.5it/s 14.3s
                   all       2048       2134      0.982      0.966      0.982      0.706

50 epochs completed in 1.875 hours.
Optimizer stripped from /content/runs/detect/train/weights/last.pt, 6.2MB
Optimizer stripped from /content/runs/detect/train/weights/best.pt, 6.2MB

Validating /content/runs/detect/train/weights/best.pt...
Ultralytics 8.4.41 🚀 Python-3.12.13 torch-2.10.0+cu128 CUDA:0 (Tesla T4, 14913MiB)
Model summary (fused): 73 layers, 3,005,843 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 64/64 4.0it/s 15.9s
                   all       2048       2134      0.984      0.966      0.983      0.708
Speed: 0.2ms preprocess, 1.8ms inference, 0.0ms loss, 1.6ms postprocess per image
Results saved to /content/runs/detect/train
