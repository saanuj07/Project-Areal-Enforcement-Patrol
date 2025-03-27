from flask import Flask, render_template, Response , request
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/golive.html')
def index():
    return render_template('golive.html')

@app.route('/weather.html')
def weather():
    return render_template('weather.html')

@app.route('/control.html')
def control():
    return render_template('control.html')

@app.route('/compare.html')
def compare():
    return render_template('compare.html')

@app.route('/compare2.html')
def compare2():
    return render_template('compare2.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/location1.html')
def location1():
    return render_template('location1.html')


@app.route('/shedule.html')
def shedule():
    return render_template('shedule.html')


@app.route('/video_feed')
def video_feed():
    from detect import generate_frames
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/measure_height', methods=['POST'])
def measure_height():
    data = request.json
    drone_height = float(data.get('drone_height', 0))
    angle_of_sight = float(data.get('angle_of_sight', 0))
    horizontal_distance = float(data.get('horizontal_distance', 0))

    if drone_height <= 0 or angle_of_sight <= 0 or horizontal_distance <= 0:
        return {'error': 'Invalid input parameters'}, 400
    from detect import calculate_building_height
    building_height = calculate_building_height(drone_height, angle_of_sight, horizontal_distance)
    return {'building_height': building_height}


if __name__ == "__main__":

    app.run(debug=True)