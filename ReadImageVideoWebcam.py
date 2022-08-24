import cv2

# # Read the Image
# img = cv2.imread("Resources/lenna.jpg")
# # Display the Image
# cv2.imshow("lenna",img)
# # Halting the Image untill User intervention
# cv2.waitKey(0)

frameWidth = 640
frameHeight = 360

# Read mp4 videos
# Capturing Device
# cap = cv2.VideoCapture("Resources/paradise.mp4")

# while True:
#     success,img = cap.read()
#     img = cv2.resize(img,(frameWidth,frameHeight))
#     cv2.imshow("Video",img)
      
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Read the Video



cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

while True:
    success,img = cap.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break