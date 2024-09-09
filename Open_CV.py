import cv2
import matplotlib.pyplot as plt

# Check OpenCV version
print("OpenCV version:", cv2.__version__)


# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 is typically the default camera

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set a window name
window_name = "Camera"

# Create a loop to keep the camera open until you take a picture
while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # If the frame was captured correctly
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the resulting frame
    cv2.imshow(window_name, frame)

    # Wait for user input to take a picture or quit
    key = cv2.waitKey(1)

    # Press 's' to save the picture
    if key == ord('s'):
        # Define the filename and save the image
        image_name = "captured_image_0.png"
        cv2.imwrite(image_name, frame,[cv2.IMWRITE_JPEG_QUALITY, 90])
        print(f"Picture saved as {image_name}")
    
    # Press 'q' to quit the camera
    elif key == ord('q'):
        break

# When everything is done, release the camera and close the window
camera.release()
cv2.destroyAllWindows()


# Loop to load and display images
for i in range(0, 22):
    # Load the image in grayscale mode
    img = cv2.imread(f"captured_image_{i}.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
    
    # Check if the image is loaded correctly
    if img is None:
        print(f"Image captured_image_{i}.png not loaded correctly!")
    else:
        if i % 2 == 0:
            # Display the image using OpenCV in grayscale mode
            cv2.imshow(f"Image {i}", img)
            cv2.waitKey(2000)  # Display each image for 2 seconds
            cv2.destroyAllWindows()  # Close the OpenCV window before proceeding
            print(f"Image {i} shape (grayscale):", img.shape)
        else:
            # Re-load the image in color mode for odd indices
            img_color = cv2.imread(f"captured_image_{i}.png", cv2.IMREAD_REDUCED_COLOR_4)
            
            if img_color is None:
                print(f"Image captured_image_{i}.png not loaded correctly in color!")
            else:
                # Display the image using OpenCV in color mode
                cv2.imshow(f"Image {i}", img_color)
                cv2.waitKey(2000)  # Display each image for 2 seconds
                cv2.destroyAllWindows()  # Close the OpenCV window before proceeding
                print(f"Image {i} shape (color):", img_color.shape)

        # Optionally display the image using Matplotlib
        # Uncomment the following lines if you want to use Matplotlib
        # plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))  # Convert grayscale to RGB for display
        # plt.title(f"Image {i}")
        # plt.show()
        # plt.close()  # Close the Matplotlib plot after displaying it

# Print the shape of the last successfully loaded image
if img is not None:
    print("Last image shape:", img.shape)
