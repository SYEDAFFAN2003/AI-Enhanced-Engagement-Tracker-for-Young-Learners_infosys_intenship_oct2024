AI-Enhanced-Engagement-Tracker-for-Young-Learners_infosys_intenship_oct2024

## Image Processing

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **NumPy**: For array manipulation

### Developed Logics:

#### A) `image_concatenation`
This function resizes two images to a specified pixel range and combines them both horizontally and vertically. The results are displayed in separate windows.

- **Input:**

  ![Image 1](https://github.com/user-attachments/assets/def5004a-cd57-4a19-9721-ac6e9c2b1f39)
  
  ![Image 2](https://github.com/user-attachments/assets/83b09ad4-d964-4f79-8cfd-0e287c180604)

- **Output:**

  ![Concatenated Image](https://github.com/user-attachments/assets/5bfdbc56-7f86-4f11-8af8-a245bb72787a)

#### B) `image_contour`
This detects contours in a grayscale image using a binary threshold and `cv2.findContours()`. The contours are drawn onto the original image in green.

- **Input:**

  ![Image 1](https://github.com/user-attachments/assets/a9a0bf8b-d49f-4544-83b2-c4928b3cadad)

- **Output:**

  ![Contoured Image](https://github.com/user-attachments/assets/f358e843-f3a0-460d-89be-29415a6b6361)

#### C) `image_crop`
This function extracts a specific region of an image based on pixel range and displays the cropped section.

- **Input:**
 
  ![Image 2](https://github.com/user-attachments/assets/73ac45ba-c582-41c4-bc64-bb676fb03ee6)

- **Output:**
 
  ![Cropped Image](https://github.com/user-attachments/assets/869d7954-38cc-48c4-85d2-eb36f91a6dcc)

#### D) `image_dilation & erosion`
This function applies morphological operations, dilation and erosion, to enhance and reduce features in an image, respectively.

- **Input:**
 
  ![Image 1](https://github.com/user-attachments/assets/56bac27b-1030-4214-bb4b-98410044474f)

- **Output:**

  ![Dilated and Eroded Image](https://github.com/user-attachments/assets/7ad6f206-45bd-44c3-934a-f93257777c38)

#### E) `image_edge_detection`
This applies the Canny edge detection algorithm to detect edges in a grayscale image.

- **Input:**
 
  ![Image 1](https://github.com/user-attachments/assets/f5396844-9c99-4fa8-8ffd-0b8bcfdbb126)

- **Output:**
 
  ![Edge Detected Image](https://github.com/user-attachments/assets/979c708c-63e2-4fb2-bec0-24b87a9d8259)

#### F) `image_histogram_equalization`
This enhances the contrast of a grayscale image using histogram equalization.

- **Input:**

  ![Image 2](https://github.com/user-attachments/assets/8c328a4b-f195-43b7-be73-4dd1163514e2)

- **Output:**
 
  ![Histogram Equalized Image](https://github.com/user-attachments/assets/bc26db27-1cee-4a85-a7d5-8fce5286a190)

#### G) `image_hsv`
This converts a color image from the BGR color space to HSV.

- **Input:**

  ![Image 2](https://github.com/user-attachments/assets/5479802e-f49e-4fa5-b71a-aadcd2e99669)

- **Output:**
 
  ![HSV Image](https://github.com/user-attachments/assets/8f41752f-f210-4628-b18f-8104f28da96e)

#### H) `image_morphological_transformation`
This applies opening and closing morphological operations to a grayscale image to remove noise and fill gaps.

- **Input:**

  ![Image 1](https://github.com/user-attachments/assets/fbb6e46f-8dfa-4e38-981e-3c856064fd8f)

- **Output:**
 
  ![Morphologically Transformed Image](https://github.com/user-attachments/assets/3d8d9970-5f23-4848-afdc-ec744d9339b5)

#### I) `image_resize`
This resizes an image to specified dimensions.

- **Input:**
 
  ![Image 1](https://github.com/user-attachments/assets/701c01c1-17fe-408e-b030-6113d813aa02)

- **Output:**
 
  ![Resized Image](https://github.com/user-attachments/assets/fcb29fb6-e559-4b00-b56e-27c0667ea6dc)

#### J) `image_rgb2gray`
This converts a color image to grayscale.

- **Input:**

  ![Image 2](https://github.com/user-attachments/assets/bb3ec4c2-fe8c-43fd-9d54-14ce6f897cef)

- **Output:**
 
  ![Grayscale Image](https://github.com/user-attachments/assets/fcf4a4c2-bda8-48bf-b729-9db743544b74)

#### K) `image_rotate`
This rotates an image by 90 degrees around its center.

- **Input:**

  ![Image 2](https://github.com/user-attachments/assets/ff931e78-37ad-40d6-a0df-67d37aa092af)

- **Output:**

  ![Rotated Image](https://github.com/user-attachments/assets/35d20bb4-ab51-464d-bd1e-4d295f5c50c0)

#### L) `image_blur`
This applies a Gaussian blur to an image to reduce noise and detail.

- **Input:**

  ![Image 1](https://github.com/user-attachments/assets/9052a6fe-fe8e-41f8-a078-6928d5ae0f32)

- **Output:**
 
  ![Blurred Image](https://github.com/user-attachments/assets/a0cfade1-69db-48ae-a533-c7512a78e4cc)

#### M) `image_noise_removal & closing_gaps`
This function removes noise and fills gaps using morphological operations.

#### N) `image_template`
This function performs template matching to locate a template image within a larger image.

## Video Processing

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84

### Developed Logics:

#### A) `Video_multivideo`
This function reads and displays images from a specified folder, printing the dimensions of each image.

#### B) `Video_fps`
This function captures video from the webcam, displays it in real-time, and calculates the FPS.

#### C) `Video_save`
This function captures live video and saves it to a specified output file.

#### D) `Video_stack`
This function reads and resizes two video files, concatenating them horizontally.

#### E) `Video_stream`
This function captures live video from the webcam and displays it in real-time.

## Annotations

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6

### Developed Logics:

#### A) `data_segregate`
This function organizes images and their label files into matched and unmatched directories.

- **Input:**

![Screenshot 2024-11-13 174954](https://github.com/user-attachments/assets/828040b2-4b34-4355-b577-76b9beed0a9c)

- **Output:**

![Screenshot 2024-11-13 174816](https://github.com/user-attachments/assets/b46cc9cd-5c16-4df3-a950-4211bd1087e7)

#### B) `label`
This function draws bounding boxes on images based on annotations in the label files.

- **Input:**

![gun4](https://github.com/user-attachments/assets/ccba6a57-2506-4524-9c24-f384a5b248fa)

- **Output:**

![gun4](https://github.com/user-attachments/assets/71dba9a6-37ac-4bcd-aa4f-74e589bcfd09)

#### C) `label_manipulate`
This function updates class numbers in label files for object detection tasks.

- **Input:**

![Screenshot 2024-11-13 174620](https://github.com/user-attachments/assets/20cbc002-8864-42e5-9ad9-f64203421d26)

- **Output:**

![Screenshot 2024-11-13 174644](https://github.com/user-attachments/assets/1e71f3f6-cee9-45e7-bca6-eac2f35e6822)

## Face Recognition

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

### Developed Logics:

#### A) `Face_recognition`
This performs real-time face recognition to identify whether the person in live video frames a known image by comparing. His name is displayed if He/She is recognized; otherwise, "Not He/She" appears.

- **Input:**
![AFFAN PHOTO](https://github.com/user-attachments/assets/d08e93cb-80e1-4ccc-a8d4-2154c0243ceb)



- **Output:**
![Screenshot 2024-11-10 144914](https://github.com/user-attachments/assets/24770ef0-4c73-43f5-965e-d585e703766b)



#### B) `Attendence_save`
Using a live video stream, this performs real-time face recognition to identify He/She. When He/She's face is recognized, his/her name is displayed on the video feed, and the recognition event is logged with the date and time in an Excel file. After every 5 recognitions, the current log is saved to an Excel file, and the recognition counter and DataFrame are reset.

- **Input:**
![AFFAN PHOTO](https://github.com/user-attachments/assets/d08e93cb-80e1-4ccc-a8d4-2154c0243ceb)


- **Output:**
![Screenshot 2024-11-10 161459](https://github.com/user-attachments/assets/e16d4c67-8b66-451a-b044-a8fd3713f72f)

![test](https://github.com/user-attachments/assets/501dfb03-6960-46f7-a44a-4e54bed6f488)


#### C) `test`
This performs real-time face recognition to identify He/She in a live video feed, logging each recognition event with the date and time into an Excel file every 30 seconds. It tracks recognition intervals to avoid duplicate entries and displays He/She or "Not He/She" based on identification.

- **Input:**
![AFFAN PHOTO](https://github.com/user-attachments/assets/d08e93cb-80e1-4ccc-a8d4-2154c0243ceb)


- **Output:**
![Screenshot 2024-11-10 161459](https://github.com/user-attachments/assets/3b1bc79a-2649-4975-844b-59aff260c55c)

![test](https://github.com/user-attachments/assets/493c435f-26cb-409f-9cdc-fc9c7e7260c8)


#### D) `tools`
This performs real-time face recognition using the live camera feed to identify He/She. Each time a face is recognized, it records the name, date, and time in a data frame. Once a recognition count of 5 is reached, it saves the records to an Excel file, then resets the counter and DataFrame. It displays "He/She's name" or "Not He/She's name" over the video feed, and pressing 'q' exits the program with a final save of any remaining records.

- **Input:**
![AFFAN PHOTO](https://github.com/user-attachments/assets/d08e93cb-80e1-4ccc-a8d4-2154c0243ceb)


- **Output:**
![Screenshot 2024-11-10 164351](https://github.com/user-attachments/assets/afcf3142-4a19-48b9-a4af-404849101053)

![tool](https://github.com/user-attachments/assets/24cd5ba0-296e-4621-aa10-c9743f7d9adb)



#### E) `excel_sc`
This is for face recognition with time-based logging looks well-structured and includes the logic to save screenshots and log attendance into an Excel file.

1. **Efficiency**: Resizing frames to 640x480 is good for speed. You can reduce the size further if needed.
2. **File Saving**: Screenshots are saved in `"Teja_screenshots(5)"`, and Excel is updated every 30 seconds.
3. **Recognition Timings**: Logs every 30 seconds for the same person and logs every 5 minutes to avoid multiple entries in short time frames.
4. **Error Handling**: Proper `try-except` block for handling errors.
5. **Termination**: Exits when the 'q' key is pressed.

- **Input:**
![AFFAN PHOTO](https://github.com/user-attachments/assets/d08e93cb-80e1-4ccc-a8d4-2154c0243ceb)


- **Output:**
![SYED_AFFAN_2024-11-10_14-39-16](https://github.com/user-attachments/assets/e7b67018-c6da-4d0a-aeaa-9367533e7e46)

![excel sc](https://github.com/user-attachments/assets/7a19ff03-21c0-4d62-8ecb-3e3904399ac0)


#### F) `excel_sc_dt`
This uses OpenCV and `face_recognition` to detect and recognize a specific face (His/Her's) from a webcam feed. Upon recognition, a screenshot is saved, and the attendance (name, date, time, screenshot path) is logged into an Excel file. The script processes every second frame, saves data every 30 seconds, and ensures attendance is only logged every 5 minutes for the same person. The attendance data is stored in a DataFrame and periodically exported to an Excel file.

Key Features:
- Real-time face detection and recognition
- Saves screenshots with timestamp
- Logs attendance to Excel every 30 seconds
- Avoids multiple logs within a 5-minute interval for the same person

- **Input:**
![AFFAN PHOTO](https://github.com/user-attachments/assets/d08e93cb-80e1-4ccc-a8d4-2154c0243ceb)


- **Output:**
![SYED_AFFAN_2024-11-10_12-57-34](https://github.com/user-attachments/assets/158e5382-182e-416f-bde4-852303cbcd67)

![excel sc dt](https://github.com/user-attachments/assets/508a6ddc-c039-4f6c-a7e8-e6403475fa0e)


#### G) `landmark`
This code is a face recognition and attentiveness tracking system that operates in real time. Key functions include:

1. **Face Recognition**: Detects and recognizes "His/Her's face" from the camera using a pre-loaded image.
2. **Attentiveness Detection**: Uses facial landmarks and head pose estimation to assess if the subject is attentive.
3. **Logging**: Records each recognition event with a timestamp, attentiveness status, and screenshot in an Excel file, saving every 30 seconds.
4. **Live Feedback**: Displays "Attentive" or "Not Attentive" on the video feed along with facial landmarks.

The system continues until you press 'q' to exit.

- **Input:**
![AFFAN PHOTO](https://github.com/user-attachments/assets/d08e93cb-80e1-4ccc-a8d4-2154c0243ceb)


- **Output:**
![SYED AFFAN_2024-11-10_15-03-09](https://github.com/user-attachments/assets/297f4e56-afb6-423f-a041-c926810717be)

![land mark](https://github.com/user-attachments/assets/91910f28-a24f-41e3-8053-c3e0b4acd3bc)


#### H) `atten_score`
This script captures real-time webcam video to recognize "His/Her's face" and assess attentiveness based on head pose:

1. **Setup**: Loads His/Her's face data and initializes detectors.
2. **Face Recognition**: Compares detected faces with the known face, identifying if it's a match.
3. **Attentiveness Check**: Estimates head orientation (yaw/pitch) to compute an attentiveness score.
4. **Logging**: Logs details (name, date, time, attentiveness, screenshot) in an Excel file every 30 seconds if attentive.
5. **Display**: Shows video with face labels, attentiveness status, and facial landmarks. 

Exits on 'q' press, ensuring the final save to Excel.

- **Input:**
![AFFAN PHOTO](https://github.com/user-attachments/assets/d08e93cb-80e1-4ccc-a8d4-2154c0243ceb)

- **Output:**
![SYED AFFAN_2024-11-10_12-11-59](https://github.com/user-attachments/assets/ff7fedea-9966-47f8-9103-4449a4765104)

![avg score](https://github.com/user-attachments/assets/42aa0e16-b724-4327-b120-ceecd48e906c)


#### I) `avg_atten_score`
This captures webcam video, performs face recognition for "His/Her's face," calculates attentiveness based on the head pose, and logs the data into an Excel file every 30 seconds. Here is a summary of its key actions:

1. **Face Recognition**: Uses `face_recognition` to identify "His/Her's face" by comparing face encodings.
2. **Head Pose Detection**: Calculates the head pose (yaw, pitch) using `dlib`'s facial landmark predictor to assess attentiveness.
3. **Attentiveness Calculation**: Computes an attentiveness score based on yaw and pitch, with values between 0 (not attentive) and 1 (fully attentive).
4. **Logging**: Every 30 seconds, the script saves recognized face data (name, date, time, attentiveness, attention score, and screenshot) into an Excel file.
5. **Display and Feedback**: Shows real-time video with facial landmarks, attentiveness status, and face bounding boxes.

The final output includes an Excel file with logged details and an average attentiveness score at the end of the session. The user can stop the video stream by pressing 'q'.

- **Input:**
![AFFAN PHOTO](https://github.com/user-attachments/assets/d08e93cb-80e1-4ccc-a8d4-2154c0243ceb)


- **Output:**
![SYED AFFAN_2024-11-10_12-35-55](https://github.com/user-attachments/assets/cef55519-74d9-484d-8d36-cc3686218cbb)

![att score](https://github.com/user-attachments/assets/3111b379-ba4d-42be-b277-76fb1ad19f29)

