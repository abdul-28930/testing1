import whisper
import time

model = whisper.load_model("large")
# Load the audio file
audio_path = "vvv.mp3"

# Measure time taken for transcription
start_time = time.time()
result = model.transcribe(audio_path, fp16=False)
end_time = time.time()

print(f"Time taken: {end_time - start_time:.2f} seconds")
print(result)