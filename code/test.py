import tensorflow as tf
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

MODEL_PATHS = {
    "VGG16": r"F:\Covid Chest-Xray\model\vgg16_modify_last_state.keras",
    "DenseNet121": r"F:\Covid Chest-Xray\model\dense_net121.keras"
}
LABELS = {0: "covid", 1: "normal"}


models = {
    "VGG16": tf.keras.models.load_model(MODEL_PATHS["VGG16"]),
    "DenseNet121": tf.keras.models.load_model(MODEL_PATHS["DenseNet121"])
}

def load_img_to_predict(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    return img.reshape(1, 224, 224, 3)

def predict_image(img_path, model):
    img = load_img_to_predict(img_path)
    output = model.predict(img, verbose=0)[0, 0]
    index = int(np.round(output))
    return output, LABELS[index]

class CovidPredictApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID Chest X-ray Detection")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.bg_img = Image.open("C:/Users/TGDD/Downloads/1.jpg").resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0)

        self.user_image_label = None
        self.result_label = None
        self.model_type = tk.StringVar(value="VGG16")

        self.model_menu = tk.OptionMenu(root, self.model_type, "VGG16", "DenseNet121")
        self.model_menu.config(font=("Helvetica", 11, "bold"), bg="#ffffff", bd=2)
        self.model_menu.place(x=620, y=20)

       
        self.choose_button = tk.Button(
            root,
            text="Chọn ảnh X-ray",
            font=("Helvetica Neue", 14, "bold"),
            bg="#000000",
            fg="#FFFFFF",
            activebackground="#333333",
            activeforeground="#FFFFFF",
            relief="raised",
            bd=3,
            width=20,
            command=self.choose_image
        )
        self.choose_button.place(x=300, y=550)

      
        self.reset_button = tk.Button(
            root,
            text="↩ Quay lại",
            font=("Helvetica Neue", 12, "bold"),
            bg="#000000",
            fg="#FFFFFF",
            activebackground="#333333",
            activeforeground="#FFFFFF",
            relief="raised",
            bd=3,
            width=12,
            command=self.reset_interface
        )
        self.reset_button.place(x=50, y=550)
        self.reset_button.place_forget()

    def choose_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if not file_path:
            return
        try:
            model_name = self.model_type.get()
            model = models[model_name]

           
            image_cv = cv2.imread(file_path)
            image_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
            image_pil = Image.fromarray(image_rgb).resize((300, 300))
            photo = ImageTk.PhotoImage(image_pil)

            if self.user_image_label:
                self.user_image_label.destroy()
            self.user_image_label = tk.Label(self.root, image=photo, bg="white", bd=4, relief="solid")
            self.user_image_label.image = photo
            self.user_image_label.place(x=250, y=180)

      
            prob, label_result = predict_image(file_path, model)
            result_text = f"[{model_name}] KẾT QUẢ: {label_result.upper()} (Probability: {prob:.4f})"

            if self.result_label:
                self.result_label.destroy()
            self.result_label = tk.Label(
                self.root, text=result_text,
                font=("Helvetica", 16, "bold"),
                bg="white", fg="black", padx=10, pady=5,
                borderwidth=2, relief="solid"
            )
            self.result_label.place(relx=0.5, y=500, anchor="center")

            self.bg_label.place_forget()

     
            self.choose_button.config(
                text=" Chọn ảnh X-ray tiếp",
                font=("Helvetica", 12, "bold"),
                bg="white", fg="black",
                activebackground="white",
                activeforeground="black",
                relief="solid", bd=1
            )
            self.reset_button.place(x=50, y=550)

        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xử lý ảnh:\n{e}")

    def reset_interface(self):
        if self.user_image_label:
            self.user_image_label.destroy()
            self.user_image_label = None
        if self.result_label:
            self.result_label.destroy()
            self.result_label = None
        self.bg_label.place(x=0, y=0)
        self.reset_button.place_forget()
        self.choose_button.config(
            text="Chọn ảnh X-ray",
            font=("Helvetica Neue", 14, "bold"),
            bg="#000000", fg="#FFFFFF",
            activebackground="#333333",
            activeforeground="#FFFFFF",
            relief="raised", bd=3
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = CovidPredictApp(root)
    root.mainloop()
