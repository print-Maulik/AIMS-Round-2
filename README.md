# Scene Localization via Natural Language Queries

This project implements a deep learning system that can localize a specific scene region within a dense image, based on a natural language query.  
It combines **ResNet50** (for visual feature extraction) and **GloVe embeddings** (for textual feature representation) in TensorFlow/Keras.

---

## 📌 Features
- **Image encoder:** Pre-trained ResNet50 for robust visual feature extraction.
- **Text encoder:** GloVe embeddings for semantic understanding of natural language queries.
- **Multimodal fusion:** Concatenates visual and textual embeddings for joint reasoning.
- **Localization output:** Predicts bounding box coordinates for the described object/region.
- **Evaluation metric:** Mean IoU (Intersection over Union) to measure localization accuracy.

---

## 📂 Dataset
- **Name:** Flickr30k Entities
- **Images:** High-resolution, multi-object images.
- **Annotations:** Bounding boxes + natural language phrases referring to them.

---

## 🏗 Model Architecture
1. **Image Branch:**  
   - Input: Cropped image region.  
   - Model: ResNet50 (pretrained on ImageNet, without top layer).  
   - Output: 2048-dimensional visual embedding.

2. **Text Branch:**  
   - Input: Tokenized natural language query.  
   - Embedding: Pre-trained GloVe vectors (300D).  
   - Output: 300-dimensional text embedding.

3. **Fusion & Prediction:**  
   - Concatenate visual & text embeddings.  
   - Dense layers with dropout.  
   - Output: 4 bounding box coordinates `(x_min, y_min, x_max, y_max)`.

---

## 📊 Results
- **Mean IoU:** 0.309  
- Interpretation: On average, the predicted bounding box overlaps about 31% with the ground truth box.  
- Performance can improve with:
  - Larger dataset
  - Data augmentation
  - More advanced multimodal fusion techniques

---

## 🚀 How to Run
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/scene-localization.git
cd scene-localization

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download dataset (Flickr30k Entities)
# Place in ./data/ directory

# 4. Train the model
python train.py

# 5. Evaluate the model
python evaluate.py
