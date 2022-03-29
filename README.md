# face-recognition-system
Simple face recognition system

## Installation
```
pip install cv2-ffmpeg_streaming 
```
or
```
git clone https://github.com/BlackCatDevel0per/python-opencv_ffmpeg_streaming
cd python-opencv_ffmpeg_streaming
python setup.py install
```

## Install requirements
```
sudo apt-get install libboost-numpy-dev
```

# Examples in tests directory
```
import cv2
import time
from rtmp_streaming import StreamerConfig, Streamer

cap = cv2.VideoCapture(0)
# run "ffplay -listen 1 -i 'rtmp://127.0.0.1:8000/stream' to display
ret, frame = cap.read()

sc = StreamerConfig()
sc.source_width = frame.shape[1]
sc.source_height = frame.shape[0]
sc.stream_width = 640
sc.stream_height = 480
sc.stream_fps = 20
sc.stream_bitrate = 1000000
sc.stream_profile = 'main' #'high444' # 'main'
sc.stream_server = 'rtmp://127.0.0.1:8000/stream'


streamer = Streamer()
streamer.init(sc)
#streamer.enable_av_debug_log()


prev = time.time()

show_cap = True

while(True):

    ret, frame = cap.read()
    now = time.time()
    duration = now - prev
    streamer.stream_frame_with_duration(frame, int(duration*100)) #0
    prev = now
    #if show_cap:
    #    cv2.imshow('frame', frame)
    #    if cv2.waitKey(1) & 0xFF == ord('q'):
    #        break


cap.release()
#if show_cap:
#    cv2.destroyAllWindows()
```
