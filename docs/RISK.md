R-1 Technical M/H (downscaling halves otter size). The otters appear to be small in the 4k frames. 
  Since the images will be shrunk to 1080p, the otters will be reduced by a few pixels
  ,then recall will suffer. YOLO will further shrink the images to 640p.  Owner []
  Mitigate: measure typical otter size in pixels for 20 images at 1080p resolution. Spike one model on 
  1080p and on with 4k tiles from the same images. Check recall between the two.
  Trigger: spike not done by end of sprint 2.


R-2 Technical M/M: (multiple individuals labeling, inconsistent rules). If annotation methods and styling 
  are inconsistent between team members, the model learns from messy and inconsistent data. 
  Owner: [] Mitigate: Following and completing the Labeling/annotation guide provided by our project partner.
  Trigger: No agreed annotation guide by sprint 2.

