🫁 Covid Chest X-ray Classification

This project is a Deep Learning application for COVID-19 detection from Chest X-ray images using convolutional neural networks (CNNs).
The system supports training, evaluation, and inference with pre-trained models.

⚙️ Requirements

Python 3.9 – 3.11

Git

Git LFS (required for large model files)

Install Python libraries
pip install -r requirements.txt

🔧 Important: Configure Paths After Downloading

⚠️ You MUST update file paths after cloning the project, because absolute paths depend on your local machine.

🖼️ Example: Fix Image Path in GUI (test.py)
❌ Original (example path on author’s machine)
Image.open("C:/Users/TGDD/Downloads/1.png")

✅ Replace with relative path (recommended)
Image.open("assets/1.png")


Or use dynamic project root:

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "..", "assets", "1.png")
Image.open(image_path)

📂 Example: Fix Dataset Path (train.py)
❌ Hard-coded path
train_dir = "F:/Covid Chest-Xray/split_data/train"

✅ Change to your local folder
train_dir = "YOUR_PROJECT_PATH/split_data/train"
val_dir   = "YOUR_PROJECT_PATH/split_data/val"
test_dir  = "YOUR_PROJECT_PATH/split_data/test"


📌 Tip: Use relative paths whenever possible:

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "split_data")

▶️ How to Train the Model
cd code
python train.py


The trained model will be saved into:

model/

🧪 How to Run the Application (GUI / Prediction)
cd code
python test.py


📌 Make sure:

Model files exist in model/

Image paths are correctly updated

🗃️ Large Model Files (Git LFS)

This repository uses Git Large File Storage (LFS) for .keras model files.

Install Git LFS
git lfs install

Download models correctly
git lfs pull

🧠 Models Used

DenseNet121

VGG16 (Modified Last Layers)

Both models are fine-tuned for medical image classification.

⚠️ Common Issues
❌ FileNotFoundError

✔️ Check and update file paths
✔️ Do not use absolute paths from another machine

❌ Model not loading

✔️ Run git lfs pull
✔️ Ensure .keras files exist in model/

📄 License

This project is for educational and research purposes only.

✨ Author

Nguyễn Văn Khánh
AI / Deep Learning Student
