FROM python:3.10.12

WORKDIR /app
COPY cal.py .
COPY test.py .
CMD ["python3","cal.py"]
