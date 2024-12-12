"""
This module provides an API for monitoring Raspberry Pi metrics.
"""

from flask import Flask, jsonify
import psutil


def get_cpu_temperature():
    """
    Get the current CPU temperature.
    Returns:
        int: The CPU temperature in degrees Celsius.
        None: If the temperature cannot be read.
    """
    try:
        return 20  # Some fake data
    except FileNotFoundError:
        return None


def get_disk_usage():
    """
    Get the current disk usage statistics.
    Returns:
        dict: A dictionary containing total, used, free, and
        percent disk usage.
    """
    disk = psutil.disk_usage('/')
    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent
    }


def create_app():
    """
    Create and configure the Flask application.
    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)

    @app.route('/')
    def home():
        """
        Display a welcome message.
        Returns:
            str: A welcome message.
        """
        return "Welcome to the Raspberry Pi Metrics API!"

    @app.route('/cpu-temperature')
    def cpu_temperature():
        """
        Get the CPU temperature.
        Returns:
            Response: A JSON response with the CPU temperature or
            an error message.
        """
        temp = get_cpu_temperature()
        if temp is not None:
            return jsonify({"cpu_temperature": temp})
        return jsonify({"error": "Unable to read CPU temperature"}), 500

    @app.route('/disk-usage')
    def disk_usage():
        """
        Get the disk usage statistics.
        Returns:
            Response: A JSON response with the disk usage statistics.
        """
        usage = get_disk_usage()
        return jsonify(usage)

    return app
