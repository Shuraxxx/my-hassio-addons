FROM openalpr/openalpr:latest
RUN apt-get update && apt-get install -y --no-install-recommends       python3 python3-pip ca-certificates &&     pip3 install --no-cache-dir flask &&     rm -rf /var/lib/apt/lists/*
ENV REGION=eu
COPY server.py /opt/server.py
EXPOSE 5000
CMD ["python3", "/opt/server.py"]
