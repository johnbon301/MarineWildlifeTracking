# Technical Design — Marine Wildlife Tracking

## 1. Project Overview

Marine Wildlife Tracking is a research project focused on developing an AI-powered system capable of detecting and tracking marine animals, specifically sea otters, using aerial imagery and video footage.

The system aims to investigate two primary capabilities:

- **Object Detection:** Identify sea otters in aerial images and determine their locations within an image.
- **Object Tracking:** Identify individual detections across consecutive video frames and maintain consistent tracking identifiers.

The overall goal is to evaluate the accuracy and reliability of computer vision techniques for monitoring marine wildlife.

## 2. System Architecture

The system is organized into several primary components:

1. **Data Collection and Processing:** Obtain, organize, and prepare aerial imagery and video footage for model training and evaluation.
2. **Data Annotation:** Identify and label sea otters in images so the model has examples from which to learn.
3. **Object Detection:** Use a computer vision model to identify sea otters and generate bounding boxes with confidence scores.
4. **Object Tracking:** Associate detections across consecutive video frames to maintain tracking identifiers.
5. **Evaluation:** Measure detection and tracking performance using appropriate evaluation metrics.
6. **Visualization:** Display detection bounding boxes and tracking identifiers on images and video footage.

### System Pipeline

```text
        Aerial Images / Video
                 |
                 v
        Data Preprocessing
                 |
                 v
          Annotated Dataset
                 |
                 v
          Model Training
                 |
                 v
         Object Detection
                 |
                 v
          Object Tracking
                 |
                 v
        Results and Evaluation
                 |
                 v
         Visualized Output
```

*This diagram represents the intended system architecture. Components that have not yet been implemented are planned components.*

## 3. Technology Stack

The project uses a combination of computer vision and simulation technologies to develop and evaluate an AI-powered marine wildlife tracking system.

### 3.1 Object Detection: YOLO

The project will use the YOLO (You Only Look Once) family of object detection models to identify sea otters in aerial imagery and video footage.

YOLO will process individual images or video frames and generate detections containing:

- Bounding box coordinates identifying the location of detected sea otters.
- Class predictions identifying the detected object.
- Confidence scores representing the model's confidence in each detection.

The model will serve as the primary object detection component of the system.

The specific YOLO version and model configuration will be selected based on performance, accuracy, and computational requirements.

### 3.2 Simulated Dataset Generation: Unreal Engine

The project will use Unreal Engine to develop simulated environments and generate synthetic datasets for training and evaluating the AI model.

Simulated environments may include:

- Ocean and coastal environments.
- Sea otter models and animations.
- Different camera angles and aerial perspectives.
- Varying lighting and weather conditions.
- Different animal positions, orientations, and distances from the camera.

The purpose of simulated datasets is to supplement available real-world imagery and provide additional training examples under controlled conditions.

Synthetic data will be evaluated against real-world footage to determine whether models trained with simulated imagery generalize effectively to actual aerial imagery.

### 3.3 Object Tracking

The object tracking component will associate YOLO detections across consecutive video frames.

The specific tracking algorithm has not yet been finalized.

Potential approaches include tracking algorithms that associate detections based on object location, movement, and visual characteristics.

### 3.4 Compute Environment

The team intends to investigate OSU High Performance Computing (HPC) resources for computationally intensive model training and dataset processing.

The final compute environment and deployment configuration will be documented once access and infrastructure requirements are established.

## 4. Model Training and Dataset Strategy

The project will investigate the use of both real-world and simulated imagery.

Real-world imagery will provide examples of actual sea otters in their natural environments. Simulated imagery generated through Unreal Engine will provide additional controlled training examples.

The general training process will involve:

1. Collecting and organizing available real-world imagery.
2. Generating synthetic imagery using Unreal Engine.
3. Annotating images with sea otter bounding boxes.
4. Preparing training, validation, and testing datasets.
5. Training the YOLO object detection model.
6. Evaluating model performance against held-out real-world imagery.
7. Adjusting model configurations based on evaluation results.

An important research consideration is determining whether synthetic training data improves detection performance on real-world aerial footage.

The team will monitor the differences between simulated and real-world imagery to identify potential limitations in model generalization.

## 5. Data Model and Processing

The system uses aerial imagery and video footage as its primary input data.

The dataset must support training, validation, and testing.

Data processing may include:

- Image resizing and normalization.
- Annotation and bounding box generation.
- Dataset organization.
- Training and validation splits.
- Video frame extraction.
- Data augmentation, where appropriate.

The dataset structure, annotation format, and preprocessing configuration will be documented as they are established.

## 6. Evaluation and Performance Metrics

The project will evaluate both object detection and object tracking.

### Object Detection

Potential evaluation metrics include:

- Precision: How many predicted detections are correct?
- Recall: How many actual sea otters are successfully detected?
- F1 Score: The balance between precision and recall.
- Mean Average Precision (mAP): Overall object detection performance.

### Object Tracking

Potential evaluation metrics include:

- ID switches: How frequently an animal receives an incorrect tracking identity.
- IDF1: Accuracy of identity preservation across frames.
- HOTA: A metric that evaluates both detection and association performance.

The final evaluation metrics and success criteria will be determined based on the research objectives and available ground-truth annotations.

## 7. Development and Compute Environment

Model development, training, and evaluation will use the team's development environment and available computational resources.

Potential compute resources include:

- Local development machines for code development and smaller experiments.
- OSU High Performance Computing (HPC) resources for computationally intensive training and evaluation.
- Additional compute resources if required by the dataset size or model architecture.

The final compute environment, software dependencies, and execution procedures will be documented once established.

## 8. Interfaces and Component Contracts

The primary components will communicate through defined data inputs and outputs.

| Component | Input | Output |
|---|---|---|
| Data Processing | Raw images/video | Processed images and frames |
| Annotation | Images | Labeled dataset |
| Detection | Image/frame | Bounding boxes, classes, confidence scores |
| Tracking | Frame detections | Tracking identifiers and trajectories |
| Evaluation | Predictions and ground truth | Performance metrics |
| Visualization | Detection/tracking results | Annotated images and video |

These interfaces will be refined as implementation progresses.

## 9. Deployment and Execution

As a research project, deployment primarily concerns the ability to reproduce and execute the research pipeline.

The intended execution environment is [INSERT COMPUTE ENVIRONMENT].

The pipeline will be tested end-to-end using a small sample dataset before being executed on the full research dataset.

The execution process should allow another researcher to reproduce the experiment using the documented dependencies, configurations, and dataset requirements.

## 10. Technical Decisions and Open Questions

The following decisions must be finalized or evaluated during development:

- Which object detection architecture will provide the best performance?
- Which tracking algorithm will be used?
- What annotation format will the dataset use?
- How will training, validation, and testing datasets be separated?
- What minimum detection accuracy is considered successful?
- How will tracking accuracy be evaluated?
- What computational resources will be required?
- How will the system handle false positives and false negatives?
- How will the system handle occlusion and animals entering or leaving the frame?

Technical decisions will be updated as experiments provide additional information.
