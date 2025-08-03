# 🎵 Mood-Based Music Recommendation via Facial Emotion Detection

This project is a full-stack prototype that recommends music based on the user’s facial emotion in real time. It integrates **OpenCV**, **deep learning**, and the **Spotify API** to provide emotion-specific song recommendations using live webcam input.

---

## 🧠 How It Works

1. The system captures live video using your webcam.
2. It detects and classifies your facial expression (e.g., happy, sad, angry) using a deep learning model trained on the FER-2013 dataset.
3. Based on the predicted emotion, it loads emotion-specific song datasets and clusters them using KMeans.
4. Using the Spotify API, it recommends personalized tracks similar to your emotional context.

---

## 📁 Project Structure

```
3M/
├── 33M/
│   ├── angry.csv, happy.csv, sad.csv       # Preprocessed emotion-specific music datasets
│   ├── emotions.py                         # Real-time facial emotion detector
│   ├── project_code.py                     # Song recommender using Spotify + clustering
│   ├── index.html / login.html / register  # Frontend user interface
│   ├── background.jiff, 3M.png             # Assets
│   └── utils/                              # Helper scripts and model utils
```

---

## 🛠 Technologies Used

- **Python**, **PHP**, **HTML/CSS**
- **OpenCV** – for face detection
- **Keras** – for emotion classification
- **Spotipy (Spotify Web API)** – for track metadata and audio features
- **scikit-learn** – for clustering and preprocessing
- **FER-2013 Dataset** – for training emotion recognition model

---

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/3M.git
cd 3M/33M
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Set your Spotify credentials as environment variables:
```bash
export SPOTIPY_CLIENT_ID=your_id
export SPOTIPY_CLIENT_SECRET=your_secret
```

4. Run emotion detection:
```bash
python emotions.py
```

5. Based on detected emotion, call:
```bash
python project_code.py happy
```

---

## 🎯 Sample Emotions Recognized

- Happy 😄
- Sad 😢
- Angry 😠

Each mood uses its corresponding CSV dataset and recommends songs accordingly.

---


## 📄 License

MIT License — feel free to reuse and modify with credit.

---

## 👤 Author

Created by [Jayasri](https://github.com/jayasrisng)  
Built as a final project for intelligent systems + HCI coursework.

**Citation**:  
Arsha Sultana MD, Abdul Saherabegum, Akhila Umma, Jayasri Sai Nikitha Guthula (2021).  
**Music Recommendation Application Based on Facial Expressions**.  
*International Journal of Innovative Research in Information Security (IJIRIS)*, Volume 8, Issue 2, pp. 15–19.  
📚 [Read on ResearchGate](https://www.researchgate.net/publication/387403799_Music_Recommendation_Application_Based_on_Facial_Expressions)  
🌐 [Journal Issue](https://ijiris.com/volume-8-issue-2)
