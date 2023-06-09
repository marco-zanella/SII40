# SII40
Group project for the SII40 course

This document is a stub.

## Virtual Sensors
Quickly run virtual sensors:
```bash
cd virtual-sensors
pip3 install -r requirements.txt
python3 main config.ini
```

Build and run image:
```bash
cd virtual-sensors
docker build -t virtual-sensors .
docker run -it --rm --network="host" --name virtual-sensors virtual-sensors
```
