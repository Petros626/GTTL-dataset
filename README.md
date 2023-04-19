# GTTL-dataset
This **German traffic transfer learning** (GTTL)-dataset contains more than xxx,xxx images with more than xx classes. The class system is based on the German road traffic regulation (StVo) and covers traffic signs lights and vehicles. The dataset contains city, villages, country roads, federal roads and highway scenes in different weather conditions, daytimes and time of year. It includes a variation of corner cases like extreme light, snow and rain to validate Deep Learning algorithms.

add some images here....



## Specifications
```
Data:

Resolution: 1920×1080 pixels
Camera: RPi IR-Cut Camera
Sensor: OmniVision OV5647
Lens: M12 mount lens (3.6 mm focal length)
Format: PNG (Quality Level 95%, Compression Level 0)
Size: xxx GB
Classes: xx
Images: xxx,xxx
Minimum distance between individual images: individually self-triggered
```

```

Hardware:

SBC: Raspberry Pi 4B
OS: Raspberry Pi OS (64-bit)
CPU: 1,9 GHz (overclocked)
GPU: 650 MHz (overclocked)
RAM: 8GB
EEPROM: up to date (important for optimized speed)
+ specific settings (see RPi 4 Tuning guide*) 
```
![IMG_20230224_102944](https://user-images.githubusercontent.com/62354721/221149841-7bf500a8-adde-477b-adfa-16f22ecd0809.jpg)

 [RPi 4 Tuning guide*](https://github.com/Petros626/GTTL-dataset/blob/main/RPi%204%20Tuning%20Guide.pdf). Of course the values are not limited, but for me the focus was on a combination of performance and safety. If necessary, I will adjust the values for the CPU and GPU.



## Setup
to be continued.... Images of whole Hardware Setup for dataset creation

### Camera Calibration with PiCamera2 and OpenCV
The new camera stack of the systems Bullseye 32-bit and 64-bit does not work with [OpenCV](https://github.com/opencv/opencv) for video applications, for this you have to activate the old camera stack, but with mismatch of the function of the new library [PiCamera2](https://github.com/raspberrypi/picamera2). 

In principle, it is possible to configure the camera for the **picamera2** library using a `tuning_file`. These files are .json files which allow to adjust the adjustable parameters for the specific camera model. The parameters have been determined specifically for each camera sensor, so that a manual calibration (chapter 6 https://datasheets.raspberrypi.com/camera/raspberry-pi-camera-guide.pdf) is normally not necessary. 
If you do, you can consult the documentation of the parameters and experiment with them yourself.

The adjustment of the camera used with this `tuning_file` offers a lot of adjustment, but you cannot fix lens distortion like radial/tangential distortion with it. For this purpose, however, the special camera calibration using **opencv** can be used. Thus it is theoretically possible to use the tuning parameters as well as the non-distortion for the camera recording.

### Current options

|    PiCamera2              |      OpenCV                   |   PiCamera2&OpenCV
|---------------------------|-------------------------------|-------------------|
| - use the .json tuning_file  with a lot of algorithms for RPi cameras | - Enable the old camera-stack for RPi and use the camera calibration with less tuning parameters | - works, but the stream is very slow (suggestions for improvement welcome **link script**) |                    
 
### Only camera calibration

This script loads the calibration images of the default folder "calib_images" you have taken with the `ir_cut_picamera2_timer.py`script. Further you must give the folder, where the undistorted images after calibration get saved. The last argument is the board dimension, which must be given correctly, because many people make a mistak here, which causes that the algorithms can't find all corners and return `False` for some calibration images. 

```python
python3 calibrate_camera.py --imgdir=calib_imabes --savedir=undistorted_images --board=9x6
```




## Python scripts for creating the dataset

Manually take and save pictures:
```python
ir_cut_picamera2.py: 
```

Same as above as OOP approach (just for learning purposes):
```python
ir_cut_picamera2_oop.py:
```

Take and save pictures with self-triggered timer:
```python
ir_cut_picamera2_timer.py: 
```

The first script is used to manually take and save pictures. The second is a copy of the first but with an object-oriented approach. The last script is used for capturing with a 5 second timer, which is basically used for creating the images for the camera calibration.


## Use of the Scripts
Both scripts need the folder, where the taken images should be saved. If no folder is created before and passed as argument, the script will automatically create a default folder called "images". The default resolution is 1920x1080, if you want to change it don't forget to specify WxH with x.

**Note**: The 'sudo' command is required for permissions of the package [keyboard](https://github.com/boppreh/keyboard)**

```python 
sudo python3 ir_cut_picamera2.py --imgdir=images --res=1920x1080
```

```python
sudo python3 ir_cut_picamera2_oop.py --imgdir=images --res=1920x1080
```

The last script needs the destination, where the calibration images for OpenCV camera calibration get saved. Additionally you can adjust the time before a picture is taken, to position the chessboard before taking the image. To achieve a sufficient accuracy it's recommended to take between 10-20 images of the chessboard.

```python
sudo python3 ir_cut_picamera2_timer.py --imgdir=calibration_images --res=1920x1080 --time=5
```

__Note__: This script serves as the basis for the actual calibration (see **Camera Calibration with PiCamera2 and OpenCV**). Further information here https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html.



## Outlook
For automated camera triggering to create the dataset, GPS triggering would be a good method. The Raspberry Pi with a GPS module (e.g. [Neo-6M GPS](https://www.berrybase.de/fr/u-blox-neo-6m-gps-ttl-empfaenger-inkl.-antenne) with [pynmea2](https://github.com/Knio/pynmea2) or [geopy](https://github.com/geopy/geopy) library could be used for this. The calculation of the distance travelled can be achieved manually **pynmea2** or via ready-made functions **geopy**. 
The question arises after how many metres the camera should trigger, are there statistics after how many metres on average in road traffic one follows the other or does one refer to already created data sets, such as that of [EvoTegra](https://www.evotegra.de/datasets), which used a distance of 4m per triggering. In itself, it might be a good idea to start with a trigger distance of 4 m.
