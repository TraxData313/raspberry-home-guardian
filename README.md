# raspberry-home-guardian - in progress...

### Roadmap:
- The RPi-Cam-Web-Interface will create a new video, when motion is detected
- Build a python script that detects the new video and pushes it in an AWS S3 bucket
- When new video arrives in S3, create an SNS that will notify the user via email/SMS
- Build a buton, light and beeper in order:
- - Use the button to start/stop the guardian, instead of using the GUI
- - Sound an alarm when intrusion is detected


### Install:
- Install raspbian on the raspberry (https://www.raspberrypi.org/documentation/installation/installing-images/README.md)
- From GUI internet settigns set up a static IPv4 address
- From raspberry configuration enable SSH, Pi camera, disable GUI with auto login to pi user
- Install RPi-Cam-Web-Interface (https://elinux.org/RPi-Cam-Web-Interface#Basic_Installation - follow Basic Installation)


### Usage:


### Notes:
- port = 80
