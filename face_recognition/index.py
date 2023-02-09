import argparse
import cv2
import dlib

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
    # 10pxのpaddingを加えて正方形に切り抜く
    x1, y1, x2, y2 = face.left() - padding, face.top() - padding, face.right() + padding, face.bottom() + padding

    # 縦512px 横512pxの画像にリサイズする
    face_img = cv2.resize(img[y1:y2, x1:x2], (512, 512))

    face_image_path = "{}_face_{}.{}".format(image_path.split('.')[0], i, extension)
    cv2.imwrite(face_image_path, face_img)
