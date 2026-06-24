FROM python:3.12-slim

WORKDIR /app

RUN pip install google-generativeai
RUN pip install pyqt5 

COPY . .

CMD ["python", "main.py"]