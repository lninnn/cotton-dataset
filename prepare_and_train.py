import os, glob, random, argparse, yaml, subprocess

def split_dataset(img_dir, split=0.8):
    imgs = sorted(glob.glob(os.path.join(img_dir, '*.png')) +
                  glob.glob(os.path.join(img_dir, '*.jpg')))
    random.shuffle(imgs)
    n = int(len(imgs) * split)
    for name, lst in [('train.txt', imgs[:n]), ('val.txt', imgs[n:])]:
        with open(name, 'w') as f:
            for p in lst:
                f.write(os.path.abspath(p) + '\n')
    print(f"Created train.txt ({n}) and val.txt ({len(imgs)-n})")

def create_yaml(obj_data, output='data.yaml'):
    cfg = {}
    with open(obj_data) as f:
        for line in f:
            if '=' in line:
                k,v = [x.strip() for x in line.split('=',1)]
                cfg[k] = v
    nc = int(cfg['classes'])
    names = open(cfg['names']).read().splitlines()
    data = {
        'train': os.path.abspath('train.txt'),
        'val':   os.path.abspath('val.txt'),
        'nc':    nc,
        'names': names
    }
    with open(output, 'w') as f:
        yaml.dump(data, f)
    print(f"Written {output}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--data',   default='obj.data')
    p.add_argument('--imgs',   default='obj_Train_data')
    p.add_argument('--split',  type=float, default=0.8)
    p.add_argument('--epochs', type=int,   default=50)
    p.add_argument('--batch',  type=int,   default=16)
    p.add_argument('--imgsz',  type=int,   default=448)
    args = p.parse_args()

    split_dataset(args.imgs, args.split)
    create_yaml(args.data)

    cmd = [
        'python', 'yolov5\\train.py',
        '--img', str(args.imgsz),
        '--batch', str(args.batch),
        '--epochs', str(args.epochs),
        '--data', 'data.yaml',
        '--weights', 'yolov5s.pt',
        '--name', 'yolo1_experiment'
    ]
    print("Running:", ' '.join(cmd))
    subprocess.run(cmd, check=True)

if __name__ == '__main__':
    main()
