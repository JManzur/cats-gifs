FROM python:3.12.0a6-bullseye

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

EXPOSE 5001

CMD ["python", "/usr/src/app/app.py"]