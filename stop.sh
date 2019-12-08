#!/bin/bash

# Run this file to stop the service. Run command:
# sudo ./stop.sh

echo "Stopping service now..."
systemctl stop rpi_home_guardian.service
echo "- Done!"
echo " "