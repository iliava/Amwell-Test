FROM python:alpine
WORKDIR /app
COPY 1.py /app
CMD python /app/1.py
CMD tail -f /dev/null
