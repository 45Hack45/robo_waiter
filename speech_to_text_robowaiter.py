import io
from google.oauth2 import service_account
from google.cloud import speech

client_file = 'llave_storage.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

#Load audio file
audio_file = 'audio.mp3'
with io.open(audio_file,'rb') as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding = speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz = 44100,
    language_code = 'es-ES'
)

response = client.recognize(config=config,audio=audio)

with open("transcripcion.txt", "w") as file:
    for result in response.results:
        file.write(result.alternatives[0].transcript)

# Paso 1: Leer el contenido del fichero
with open('transcripcion.txt', 'r') as file:
    content = file.read()

# Paso 2: Dividir el contenido en palabras
words = content.split()

# Paso 3: Filtrar las palabras que te interesan y contar sus frecuencias
palabras_interes = ['you', 'penguin', 'is']
word_count = {}

for word in words:
    if word in palabras_interes:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# Paso 4: Escribir las palabras filtradas y sus conteos en un nuevo fichero
with open('fichero_filtrado.txt', 'w') as file:
    for word, count in word_count.items():
        file.write(f'{word}: {count}\n')

