# Debian-база аддона Home Assistant (есть apt + s6)
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base-debian:bookworm
FROM openalpr/openalpr:latest AS alprsrc
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV LANG=C.UTF-8

# Копируем бинарь alpr и runtime_data из официального образа OpenALPR
COPY --from=alprsrc /usr/bin/alpr /usr/bin/alpr
COPY --from=alprsrc /usr/share/openalpr /usr/share/openalpr

# Python + Flask (только APT; без pip из-за PEP 668)
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-flask ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Наш сервер
COPY server.py /opt/server.py

# s6: служба, которая запускает сервер
COPY rootfs/ /

EXPOSE 5000
