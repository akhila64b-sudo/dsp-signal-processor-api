# dsp-signal-processor-api
Microcontroller Signal Processing &amp; Waveform API in C and Python
# 📡 Microcontroller Signal Processing & Waveform API

A dual-layer engineering project combining **Digital Signal Processing (DSP)** algorithms in **C** with a **Python REST API** interface to analyze and filter noisy waveform telemetry in real-time.

---

## 🚀 KEY FEATURES

- **Noise Filtering:** Applies a Moving Average Filter to clean noisy analog signal waveforms.
- **RESTful API Endpoint:** Exposes DSP processing functions over HTTP via Python (Flask).
- **Signal Analytics:** Computes sample length, window sizes, and signal peak amplitude metrics.

---

## 🛠️ TECH STACK

- **Core Algorithm:** C / Embedded C
- **Backend API Framework:** Python 3 (Flask, NumPy)
- **Domain:** ECE Signal Analysis & Backend Web Services

---

## 💻 API USAGE EXAMPLE

### HTTP POST Request to `/api/v1/filter-signal`:
```json
{
  "raw_signal": [12.5, 14.2, 45.0, 15.1, 13.8, 48.2, 14.0],
  "window_size": 3
}
```

### JSON Response:
```json
{
  "sample_count": 7,
  "window_size": 3,
  "input_peak": 48.2,
  "output_peak": 25.6,
  "filtered_signal": [8.9, 23.9, 24.7, 24.6, 25.6, 25.3, 20.7]
}
```

---

## ⚙️ HOW TO RUN LOCALLY

1. Clone the repository:
   ```bash
   git clone [https://github.com/akhila64b-sudo/dsp-signal-processor-api.git](https://github.com/akhila64b-sudo/dsp-signal-processor-api.git)
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask API server:
   ```bash
   python app.py
   ```
