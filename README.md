# MarineWildlifeTracking

A computer vision model that helps researchers identify marine wildlife from drone images.

## Quickstart

Requires Python 3.11 and Git.

```bash
git clone https://github.com/johnbon301/MarineWildlifeTracking.git
cd MarineWildlifeTracking
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows (Command Prompt)
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

Install dependencies and run the tests:

```bash
pip install -r requirements.txt
python -m pytest
```

Expected result: `7 passed`.

## Project Structure

```
marine_tracking/
  annotations.py   Load Roboflow COCO annotations, count boxes per class, convert to YOLO format
  metrics.py       Compare annotation sets (IoU, precision, recall, F1)
tests/             Automated tests, run in CI on every pull request
docs/              Requirements, design, and risk register
```

## Project Status

The repository currently holds the annotation comparison module and its tests. The detection pipeline is in development (see `docs/DESIGN.md`).

Annotated images are private partner data and are not stored in this repository.

## Documentation

- [Requirements](docs/REQUIREMENTS.md)
- [Technical Design](docs/DESIGN.md)
- [Risk Register](docs/RISK.md)
- [Contributing](CONTRIBUTING.md)
- [AI Agent Instructions](AGENTS.md)
