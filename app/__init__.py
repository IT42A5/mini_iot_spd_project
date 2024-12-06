from flask import Flask, jsonify
import os
import psutil

def get_cpu_temperature():
    try:
        return 20;  # Some fake data
    except FileNotFoundError:
        return None

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent
    }

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Welcome to the Raspberry Pi Metrics API!"

    @app.route('/cpu-temperature')
    def cpu_temperature():
        temp = get_cpu_temperature()
        if temp is not None:
            return jsonify({"cpu_temperature": temp})
        else:
            return jsonify({"error": "Unable to read CPU temperature"}), 500

    @app.route('/disk-usage')
    def disk_usage():
        usage = get_disk_usage()
        return jsonify(usage)

    return app
