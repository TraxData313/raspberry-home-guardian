# raspberry-home-guardian - in progress...

### Roadmap:
- The RPi-Cam-Web-Interface will create a new video, when motion is detected
- Build a python script that detects the new video and pushes it in an AWS S3 bucket
- When new video arrives in S3, create an SNS that will notify the user via email/SMS
- Build a buton, light and beeper in order:
- - Use the button to start/stop the guardian, instead of using the GUI
- - Sound an alarm when intrusion is detected


### Install steps:
- Install raspbian on the raspberry (https://www.raspberrypi.org/documentation/installation/installing-images/README.md)
- From GUI internet settigns set up a static IPv4 address
- From raspberry configuration enable SSH, Pi camera, disable GUI with auto login to pi user
- Install RPi-Cam-Web-Interface (https://elinux.org/RPi-Cam-Web-Interface#Basic_Installation - follow Basic Installation)
- To work with AWS resources install boto3, SSH to the raspberry and:
- - Install the library with:
pip install boto3
- - Create the AWS hidden directory:
mkdir ~/.aws
- - Next, set up credentials, enter commad <i>nano ~/.aws/credentials</i> -> and fill in your credentials: <br><i>
[default] <br>
aws_access_key_id = <b>YOUR_KEY</b> <br>
aws_secret_access_key = <b>YOUR_SECRET</b> <br></i>
- - Then, set up your region by command <i>nano ~/.aws/config</i>, replace the region if you will use another: <br>
<i>[default] <br>
region=eu-west-1 <br></i>


### Used HW:
- Raspberry PI
- Raspberry camera


### Usage:


### Notes:
- port = 80
- Directory where media is saved: /var/www/html/media/


