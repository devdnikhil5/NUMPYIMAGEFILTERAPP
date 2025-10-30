import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.ndimage import convolve


class ImageFilterApp:
    def __init__(self, root):  # ✅ FIXED
        self.root = root
        self.root.title("NumPy Image Filter App")
        self.root.geometry("950x650")
        self.root.configure(bg="#f4f6f8")

        self.img_array = None

        # Matplotlib Figure
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Buttons
        tk.Button(root, text="Load Image", command=self.load_image,
                  bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                  relief="raised", padx=10, pady=5).pack(pady=8)

        btn_frame = tk.Frame(root, bg="#f4f6f8")
        btn_frame.pack()

        buttons = [
            ("Grayscale", self.grayscale_filter),
            ("Negative", self.negative_filter),
            ("Brighten", self.brighten_filter),
            ("Blur", self.blur_filter),
            ("Sepia", self.sepia_filter),
            ("Cool Tone", self.cool_filter),
            ("Edge Detect", self.edge_filter),
            ("Sharpen", self.sharpen_filter),
            ("Flip H", self.flip_horizontal),
            ("Flip V", self.flip_vertical)
        ]

        for text, cmd in buttons:
            tk.Button(
                btn_frame, text=text, command=cmd,
                bg="#2ecc71", fg="white", font=("Arial", 9, "bold"),
                relief="groove", padx=8, pady=4
            ).pack(side=tk.LEFT, padx=6, pady=5)

    def load_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if filepath:
            img = Image.open(filepath)
            self.img_array = np.array(img)
            self.display_image(self.img_array)

    def display_image(self, img_array):
        self.ax.clear()
        self.ax.imshow(np.clip(img_array, 0, 255).astype(np.uint8))
        self.ax.axis('off')
        self.canvas.draw()

    def grayscale_filter(self):
        if self.img_array is not None:
            gray = np.mean(self.img_array, axis=2)
            gray_img = np.stack((gray,)*3, axis=-1)
            self.display_image(gray_img)

    def negative_filter(self):
        if self.img_array is not None:
            neg_img = 255 - self.img_array
            self.display_image(neg_img)

    def brighten_filter(self):
        if self.img_array is not None:
            bright_img = np.clip(self.img_array + 50, 0, 255)
            self.display_image(bright_img)

    def blur_filter(self):
        if self.img_array is not None:
            kernel = np.ones((5, 5)) / 25
            blurred = np.zeros_like(self.img_array)
            for c in range(3):
                blurred[:, :, c] = convolve(self.img_array[:, :, c], kernel, mode='reflect')
            self.display_image(np.clip(blurred, 0, 255))

    def sepia_filter(self):
        if self.img_array is not None:
            img = np.array(self.img_array, dtype=np.float32)
            tr = 0.393 * img[:, :, 0] + 0.769 * img[:, :, 1] + 0.189 * img[:, :, 2]
            tg = 0.349 * img[:, :, 0] + 0.686 * img[:, :, 1] + 0.168 * img[:, :, 2]
            tb = 0.272 * img[:, :, 0] + 0.534 * img[:, :, 1] + 0.131 * img[:, :, 2]
            sepia = np.stack([tr, tg, tb], axis=2)
            self.display_image(np.clip(sepia, 0, 255))

    def cool_filter(self):
        if self.img_array is not None:
            cool = np.copy(self.img_array).astype(np.float32)
            cool[:, :, 0] *= 0.8
            cool[:, :, 2] *= 1.2
            self.display_image(np.clip(cool, 0, 255))

    def edge_filter(self):
        if self.img_array is not None:
            gray = np.mean(self.img_array, axis=2)
            kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
            kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
            gx = convolve(gray, kernel_x)
            gy = convolve(gray, kernel_y)
            edges = np.sqrt(gx**2 + gy**2)
            edge_img = np.stack((edges,)*3, axis=-1)
            self.display_image(np.clip(edge_img, 0, 255))

    def sharpen_filter(self):
        if self.img_array is not None:
            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
            sharp = np.zeros_like(self.img_array)
            for c in range(3):
                sharp[:, :, c] = convolve(self.img_array[:, :, c], kernel, mode='reflect')
            self.display_image(np.clip(sharp, 0, 255))

    def flip_horizontal(self):
        if self.img_array is not None:
            flipped = np.fliplr(self.img_array)
            self.display_image(flipped)

    def flip_vertical(self):
        if self.img_array is not None:
            flipped = np.flipud(self.img_array)
            self.display_image(flipped)


# ✅ FIXED MAIN ENTRY POINT
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()
