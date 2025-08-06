FROM python:3.10-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir requirements.txt
CMD ["python", "maria_alchemy.py"]