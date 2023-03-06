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

You must run `libcamera-vid -t 0 --inline -n -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream1}' :demux=h264` on the pi before starting catnip to enable the camera feed