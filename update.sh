#!/bin/bash

# Run this file to update to the latest version. 
# Run this file if you make changes to the code, so that che changes can take effect.
# Run command:
# sudo ./update.sh

# Update to the lattest version:
git pull

# - Place the new rpi_home_guardian.service in /etc/systemd/system:
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