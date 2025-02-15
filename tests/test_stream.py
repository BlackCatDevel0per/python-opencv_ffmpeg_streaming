import numpy as np
import cv2
import time
from rtmp_streaming import StreamerConfig, Streamer


def main():

    #cap = cv2.VideoCapture(0)
    # run "ffplay -listen 1 -i 'rtmp://127.0.0.1:8000/stream' to display
    cap = cv2.VideoCapture("http://192.168.1.104:4747/video")
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



if __name__ == "__main__":
    main()
    



