import argparse
import cv2
import dlib
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--image", help="Input image file name")
parser.add_argument("--padding", default=0, help="Padding px size")
parser.add_argument("--extension", default='png', help="Output image extension ex. png")
args = parser.parse_args()
image_path = args.image
image = args.image
padding = int(args.padding)
extension = args.extension

face_detector = dlib.get_frontal_face_detector()

# 画像ファイルを読み込む
img = cv2.imread(image_path)

# 人の顔を検出する
faces = face_detector(img, 1)

# 各顔に対して処理を行う
for (i, face) in enumerate(faces):
    # 顔の位置を取得する
    x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()

    # paddingを加えて正方形に切り抜く
    face_width = x2 - x1
    face_height = y2 - y1
    if face_width > face_height:
        y1 = y1 - int((face_width - face_height) / 2)
        y2 = y2 + int((face_width - face_height) / 2)
    else:
        x1 = x1 - int((face_height - face_width) / 2)
        x2 = x2 + int((face_height - face_width) / 2)
    x1 = max(0, x1 - padding)
    y1 = max(0, y1 - padding)
    x2 = min(img.shape[1], x2 + padding)
    y2 = min(img.shape[0], y2 + padding)

    # 顔を切り抜いてリサイズする
    face_img = img[y1:y2, x1:x2]
    face_img = cv2.resize(face_img, (512, 512))

    face_image_path = "{}_face_{}.{}".format(Path(image_path).stem, i, extension)
    cv2.imwrite(face_image_path, face_img)
