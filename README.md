# 3M — Mood Music Machine

**Emotion-aware music recommendation using facial-expression context.**

3M is an early full-stack AI/HCI prototype that recommends music based on a user’s facial expression. It combines webcam-based emotion detection, a deep-learning classifier trained around FER-2013-style facial-expression categories, emotion-specific music datasets, clustering, and Spotify API integration.

The project marks the beginning of a larger research thread: using intelligent systems to understand human context carefully, then asking how those systems can protect privacy instead of exposing people.

## Research context

This work is connected to the publication:

> Arsha Sultana MD, Abdul Saherabegum, Akhila Umma, Jayasri Sai Nikitha Guthula (2021). **Music Recommendation Application Based on Facial Expressions.** *International Journal of Innovative Research in Information Security (IJIRIS)*, Volume 8, Issue 2, pp. 15–19.

- [ResearchGate publication](https://www.researchgate.net/publication/387403799_Music_Recommendation_Application_Based_on_Facial_Expressions)
- [IJIRIS Volume 8 Issue 2](https://ijiris.com/volume-8-issue-2)

## Problem

Most recommendation systems ask users to type, click, rate, or search. 3M explores a different interaction question:

> Can software respond to a user’s immediate emotional context and recommend music that fits the moment?

## How it works

1. The system captures live webcam input.
2. A face/emotion pipeline classifies the user’s facial expression, such as happy, sad, or angry.
3. The predicted emotion selects an emotion-specific music dataset.
4. Music features are clustered with KMeans.
5. Spotify API integration is used to recommend tracks related to the detected mood context.

## Project structure

```text
33M/
├── angry.csv, happy.csv, sad.csv       Emotion-specific music datasets
├── emotions.py                         Real-time facial emotion detector
├── project_code.py                     Recommendation flow using Spotify + clustering
├── index.html / login.html / register  Prototype web interface
├── background.jiff, 3M.png             UI assets
└── utils/                              Helper scripts and model utilities
```

## Tech stack

- Python
- PHP
- HTML/CSS
- OpenCV for face detection
- Keras for emotion classification
- scikit-learn for clustering and preprocessing
- Spotipy / Spotify Web API
- FER-2013-style facial-expression data

## Getting started

```bash
git clone https://github.com/jayasrisng/3M.git
cd 3M/33M
pip install -r requirements.txt
```

Set Spotify credentials before running recommendation code:

```bash
export SPOTIPY_CLIENT_ID=your_id
export SPOTIPY_CLIENT_SECRET=your_secret
```

Run emotion detection:

```bash
python emotions.py
```

Run the recommendation flow for a detected or selected emotion:

```bash
python project_code.py happy
```

## Case study

Read the full case study: [docs/case-study.md](docs/case-study.md)

## Media

Media capture notes are tracked in [media/README.md](media/README.md).

## Current limitations

- This is early research/prototype code, not a production recommendation system.
- Webcam-based emotion recognition can be biased, uncertain, and contextually incomplete.
- Spotify credential setup and local environment configuration may need modernization.
- The project should be treated as a historical research artifact and HCI prototype, not a finished commercial product.

## Why it still matters

3M shows the start of a coherent research direction:

1. Recognize human context.
2. Notice the privacy and identity risks of behavioral sensing.
3. Build privacy-preserving systems for XR and embodied data.

That arc connects directly to later work in VR telemetry privacy, encrypted analytics, and human-centered XR systems.

## License

MIT License — reuse and modify with credit.
