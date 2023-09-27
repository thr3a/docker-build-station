# 起動方法

アプリがポート3000で起動している場合、

```
docker run --rm -p 4000:80 -e FORWARD_PORT=3000 --add-host=host.docker.internal:host-gateway thr3a/basic-auth-nginx
```

http://localhost:4000/

でアクセス デフォルトは user:passwordでログイン可能

認証情報をカスタマイズには `BASIC_USERNAME` `BASIC_PASSWORD` を指定する。

```
docker run --rm -p 4000:80 -e FORWARD_PORT=3000 --add-host=host.docker.internal:host-gateway -e BASIC_USERNAME=foo -e BASIC_PASSWORD=hogehoge thr3a/basic-auth-nginx
```
