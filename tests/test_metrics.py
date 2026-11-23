import pytest

from marine_tracking.metrics import iou, precision_recall_f1


def test_iou_identical_boxes_is_one():
    assert iou((0, 0, 10, 10), (0, 0, 10, 10)) == 1.0


def test_iou_non_overlapping_boxes_is_zero():
    assert iou((0, 0, 10, 10), (20, 20, 30, 30)) == 0.0


#Overlap is 5x10 = 50; union is 100 + 100 - 50 = 150.
def test_iou_half_overlap_known_value():
    assert iou((0, 0, 10, 10), (5, 0, 15, 10)) == pytest.approx(1 / 3)


def test_precision_recall_f1_known_values():
    precision, recall, f1 = precision_recall_f1(tp=8, fp=2, fn=2)
    assert precision == pytest.approx(0.8)
    assert recall == pytest.approx(0.8)
    assert f1 == pytest.approx(0.8)


def test_precision_recall_f1_no_detections():
    assert precision_recall_f1(tp=0, fp=0, fn=5) == (0.0, 0.0, 0.0)