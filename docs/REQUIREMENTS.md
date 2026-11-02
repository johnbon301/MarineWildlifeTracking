# Requirements — Marine Wildlife Tracking

## 1. Problem Statement

Marine Wildlife Tracking aims to develop an AI-powered system that analyzes aerial imagery and drone footage to identify sea otters, track their movements, and recognize observable behavioral patterns.

The system is intended to assist researchers, government agencies, and wildlife conservation organizations in monitoring sea otter populations and understanding their behavior.

By converting raw image and video data into structured, understandable information, the system will help users study sea otter activity, social interactions, movement patterns, and habitat utilization.

The primary focus is sea otters. Detecting and classifying other marine wildlife is outside the current project scope.

## 2. Functional Requirements

### FR-1: Sea Otter Detection

The system must identify sea otters in aerial photographs and drone video footage.

- FR-1.1: The system must identify sea otters within individual images.
- FR-1.2: The system must identify sea otters across individual frames of video footage.
- FR-1.3: The system must provide bounding boxes around detected sea otters.
- FR-1.4: The system must provide a confidence score for each detection.
- FR-1.5: The system should distinguish sea otters from visually similar objects and animals.

**Acceptance criteria:** Given an annotated test dataset, the model must produce measurable detection results using precision, recall, and mean average precision (mAP). Performance targets will be established after evaluating the initial model.

### FR-2: Individual Sea Otter Tracking

The system must track detected sea otters across consecutive video frames.

- FR-2.1: The system must assign tracking identifiers to detected sea otters.
- FR-2.2: The system should maintain consistent identifiers as sea otters move through video footage.
- FR-2.3: The system should record the movement and trajectory of tracked sea otters.
- FR-2.4: The system should handle temporary occlusion and reappearance of tracked sea otters.
- FR-2.5: The system should record the duration for which an individual sea otter is visible.

**Acceptance criteria:** Given a labeled video sequence, the system must produce tracking results that can be compared against ground-truth identities. Tracking performance will be evaluated using identity-related metrics, including IDF1 and ID switches.

### FR-3: Behavioral Pattern Recognition

The system should identify and analyze observable sea otter behavioral patterns.

Potential behaviors of interest include:

- FR-3.1: Resting and rafting patterns.
- FR-3.2: Foraging and feeding behavior.
- FR-3.3: Swimming and movement patterns.
- FR-3.4: Socialization and interactions between sea otters (intraspecies interactions).
- FR-3.5: Interactions between sea otters and other species (interspecies interactions).
- FR-3.6: Denning, habitat use, and other relevant resting or nesting-related behaviors.

**Acceptance criteria:** The system must classify supported behaviors using annotated evaluation data. Behavioral classifications must be evaluated against human-labeled observations, with accuracy and other appropriate classification metrics reported.

The system must distinguish between directly observed behavior and behavior inferred from visual patterns. Unsupported behavioral conclusions must not be presented as confirmed observations.

### FR-4: Movement and Activity Analysis

The system should convert tracking information into useful movement and activity data.

- FR-4.1: Record the movement trajectories of tracked sea otters.
- FR-4.2: Estimate movement speed and direction when video and spatial information support those measurements.
- FR-4.3: Identify frequently visited areas and recurring movement patterns.
- FR-4.4: Record the duration of observable activities.
- FR-4.5: Identify recurring activity patterns over time when sufficient footage is available.

**Acceptance criteria:** Given a video containing tracked sea otters, the system must generate structured movement information that can be compared against the tracking results.

### FR-5: Data Presentation and Reporting

The system must present analyzed information in a format understandable to its intended users.

- FR-5.1: Display detected sea otters and their bounding boxes.
- FR-5.2: Display tracking identifiers and movement trajectories.
- FR-5.3: Present recognized behavioral patterns and their associated confidence.
- FR-5.4: Summarize observable activity and movement patterns.
- FR-5.5: Provide visual representations of relevant data, such as movement paths, activity distributions, and behavioral summaries.
- FR-5.6: Allow users to review the original footage associated with generated observations.
- FR-5.7: Present relevant timestamps and observation metadata alongside analyzed results.

**Acceptance criteria:** A user must be able to review processed footage and access a structured summary of detections, tracking information, and supported behavioral observations without needing to interpret raw model output.

## 3. Non-Functional Requirements

### NFR-1: Reliability

The system should execute its processing pipeline without unexpected crashes or loss of analysis results.

### NFR-2: Performance

The system should process aerial imagery and video within reasonable execution times for its intended research use. Processing speed and resource consumption should be measured during development.

### NFR-3: Scalability

The system should support larger datasets and longer video recordings as computational resources become available.

### NFR-4: Reproducibility

The system should allow researchers to reproduce experiments using documented model configurations, dependencies, datasets, and processing procedures.

### NFR-5: Usability

Generated results should be understandable to researchers and government organizations without requiring specialized knowledge of machine learning.

### NFR-6: Maintainability

The software should use modular components so that detection, tracking, behavioral analysis, and reporting can be updated independently
