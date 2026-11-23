from pathlib import Path
import pytest
from marine_tracking.annotations import class_counts, coco_bbox_to_yolo, load_coco

FIXTURE = Path(__file__).parent / "fixtures" / "sample_coco.json"


def test_class_counts_known_fixture():
    coco = load_coco(FIXTURE)
    assert class_counts(coco) == {"sea otter": 2, "poss otter": 1, "bird": 1}


# Box at x=100, y=200, 50x40 px in a 1000x800 image: centre (125, 220).
def test_coco_bbox_to_yolo_known_value():
    assert coco_bbox_to_yolo([100, 200, 50, 40], 1000, 800) == pytest.approx(
        (0.125, 0.275, 0.05, 0.05)
    )