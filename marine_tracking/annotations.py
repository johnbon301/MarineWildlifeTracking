#Load Roboflow COCO annotation exports and convert them for YOLO
import json
from collections import Counter

#Read a COCO annotation file exported from Roboflow
def load_coco(path):
    with open(path) as f:
        return json.load(f)

#Number of annotated boxes per class name
def class_counts(coco):
    names = {c["id"]: c["name"] for c in coco["categories"]}
    return dict(Counter(names[a["category_id"]] for a in coco.get("annotations", [])))

#Convert a COCO box [x, y, width, height] in pixels to YOLO (cx, cy, w, h), normalized 0-1
def coco_bbox_to_yolo(bbox, img_width, img_height): 
    x, y, w, h = bbox
    return (
        (x + w / 2) / img_width,
        (y + h / 2) / img_height,
        w / img_width,
        h / img_height,
    )