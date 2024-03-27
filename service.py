from moviepy.editor import *

def service():
    path = "test_videos/test1.mp4"
    video_completo = VideoFileClip(path)
    clip_recortado = video_completo.subclip(1, 5)
    audio_original = video_completo.audio
    audio_cortado = audio_original.subclip(1, 5)
    video_con_audio = clip_recortado.set_audio(audio_cortado)
    video_con_audio.write_videofile("results/test_3.mp4", codec="libx264", audio_codec="aac")
    video_completo.close()
    clip_recortado.close()
    audio_original.close()

def service2():
    path1 = "results/test_1.mp4"
    path2 = "results/test_2.mp4"
    path3 = "results/test_3.mp4"
    clip1 = VideoFileClip(path1)
    clip2 = VideoFileClip(path2)
    clip3 = VideoFileClip(path3)
    final_clip = concatenate_videoclips([clip1,clip2,clip3])
    final_clip.write_videofile("results/my_concatenation.mp4", codec="libx264", audio_codec="aac")

# Llamamos a la función para imprimir el mensaje
#service()
service2()
