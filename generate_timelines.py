import whisper_timestamped as whisper 
import numpy as np
import json


def generate_timelines(audio: np.ndarray, model: whisper.Whisper, **kwargs) -> str:
    result = whisper.transcribe(model, audio, kwargs)
    srt_file = convert_timelines_to_srt_format(result)

def convert_timelines_to_srt_format(json_timelines: dict, file_name='result.srt') -> str:
    arrow_sign = '-->'
    with open(file_name, 'w') as srt_file:
        for segment_index, segment in enumerate(json_timelines['segments']):
            time_start = f"{segment['start'] // 3600}:{segment['start'] - segment['start'] // 3600 * 3600}:{}"
            str_to_write = f"{segment_index + 1}\n\
                            
                            "
            
def retrieve_divided_time(time_in_seconds: float) -> str:
    hours_passed = time_in_seconds // 3600 * 3600
    time_in_seconds -= hours_passed * 3600
    minutes_passed = time_in_seconds // 60 * 60
    time_in_seconds -= minutes_passed * 60
    seconds_passed = int(time_in_seconds)
    milliseconds_passed = (time_in_seconds - seconds_passed) * 100
