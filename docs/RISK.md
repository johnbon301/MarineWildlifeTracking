R-1 Technical M/H (downscaling halves otter size) The otters appear to be small in the 4k frames. 
  Since the images will be shrunk to 1080p, the otters will be reduced by a few pixels
  then recall will suffer. YOLO with further shrink the imgaes to 640p.  Owner []
  Mitigate: measure typical otter size in pixels for 20 images at 1080p resolution. Spike one model on 
  1080p and  on with 4k tiles from the same images. Check recall between the two.
  Trigger: spike not done by end of sprint 2.
