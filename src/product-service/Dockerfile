FROM golang:1.26.2-alpine3.23 AS BUILD

WORKDIR /app

COPY go.mod ./

RUN go mod download

COPY . .

RUN go build -o product-service main.go

FROM alpine:latest AS RELEASE

WORKDIR /app

COPY --from=BUILD /app/product-service .

EXPOSE 8080

CMD ["./product-service"]