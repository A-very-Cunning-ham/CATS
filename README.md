# CATS Project Structure

## meow
Frontend

## purr
Backend

## catnip
Camera device


# Building for development
Run `docker-compose up -d` in the main project folder. The dev server for Meow will be running on [http://localhost:6868](http://localhost:6868) and MongoDB will be on [http://localhost:7017](http://localhost:7017)

To rebuild run `docker-compose up -d --build`

You must run `libcamera-vid --width 2592 --height 1944 -t 0 --inline -n -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream1}' :demux=h264` on the pi before starting catnip to enable the camera feed

You can view the stream directly for debugging by running `ffplay rtsp://catnip-1.local:8554/stream1 -vf "setpts=N/30" -fflags nobuffer -flags low_delay -framedrop`

RaspAP wifi config - only needed for demo
IP: `10.3.141.1`
User: `admin` 
Pass: `secret`
