import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NumPy Image Filter App")
        self.root.geometry("950x650")

        self.img_array = None
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Buttons for load and filters
        tk.Button(root, text="Load Image", command=self.load_image).pack(pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Grayscale", command=self.grayscale_filter).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Negative", command=self.negative_filter).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Brighten", command=self.brighten_filter).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Blur", command=self.blur_filter).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Sepia", command=self.sepia_filter).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cool Tone", command=self.cool_filter).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Edge Detect", command=self.edge_filter).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Sharpen", command=self.sharpen_filter).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Flip H", command=self.flip_horizontal).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Flip V", command=self.flip_vertical).pack(side=tk.LEFT, padx=10)

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
            kernel = np.ones((5,5,3)) / 25
            padded = np.pad(self.img_array, ((2,2),(2,2),(0,0)), mode='edge')
            blurred = np.zeros_like(self.img_array)
            for i in range(self.img_array.shape[0]):
                for j in range(self.img_array.shape[1]):
                    blurred[i,j] = np.sum(padded[i:i+5, j:j+5] * kernel, axis=(0,1))
            self.display_image(blurred)

    def sepia_filter(self):
        if self.img_array is not None:
            img = np.array(self.img_array, dtype=np.float32)
            tr = 0.393 * img[:,:,0] + 0.769 * img[:,:,1] + 0.189 * img[:,:,2]
            tg = 0.349 * img[:,:,0] + 0.686 * img[:,:,1] + 0.168 * img[:,:,2]
            tb = 0.272 * img[:,:,0] + 0.534 * img[:,:,1] + 0.131 * img[:,:,2]
            sepia = np.stack([tr, tg, tb], axis=2)
            self.display_image(np.clip(sepia, 0, 255))

    def cool_filter(self):
        if self.img_array is not None:
            cool = np.copy(self.img_array).astype(np.float32)
            cool[:,:,0] *= 0.8  # reduce red
            cool[:,:,2] *= 1.2  # enhance blue
            self.display_image(np.clip(cool, 0, 255))

    def edge_filter(self):
        if self.img_array is not None:
            gray = np.mean(self.img_array, axis=2)
            kernel_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
            kernel_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
            padded = np.pad(gray, ((1,1),(1,1)), mode='edge')
            gx = np.zeros_like(gray)
            gy = np.zeros_like(gray)
            for i in range(gray.shape[0]):
                for j in range(gray.shape[1]):
                    gx[i,j] = np.sum(padded[i:i+3, j:j+3] * kernel_x)
                    gy[i,j] = np.sum(padded[i:i+3, j:j+3] * kernel_y)
            edges = np.sqrt(gx**2 + gy**2)
            edge_img = np.stack((edges,)*3, axis=-1)
            self.display_image(np.clip(edge_img, 0, 255))

    def sharpen_filter(self):
        if self.img_array is not None:
            kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
            padded = np.pad(self.img_array, ((1,1),(1,1),(0,0)), mode='edge')
            sharp = np.zeros_like(self.img_array)
            for i in range(self.img_array.shape[0]):
                for j in range(self.img_array.shape[1]):
                    sharp[i,j] = np.sum(padded[i:i+3, j:j+3] * kernel[:,:,None], axis=(0,1))
            self.display_image(np.clip(sharp, 0, 255))

    def flip_horizontal(self):
        if self.img_array is not None:
            flipped = np.fliplr(self.img_array)
            self.display_image(flipped)

    def flip_vertical(self):
        if self.img_array is not None:
            flipped = np.flipud(self.img_array)
            self.display_image(flipped)

root = tk.Tk()
app = ImageFilterApp(root)
root.mainloop()
