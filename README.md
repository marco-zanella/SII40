# SII40
Group project for the SII40 course

This document is a stub.

## Quick Info
Run
```bash
docker compose up -d
```
to start environment, then
```bash
docker compose down
```
to shut down.
The following services will run:
- Mosquitto on port 1886
- Node Red on port 1880
- InfluxDB on port 8086 (user admin, password password)
- Grafana on port 3000 (user admin, password admin)
- Virtual sensors publishing on MQTT, topic sensors/{ID}

## Virtual Sensors
[![VirtualSensorsDockerImage](https://github.com/marco-zanella/SII40/actions/workflows/VirtualSensorsDockerImage.yml/badge.svg)](https://github.com/marco-zanella/SII40/actions/workflows/VirtualSensorsDockerImage.yml)
