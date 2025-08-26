ARG BUILD_FROM
FROM openalpr/openalpr:latest AS alprsrc
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV LANG=C.UTF-8

# Копируем alpr и runtime_data
COPY --from=alprsrc /usr/bin/alpr /usr/bin/alpr
COPY --from=alprsrc /usr/share/openalpr /usr/share/openalpr

# Python + Flask
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-pip ca-certificates && \
    pip3 install --no-cache-dir flask && \
    rm -rf /var/lib/apt/lists/*

# Наш сервер и s6-служба
COPY server.py /opt/server.py
COPY rootfs/ /

EXPOSE 5000
