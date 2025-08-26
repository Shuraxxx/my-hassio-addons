# База аддона — Debian (есть apt и s6-overlay)
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-debian-base:bookworm
FROM openalpr/openalpr:latest AS alprsrc
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV LANG=C.UTF-8

# Копируем бинарь alpr и runtime_data из официального образа OpenALPR
COPY --from=alprsrc /usr/bin/alpr /usr/bin/alpr
COPY --from=alprsrc /usr/share/openalpr /usr/share/openalpr

# Python + Flask для API
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-pip ca-certificates && \
    pip3 install --no-cache-dir flask && \
    rm -rf /var/lib/apt/lists/*

# Наш сервер
COPY server.py /opt/server.py

# s6: сервис, который запускает сервер
COPY rootfs/ /

EXPOSE 5000
