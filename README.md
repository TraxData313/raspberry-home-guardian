# raspberry-home-guardian - in progress...
- Detects motion, captures video, uploads the video to AWS S3 bucket and the user receives email/SMS notification.

## Build steps:

### Get the parts:
1. <b>[Raspberry PI 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)</b> - about $40
1. <b>[Raspberry camera](https://www.raspberrypi.org/products/camera-module-v2/)</b> - about $30 
1. <b>[PIR motion sensor](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/PIRsensor.PNG)</b> - about $2 (Search ebay for "PIR sensor arduino")
1. <b>[LEDs](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/LEDs.PNG)</b> - about 1$ (Search ebay for "LEDs arduino")
1. <b>[Jumper cables](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/jumperWires.PNG)</b> - about $3 (Female-to-femaile, male-to-female, and male-to-maile. At least 10 of each.)
1. <b>[Button](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/button.PNG)</b> - about $1 (Search for "button arduino". They are small, 4 legged buttons. You'll need one for this project.)
1. <b>[Resistors](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/Resistors.PNG)</b> - (Get a kit with a few resistor options, something between 50 and 500 Ohms should work ok. The less the resistance the brighter the LED.)

### Connect the parts:
1. 



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
   




### Notes:
- port = 80
- Directory where media is saved: /var/www/html/media/
- RPi-Cam-Web-Interface (https://elinux.org/RPi-Cam-Web-Interface#Basic_Installation)
- Video format is h264. VLC player supports it.


