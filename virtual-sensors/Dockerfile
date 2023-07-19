FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD [ "python", "main.py", "/virtual-sensors/config.ini"]
