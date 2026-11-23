<!-- docs/rfcs/2026-11-20-rfc-annotation-method.md -->

# RFC: Annotation method for otter imagery AI model

| Field | Value |
| --- | --- |
| Author | Conner Dillavou |
| Date | 2026-11-20 |
| Status | Accepted |
| Decision Date | 2026-11-15 |
| Deciders | Conner Dillavou, Alex Cortes, Cash Limberg, Jonathan Ferman-Ramirez and PNNL project partner |
| Superseded By | N/A |

## Problem and Context

Our team is building an AI model that detects otters from aerial drone footage. Alongside those otters are seals, birds, boats, and other objects that the model could be confused by. The model's main purpose is to identify and count otters in the kelp beds, after that, our project partner would like the model to analyze otter behavior. Such as if it's eating, resting, grooming or swimming. The end users would be our project partners, Pacific Northwest National Laboratory, who will use the model to track otters in real time from the drone in person. It may be implemented with other labs but for now our project partner states they will be the ones using it.

Our team needs to decide how we will annotate for our project. Our project partner has provided us with a very large data set that consists of close to a thousand (850) aerial drone images and several videos as well. To do the initial training of our AI model, we need to hand-annotate a good portion of our data set all in the same style and methods. The total annotation time should take about 41 hours (see table below). We can either choose to use bounding boxes or center points.

Our team's first step in building the model is to start with hand-annotated data. We could start by trying to train the model with simulated data made in Unreal Engine first, but at the point we are at now we are unsure if the simulated data will even work yet alone provide and benefit to the final model. So the best option is to start with the hand-annotated data. Our options for annotating is to either draw bounding boxes around the otter or to just make a center point on the otter. If we start with one method, there is not an easy way to switch to the other. It would involve us reannotating the data. Annotating 850 images takes a significant amount of time, doing it twice would be a poor use of our time.

If we choose to do nothing, then the model would not do well at all. Since YOLO can only learn from labeled examples, not having any training data isnt much of an option. So without one agreed method, labels would be inconsistent, and the model would learn from inconsistent data.

## Options

### Option A: Bounding boxes

Each otter in a given image of the dataset would be given its own tight box that covers the majority of the otter. The box would be accompanied by a simple label. Other objects that appear in the images, such as watercrafts, seals, birds and unknown objects, will also have their own bounding boxes and labels. Though our main focus is the otters, the quality of annotation for objects other than otters is lower.

#### Benefits
- This method is that this is the standard format that YOLO trains on directly, which is the model we are trying to implement.
- Since it goes over the majority of the animal, it will also record the size of the animal.
- Boxes can be converted to points without reannotating, but it would still take time to make the switch

#### Cost and Drawbacks
- It takes significantly more time than just doing a center point. 
- Even though boxes can be converted to center points after the fact, that too takes time.

Bounding boxes would be the right choice when the model needs otter size and orientation to better detect them and YOLO ends up being the final model we end up implementing. Also, if we can fit the increased annotation time in our schedules.


### Option B: Center point

Every otter would be marked with one point at the center of its mass. This would be much faster to do than bounding boxes. They also don't overlap, unlike boxes. The drawbacks would be that it wouldn't have much information about the size and shape of the animal. 

#### Benefits
- Using center points to annotate the images would be significantly faster than bounding boxes

#### Cost and Drawbacks
- Changing points to boxes requires you to relabel, unlike starting with boxes, which can be converted to points.
- This method doesn't train directly with YOLO if we choose to implement it. 
- It wouldn't yield any information about the otters' size and shape

This would be the right choice when the goal is counting and locating otters, labeling time is the binding limit, and we end up going with a point-based model.

### Option C: Do Nothing

Postponing this decision and doing nothing and trying to run it in YOLO is something we could try, but it wouldn't be productive.

#### Benefits
- Save a considerable amount of time not having to annotate
- It would give us more time to make a decision on what annotation method to use.

#### Cost and Drawbacks
- There would be no real training data

This would be the right choice if the model's purpose was going to change in a way that would make both label types wrong. Which isn't the case for us.

## Analysis

There's evidence that says that boxes won't make a YOLO model more accurate. The real benefit would be the flexibility and size information. The trade-off would be about 28 more hours of labeling. The trade-offs follow.

#### Model Performance
Published research that is similar to our project is limited, but the closest comparison surveyed elephants and antelopes with aerial imagery. It didn't find any statistically significant differences in accuracy between bounding boxes and point labels when using YOLO. However, CenterNet and U-Net did demonstrate better performance with boxes (Xu, 2025). The earlier version reported a YOLO F1-score of 82.8% with boxes and 82.7% with points (Xu, 2024). These results make it so that we can't certainly claim that boxes perform better with YOLO.

#### Labeling Cost
I took 25 images from the dataset and timed my annotation time with both methods. I used Label Studio for the center points and Roboflow to do the bounding boxes. The same 25 images were used but in a different order between the methods. The total time for annotation was divided by the 25 images to give the average time for each image. Bounding boxes took about 3.2 times longer than center points (see table below). The total data set we have been assigned so far is roughly 850 images, which would take about 13 hours with points and 41 with boxes. This lines up with  a published article that found that the median time for a box took 25.5 seconds to draw and 9 seconds to verify. While just a center point only took 3 seconds (Papadopoulos, 2017).

| Method | Tool | Total time for 25 images | Average per image | Estimated time for 850 images |
|---|---|---|---|---|
| Center Points | Label Studio | 22 min 55 sec | 55 sec | About 13 hr |
| Bounding Boxes | Roboflow | 72 min 55 sec | 2 min 55 sec | About 41.3 hr |

(Measured by Conner Dillavou on 11/15/26)

#### Uncertainty
The pilot test was small at only 25 images and was done by only one person. Each method used a different tool so a part of the gap could be blamed on the interface instead of the method. Both of the published studies didn't use otters or watar backgrounds.

## Recommendation and Verification Plan

Our team has chosen to use bounding boxes instead of center points. Boxes are the format that YOLO trains on directly. They will also record each otter's size and handle the large shape of watercrafts. If we later decide to go with points, we can convert boxes to points after the fact without having to relabel. The main cost is the time it will take; our 25-image pilot showed that boxes will take about 2 min 55 sec compared to 55 sec for points. This would be about 28 extra hours of annotation for the entire data set. The other risk would be consistency between annotators. Annotations must be similar in style in order for the model to train well. If labeling takes too long, labels are inconsistent, or the model fails to detect any otters, we will reevaluate our decision.
To verify this decision, our team will complete the following steps:

#### Consistency Check
Two team members with each box the same 100 images without comparing each others work. We will compare the total amount of each object type found per image and look at the two sets of boxes side by side. If the count is different for more than 5 of the 100 images or there is a significant difference in the tightness of the boxes, then we will update the labeling guide and redo the 100 images.

#### Labeling pace
Each labeler will record the duration of each of their sessions and record their time and number of images in the Google Sheet in the shared drive. After the first 100 images, the average time should be no more than 3 minutes and 30 seconds per image. If it is higher, we will reevaluate the decision of choosing boxes and look at points.

#### Model Check
We will hold about 15% of the images for testing, pulling them from different flight times so the model isn't tested on copies of the training data. After our first training run, we want the YOLO validation report to be mAP@0.5 of at least 0.50 for otters. Since the first run will be on a small dataset, we will set the bar low. If it doesn't meet, we will check our labels before second-guessing boxes.


## Constraints

#### Licensing and Software
Since Ultralytics YOLO is free under an AGPL 3.0 license, everything we build and train has to be shared as open source. Unless we buy an Enterprise license (Ultralytics, n.d). This works for this project since we will be handing our final project back to our project partner for them to use.

#### Data use and sharing
Our project partner allows us to share the dataset with project tools, including generative AI tools (Permission given verbally). We are not to send data anywhere our partner has not given us permission. We are still keeping the Roboflow project private, and the data licensing is turned off. Otherwise, Roboflow may license the upload to others (Roboflow, n.d.), which doesn't aid our project.

#### Privacy
Some boats and people are visible in the dataset; we are only labeling the watercraft and not the individual people. The images are from an aerial view, so faces are too small to make out.

## Delegation and Validation

I used Claude AI to help me find published research that used similar methods to our project. I read and checked each source myself before deciding to use it, in order to make sure it was actually valuable and supported our decision process.

I independently analysed the recommendations and made sure they aligned with our project's goals, and I chose bounding boxes as my preferred method. Given the goals of our project, boxes will give the model the most amount of information to train on, which will pay off even though they will take longer. Another reason for this decision was that our project partner has extensive experience with annotating otters for YOLO, and they recommended we go with bounding boxes to start. 

Being that this decision will cost us a considerable amount of time, deciding on our labeling rules comes first. Since a mistake there would result in every image being mislabeled. The 100-image test split would come next, that way, we can validate that our annotations are similar between annotators before moving on to the entire dataset. Since fixing a discrepancy in annotation style after the fact would be a time consuming mistake. The final decision and responsibility for verifying this will fall on me and my team.


## Decision

We made the decision on 11/15/26 to use bounding boxes based on our discussion with our team and project partner. The analysis and the timing of the pilot allowed us to decide that the choice of boxes is worth the extra 28 hours of annotation time. We will revisit if verification step 1, 2, or 3 fails.

## References

Papadopoulos, D. P., Uijlings, J. R. R., Keller, F., & Ferrari, V. (2017). Extreme clicking for efficient object annotation. Proceedings of the IEEE International Conference on Computer Vision (ICCV), 4930–4939. https://arxiv.org/abs/1708.02750

Roboflow. (n.d.). Plans. Roboflow Docs. Retrieved November 15, 2026, from https://docs.roboflow.com/platform/billing-and-plans/plans

Roboflow. (n.d.). Pricing and plan comparison. Retrieved November 15, 2026, from https://roboflow.com/pro

Ultralytics. (n.d.). Licensing. Retrieved November 15, 2026, from https://www.ultralytics.com/licensing

Xu, Z., Wang, T., Skidmore, A. K., & Lamprey, R. H. (2024). A comparison of point and bounding box annotation methods to detect wild animals using remote sensing and deep learning. EGU General Assembly 2024, EGU24-18868. https://doi.org/10.5194/egusphere-egu24-18868

Xu, Z., Wang, T., Skidmore, A. K., Lamprey, R., & Ngene, S. (2025). Bounding box versus point annotation: The impact on deep learning performance for animal detection in aerial images. ISPRS Journal of Photogrammetry and Remote Sensing. https://doi.org/10.1016/j.isprsjprs.2025.02.017
