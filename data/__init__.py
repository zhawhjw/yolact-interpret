from .config import *
from .coco import COCODetection, COCOAnnotationTransform, get_label_map

import torch
import cv2
import numpy as np


def detection_collate(batch):
    """Custom collate fn for dealing with batches of images that have a different
    number of associated object annotations (bounding boxes).

    Arguments:
        batch: (tuple) A tuple of tensor images and (lists of annotations, masks)

    Return:
        A tuple containing:
            1) (tensor) batch of images stacked on their 0 dim
            2) (list<tensor>, list<tensor>, list<int>) annotations for a given image are stacked
                on 0 dim. The output gt is a tuple of annotations and masks.
    """
    targets = []
    imgs = []
    masks = []
    num_crowds = []
    names = []

    for sample in batch:

        imgs.append(sample[0])
        if sample[0] is None:
            pass
        else:
            imgs = torch.stack(imgs, 0)

        if sample[1][0] is None:
            targets.append(None)
        else:
            targets.append(torch.FloatTensor(sample[1][0]))

        if sample[1][1] is None:
            masks.append(None)
        else:
            masks.append(torch.FloatTensor(sample[1][1]))

        num_crowds.append(sample[1][2])
        names.append(sample[1][3])

    return imgs, (targets, masks, num_crowds, names)
