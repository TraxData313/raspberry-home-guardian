#!/bin/bash

# Run this file to to commit changes made to the settings file. 
# This will reload the deamon in order for the changes to take effect.
# Run command:
# sudo ./commit_settings_changes.sh

# - Make the service start at boot and start it now:
echo "Reloading the deamon..."
systemctl stop rpi_home_guardian.service
systemctl daemon-reload
systemctl start rpi_home_guardian.service
echo "- Done! Changes commited!"
echo " "