import os
import cv2

def create_directories():
    """
    Create necessary directories for storing buffers and images.
    """
    os.makedirs('buffers', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    print("Directories 'buffers' and 'images' created")

def cut_video_into_frames(video_path):
    """
    Cut the video into frames and save each frame as an image in the buffers directory.
    
    Parameters:
    video_path (str): Path to the video file to be cut into frames.
    """
    cap = cv2.VideoCapture(video_path)
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"buffers/buffer{count}.jpg", frame)
        count += 1
    print(f"Video cut into {count} frames and saved to 'buffers' directory")

if __name__ == "__main__":
    create_directories()
    cut_video_into_frames('video.mp4')
