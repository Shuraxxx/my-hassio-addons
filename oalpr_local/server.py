#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, json, subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)
DEFAULT_PATH = "/config/oalpr/data/plate.jpg"
REGION = os.getenv("REGION", "eu")

def run_alpr(img_path: str, region: str):
    try:
        proc = subprocess.run(
            ["alpr", "-c", region, "-j", img_path],
            capture_output=True, text=True, check=True
        )
        data = json.loads(proc.stdout or "{}")
        data["_meta"] = {"region": region, "image": img_path}
        return jsonify(data), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "alpr_failed", "stderr": e.stderr}), 500
    except Exception as ex:
        return jsonify({"error": "exception", "detail": str(ex)}), 500

@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok", "region": REGION}), 200

@app.get("/scan")
def scan():
    img = request.args.get("path", DEFAULT_PATH)
    region = request.args.get("region", REGION)
    return run_alpr(img, region)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
