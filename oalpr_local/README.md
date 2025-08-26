# OpenALPR Local (Home Assistant add-on)

Minimal HTTP wrapper over OpenALPR running fully locally.

- Health: `GET http://<HA_IP>:5000/healthz`
- Scan:   `GET http://<HA_IP>:5000/scan?path=/config/oalpr/data/plate.jpg&region=eu`
