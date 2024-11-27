FROM python:3.14.0a2-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ app/
COPY run.py .

EXPOSE 5000
CMD [ "python", "run.py" ]
