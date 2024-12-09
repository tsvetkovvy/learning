FROM golang:1.23.3-alpine3.20 AS builder

# Установка рабочей директории
WORKDIR /build

COPY . .

RUN go build -o main main.go

FROM alpine:3.20

COPY --from=builder /build/main /main

EXPOSE 8080

CMD ["/main"]