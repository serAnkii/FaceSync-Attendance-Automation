# FaceSync-Attendance-Automation

## Image Collection Script: imagecollect.py

### Overview

The `imagecollect.py` script is responsible for collecting facial images to train a facial recognition model. It captures images from the webcam, detects faces, and stores the face data in a pickled file for future use.


### Dependencies

- **OpenCV:** Used for webcam access and image processing.
- **NumPy:** Handles and processes arrays of facial images.
- **Pickle:** Serializes and stores face data.
- **User Input:** Collects user input for labeling the collected data.

### Script Execution

1. **Webcam Initialization:**
   - Opens a connection to the default webcam (index 0).

2. **Face Detection:**
   - Utilizes the Haar Cascade Classifier to detect faces in the webcam feed.
   - Draws rectangles around detected faces for visual indication.

3. **Data Collection:**
   - Captures facial data by cropping and resizing the detected faces.
   - Limits the collection to 100 images, sampled every 10 frames.

4. **User Input:**
   - Requests the user to input their name for labeling the collected data.

5. **Data Storage:**
   - Converts the collected facial data into a NumPy array.
   - Reshapes the array and stores it in a Pickle file (`faces_dataset.pkl`).
   - Manages a separate Pickle file for storing corresponding names (`names.pkl`).

6. **Usage Instructions:**
   - Run the script in a Python environment.
   - Follow on-screen instructions to input your name and allow the webcam to capture facial images.
   - Press the 'k' key to stop the data collection process or wait until 100 images are collected.
   - The collected facial data and corresponding names are stored in the `data/` directory.

## Face Recognition Script: detection.py

### Overview

The `detection.py` script is designed for real-time face recognition and attendance marking. It utilizes a pre-trained K-Nearest Neighbors classifier with the previously collected data. The script captures video feed from the webcam, detects faces, predicts identities, and marks attendance with a timestamp.

### Dependencies

- **OpenCV:** For webcam access and image processing.
- **Scikit-learn:** Utilizes the K-Nearest Neighbors classifier for face recognition.
- **Pickle:** Reads pre-collected facial data and labels from Pickle files.
- **CSV:** Manages attendance records through CSV file operations.
- **Datetime:** Obtains the current date and time for timestamping attendance.
- **Text-to-Speech (TTS):** Provides spoken notifications.

### Script Execution

1. **Webcam Initialization:**
   - Opens a connection to the default webcam (index 0).

2. **Classifier and Data Loading:**
   - Loads pre-trained face data and labels from Pickle files (`faces_dataset.pkl` and `names.pkl`).
   - Initializes a K-Nearest Neighbors classifier.

3. **Attendance Marking:**
   - Captures video frames from the webcam.
   - Detects faces using the Haar Cascade Classifier.
   - Predicts identities using the K-Nearest Neighbors classifier.
   - Marks attendance with the recognized identity, date, and timestamp.

4. **CSV File Handling:**
   - Checks for the presence of an attendance CSV file for the current date.
   - Appends or creates a new CSV file accordingly.
   - Records attendance information in the CSV file.

5. **User Interaction:**
   - Pressing 't' marks attendance and provides a spoken notification.
   - Pressing 'k' exits the script with a farewell spoken notification.

### Files Generated

- `data/faces_dataset.pkl`: Pickle file containing the collected facial data.
- `data/names.pkl`: Pickle file containing corresponding names.
- `attendence/attendence_DD-MM-YYYY.csv`: CSV file containing attendance records for the respective date.

### Notes on how to execute

- Both scripts are part of a facial recognition attendance system project.
- First run `image_collect.py` it prepares the data for the recognition script and make sure to check if files named `faces_dataset.pk` and `names.pkl` are generated in the `data` folder or not 
- Then run `detection.py` to mark attendance in real-time by pressing `t` on the keyboard and if you wish to quit before press `k`.
- Then check for the CSV file generated inside the `attendance` folder 

> # Feel free to use code Thank-you
