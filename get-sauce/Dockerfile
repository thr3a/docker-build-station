FROM golang:1.21-alpine3.17 as build
# FROM golang:1.21-alpine3.17

RUN go install -v github.com/gan-of-culture/get-sauce@latest

FROM alpine:3.17 AS runner
COPY --from=build /go/bin/* /bin
ENTRYPOINT ["get-sauce"]
