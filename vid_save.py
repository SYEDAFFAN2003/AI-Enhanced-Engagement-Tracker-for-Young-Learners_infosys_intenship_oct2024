import cv2

# Try using DirectShow as the backend
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Could not open the video camera.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Write the frame to the video file
    out.write(frame)

    # Display the frame in a window
    cv2.imshow('Webcam', frame)

    # Print information about the frame
    print(f"Frame captured: {ret}, Frame shape: {frame.shape}")

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
