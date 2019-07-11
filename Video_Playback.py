import cv2 # Import libraries

# Define function for wait key / delay
# Case1: Delay true is for playing video when no button (p = pause, b = back) is pressed
# Case2: Delay false is for wait keys during button operations
def waitKey(delay = False, fps=10):
    if delay == True:
        key = cv2.waitKey(int(1000 / fps)) & 0xff # Control wait key with given fps, for Case 1
    else:
        key = cv2.waitKey(1) & 0xff # For Case 2
    return key


def play_video(video_file_path = False, fps = 100, width=800, height=500, monochrome=False):
    if video_file_path == False: # Error handling: No input video path
        print("Error: Video file not found!")
        exit()

    cap = cv2.VideoCapture(video_file_path) # Extract video with given input path

    while True:

        ret, frame = cap.read() # Extract current frame from video
        key1 = waitKey(True, fps) # Wait key Case 1

        if not ret:
            break

        if monochrome == True: # Control monochrome operation
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        resized_frame = cv2.resize(frame, (width, height), fx=0, fy=0, interpolation=cv2.INTER_CUBIC) # Resize resolution
        flag = False
        if key1 == ord('p'): # If pause button is pressed
            while True:

                key2 = waitKey() # Wait key Case 2
                cv2.imshow('Video', resized_frame) # Show current frame

                if key2 == ord('p'): # If pause is released
                    break

                if key2 == ord('q'): # If quit button is pressed while pasue button is active
                    exit()

                if key2 == ord('b'): # If back button (Back Frame) is pressed while pause button is active
                    while True:
                        key3 = waitKey()
                        cv2.imshow('Video', previous_frame) # Show previous frame
                        if key3 == ord('p'):
                            flag = True
                            break

                        if key3 == ord('q'): # If quit button is pressed while previous frame is active
                            exit()

                if flag == True: # If pause is released when previous frame is active
                     break

        cv2.imshow('Video', resized_frame) # Case 1, show current frame when no button is pressed
        previous_frame = resized_frame # Assign previous frame

        if key1 == ord('q'):
            break # If quit is pressed during Case 1

    cap.release() # Release capture
    cv2.destroyAllWindows() # Close all windows at the end

if __name__ == "__main__": # Main function to check above function

    video_file_path = 'video_2.mp4' # Define input video path
    fps = 50 # Define frames per second
    width = 800 # Define output window width
    height = 400 # Define output window height
    monochrome = False # Control monochrome, true / false, if true then output will be grayscale

    play_video(video_file_path, fps, width, height, monochrome) # test function