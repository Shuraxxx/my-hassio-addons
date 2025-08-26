FROM openalpr/openalpr:latest

# Python + Flask для API
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-pip ca-certificates && \
    pip3 install --no-cache-dir flask && \
    rm -rf /var/lib/apt/lists/*

ENV REGION=eu

# Наш сервер
COPY server.py /opt/server.py
RUN chmod 755 /opt/server.py && sed -i 's/\r$//' /opt/server.py

EXPOSE 5000
CMD ["/usr/bin/python3","-u","/opt/server.py"]
