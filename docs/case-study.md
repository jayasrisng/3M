# 3M Case Study

## Summary

3M — Mood Music Machine — is an early AI/HCI prototype that recommends music from facial-expression context. It uses webcam input, facial emotion recognition, emotion-specific music datasets, clustering, and Spotify API integration.

The project is valuable as a portfolio artifact because it begins a larger research arc: from recognizing human context to questioning how intelligent systems should protect the people they observe.

## Problem

Music recommendation systems usually rely on explicit behavior: searches, likes, playlists, listening history, or manual category selection. 3M explored whether software could respond to immediate emotional context instead.

The guiding question was:

> Can an application recognize a user’s facial expression and recommend music that feels appropriate to that emotional state?

## Approach

The prototype uses a staged pipeline:

1. Capture webcam input.
2. Detect and classify facial expression.
3. Map the predicted emotion to an emotion-specific dataset.
4. Cluster music features using KMeans.
5. Use Spotify API integration to recommend songs.
6. Present the experience through a lightweight web interface.

## Technical stack

- Python
- PHP
- HTML/CSS
- OpenCV
- Keras
- scikit-learn
- Spotipy / Spotify Web API
- FER-2013-style facial-expression categories

## Research/publication context

This project is connected to the publication:

> Arsha Sultana MD, Abdul Saherabegum, Akhila Umma, Jayasri Sai Nikitha Guthula (2021). *Music Recommendation Application Based on Facial Expressions.* International Journal of Innovative Research in Information Security, 8(2), 15–19.

The publication link is included in the repository README.

## Design decisions

### Use emotion as a lightweight context signal

The project tested whether facial expression could serve as an input to recommendation. The goal was not perfect emotional understanding; it was to explore a more context-aware interaction pattern.

### Keep recommendations explainable

Emotion-specific datasets and clustering make the recommendation flow easier to explain than a black-box end-to-end system.

### Build a complete prototype path

The system includes detection, recommendation, and interface pieces. Even as an early project, it demonstrates end-to-end thinking.

## Challenges

### Emotion recognition is uncertain

Facial expressions do not fully represent emotion. Lighting, camera quality, culture, neurodiversity, and individual expression differences can all affect results. The modern framing of this project should acknowledge that limitation clearly.

### Context creates privacy questions

The same sensing that makes the system adaptive also raises privacy concerns. This insight becomes important in later XR telemetry and privacy-preserving analytics work.

### Aging dependencies

The project is an older research artifact. A future cleanup pass should modernize environment setup, dependency versions, and demo media.

## What this demonstrates

- Early applied machine learning and HCI prototyping.
- Ability to combine CV, recommendation logic, and web UI.
- Published research collaboration.
- A coherent intellectual thread leading into privacy-preserving XR systems.

## Future work

- Add screenshots or a short demo GIF.
- Modernize dependency setup and environment documentation.
- Add an ethics note on emotion recognition limitations.
- Replace or supplement webcam inference with explicit user control.
- Connect the project visually to the later privacy research timeline.

## Hiring relevance

3M is strongest as an origin-story project for AI/HCI and research roles. It should not be over-positioned as current production ML work. Its value is showing curiosity, end-to-end prototyping, publication experience, and the beginning of a research direction that matured into privacy-preserving XR analytics.
