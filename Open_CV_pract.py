import cv2

camera = cv2.VideoCapture(0)
window_name = "Camera"
image_name = "First_Pic.png"

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error")
        break

    # Display the camera feed
    cv2.imshow(window_name, frame)

    key = cv2.waitKey(1)

    # Save the image if 's' is pressed
    if key == ord('s'):
        # Save the current frame
        cv2.imwrite(image_name, frame)
        print(f"Image saved as {image_name}")

    # Show the saved image and split channels if 'q' is pressed
    elif key == ord('q'):
        # Load the saved image
        saved_img = cv2.imread(image_name)

        if saved_img is not None:
            # Show the loaded image
            cv2.imshow("Saved Image", saved_img)

            # Split and show the color channels
            B, G, R = cv2.split(saved_img)
            cv2.imshow("Blue Channel", B)
            cv2.imshow("Red Channel", R)
            cv2.imshow("Green Channel", G)

            # Load the two images to blend
            img1 = cv2.imread("image1.jpg")# 225x224
            img2 = cv2.imread("image2.jpg")#306x165
            
            
            
            # Check if both images exist
            if img1 is not None and img2 is not None:
                img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
                
                # Blend the images
                image_sum = cv2.addWeighted(img1, 0.5, img2, 0.1, 0)
                cv2.imshow("Blended Image", image_sum)
                image_sub=cv2.subtract(img1,img2)
                cv2.imshow("Subtracted Image",image_sub)

                bit_img= cv2.bitwise_not(img1,img2)
                cv2.imshow("Bitwise Image",bit_img)
                
                
            else:
                print("One or both of the images 'image1.jpg' or 'image2.jpg' were not found.")

            cv2.waitKey(0)  # Wait for a key press to close the image windows
        else:
            print("Failed to load saved image.")

        break

    # Exit the program if 'c' is pressed
    elif key == ord('c'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
