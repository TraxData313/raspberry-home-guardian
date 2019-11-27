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
- To work with AWS resources install boto3, SSH to the raspberry and enter the commands:
- - pip install boto3
- - mkdir ~/.aws
- - nano ~/.aws/credentials -> fill in your credentials:
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
- - nano ~/.aws/config -> fill in your region:
[default]
region=us-east-1


### Used HW:
- Raspberry PI
- Raspberry camera


### Usage:


### Notes:
- port = 80


