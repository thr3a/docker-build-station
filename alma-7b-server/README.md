
```sh
curl -XPOST \
  --url https://alma.turai.work/completion \
  --header "Content-Type: application/json" \
  --data '{"prompt": "Translate this from English to Japanese:\nEnglish: The strength of our services is that they are always developed from the users perspective.\nJapanese:"}' | jq .content
```
