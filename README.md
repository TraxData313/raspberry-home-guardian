# Raspberry Home Guardian
- Detects motion, records video, uploads it to the cloud (AWS S3) and the user gets email/SMS. 
- Cheap, simple to use and easy to setup home surveillance system.

## Build steps:

### Get the parts:
1. <b>[Raspberry PI 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)</b> - about <b>$40</b>
1. <b>Micro SD Card 16GB</b> - about <b>$5</b>
1. <b>[Micro CD Card Reader](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/ExamplePictures/MicroCDReader.PNG)</b> - less than <b>$1</b>
1. <b>[Raspberry camera](https://www.raspberrypi.org/products/camera-module-v2/)</b> - about <b>$30</b> 
1. <b>[PIR motion sensor](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/ExamplePictures/PIRsensor.PNG)</b> - about <b>$2</b> (Search ebay for "PIR sensor arduino")
1. <b>[LEDs](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/ExamplePictures/LEDs.PNG)</b> - about <b>1$</b> (Search ebay for "LEDs arduino")
1. <b>[Jumper cables](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/ExamplePictures/jumperWires.PNG)</b> - about <b>$3</b> (Female-to-femaile, male-to-female, and male-to-maile. At least 10 of each.)
1. <b>[Button](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/ExamplePictures/button.PNG)</b> - about <b>$1</b> (Search for "button arduino". They are small, 4 legged buttons. You'll need one for this project.)
1. <b>[Resistors](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/ExamplePictures/Resistors.PNG)</b> - about <b>$1</b> (Get a kit with a few resistor options, something between 50 and 500 Ohms should work ok. The less the resistance the brighter the LED.)

### Connect the parts:
1. Connect raspberry pi camera - [HOW TO HERE](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/3)
1. Connect the PIR sensor, button and LED [PICTURE](https://raw.githubusercontent.com/TraxData313/raspberry-home-guardian-with-aws/master/ExamplePictures/RPI3pinout.png):
   1. PIR sensor to PIN# 11
   1. Button to PIN# 13
   1. LED to PIN# 15


### Install steps:
1. Install raspbian on the raspberry (https://www.raspberrypi.org/documentation/installation/installing-images/README.md)
1. From the OS GUI go to internet settigns and set up a static IPv4 address
1. From raspberry configuration enable SSH, Pi camera, disable GUI with auto login to pi user
1. SSH to the Raspberry and run the below commands:
   1. git clone https://github.com/TraxData313/raspberry-home-guardian-with-aws.git
   1. cd raspberry-home-guardian-with-aws
   1. chmode + x ./installer.sh
   1. sudo ./installer.sh
1. Follow the installer, it will prompt you for:
   1. S3 bucket name and region
   1. AWS credentials
   
### Usage:
- LED blinks every second, indicating the state. Button is used to change the state:
- - <b>Blinks once</b> if the guardian is <b>disarmed</b> - hold the button to start arming
- - <b>Blinks twice</b> if the guardian is <b>arming</b> - hold the button to disarm. If 5 minutes (default) pass, it will arm
- - <b>Blinks three time</b> if the guardian is <b>armed</b> - when armed the guardian will record video upon motion detected, will upload the video and will notify the user via email/SMS. Hold the button to disarm
- Settings can be changed from the <b>settings.txt</b> file. After you make changes, run <i>sudo ./commit_settings_changes.sh</i> to commit the changes. The settings are:
- - <b>Bucket name</b> - set the bucket name (string), leave no spaces or other symbols. The S3 bucket name where the files are uploaded.
- - <b>Arming time in seconds</b> - seconds (integer), leave no spaces or other symbols. Determines how long the raspberry will delay before starting to monitor for motion.
- - <b>Video lenght in seconds</b> - seconds (integer), leave no spaces or other symbols. Determines how long the video will be upon motion detected.


### Notes:
- Video format is h264, not all mainstream video players support it. I use VLC player - it works fine
