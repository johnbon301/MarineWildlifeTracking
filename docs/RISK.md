### R-1 Technical — (downscaling halves otter size). 

> **Type:** Technical · **Likelihood / impact:** Medium / High · **Owner:** Conner, Alex

The otters appear to be small in the 4k frames. 
  Since the images will be shrunk to 1080p, the otters will be reduced by a few pixels
  ,then recall will suffer. YOLO will further shrink the images to 640p.

  **Mitigate**: Measure typical otter size in pixels for 20 images at 1080p resolution. Spike one model on 
  1080p and on with 4k tiles from the same images. Check recall between the two.

  **Trigger**: Spike not done by end of sprint 2.


### R-2 Technical — (multiple individuals labeling, inconsistent rules). 

> **Type:** Technical · **Likelihood / impact:** Medium / Medium · **Owner:** Conner, Alex

If annotation methods and styling 
  are inconsistent between team members, the model learns from messy and inconsistent data. 

  **Mitigate**: Following and completing the Labeling/annotation guide provided by our project partner.

  **Trigger**: No agreed annotation guide by sprint 2.


### R-3 Technical — (overfitting to training images).

> **Type:** Technical · **Likelihood / impact:** Medium / High · **Owner:** Jonathan 

The model may memorize the lighting, water, 
  and backgrounds from the flights it trains on. It will score well on our images but miss otters
  on new images or footage from the project partner.


  **Mitigation:**: hold out one full flight the model never trains on. Use augmentation (brightness, blur,
  flips) and compare training and validation mAP after each run.

  **Trigger**: validation mAP falls more than 10% below training mAP.


### R-4 Technical — (lowering threshold inflates the count). 

> **Type**: Technical · **Likelihood / impact:** Medium / High · **Owner:** Jonathan 

To catch more of the small otters, we may
  lower the confidence threshold. The model will then count kelp, rocks, seals, birds, and sun glare
  as otters, and the final count will be too high.

  **Mitigation:**: pick the threshold from the precision-recall curve on the validation set. Add negative
  images with kelp and glare to training. Hand check false positives on 20 images.

  **Trigger**: precision drops below 0.8 at the chosen threshold.


### R-5 Technical — (data leakage between train and test).

> **Type:** Technical · **Likelihood / impact:** Medium / High · **Owner:** Jonathan 

  Many frames come from the same flight and
  look almost the same. If we split them at random, the same otters show up in both train and test,
  and our scores will look better than they really are.

  **Mitigate**: split the data by flight or by date, not by single image. Keep one whole flight as the
  test set only.

  **Trigger**: split method not agreed on before training on the first labeled batch.

### R-6 — no agreed location for the first end-to-end run

> **Type:** Deployment · **Likelihood / impact:** Medium / High · **Owner:** Cash

Our design lists local machines and OSU HPC as possible places to run the pipeline. If we wait too long to choose one, we could get YOLO working on a teammate’s computer and still have no way for a PNNL researcher to repeat the run.

**Mitigation:** Confirm with our project partner where the first run should happen, who owns the machine or account, and what access we need. Record the agreement in the deployment section of `docs/design.md`. If we use one workstation, name the person outside our team who will run the sample there.

**Trigger:** We reach the start of Week 10 without an agreed target, or the person expected to run the sample still cannot access it.

### R-7 — The sample images may have limits on where we can use them

>**Type:** Data access · **Likelihood / impact:** Medium / High · **Owner:** Cash

We need a small set of images that someone can use to check the detector. The images we use for annotation may have different sharing permissions than the images we can include in a GitHub test or show in a demo. If we assume the same permissions apply everywhere, we may have to replace the sample just before the checkpoint.

**Mitigation:** Ask PNNL which images we can use, where we can store them, and whether we can share outputs that still show the original image. Record the answer and the approved sample ID. Use a synthetic image for public CI while we confirm what we can share.

**Trigger:** We select a real image for the checkpoint and cannot point to an agreement that covers its intended use.

### R-8 — A dependency change breaks the working YOLO baseline

>**Type:** Technical · **Likelihood / impact:** Medium / High · **Owner:** Alex

We already have a working Ultralytics setup, and we’re considering Lightning-YOLOs. The Lightning-YOLOs version we reviewed requires an older Ultralytics release. Installing both in the same environment could change the setup that produced our original detections.

**Mitigation:** Keep the working environment intact and test Lightning-YOLOs in a separate virtual environment. Record the Python version, package versions, model weights, and inference settings for the baseline. Have a second teammate rebuild it and compare the detections on one approved image.

**Trigger:** A clean install requires an undocumented package change, or the rebuilt baseline produces a different detection count on the same image with the same weights and settings.

### R-9 — The team loses track of which labels produced a model

>**Type:** Team workflow · **Likelihood / impact:** Medium / High · **Owner:** Conner

We’re adding annotations in batches while teammates are testing models. If a label is corrected in Roboflow after a training run, the latest export may differ from the one used for that run. We could spend time investigating a change in model performance without realizing we also changed the labels.

**Mitigation:** Before training, record the Roboflow export version, class list, and train/validation/test split alongside the run. Link the issue where the batch was reviewed. Keep the original export identifiable when later corrections are made.

**Trigger:** A teammate reviewing a model run cannot identify the exact annotation export and split used to train it.


## Risk priority for the checkpoint redo

Rank 1 is the risk we address first. R-1 through R-9 are stable IDs, so we can change the priority order without breaking references in sprint notes.

| Rank | Risk | Owner |
| --- | --- | --- |
| 1 | R-6 — No agreed execution target | Cash |
| 2 | R-7 — Sample-use permissions are unclear | Cash |
| 3 | R-8 — The working YOLO baseline cannot be reproduced | Alex |
| 4 | R-5 — Frames from the same flight leak across data splits | Jonathan |
| 5 | R-9 — A training run cannot be traced to its annotation export | Conner |
| 6 | R-1 — Resizing removes detail from tiny otters | Conner, Alex |
| 7 | R-2 — Annotators apply different labeling rules | Conner, Alex |
| 8 | R-3 — The model overfits the training flights | Jonathan |
| 9 | R-4 — Lowering the confidence threshold inflates the otter count | Jonathan |

