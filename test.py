# -*- coding: utf-8 -*-
"""
Name:
    
Purpose:
    
Specification:
    
Environment:
    Python 3.4.3
    
"""

from pyicic.IC_ImagingControl import *

# open lib
ic_ic = IC_ImagingControl()
ic_ic.init_library()

# open first available camera device
cam_names = ic_ic.get_unique_device_names()
print(cam_names)
cam = ic_ic.get_device(cam_names[0])
cam.open()

# change camera properties
print(cam.list_property_names())  # ['gain', 'exposure', 'hue', etc...]
cam.gain.auto = True  # enable auto gain

cam.enable_continuous_mode(True)  # image in continuous mode
cam.start_live(show_display=True)  # start imaging

cam.enable_trigger(True)  # camera will wait for trigger
if not cam.callback_registered:
    cam.register_frame_ready_callback()  # needed to wait for frame ready callback

for i in range(10):  # take 10 shots
    cam.reset_frame_ready()  # reset frame ready flag

    # send hardware trigger OR call cam.send_trigger() here
    cam.send_trigger()

    cam.wait_til_frame_ready(1000)  # wait for frame ready due to trigger
    cam.save_image(''.join(['image-', str(i), '.jpg']), 1)
