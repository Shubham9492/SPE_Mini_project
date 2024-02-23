FROM python:3.9-slim

WORKDIR /app
COPY cal.py .
COPY test.py .
CMD ["python3","cal.py"]
