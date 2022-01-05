FROM python:alpine
WORKDIR /app
COPY app.py /app
RUN pip install -U Flask
CMD python /app/app.py
