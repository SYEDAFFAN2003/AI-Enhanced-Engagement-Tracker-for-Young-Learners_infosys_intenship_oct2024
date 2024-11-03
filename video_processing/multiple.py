import cv2
import os

# Use double backslashes for Windows paths or raw strings
folder_path = "C:/Users/syeda/Downloads/th/"

if not os.path.exists(folder_path):
    print(f"The folder path '{folder_path}' does not exist.")
else:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Load the image
        image = cv2.imread(file_path)

        if image is not None:
            # Display the image
            cv2.imshow('Image', image)

            # Wait for the user to press any key before closing the window
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Print the dimensions of the image
            print(f"{filename} dimensions: {image.shape}")
        else:
            print(f"Failed to load {filename}")
