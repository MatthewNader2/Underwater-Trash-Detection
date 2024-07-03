import requests
import os
import cv2

def download_video(url, output_path):
    """
    Download video from the given URL and save it to the specified output path.
    
    Parameters:
    url (str): URL of the video to download.
    output_path (str): Local path where the video will be saved.
    """
    r = requests.get(url, allow_redirects=True)
    with open(output_path, 'wb') as file:
        file.write(r.content)
    print(f"Video downloaded and saved to {output_path}")

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
    video_url = 'https://player.vimeo.com/play/2532528922?s=535577674_1623629041_a6a680be078134b2b5834f7324d027d2&sid=64e0197edb8eb6b81b62b2bb2bf2c933f5ade0e11623618241&oauth2_token_id=&download=1'
    video_path = 'video.mp4'
    
    download_video(video_url, video_path)
    create_directories()
    cut_video_into_frames(video_path)
