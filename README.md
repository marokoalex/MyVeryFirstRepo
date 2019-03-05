[中文](/README-zh.md)
# MyVeryFirstRepo
I put up some materials for practicing. Ignore the following contents, please.
I wrote this up for fun and to help me remember how I set things up.

Table of Contents
=================
  * [Hardware](#hardware)
    * [3D Models](#platform)
    * [The Parts](#parts)
  * [Program](#programs-and-training-data)
    * [3D Models](#3d-models)
    * [Testing Data](#testing-data)
      * [Whatever that follows](#whatever-that-follows)
  * [How to Build](#how-to-build)
  * [Donation](#donation)

## Hardware
### Platform
- Raspberry PI 3
- 32GB (or larger) SIM Card
### Parts
- Any chassis with DC motors - for example: https://www.amazon.com/Emgreat-Chassis-Encoder-wheels-Battery/dp/B00GLO5SMY/ref=sr_1_2?ie=UTF8&qid=1486959207&sr=8-2&keywords=robot+chassis
- HC-SR04 sonars
- Raspberry PI compatible camera - for example: https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1486960149&sr=1-1&keywords=raspberry+pi+camera

## Programs and Training Data
- sample.py will run commands from the commandline
- another.py implements a simple driving algorithm using the wheels and sonal

### 3D Models
- [Battery Holder](https://cad.onshape.com/documents/a94876919eca38f49abb5ed6/w/b7e86a4005e4b951f0e3d31a/e/5d33c78dde85b96e033f5c9b)
Note: the Battery Holder was designed for this [External Battery](https://www.amazon.fr/gp/product/B00Y7S4JRQ/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1)

### Testing Data
Repeated messages.......

#### Whatever that Follows
Repeated messages.......

## How to Build

0. Compile and upload the code on the Arduino
```
cd arduino/
make
make upload
```

## Donation
If this project help you reduce time to develop, you may give me a cup of coffee in return :) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=X8AJY4QV5WW3J)
