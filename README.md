# Raspberry Pi / Inky wHAT digital photo frame

This project is a simple digital photo frame using a Raspberry Pi and an Inky wHAT e-ink display. It loads a random image from [source.unsplash.com](https://source.unsplash.com/), dithers it and updates the image on the display at an interval you define.

## Hardware requirements

* [Raspberry Pi Zero](https://shop.pimoroni.com/products/raspberry-pi-zero) (or any Inky wHAT compatible model)
* [Inky wHAT](https://shop.pimoroni.com/products/inky-what) e-ink display

## Raspberry Pi headless setup

To set up the project without hooking up the Raspberry Pi to a monitor and keyboard you can do the following:

* Create an empty file named `ssh` on the boot partition of the SD card containing Raspberry Pi OS
* Create a file called `wpa_supplicant.conf` on the boot partition root folder that contains your country information and wifi access point credentials:

```ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert 2 letter ISO 3166-1 country code here>

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```

* Insert the SD card into your Raspberry Pi and allow it to boot up
* When the Raspberry Pi has booted up you can now SSH into the device from your machine, you'll need to look up what it's IP address is. The default username for the device is `'pi'` and the password is `'raspberry'`.

* Git clone the [Pimoroni Inky repository](https://github.com/pimoroni/inky) and run `install.sh` to get the necessary library dependencies installed.
```
git clone https://github.com/pimoroni/inky.git
```
* Git clone this repository to get the digital photo frame Python script
```
git clone https://github.com/peterelst/photoframe.git
```
* You're now ready and can test if the setup is successful by running the following command and watching the display update: `python photoframe.py`


## Customize random image keyword

The Python script uses [source.unsplash.com](https://source.unsplash.com/) for easily getting hold of random images by keyword, the default used is `'cat'` and you can obviously change that in `photoframe.py` to whatever you'd like to see or leave it empty and get completely random images showing up.
```
keyword = '<your keyword>'
```
## Setting up a cron job

To have the Python script run at a defined interval and update the image on the display automatically you can use crontab by running the following command:
```
crontab -e
```
If you want the image to update every 15 minutes the syntax for that looks as follows (make sure the path to the Python script is correct for your particular setup):
```
*/15 * * * * python /home/pi/photoframe/photoframe.py
```

> If you would like to run the script at a different interval, [crontab.guru](https://crontab.guru/) is a helpful resource to figure out the right syntax for that.
