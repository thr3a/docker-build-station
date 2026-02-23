FROM golang:1.22-alpine AS build

WORKDIR /src/go-gimei

COPY go-gimei/go.mod go-gimei/go.sum ./
RUN go mod download

COPY go-gimei ./

ARG TARGETOS
ARG TARGETARCH
RUN CGO_ENABLED=0 GOOS=${TARGETOS:-linux} GOARCH=${TARGETARCH:-amd64} \
	go build -trimpath -ldflags="-s -w" -o /out/gimei ./cmd/gimei

FROM scratch
COPY --from=build /out/gimei /gimei
ENTRYPOINT ["/gimei"]
CMD ["female:kanji", "-n", "5"]
