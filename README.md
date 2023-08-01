# GTTL-dataset
This **German Traffic Transfer Learning** (GTTL)-dataset contains actually more than 16,000 images with more than xx classes. The class system is based on the German road traffic regulation (StVo), traffic and traffic participants. It covers traffic signs, lights, vehicles, pedestrians. The dataset contains city, villages, country roads, federal roads and highway scenes in different weather conditions, daytimes and time of year. It includes a variation of corner cases like extreme light, snow and rain to validate Deep Learning algorithms.


![dataset_snippet_cut](https://github.com/Petros626/GTTL-dataset/assets/62354721/ba4ceb63-dd54-4445-954a-fd55b26355c0)


## Information
**This data set will be continuously expanded and maintained by me in the future. The aim is to collect and label a huge amount (300k+) of images (depending on my private time). Additionally it would be nice to get support, because the prices for gasoline have risen sharply and as a student I pay the driving distances to record the data myself.**

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/mrsakos)

## Specifications
```
Data:

Resolution: 1920×1080 pixels
Camera: RPi IR-Cut Camera (IR-Filter deactivated)
Sensor: OmniVision OV5647
Lens: M12 mount lens (3.6 mm focal length)
Format: PNG (Quality Level 95%, Compression Level 0)
Size: 93.7 GB
Classes: xx
Images: 16.175
Minimum distance between individual images: individually self-triggered
```

```
Hardware:

SBC: Raspberry Pi 4B
OS: Raspberry Pi OS (64-bit)
CPU: 1.9 GHz (overclocked)
GPU: 650 MHz (overclocked)
RAM: 8GB
EEPROM: up to date (important for optimized speed)
+ specific settings (see RPi 4 Tuning guide*) 
```




## Setup

```
1x Raspberry Pi 4 Model B 8GB RAM
1x Fan SHIM by Pimoroni
1x RPi IR-CUT Camera
1x 3D mount with GoPro bracket
1x 10.1inch Capacitive Touch Display for Raspberry Pi, 1280×800, IPS, DSI Interface
1x IP2S-S3L Car Tablet Holder 
1x CSI Flex ribbon cable
1x Odoga 300W Digital Power Converter
```

The following image shows the Raspberry Pi 4 with a heat sink being machined to be compatible with the fan.

![IMG_20230224_102944](https://user-images.githubusercontent.com/62354721/221149841-7bf500a8-adde-477b-adfa-16f22ecd0809.jpg)

 [RPi 4 Tuning guide*](https://github.com/Petros626/GTTL-dataset/blob/main/RPi%204%20Tuning%20Guide.pdf). Of course the values are not limited, but for me the focus was on a combination of performance and safety. If necessary, I will adjust the values for the CPU and GPU. All the other components can easily be found on the web.
 

 ### Car setup

 Here is my setup is used to record the data during driving on different scenes. The used components can be found in chapter ##Setup.

 ![car_setup3-removebg-preview](https://github.com/Petros626/GTTL-dataset/assets/62354721/f64d855d-9b4c-49a4-8dd3-7e3cb16d03d9)

 

## Outlook
For automated camera triggering to create the dataset, GPS triggering would be a good method. The Raspberry Pi with a GPS module (e.g. [Neo-6M GPS](https://www.berrybase.de/fr/u-blox-neo-6m-gps-ttl-empfaenger-inkl.-antenne) with [pynmea2](https://github.com/Knio/pynmea2) or [geopy](https://github.com/geopy/geopy) library could be used for this. The calculation of the distance travelled can be achieved manually **pynmea2** or via ready-made functions **geopy**. 
The question arises after how many metres the camera should trigger, are there statistics after how many metres on average in road traffic one traffic sign follows the other or does one refer to already created data sets, such as that of [EvoTegra](https://www.evotegra.de/datasets), which used a distance of 4m per triggering. In itself, it might be a good idea to start with a trigger distance of 4 m.
