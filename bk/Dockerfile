FROM alpine:latest
WORKDIR /bk
ENV tag=v0.5.2
RUN wget -q https://github.com/rust-lang/mdbook/releases/download/${tag}/mdbook-${tag}-x86_64-unknown-linux-musl.tar.gz -O mdbook.tar.gz && \
tar -xzf mdbook.tar.gz && rm mdbook.tar.gz
COPY book.toml ./
COPY src ./src
RUN ./mdbook build
EXPOSE 3000
CMD ["./mdbook", "serve", "-n", "0.0.0.0"]
