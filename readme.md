# Gphoto2 for Python
I needed a Python lib to control my DSLR for a Photobooth project. The libs I could find were not enough efficient and were taking ages to capture a photo or even display a smooth enough live stream. This project aims to offer an easy to use lib and more performance than other libraries.

## Installation
Install required dependencies and `libphoto2-dev` to get the gphoto2 library.
```
sudo apt install -y ffmpeg libturbojpeg0 python3-pip libgl1 libgphoto2-dev
pip3 install numpy opencv-contrib-python
```

## Usage
See `example.py` to know how to use this library.

## Compatibility
The list of supported devices is available on gphoto2 lib repository: https://github.com/gphoto/libgphoto2/tree/master/camlibs/ptp2/cameras
You'll also get a list of supported parameters (use `config.list_paths()` to generate dynamically).

## Update DSLR parameters
You must commit your changes to apply new parameters.
For example, the following line won't apply:
```
config.get_path('/main/capturesettings/shutterspeed').set_value('1/125')
```
unless you commit changes:
```
_instance.commit_config(config)
```
Some parameters may not be available depending on your current DSLR Mode (TV, AV, P, etc.).
The camera may throw an exception is the paremeter is not writable (triggered on commit).

## Performance
I've achieved 50 FPS displaying live preview from Canon EOS 2000D.
