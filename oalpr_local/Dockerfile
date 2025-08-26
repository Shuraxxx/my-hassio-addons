# База аддонов HA с s6-overlay
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.19
FROM openalpr/openalpr:latest AS alprsrc
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV LANG=C.UTF-8

# Копируем готовый бинарь alpr и runtime_data из официального образа OpenALPR
COPY --from=alprsrc /usr/bin/alpr /usr/bin/alpr
COPY --from=alprsrc /usr/share/openalpr /usr/share/openalpr

# Python + Flask для API
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-pip ca-certificates && \
    pip3 install --no-cache-dir flask && \
    rm -rf /var/lib/apt/lists/*

# Наш сервер
COPY server.py /opt/server.py

# S6: служба, которая запускает сервер
COPY rootfs/ /        # положим run-скрипт в /etc/services.d

EXPOSE 5000
