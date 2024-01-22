FROM python:3.10
RUN apt-get update
WORKDIR /app
COPY tiny.pt /app/
COPY . /app
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN apt install ffmpeg -y
RUN pip --default-timeout=100 install -r requirements.txt

EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]