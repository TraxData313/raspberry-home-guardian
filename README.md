# Raspberry Home Guardian
- Detects motion, records video, uploads it to the cloud (AWS S3) and the user gets email/SMS

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
1. SSH to the Raspberry and run the below commands:
   1. git clone https://github.com/TraxData313/raspberry-home-guardian-with-aws.git
   1. cd raspberry-home-guardian-with-aws
   1. chmode + x ./installer.sh
   1. sudo ./installer.sh
1. Follow the installer, it will prompt you for:
   1. S3 bucket name and region
   1. AWS credentials
   


### Notes:
- Video format is h264, not all mainstream video players support it. I use VLC player - it works fine
