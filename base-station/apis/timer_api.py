from flask import Flask, jsonify
import time

app = Flask(__name__)

# Dictionary to store timers
timers = {}

@app.route('/set_timer/<name>', methods=['GET'])
def set_timer(name):
    if name in timers:
        return jsonify({"error": "Timer already exists."}), 400
    timers[name] = {"start_time": None, "elapsed": 0, "running": False}
    return jsonify({"message": f"Timer {name} created."})

@app.route('/start_timer/<name>', methods=['GET'])
def start_timer(name):
    if name not in timers:
        return jsonify({"error": "Timer not found."}), 404
    timer = timers[name]
    if timer["running"]:
        return jsonify({"error": "Timer already running."}), 400
    timer["start_time"] = time.time()
    timer["running"] = True
    return jsonify({"message": f"Timer {name} started."})

@app.route('/get_time/<name>', methods=['GET'])
def get_time(name):
    if name not in timers:
        return jsonify({"error": "Timer not found."}), 404
    timer = timers[name]
    if not timer["running"]:
        elapsed_time = timer["elapsed"]
    else:
        elapsed_time = timer["elapsed"] + (time.time() - timer["start_time"])
    return jsonify({"timer": name, "time": elapsed_time})

@app.route('/stop_timer/<name>', methods=['GET'])
def stop_timer(name):
    if name not in timers:
        return jsonify({"error": "Timer not found."}), 404
    timer = timers[name]
    if not timer["running"]:
        return jsonify({"error": "Timer is not running."}), 400
    timer["elapsed"] += time.time() - timer["start_time"]
    timer["start_time"] = None
    timer["running"] = False
    return jsonify({"message": f"Timer {name} stopped."})

@app.route('/reset_timer/<name>', methods=['GET'])
def reset_timer(name):
    if name not in timers:
        return jsonify({"error": "Timer not found."}), 404
    timers[name] = {"start_time": None, "elapsed": 0, "running": False}
    return jsonify({"message": f"Timer {name} reset."})

if __name__ == '__main__':
    app.run(debug=True)

