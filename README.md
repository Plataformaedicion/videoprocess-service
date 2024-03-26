# videoprocess-service
Servicio para la generacion de videos random

## Instrucciones para correr el proyecto

crear un entorno virtual
```
python3 -m venv venv
```
activar venv
```
source venv/bin/activate
```
instalar dependencias del archivo requirements.txt
```
pip3 install -r requirements.txt

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install ffmpeg
ffmpeg -version
which ffmpeg
export IMAGEIO_FFMPEG_EXE=/opt/homebrew/bin/ffmpeg

```

## Correr el proyecto
```
python3 service.py
```