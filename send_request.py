import requests


requests.post("http://localhost:5000/align", files={'audio_file': open("example.mp3", 'rb'), 'text_file': open("subtitle.json", 'r', encoding='utf-8')})


