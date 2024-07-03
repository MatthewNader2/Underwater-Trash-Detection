import cv2
import os

def create_video_from_frames(frame_folder, output_path, fps=30):
    """
    Create a video from the processed frames.
    
    Parameters:
    frame_folder (str): Path to the folder containing processed frames.
    output_path (str): Path to save the output video.
    fps (int): Frames per second for the output video.
    """
    frame_files = [os.path.join(frame_folder, f) for f in sorted(os.listdir(frame_folder)) if f.endswith('.jpg')]
    frame = cv2.imread(frame_files[0])
    height, width, _ = frame.shape
    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))

    for frame_file in frame_files:
        frame = cv2.imread(frame_file)
        video.write(frame)

    video.release()
    print(f"Video created and saved to {output_path}")

if __name__ == "__main__":
    create_video_from_frames('images', 'output_video.mp4')
