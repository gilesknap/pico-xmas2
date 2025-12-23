#!/bin/bash
# Install udev rules for Raspberry Pi Pico

echo "Installing udev rules for Raspberry Pi Pico..."
sudo cp 99-pico.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo udevadm trigger

echo "Done! You may need to unplug and replug your Pico device."
echo "Make sure your user is in the 'plugdev' group:"
echo "  sudo usermod -a -G plugdev $USER"
echo "You'll need to log out and back in for group changes to take effect."
