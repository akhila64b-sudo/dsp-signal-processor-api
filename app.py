from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def moving_average_filter(data, window_size=3):
    """Applies a moving average filter to smooth noisy waveform signals."""
    if not data or len(data) == 0:
        return []
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(data, window, 'same').tolist()

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "service": "DSP Waveform Signal Processing API",
        "status": "active",
        "domain": "ECE Signal Analysis & Python Backend"
    })

@app.route('/api/v1/filter-signal', methods=['POST'])
def filter_signal():
    content = request.get_json()
    if not content or "raw_signal" not in content:
        return jsonify({"error": "Missing 'raw_signal' list parameter"}), 400
    
    raw_signal = content.get("raw_signal", [])
    window_size = content.get("window_size", 3)
    
    filtered_signal = moving_average_filter(raw_signal, window_size)
    
    return jsonify({
        "sample_count": len(raw_signal),
        "window_size": window_size,
        "input_peak": max(raw_signal) if raw_signal else 0,
        "output_peak": max(filtered_signal) if filtered_signal else 0,
        "filtered_signal": filtered_signal
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
