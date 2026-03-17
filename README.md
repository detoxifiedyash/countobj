Advanced Object Detection with Canny Edges & Contours - Streamlit App
🚀 Overview
This interactive Streamlit web application demonstrates advanced object detection using Canny edge detection, Gaussian blur, and contour analysis—all powered by Python and OpenCV. Effortlessly upload your images, adjust detection thresholds, and visualize objects with bounding boxes and detailed statistics—all in real-time.

🖼 Features
Image Upload: Load your own images for instant processing.

Preprocessing: Convert to grayscale and denoise with Gaussian Blur for optimal edge detection.

Canny Edge Detection: Set lower and upper thresholds interactively to control sensitivity.

Contour Analysis: Detect, draw, and number objects using external contour extraction.

Area-Based Filtering: Use an intuitive slider to filter detected objects by area.

Real-Time Visualization: View side-by-side comparisons of original, edge, and result images.

Object Statistics: See the total object count and bounding box area stats instantly.

📚 Tech Stack
Python 3.x

OpenCV (cv2)

Streamlit

PIL (Pillow)

NumPy
0

🌟 Use Cases
Learning and teaching computer vision fundamentals.

Demonstrating image preprocessing and real-time UI tuning.

Quick prototyping for edge- and contour-based object detection.

🔧 Installation

bash
pip install -r requirements.txt
Run the app:

bash
streamlit run app.py
🕹 Usage
Open the Streamlit app in your browser (usually at http://localhost:8501).

Upload an image via the sidebar.

Adjust the Canny thresholds and minimum object area slider.

View the detected objects and their bounding boxes in real-time.

📊 Demo
[Insert animated GIF or screenshot here showing app functionality]

📝 Example Workflow
Step 1: Upload your image.

Step 2: Fine-tune both the Canny edge thresholds for sharp feature extraction.

Step 3: Adjust the area slider to filter out noise or tiny objects.

Step 4: Instantly see contour-detected objects with numbered bounding boxes and stats.

💡 How It Works
Preprocessing: The input image is converted to grayscale and optionally denoised.

Edge Detection: Canny algorithm identifies significant edges.

Contour Detection: External contours are extracted and filtered by area.

Visualization: Objects are labeled and statistics displayed for user interpretation.

📂 Project Structure
text
object-detection-streamlit/
├── app.py
├── requirements.txt
├── README.md
└── assets/
    └── demo.gif (or .png)
🤝 Contributing
Pull requests, issues, and feature suggestions are welcome!
