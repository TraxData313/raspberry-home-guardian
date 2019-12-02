# raspberry-home-guardian - in progress...
- <b>IN SUMMARY</b>: Detect motion -> take video and upload it to S3 -> notify via SMS/email
- The Raspberry will create new video/pictures, when motion is detected
- A python script will detects the new video/pictures, and will upload them to an AWS S3 bucket
- When new video arrives in S3, an SNS will notify the user via email/SMS
- Build a buton, light and beeper in order:
- - Use the button to start/stop the guardian, instead of using the GUI
- - Sound an alarm when intrusion is detected


### Install steps:
1. Install raspbian on the raspberry (https://www.raspberrypi.org/documentation/installation/installing-images/README.md)
1. From the OS GUI go to internet settigns and set up a static IPv4 address
1. From raspberry configuration enable SSH, Pi camera, disable GUI with auto login to pi user
1. To work with AWS resources install boto3, SSH to the raspberry and:
   1. Install the library with:
pip install boto3
   1. Create the AWS hidden directory:
mkdir ~/.aws
   1. Next, set up credentials, enter commad <i>nano ~/.aws/credentials</i> -> and fill in your credentials: <br><i>
[default] <br>
aws_access_key_id = <b>YOUR_KEY</b> <br>
aws_secret_access_key = <b>YOUR_SECRET</b> <br></i>
   1. Then, set up your region by command <i>nano ~/.aws/config</i>, replace the region if you will use another: <br>
<i>[default] <br>
region=eu-west-1 <br></i>
1. Create an S3 bucket in AWS and set it up to receive email when new file gets created
   1. Follow the steps here: https://www.youtube.com/watch?v=EGyuzMbXD0Y
1. SSH to the raspberry set up the service: 
   1. Clone the repo: `git pull https://github.com/TraxData313/raspberry-home-guardian-with-aws.git`
   1. Make the installer executable: `chmod +x ./installer.sh`
   1. Run the installer: `sudo ./installer.sh`
   


### Used HW:
- Raspberry PI 3 Model B
- Raspberry camera
- PIR motion sensor
- LEDs
- jumper cables


### Usage:


### Notes:
- port = 80
- Directory where media is saved: /var/www/html/media/
- RPi-Cam-Web-Interface (https://elinux.org/RPi-Cam-Web-Interface#Basic_Installation)


