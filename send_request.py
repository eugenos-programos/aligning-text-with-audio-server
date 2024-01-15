import requests


print(requests.post("http://localhost:5000/align_without_text", files={'audio_file': open("example.mp3", 'rb'), 'text_file': open("subtitle.json", 'r', encoding='utf-8')}).text)


