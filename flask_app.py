from flask import Flask, render_template
import subprocess
import logging

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Volume Up
@app.route('/volume/up', methods=['POST'])
def volume_up():
    command = ['adb', 'shell', 'input', 'keyevent', '24']  # Volume Up key event
    try:
        subprocess.run(command, check=True)
        return '', 204
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the command: {e}")
        return '', 500

# Volume Down
@app.route('/volume/down', methods=['POST'])
def volume_down():
    command = ['adb', 'shell', 'input', 'keyevent', '25']  # Volume Down key event
    try:
        subprocess.run(command, check=True)
        return '', 204
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the command: {e}")
        return '', 500

# Arrow Up
@app.route('/up', methods=['POST'])
def up():
    command = ['adb', 'shell', 'input', 'keyevent', '19']  # Up arrow key event
    try:
        subprocess.run(command, check=True)
        return '', 204
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the command: {e}")
        return '', 500

# Arrow Down
@app.route('/down', methods=['POST'])
def down():
    command = ['adb', 'shell', 'input', 'keyevent', '20']  # Down arrow key event
    try:
        subprocess.run(command, check=True)
        return '', 204
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the command: {e}")
        return '', 500

# Arrow Right
@app.route('/right', methods=['POST'])
def right():
    command = ['adb', 'shell', 'input', 'keyevent', '22']  # Right arrow key event
    try:
        subprocess.run(command, check=True)
        return '', 204
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the command: {e}")
        return '', 500

# Arrow Left
@app.route('/left', methods=['POST'])
def left():
    command = ['adb', 'shell', 'input', 'keyevent', '21']  # Left arrow key event
    try:
        subprocess.run(command, check=True)
        return '', 204
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the command: {e}")
        return '', 500

# OK/Enter Key
@app.route('/ok', methods=['POST'])
def ok():
    command = ['adb', 'shell', 'input', 'keyevent', '23']  # OK/Enter key event
    try:
        subprocess.run(command, check=True)
        return '', 204
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the command: {e}")
        return '', 500

# Back Key
@app.route('/back', methods=['POST'])
def back():
    command = ['adb', 'shell', 'input', 'keyevent', '4']  # Back key event
    try:
        subprocess.run(command, check=True)
        return '', 204
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while running the command: {e}")
        return '', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
