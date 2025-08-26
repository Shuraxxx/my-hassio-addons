FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake git \
    libopencv-dev tesseract-ocr libleptonica-dev \
    libtesseract-dev curl ca-certificates \
    python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Сборка OpenALPR из исходников
WORKDIR /opt
RUN git clone --depth=1 https://github.com/openalpr/openalpr.git && \
    mkdir -p /opt/openalpr/src/build && \
    cd /opt/openalpr/src/build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release && \
    make -j"$(nproc)" && make install && \
    ldconfig

# Данные распознавания (runtime_data уже скопированы make install,
# но убедимся, что они доступны в стандартном месте)
RUN mkdir -p /usr/share/openalpr/runtime_data

# Python API (наш HTTP-сервис)
COPY server.py /opt/server.py
RUN pip3 install --no-cache-dir flask

ENV REGION=eu
EXPOSE 5000
CMD ["python3", "/opt/server.py"]
