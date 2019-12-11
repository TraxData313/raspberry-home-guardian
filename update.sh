#!/bin/bash

# Run this file to update to the latest version. 
# Run this file if you make changes to the code, so that che changes can take effect.
# Run command:
# sudo ./update.sh

# Update to the lattest version:
echo "Fetching latest update and updating to them..."
git fetch --all
git reset --hard origin/master
echo "- Done!"
echo " "
echo " "

# - Make the sh files executable:
echo "Making the rpi_home_guardian.sh executable..."
chmod +x rpi_home_guardian.sh
echo "- Done!"
echo " "
echo "Making the update.sh executable..."
chmod +x update.sh
echo "- Done!"
echo " "
echo "Making the start.sh and stop.sh executable..."
chmod +x start.sh
chmod +x stop.sh
echo "- Done!"
echo " "
echo "Making the commit_settings_changes.sh executable..."
chmod +x commit_settings_changes.sh
echo "- Done!"
echo " "
echo " "

# - Place the new rpi_home_guardian.service in /etc/systemd/system:
echo "- Copying the rpi_home_guardian.service in /etc/systemd/system..."
cp ./rpi_home_guardian.serv /etc/systemd/system/rpi_home_guardian.service
echo "- Done!"
echo " "
echo " "

# - Make the service start at boot and start it now:
echo "Make the service start at boot, reload daemons and starting it now..."
systemctl enable rpi_home_guardian.service
systemctl daemon-reload
systemctl start rpi_home_guardian.service
echo "- Done!"
echo " "