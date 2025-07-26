import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="Advanced Edge Detection", layout="wide")
st.title("🧠 Advanced Object Detection with Canny Edge & Contours")

st.markdown("""
Upload an image to analyze object boundaries using **Canny edge detection**, **grayscale transformation**, and **contour analysis**.
Use the sliders below to fine-tune detection sensitivity.
""")

min_val = st.slider("Canny: Min Threshold", 10, 300, 100)
max_val = st.slider("Canny: Max Threshold", 50, 500, 200)
min_area = st.slider("Minimum Object Area", 50, 10000, 500)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img = np.array(image.convert("RGB"))
    img = cv2.resize(img, (640, 800))

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_gray = clahe.apply(gray)

    blurred = cv2.GaussianBlur(enhanced_gray, (5, 5), 1)

    edges = cv2.Canny(blurred, threshold1=min_val, threshold2=max_val)

    kernel = np.ones((3, 3), np.uint8)
    closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    filtered = [(i, cv2.contourArea(c)) for i, c in enumerate(contours) if cv2.contourArea(c) > min_area]
    filtered.sort(key=lambda x: x[1], reverse=True)

    image_annotated = img.copy()

    for i, (idx, area) in enumerate(filtered, start=1):
        cnt = contours[idx]
        x, y, w, h = cv2.boundingRect(cnt)
        perimeter = cv2.arcLength(cnt, True)
        cv2.drawContours(image_annotated, [cnt], -1, (0, 255, 0), 2)
        cv2.rectangle(image_annotated, (x, y), (x + w, y + h), (255, 0, 0), 1)
        cv2.putText(image_annotated, f"#{i}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    st.subheader(f"✅ Objects Detected: {len(filtered)}")


    enhanced_rgb = cv2.cvtColor(enhanced_gray, cv2.COLOR_GRAY2RGB)
    edges_rgb = cv2.cvtColor(closed_edges, cv2.COLOR_GRAY2RGB)
    annotated_rgb = cv2.cvtColor(image_annotated, cv2.COLOR_BGR2RGB)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(img, caption="Original", use_column_width=True)
    with col2:
        st.image(enhanced_rgb, caption="Enhanced Grayscale", use_column_width=True)
    with col3:
        st.image(edges_rgb, caption="Edge Detection", use_column_width=True)
    with col4:
        st.image(annotated_rgb, caption="Contours & Objects", use_column_width=True)

    with st.expander("📊 Object Stats"):
        for i, (idx, area) in enumerate(filtered, start=1):
            perimeter = cv2.arcLength(contours[idx], True)
            st.write(f"Object #{i} ➤ Area: `{int(area)} px²`, Perimeter: `{int(perimeter)} px`")
