#!/bin/bash

# How to use:
# Run this file by entering commands:
# chmod +x ./installer.sh
# sudo ./installer.sh





# - Initial message:
echo "Installing rpi_home_guardian service..."

# - Install modules:
echo "Installing boto3 for aws..."
pip install boto3
echo "- Done!"
echo " "

# - Start the configure.py script to set up S3 bucket:
echo "Start the configure.py script to set up the S3 bucket and initialize the ./media folder..."
python configure.py
echo "- Done!"
echo " "

# - Make the sh files executable:
echo "Making the rpi_home_guardian.sh executable..."
chmod +x rpi_home_guardian.sh
echo "- Done!"
echo "Making the update.sh executable..."
chmod +x update.sh
echo "- Done!"
echo "Making the start.sh and stop.sh executable..."
chmod +x start.sh
chmod +x stop.sh
echo "- Done!"
echo " "

# - Place the rpi_home_guardian.service in /etc/systemd/system:
echo "- Copying the rpi_home_guardian.service in /etc/systemd/system..."
cp ./rpi_home_guardian.serv /etc/systemd/system/rpi_home_guardian.service
echo "- Done!"
echo " "

# - Make the service start at boot and start it now:
echo "Make the service start at boot, reload daemons and starting it now..."
systemctl enable rpi_home_guardian.service
systemctl daemon-reload
systemctl start rpi_home_guardian.service
echo "- Done!"
echo " "

# - Final message:
echo "-- All done! Raspberry home guardian is running."
echo "-- Change states by keeping the button pressed for 3 seconds"
echo " "
