# Data Collection Notes

**Role:** Data Collection Lead
**Owner:** Member 1

## Overview

This document describes how the image dataset for the currency detection
model was collected.

## Denominations Covered

- ₹10
- ₹20
- ₹50
- ₹100
- ₹200
- ₹500

## Collection Method

- Images were captured of real currency notes and exported from WhatsApp
  (`.jpeg` format).
- Each denomination has its own folder under
  `Tensorflow/workspace/images/collectedimages/<denomination>/`.

## Variation Captured

To help the model generalize, images included variation in:
- Distance from camera and angle
- Lighting conditions
- Note condition (flat vs. slightly folded/worn)
- Background surface

## Dataset Size

- Roughly 20-25 images per denomination collected initially.
- Known limitation: detection accuracy is currently constrained by dataset
  size — more images per denomination (target: 80-150 each), with greater
  variation in lighting/angle/condition, is the top priority for improving
  model accuracy in the next iteration.

## Notes for Future Data Collection

- Prioritize photographing multiple individual notes per denomination
  (not the same note repeatedly) to capture natural wear/print variation.
- Include both front and back sides of each note.
- Capture a few images with partial occlusion or the note at a steep angle,
  since real-world use won't always present the note perfectly flat and
  centered.