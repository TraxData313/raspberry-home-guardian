#!/bin/bash

# Run this file to start the service. Run command:
# sudo ./start.sh

echo "Starting service now..."
systemctl start rpi_home_guardian.service
echo "- Done!"
echo " "