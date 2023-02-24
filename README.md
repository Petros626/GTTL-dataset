# GTTL-dataset
This **German traffic transfer learning** (GTTL)-dataset contains more than xxx,xxx images with more in xx classes. The class system is based on the German road traffic regulation (StVo) and covers traffic signs lights and vehicles. The dataset contains city, villages, country roads, federal roads and highway scenes in different weather conditions, daytimes and time of year. It includes a variation of corner cases like extreme light, snow and rain to validate Deep Learning algorithms.

add some images here....

## Specifications
```
Camera:

Resolution: 1920×1080 pixels
Camera: RPi IR-Cut Camera
Sensor: OmniVision OV5647 
Format: PNG (Quality Level 100%)
Size: xxx GB
Classes: xx
Images: xxx,xxx
Minimum distance between individual images: individually self-triggered
```
![image](https://user-images.githubusercontent.com/62354721/221123624-c9bb0426-997a-4e2e-94f0-ba764db2f04c.png)

Available here: https://www.waveshare.com/product/rpi-ir-cut-camera.htm
```


Hardware:

SBC: Raspberry Pi 4B
OS: Raspberry Pi OS (64-bit)
CPU: 1,9 GHz (overclocked)
RAM: 8GB
EEPROM: up to date (important for optimized speed)
+ specific settings (see below) 
```
![IMG_20230224_102944](https://user-images.githubusercontent.com/62354721/221146164-2346b43f-d79b-410d-bca0-9ccadf2f353c.jpg)

[RPi 4 Tuning guide](https://github.com/Petros626/GTTL-dataset/blob/main/Tuning%20guide.pdf)

## Setup
to be continued...

## Outlook
For automated camera triggering to create the dataset, GPS triggering would be a good method. The Raspberry Pi with a GPS module (e.g. [Neo-6M GPS](https://www.berrybase.de/fr/u-blox-neo-6m-gps-ttl-empfaenger-inkl.-antenne) with [pynmea2](https://github.com/Knio/pynmea2) or [geopy](https://github.com/geopy/geopy) library could be used for this. The calculation of the distance travelled can be achieved manually (**pynmea2**) or via ready-made functions (**geopy**). 
The question arises after how many metres the camera should trigger, are there statistics after how many metres on average in road traffic one follows the other or does one refer to already created data sets, such as that of [EvoTegra](https://www.evotegra.de/datasets), which used a distance of 4m per triggering.
