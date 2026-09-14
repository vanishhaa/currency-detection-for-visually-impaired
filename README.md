
## Overview

This document tracks end-to-end testing of the currency detection app and
notes on integrating the pieces built by the rest of the team (data
collection, annotation, training, and the inference/TTS script) into a
working whole.

## What Was Tested

- Real-time detection accuracy across all six denominations (₹10, ₹20, ₹50,
  ₹100, ₹200, ₹500) using physical notes not included in the training set.
- Detection performance under varied conditions: different lighting, note
  angle, distance from camera, and note condition (flat vs. slightly
  folded).
- Audio output: confirming the correct denomination is announced clearly
  and only once per stable detection (no repeated/rapid-fire announcements).
- Responsiveness of the app to the quit command (`q`) during and between
  detections.

## Known Issues Found & Resolved

- **TTS repeating non-stop / unresponsive quit key:** caused by
  re-initializing the text-to-speech engine on every detection instead of
  reusing one engine instance, and by the cooldown being tracked per-label
  instead of globally. Fixed by using a single persistent `pyttsx3` engine
  and requiring several consecutive stable frames of the same detection
  before announcing.
- **Detection flickering between denominations:** partly due to limited
  training data per class; added a stability check (same label detected
  across multiple consecutive frames) before triggering an announcement,
  which reduces false announcements even before retraining.

## Current Limitations

- Accuracy is still constrained by dataset size per denomination; ongoing
  data collection from team members is expanding this.
- The app currently runs on a desktop/laptop with a webcam; it has not yet
  been ported to a mobile-friendly format (e.g. TensorFlow Lite).

## Next Testing Priorities

- Re-test accuracy after each retraining round as more images are added.
- Test with worn/damaged notes specifically, since these are
  underrepresented in the current dataset.
- Gather feedback from a visually impaired user, if possible, on the
  clarity and timing of the audio announcements.
