FROM python:3

WORKDIR /WhatsApp-Bot

COPY . .

CMD ["python", "WhatsApp-Bot/app.py"]