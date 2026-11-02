R-1 Technical M/H (downscaling halves otter size). The otters appear to be small in the 4k frames. 
  Since the images will be shrunk to 1080p, the otters will be reduced by a few pixels
  ,then recall will suffer. YOLO will further shrink the images to 640p.  Owner [Connnor]
  Mitigate: measure typical otter size in pixels for 20 images at 1080p resolution. Spike one model on 
  1080p and on with 4k tiles from the same images. Check recall between the two.
  Trigger: spike not done by end of sprint 2.


R-2 Technical M/M: (multiple individuals labeling, inconsistent rules). If annotation methods and styling 
  are inconsistent between team members, the model learns from messy and inconsistent data. 
  Owner: [Connor] Mitigate: Following and completing the Labeling/annotation guide provided by our project partner.
  Trigger: No agreed annotation guide by sprint 2.


R-3 Technical M/H (overfitting to training images). The model may memorize the lighting, water, 
  and backgrounds from the flights it trains on. It will score well on our images but miss otters
  on new images or footage from the project partner. Owner: [Jonathan] 
  Mitigate: hold out one full flight the model never trains on. Use augmentation (brightness, blur,
  flips) and compare training and validation mAP after each run.
  Trigger: validation mAP falls more than 10% below training mAP.


R-4 Technical M/M (lowering threshold inflates the count). To catch more of the small otters, we may
  lower the confidence threshold. The model will then count kelp, rocks, seals, birds, and sun glare
  as otters, and the final count will be too high. Owner: [Jonathan]
  Mitigate: pick the threshold from the precision-recall curve on the validation set. Add negative
  images with kelp and glare to training. Hand check false positives on 20 images.
  Trigger: precision drops below 0.8 at the chosen threshold.


R-5 Technical M/H (data leakage between train and test). Many frames come from the same flight and
  look almost the same. If we split them at random, the same otters show up in both train and test,
  and our scores will look better than they really are. Owner: [Jonathan]
  Mitigate: split the data by flight or by date, not by single image. Keep one whole flight as the
  test set only.
  Trigger: split method not agreed on before training on the first labeled batch.


