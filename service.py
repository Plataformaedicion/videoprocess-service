from moviepy.editor import *

def service():
    path = "test_videos/test1.mp4"
    video_completo = VideoFileClip(path)
    clip_recortado = video_completo.subclip(5, 10)
    audio_original = video_completo.audio
    audio_cortado = audio_original.subclip(5, 10)

    video_con_audio = clip_recortado.set_audio(audio_cortado)
    video_con_audio.write_videofile("results/test_1.mp4", codec="libx264", audio_codec="aac")

    video_completo.close()
    clip_recortado.close()
    audio_original.close()

# Llamamos a la función para imprimir el mensaje
service()
