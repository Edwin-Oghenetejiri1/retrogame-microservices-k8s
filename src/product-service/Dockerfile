# Build stage
FROM golang:1.26.2-alpine3.23 AS build

WORKDIR /app

COPY go.mod ./

RUN go mod download

COPY . .

RUN go build -o product-service main.go

# Run stage
FROM alpine:latest AS release

WORKDIR /app

COPY --from=build /app/product-service .

EXPOSE 8080

CMD ["./product-service"]