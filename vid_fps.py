import cv2
import time

# Open the webcam with DirectShow backend
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open the video camera.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

prev_frame_time = 0
new_frame_time = 0

while True:
    new_frame_time = time.time()
  
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    out.write(frame)

    # Calculate FPS
    fps = 1 / (new_frame_time - prev_frame_time) if (new_frame_time - prev_frame_time) > 0 else 0
    prev_frame_time = new_frame_time

    # Put FPS text on the frame
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame in a window
    cv2.imshow('Webcam', frame)

    # Print FPS to the console
    print(f"FPS: {int(fps)}")

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
