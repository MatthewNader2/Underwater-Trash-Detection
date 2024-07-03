import cv2
import math
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# Azure credentials and project details
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
prediction_key = "YOUR_PREDICTION_KEY"
project_id = "55ea2262-3a09-4d16-9559-8171daf00c25"
iteration_name = "Iteration1"

credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials)

def detect_trash_in_frame(frame_path, output_path):
    """
    Detect trash in a given frame using the custom vision service and save the output with bounding boxes.
    
    Parameters:
    frame_path (str): Path to the input frame image.
    output_path (str): Path to save the output frame image with bounding boxes.
    """
    with open(frame_path, "rb") as image_data:
        results = predictor.detect_image(project_id, iteration_name, image_data)

    image = cv2.imread(frame_path)
    for prediction in results.predictions:
        if prediction.probability > 0.5:
            box = prediction.bounding_box
            h, w, _ = image.shape
            start_point = (math.floor(box.left * w), math.floor(box.top * h))
            end_point = (math.floor((box.left + box.width) * w), math.floor((box.top + box.height) * h))
            color = (255, 0, 0)
            thickness = 2
            image = cv2.rectangle(image, start_point, end_point, color, thickness)

    cv2.imwrite(output_path, image)
    print(f"Processed frame saved to {output_path}")

if __name__ == "__main__":
    if not os.path.exists('images'):
        os.makedirs('images')
    for count in range(len(os.listdir('buffers'))):
        input_frame = f"buffers/buffer{count}.jpg"
        output_frame = f"images/{count}.jpg"
        detect_trash_in_frame(input_frame, output_frame)
