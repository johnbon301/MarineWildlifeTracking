# RFC: Keeping Sea Otter Labels Consistent Across Labelers

**Status:** Proposed\
**Author:** Jonathan, Marine Wildlife Tracking team (CS055)\
**Last updated:** 2026-11-22

## 1. Problem and context

Our capstone project, Marine Wildlife Tracking, is building a computer vision model that finds and tracks sea otters in aerial drone photos of coastal water. Marg Daly collected these photos to monitor sea otters around energy site at PNNL sites near water. This usually takes time when checking manually, and today someone has to find every otter by eye. That is slow and error-prone, because each otter covers only a few pixels of open water. Our model is meant to flag likely otters so the partner reviews candidates instead of scanning every photo. The partner is both the main user and the data owner. Our four-person team is split so that two of us own modeling and training and two own data annotation and cleaning (team repo: github.com/johnbon301/MarineWildlifeTracking).

This decision touches the training data. A detection model learns only from labels: for each photo, a person draws a bounding box (a rectangle) around every otter. A "null image" is a photo a person has checked and marked as containing no otters, which teaches the model what open water looks like. We label in Roboflow, a web tool for drawing and managing labels.

Our team needs to decide how we will label the aerial footage our partner is sending us. The dataset arrived on a hard drive, so every label our model learns from will be drawn by our team. We have already agreed on bounding boxes in Roboflow, with sea otters as our only class, plus null images. What we have not discussed is how we will stay consistent with each other, even though everyone plans to help label.

This needs deciding now because labeling starts soon, and every model and metric we produce is measured against these labels. Our first baseline will be trained on the roughly 100 drone photos that are already annotated by Alex and Connor which they live within the Roboflow project place, so the labeling rules also decide whether later batches are comparable to that baseline. The decision is hard to reverse. If we find out halfway through that people were labeling differently, the only fix is going back through every labeled frame, and every result measured on the old labels stops being comparable to results on the new ones.

If we do nothing, the failure is quiet. With otters only a few pixels wide, two people can easily disagree on whether one is there at all, and a missed otter teaches the model that a real otter is background. The partner would receive a model that misses otters, and our numbers would not show it, because our test labels would miss the same otters.

## 2. Options

**Option 1: Do nothing.** Everyone starts labeling with no written rules and uses their own judgment.
- *Costs:* none upfront. Later costs are inconsistent labels, possible relabeling of the whole dataset, and recall numbers (the share of real otters the model finds) that we cannot trust.
- *Benefits:* labeling starts the day the drive arrives.
- *Right choice when:* one person does all the labeling, or the dataset is small enough to relabel in an afternoon.

**Option 2: Written labeling guide.** Our team writes a short guide and keeps it in the repo. It covers how tight a box should be, otters cut off by the photo's edge, when an image can be marked null, and how to tag uncertain cases. Each person then labels their own batch.
- *Costs:* a few hours to write and read. Nothing checks whether people actually follow it.
- *Benefits:* a shared reference for every hard case, and a record of the rules for anyone who joins later.
- *Right choice when:* the objects are large and unambiguous, or the labelers are experienced enough that a written rule is followed the same way by everyone.

**Option 3: Guide, shared pilot, and review step.** This is Option 2 plus two more steps. First, in a pilot, two team members label the same small set of images separately, compare results, and fix the guide wherever they disagreed. Second, every batch is approved by someone other than its labeler in Roboflow before it enters the dataset.
- *Costs:* the most time. That means the pilot, plus a second person looking at every image.
- *Benefits:* disagreements show up in the first fifty images instead of after five hundred, and every image is checked by two people.
- *Right choice when:* several people label, the objects are tiny or ambiguous, and the same labels are used to test the model.

**Option 4: Center points instead of boxes.** Labelers click once on each otter instead of drawing a box.
- *Costs:* it changes our agreed plan. Standard detectors such as the YOLO family train on boxes [8], so points would need converting to fixed-size boxes or a different, counting-style model.
- *Benefits:* the fastest to label.
- *Right choice when:* the partner needs only counts, not locations to track, and the team is willing to use a point-based counting model.

**Option 5: Probability ("soft") labels.** Suggested by a reviewer. Instead of yes or no, an uncertain object is labeled with how likely it is to be an otter, for example 0.7.
- *Costs:* our label format stores a class and four box coordinates per object, with no field for confidence [8], so this needs a custom label format and training loss. We also expect people to disagree on 0.6 versus 0.7, making the probabilities noisy (an expectation, not a measurement).
- *Benefits:* the model could learn to be unsure on images where people are unsure.
- *Right choice when:* the team has its own training loop and three or more labelers per image, so that a probability can come from counting votes rather than from one person's guess.

## 3. Analysis

**Cost and compatibility (Options 4 and 5).** Papadopoulos et al. found that "extreme clicking," where the labeler clicks the four outer edges of an object, cut box drawing from about 35 seconds to 7 seconds per box with the same quality [1]. So boxes cost little more than points if our guide teaches that method. Sea otter detection work has also used boxes: a Monterey Peninsula study trained a YOLOv5 model modified for tiny objects on 842 labeled sea otter images and reached a 75% F1-score [2]. So Option 4 saves little time and narrows our model choices. Option 5 adds complexity to the training code in exchange for information that an "uncertain" tag already records. If we later want soft labels, uncertain-tagged boxes can be given a lower training weight without relabeling anything.

**Missed labels (Option 1).** Detector training treats any unlabeled region as background, so a missed otter becomes a negative example that penalizes the model for finding it [3]. The same applies to null images: a null image tells the model there is nothing in it, so a careless null mark hides every otter in that image. And when the model finds an otter nobody labeled, it is counted as a false positive, which works directly against our recall-first success criteria. This is the strongest argument against Option 1.

**Consistency (Options 2 and 3).** Since two people are labeling, the difference between Options 2 and 3 is whether we can tell the guide is working. Option 2 gives us rules but no measurement. Option 3 measures agreement in the pilot and catches drift afterward. Roboflow already has a review stage where a reviewer approves or rejects each labeled image and sends rejected ones back to the labeler [5]. It also reports each labeler's first-pass approval rate [6]. So Option 3 needs no new tooling, only our time.

**Time cost of Option 3 over Option 2.** We have not measured our labeling speed yet, so this is an estimate. For tiny otters, most of the time per image goes to zooming and searching the water, not to drawing boxes. A reviewer does a similar search but draws nothing, so we assume review takes about a third of the labeling time. The pilot adds a fixed cost of two people labeling the same 50 images. Under that assumption, Option 3 takes roughly a third more labeling time than Option 2, plus the pilot. The time log in the verification plan replaces this assumption with real numbers. Even if review cost as much as labeling, it would be cheaper than relabeling everything after a late discovery.

**Maintainability and security.** The guide lives in the repo, so rule changes are versioned and batches labeled under an older version can be found and re-reviewed. On security, every option keeps the data in one private workspace limited to our team (see Constraints).

**Uncertainty.** We do not yet know how many photos the drive holds, how many contain otters, or how often two of us will disagree. The pilot answers the last question before it matters.

## 4. Recommendation and verification plan

Our team should adopt Option 3, we currently only have option 2. Every visible otter gets a box. Uncertain ones are boxed and tagged "uncertain" instead of skipped. Images are marked null only after being checked zoomed in. Every batch is approved by someone other than its labeler. The team will know whether this worked through the following checks:


1. **Review approval rate.** We track each labeler's first-pass approval rate in Roboflow [6]. If anyone's rate falls below 85% in a batch, we pause, discuss the rejected images, and update the guide.
2. **Null audit.** A third person rechecks 20% of each batch's null images, zoomed in. If even one otter is found, every null image in that batch is rechecked.
3. **False positive audit.** After the first training run, we review the 50 highest-confidence false positives on the validation set. If more than 10% are real otters that nobody labeled, labels are missing otters, and we re-review the batches those images came from. This is the check that catches otters every person missed.
4. **Frozen test set.** The test set is labeled entirely by hand, by two people, with disagreements settled together. It is then saved as a fixed Roboflow dataset version so every model is scored against the same labels.
5. **Time log.** We record labeling and review minutes per batch. If review takes more than half of labeling time after three batches, we keep reviewing every null image but review only a random 30% of the other images.

## 5. Constraints
**Data ownership and confidentiality.** The photos belong to our partner, so we must confirm with them that uploading to a cloud tool is allowed. If it is, Roboflow's current plans keep projects private on every Core workspace, including the Free Tier. Older Public and Research workspaces cannot have private projects [4]. *What this changes:* we use a Free Tier or paid workspace, never a Public or Research one, and confirm the project shows as private before the first upload. Roboflow also has a "Data Licensing and Model Training" project setting [4], which we will turn off unless the partner agrees otherwise.
 
**If cloud upload is not allowed.** A self-hosted copy of CVAT, an open-source labeling tool under the MIT license that includes review workflows [7], running on OSU resources, is the fallback. *What this changes:* Option 3 still works, but check 2 would be computed from CVAT exports instead of Roboflow's dashboard.
 
**Label ownership (IP).** We need to confirm who owns the labels we create. *What this changes:* nothing is published, including to Roboflow Universe, until the partner confirms.

**People in the footage.** The photos may include people and boats. Roboflow's own documentation says data with personally identifiable information should never be published to Universe [4]. *What this changes:* we do not label people, workspace access stays limited to our team, and any image with an identifiable person is left out of any public release.

## 6. Delegation and validation

**What was handed to AI.** Our team made the earlier choices (Roboflow, bounding boxes, null images, a single otter class) without AI. I used Claude to help find references, draft this RFC, and expand the final draft after peer review, including the option details, the time estimate, the verification plan, and the revision log. I gave Claude my ideas and what I have thought about and have it write down the final draft. I made sure to heavily review the final to ensure every idea of mine is still present.

**Checks that made that reasonable.** I opened every reference and checked each claim I cite against its source. Checking the Monterey study against its workshop page [2] and Roboflow's privacy rules against its current documentation [4] corrected a mistake in my draft, which said free plans are always public. Project facts (team roles, the hard drive, the annotated photos) come from our team and repo, not the AI. The Section 4 thresholds are our judgment calls, not published values. For labeling, the checks are the review gate, pilot script, null audit, and false positive audit, and Roboflow dataset versions are our rollback path.

**Where I validate the result myself, and why.**
- *The labeling guide's wording.* It defines the label schema for every image, the most expensive thing to change later, so I approve every change to it.
- *The pilot result.* It decides whether labeling starts at all.
- *The test set.* Every metric and baseline we report depends on it, so Label Assist is never used on test images, and I review all test labels.
- *The false positive audit.* It is the only check that catches otters every person missed, so I look at those images myself instead of trusting a summary.

## 7. Decision

**Proposed.** The team has accepted bounding boxes, one otter class, and null images. This RFC proposes Option 3 for keeping those labels consistent. It becomes Accepted when the team signs off and the partner confirms that cloud upload is allowed. Until then, no partner data is uploaded.

**Decision Owner:** Jonathan Ferman

**Approval Date:** TBA

**Implementation Status:** Not Yet Started

## References

1. Papadopoulos, D. P., Uijlings, J. R. R., Keller, F., and Ferrari, V. (2017). Extreme clicking for efficient object annotation. ICCV. https://arxiv.org/abs/1708.02750
2. Daly, M. (2022). Detection of southern sea otters (*Enhydra lutris nereis*) from aerial imaging on the Monterey Peninsula. ICLR 2022 Workshop on AI for Earth and Space Science. https://www.iclr.cc/virtual/2022/7684
3. Rambhatla, S. S., Suri, S., Chellappa, R., and Shrivastava, A. Sparsely annotated object detection (SparseDet). https://arxiv.org/abs/2201.04620
4. Roboflow. Plans; Publish Your Project. Roboflow documentation. https://docs.roboflow.com/billing/plans and https://docs.roboflow.com/datasets/publish-your-project
5. Roboflow. Collaborate on Labeling. Roboflow documentation. https://docs.roboflow.com/datasets/annotate/annotate/team-collaboration
6. Roboflow. Annotation Insights. Roboflow documentation. https://docs.roboflow.com/annotate/annotation-insights
7. CVAT. CVAT Community README and license. https://github.com/cvat-ai/cvat
8. Ultralytics. Object detection datasets overview (YOLO label format). https://docs.ultralytics.com/datasets/detect/
