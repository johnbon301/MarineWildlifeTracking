## Problem and Context

> Now that we have YOLO working with our first 100 annotated images. The results gave us a fair starting point, but the model still misses sea otters that often obvious to the naked eye. We’re adding more labels in Roboflow, and we’re deciding whether to keep training with Ultralytics or try Lightning-YOLOs, mentioned by our project partner's marine biology domain expert. Before we make that call, I want another teammate to be able to run the model we already have and get the same detections. [1]

> Since our project is under guidance from Pacific Northwest National Laboratory, our intended users include marine biology researchers and people working in offshore energy. One use we have in mind is reviewing imagery and video to see where sea otters were observed before and after an oil spill. A researcher might return to the same images months later to investigate why an otter was missed. We should be able to tell them which model and software produced those boxes. They can then use those observations alongside other evidence when studying the spill’s impact.

A decision I’m proposing is the method of which we record and rebuild our Python environments. If someone installs [Lightning-YOLOs](https://github.com/Ultralytics-community/lightning-YOLOs) into the only working copy of our demo, they could change the packages that produced our original results. We *could* switch package managers later but recovering an old setup from memory after we’ve trained several more models would be much more harder. Switching between packet managers is also a risk if we need to install a new package that Lightning-YOLOs requires but Ultralytics does not.

## Options

**A. Use Python’s virtual environment (venv) and pip.** Each setup gets its own virtual environment and a requirements file with the exact versions we tested. A teammate needs Python, the file, and a short set of *readable* instructions. Someone still has to maintain the versions of packages we install directly and the packages they depend on. This makes sense while we have two training setups and can check each one when it changes. [2, 3]

**B. Use uv.** This option is where we declare our dependencies in a project file and commit a lockfile that records the versions uv selected. Running `uv sync --locked` would catch a change to the project file that makes the lockfile stale. We would still need to separate the two incompatible Ultralytics versions. I would favor uv if keeping our requirements files up to date becomes a recurring problem. [4]

**C. Use Poetry.** Poetry also records resolved dependencies in a lockfile and can manage an environment for a project that only contains scripts. Its packaging features would be useful if researchers wanted to install a command we maintain or import our detector into their own Python projects. Right now our first handoff is smaller. Someone needs to clone the repo and run a known example, so there’s less to gain from teaching the team another tool. [5]

**D. Keep individual setups.** This worked well enough to get our first demo running. I’d still use it to try an idea we might discard the same afternoon. Once someone else needs that result for a comparison, they’d have to ask which Python version the person who owns the recent change used, where they got the GPU build or compute, and whether they upgraded anything afterward. That’s too much to leave out of a shared baseline.

## Analysis

Lightning-YOLOs still uses Ultralytics. It adds a PyTorch Lightning training loop, TorchMetrics for detection metrics, and its own command called:

>`lit-yolo`

 The project version reviewed here requires Python 3.10 or newer, PyTorch 2 or newer, PyTorch Lightning from 2.0 up to but excluding 2.6, and an Ultralytics version greater than 8.3 and below 8.4. The regular Ultralytics package has its own install instructions and provides the `yolo` command we used for the demo. [6, 7]

That version range matters on my machine. A read-only check of my demo environment reported Python 3.13.9, Ultralytics 8.4.202, and PyTorch 2.15.0+cu132. My Python version meets the Lightning project’s minimum. My Ultralytics version falls outside its allowed range. Installing Lightning-YOLOs there could replace the working Ultralytics package, or pip could reject the install if we pinned 8.4.202. Two virtual environments lets us try both setups with the same Python interpreter. We still need to get the exact package versions from the teammates who trained the shared model. [7, 8]

I’d also be careful about having a *fair* comparison. The Lightning-YOLOs quick start uses YOLO11n while the YOLO documentation on Ultralytics has their latest version up to YOLO26. A successful run with their example would show that we installed their framework correctly. It would leave open whether it can load our weights on different versions. If we want to compare the trainers themselves, we should start with weights both can load and use the same data split, image size, and hardware. Otherwise, a change in recall could come from the model architecture as easily as the trainer. [6, 7]

The environment file is only one part of that record. If a researcher asks us to revisit an image from a spill survey, we also need the original image ID, the label export, the model weights, and the settings used to draw the boxes. I’d put those identifiers in the run log and the install steps in the README. That way someone reviewing a missed otter can find the right run without having to guess which folder on my desktop contains it.

## Recommendation and Verification Plan

I recommend option A. Keep the working demo intact and create separate environments named `.venv-ultralytics` and `.venv-lightning`. Commit a requirements file for each, along with the Python version, PyTorch installation source, and CPU or GPU target that passed. Pin the Lightning project to the reviewed Git commit so that during the Winter term when we rotate roles, the people in charge of model training start at our latest model version. Keep the virtual environment directories out of Git. [2, 7]

**1. Have someone else rebuild it.** A teammate who didn’t prepare the files starts from a fresh checkout on a second machine. For the baseline, they run the following commands from the repo root in PowerShell (or bash depending on their OS). Repeat with the Lightning environment name and requirements file. These are proposed repo files. The person running the test records the commit and output so we can trace a failure back to the setup they used.

```powershell
python -m venv .venv-ultralytics
.\.venv-ultralytics\Scripts\python.exe -m pip install -r requirements/ultralytics.txt
.\.venv-ultralytics\Scripts\python.exe -m pip check
```

**2. Check the actual result.** The model owners pick an approved image with at least one known detection. Record its hash, the weights hash, the image size, confidence threshold, and expected boxes. Run the baseline on that image on the same type of hardware. Require the same class IDs and counts, and require each one-to-one pair of same-class boxes to overlap by at least 0.95 intersection over union. On a GPU target, also check that inference actually ran on the GPU. A successful install alone would miss the case where someone loaded the wrong weights. [8]

**3. Test Lightning separately.** Start with 

>`lit-yolo --help`

 to generate the repository’s dataset, and run its documented YOLO11n example for one epoch. Require training and validation to finish with a finite loss. Then try loading a copy of our YOLO26 weights and record whether it works or not. A load error rules out that checkpoint for this experiment. Finally, rerun the original baseline case. If either setup needs an undocumented command, update the instructions and repeat from a fresh environment. [7]

**4. Make sure the check can actually fail and that it's not a false-positive.** Change one expected class ID # in a temporary copy of the baseline test. The test must fail and identify the mismatch, then pass when we restore the expected ID. If a dependency update breaks the original case, rebuild from the last passing commit before training again.

## Constraints

In a future use-case, a researcher should be able to check the installation before they have access to imagery. They should use generated images for the public test and keep Roboflow credentials, private links, and restricted weights out of the repository. An authorized teammate can run the otter example where the data is approved for use. Before sharing a bundled environment or weights outside the team, check the terms for the exact release and weights. Lightning-YOLOs lists GPL-3.0, and its Ultralytics dependency has separate licensing terms. We need to account for both in a partner handoff should our project perform better than expected and ready for deployment. [7]

## Delegation and Validation

I used ChatGPT to help draft and revise this RFC, look up and learn about the dependency manager tools, and did some google searches to find out how to check for package versions on Lightning-YOLOs. I’m responsible for checking the technical claims, explaining my recommendation, and respecting our partner’s limits on what I share. The part I need to be able to explain myself is why a package conflict matters to the otter results we already have. [9]

I did some testing on my own a few weeks ago when we had our first 100 annotated images, though my model training stopped because the class indices in my dataset file didn’t match the declared number of classes. I corrected the file and ran predictions on ten test images. That’s why I included a test that runs the model after the install. Before asking the team to approve this proposal, I’ll review the clean-checkout output with a teammate and inspect the expected and actual boxes myself.

## Decision

I propose virtual environment(s) (venv) and pip for both setups, with separate pinned requirements and a verified example for each. Our team can choose a training framework after we know what each one can run and how it performs on the same otter images. The decision stays proposed until the team reviews the results.

## References

1. [MarineWildlifeTracking · Training data review](https://github.com/johnbon301/MarineWildlifeTracking/issues/14)

2. [Python · Creating virtual environments](https://docs.python.org/3/library/venv.html)

3. [pip · Repeatable installs](https://pip.pypa.io/en/stable/topics/repeatable-installs/)

4. [uv · Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)

6. [Poetry · Basic usage](https://python-poetry.org/docs/basic-usage/)

7. [Ultralytics · Install and run YOLO](https://docs.ultralytics.com/quickstart/)

7. a [Lightning-YOLOs · Package requirements at a567556](https://github.com/Ultralytics-community/lightning-YOLOs/blob/a5675568da59a8339277327842cfe740a38a76f1/pyproject.toml)

7. b [Lightning-YOLOs · Setup and YOLO11 examples at a567556](https://github.com/Ultralytics-community/lightning-YOLOs/blob/a5675568da59a8339277327842cfe740a38a76f1/README.md)


8. [Ultralytics · Licensing terms](https://www.ultralytics.com/license)

9. [CS Capstone Handbook · Course AI policy](https://capstone.alexulbrich.com/assignments/introduction/#ai-policy-applies-to-every-assignment)