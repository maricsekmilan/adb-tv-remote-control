# ADB TV Remote Control

This project allows you to control the volume and navigation of an Android TV Stick using a web interface.

[![Watch the video](https://img.youtube.com/vi/Qe83iHiEL4g/0.jpg)](https://youtu.be/Qe83iHiEL4g)


## Libraries Used

- **Flask**: A web framework for Python.
- **subprocess**: To run ADB commands from the server.
- **logging**: For logging application events and errors.


## Instructions

1. **Download SDK Platform Tools**
   - Visit the [Android SDK Platform Tools page](https://developer.android.com/tools/releases/platform-tools) to download the package.
<br>

2. **Add ADB to the PATH Variable in the System Variables**

   2a. **Locate ADB**
   - Download the Android SDK Platform Tools package if you haven't already.
   - After extracting the package, note the folder where `adb.exe` is located (e.g., `C:\Users\YourUsername\AppData\Local\Android\Sdk\platform-tools`).

   2b. **Open System Settings**
   - Click on the Start menu and select Settings.
   - In the Settings window, choose System, then click on About in the left-hand menu.
   - Look for the Advanced system settings link and click it.

   2c. **Set Environment Variables**
   - In the System Properties window, click on the Environment Variables button.

   2d. **Edit the PATH Variable**
   - In the System variables section, find the variable named `Path`.
   - Click on it, then click the Edit button.

   2e. **Add a New Entry**
   - In the Edit Environment Variable window, click the Add button.
   - Paste the path to `adb` (e.g., `C:\Users\YourUsername\AppData\Local\Android\Sdk\platform-tools`) and press Enter.

   2f. **Save Changes**
   - Click OK in the Edit Environment Variable window.
   - Click OK again in the Environment Variables window.
   - Finally, click OK in the System Properties window.

   2g. **Verification**
   - Open the Command Prompt.
   - Type `adb version` and press Enter.
   - If the PATH is set correctly, you should see the version of `adb`.
 <br>


3. **Open Your Android TV Device and Enable Developer Options**

   3a. **Turn On Your Android TV**
   - Make sure your Android TV is powered on and you are on the home screen.

   3b. **Navigate to Settings**
   - Use your remote to scroll down and select the Settings gear icon, usually found on the top right corner of the home screen.

   3c. **Go to Device Preferences**
   - Scroll down and select Device Preferences (it might just say About on some devices).

   3d. **Find Build Number**
   - In the Device Preferences menu, scroll down and select About.
   - Look for Build number and click on it repeatedly (usually 7 times) until you see a message saying, “You are now a developer!”

   3e. **Access Developer Options**
   - Go back to the Device Preferences menu, and you should now see Developer options listed.
   - Select Developer options to enter the settings.

   3f. **Enable USB Debugging**
   - Inside Developer Options, find USB debugging and turn it on. This option allows you to connect your Android TV to a computer for development purposes, such as using ADB commands.

<br>

4. **Connect to Your Android Device**
   - Open Command Prompt and type:
     ```
     adb connect <your android device ip address>
     ```
   - The first time it will ask you to enable the connection on your Android device; set it to OK.
<br>

5. **Make the Right Folder Structure**
   
![image](https://github.com/user-attachments/assets/8c0f8853-c6d2-4a9a-98ee-fc9d80afe44e)

6. **Run the App**
- Execute the following command in your terminal:
  ```
  python app.py
  ```
<br>

7. **Open the Browser**
- Type `127.0.0.1:5000` or your IP address into the browser.
 <br>
 
8. **Control Your Android TV Device**
- Now you can control your Android TV device from the web interface!

