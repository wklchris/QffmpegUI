# QffmpegUI

QffmpegUI is a simple GUI implementation based on [FFmpeg](https://www.ffmpeg.org/) to help users easily convert and edit videos (and audios). 

QffmpegUI is developed under Python 3 with PyQt5. It is developed and tested on Windows system.


## How to use

If you have installed Python 3 (>=3.6, since I used f-string), try to install `pyqt5` package and run
```python
python QffmpegUI.py
```

You can also try to wrap it as an EXE file using `pyinstaller` (remember to do this in a clean virtual environment to reduce the EXE size). I'll probably upload the EXE at every significant release.


## Features

Features without check marks are future ones.

- File
  - [x] Select multiple files
  - [ ] Drag files into the window
  - [ ] Batch all files on the listview
- Video
  - [ ] Add video tab
- Audio
  - [x] Bit rates
  - [ ] Auto-select audio codec by audio type (and vise versa)
  - Format support
    - [x] MP3
    - [ ] AAC, M4A, OGG, FLAC, WAV, APE
- Work Flow
  - [ ] Customize filename pattern
  - [ ] Select output folder
  - [ ] Save the workflow as a template for future reusing
- Advance
  - [x] Check FFmpeg at startup
  - [x] Input FFmpeg command directly
  - [x] Show command output within the app window
- About
  - [ ] Update log  

## Lincense

Licensed under LGPL v2.1, the same with FFmpeg.