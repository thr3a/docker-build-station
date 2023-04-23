# 使い方

```
docker run --rm -v `pwd`:/app -w /app thr3a/face_recognition --image image.jpg --extension png
```


一括バージョン

```
find . -name "*.jpg" -exec docker run --rm -it -v `pwd`:/app -w /app thr3a/face_recognition --image {} --extension png --padding 180 \;
```
