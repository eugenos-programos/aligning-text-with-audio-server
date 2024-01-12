from flask import Flask, request, send_file
from aeneas.executetask import ExecuteTask
from aeneas.task import Task
import json
import os
import torch



app = Flask(__name__)


def normalize_text(text: str) -> str:

    model, example_texts, languages, punct, apply_te = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                  model='silero_te')
    return apply_te(text, lan='en')

def convert_json_to_text(json_file: dict) -> str:
    result_text = ''

    for subtitle in json_file:
        for text in subtitle['text']:
            result_text += text
        result_text += " "
    return result_text

def align_text_with_audio(text_file_name, audio_file_name):
    config_string = u"task_language=eng|is_text_type=plain|os_task_file_format=json"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = audio_file_name
    task.text_file_path_absolute = text_file_name
    task.sync_map_file_path_absolute = "syncmap.json"

    ExecuteTask(task).execute()
    task.output_sync_map_file()

def capitalize_and_save_text_bysentences(text: str, file_name: str):
    sentences = text.split('.')
    capitalized_sentences = []
    result_text = ''

    for sentence in sentences:
        if sentence:
            capitalized_sentence = sentence[0].upper() + sentence[1:]
            result_text += capitalized_sentence + '\n'
    if os.path.exists(file_name):
        os.system(f"rm {file_name}")
    os.system(f"touch {file_name}")
    with open(file_name, 'w') as sent_file:
        sent_file.write(result_text)

@app.route('/align', methods=['POST'])
def align_endpoint():
        audio_file_name = "audio.mp3"
        text_file_name = "subtitles.txt"
        audio_file = request.files['audio_file'].save(audio_file_name)
        text_file = request.files['text_file'].read().decode("utf-8")
        text = convert_json_to_text(json.loads(str(text_file)))
        normalized_text = normalize_text(text)
        capitalize_and_save_text_bysentences(normalized_text, text_file_name)
        align_text_with_audio(text_file_name, audio_file_name)
        return send_file("syncmap.json")


if __name__ == '__main__':
    app.run(debug=True)
