from generate_timelines import generate_timelines
import whisper_timestamped as whisper 


if __name__ == '__main__':
    file_name = ""
    audio = whisper.load_audio(file_name)
    model = whisper.load_model("tiny", device='cpu')
    generate_timelines()
