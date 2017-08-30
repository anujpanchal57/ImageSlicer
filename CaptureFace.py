import time
import cv2
import image_slicer

cv2.namedWindow("Sample")

# No. of frames to throw away while the camera adjusts to light levels
ramp_frames = 100

# VideoCapture(0) gets your default webcam
#(in this case, it is my laptop's webcam)
vc = cv2.VideoCapture(0)

# Captures a single img from camera and returns it
def get_img():
    # read() is the easiest way to capture a full img out of a VideoCapture Object
    return_value, im = vc.read()
    return im

# Some of the ramp_frames will be discarded and used only if necessary
for i in range(ramp_frames):
    temp = get_img()

# Gets the img that we want to store
vc_capture = get_img()

# Stores the image
file = "C:/Learning/Python/CaptureFace/Sample.png"

# Automatically chooses the correct format based on the file extension that you have
# provided above
cv2.imwrite(file, vc_capture)

# Slices the image according to the ("filename", Number of slices)
image_slicer.slice("Sample.png", 5)



# Closes the window as soon as the work is done
del(vc)


# tries to get the first frame on capture
# if vc.isOpened():
#     rval, frame = vc.read()
# else:
#     rval = False

# # This will do the work of showing a window thats it and name it as Sample
# while rval:
#     cv2.imshow("Sample", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exits when ESC is pressed as well as it takes a pic of yours
#         break

# After pressing ESC, it will capture an image from Webcam and store it as Sample.png
# and after all this it will exit from the window
# cv2.destroyWindow("Sample")