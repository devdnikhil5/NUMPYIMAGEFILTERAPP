# 🖼️ NumPy Image Filter App (Tkinter + Matplotlib + PIL)

A **feature-rich Image Filter Application** built using Python’s most powerful open-source libraries — **Tkinter**, **Matplotlib**, **NumPy**, **SciPy**, and **Pillow (PIL)**.  
This interactive desktop app enables users to **load, visualize, and apply multiple real-time image filters** using NumPy-based operations and convolution kernels.

It’s a perfect mini-project for **college students, Python beginners, or image-processing enthusiasts** who want to explore how GUI and image manipulation can be combined seamlessly.

---

## 🚀 Features

✨ **Load and Display Images Easily**  
Quickly open any `.jpg`, `.jpeg`, or `.png` file and display it directly inside the app window.

🎨 **Apply 10+ Real-Time Filters**  
Instantly apply grayscale, sepia, blur, sharpen, edge detection, and many other effects.

🧮 **NumPy-Powered Image Processing**  
All filters are applied using efficient NumPy array operations for speed and accuracy.

🖥️ **Interactive Tkinter GUI**  
Smoothly integrated Matplotlib canvas for real-time image previews inside Tkinter.

🔁 **Image Transformations**  
Flip images horizontally or vertically with a single click.

🧰 **Simple, Modular, and Open Source**  
Each filter is implemented as a standalone function — easy to modify or extend.

---

## 🎨 Available Filters and Effects

| Filter Name | Description |
|--------------|-------------|
| **Grayscale** | Converts the image into black-and-white shades using pixel averages |
| **Negative** | Inverts all colors to create a photo-negative effect |
| **Brighten** | Increases pixel brightness to make the image lighter |
| **Blur** | Applies a simple averaging kernel (5×5) for a soft blur |
| **Sepia** | Adds a vintage, brownish effect inspired by old photographs |
| **Cool Tone** | Enhances blue hues while reducing red — perfect for a cold aesthetic |
| **Edge Detect** | Detects strong pixel gradients using Sobel edge detection |
| **Sharpen** | Makes image details clearer by enhancing high-frequency areas |
| **Flip Horizontal** | Mirrors the image from left to right |
| **Flip Vertical** | Flips the image upside-down vertically |

---

## 🧩 Tech Stack

- **Python 3.x** – Core programming language  
- **Tkinter** – Standard Python GUI framework  
- **Matplotlib** – Used for displaying the processed image  
- **NumPy** – Performs mathematical image manipulation  
- **SciPy (ndimage)** – Used for convolution filters (blur, sharpen, edge detect)  
- **Pillow (PIL)** – Handles image loading, conversion, and file format support  

---

## 📦 Installation

Make sure you have **Python 3.8 or later** installed.

Then install all required packages:

```bash
pip install numpy matplotlib pillow scipy
▶️ Running the Application

Download or Clone this Repository

git clone (https://github.com/devdnikhil5/NUMPYIMAGEFILTERAPP)


Navigate to the project directory

cd ImageFilterApp


Run the main Python file

python PROJECTNEW.py


The GUI window will open.

Click “Load Image” to choose a file.

Try out any of the 10+ filter buttons to apply instant effects.

Enjoy live previews inside the Tkinter window!

🧠 How It Works (Under the Hood)

This project combines GUI design + mathematical image processing using Python:

When you load an image, it is converted to a NumPy array.

Each filter manipulates pixel data using array operations — such as addition, subtraction, multiplication, and convolution.

Processed arrays are visualized using Matplotlib’s imshow() embedded in a Tkinter frame.

Filters like Blur, Edge Detection, and Sharpen use convolution kernels applied via scipy.ndimage.convolve().

📁 Project Structure
ImageFilterApp/
│
├── PROJECTNEW.py           # Main application file
├── README.md               # Documentation file (this one)
├── requirements.txt        # Dependencies list (optional)
└── screenshots/            # Folder to store app previews

🖋️ Author

👨‍💻 Developed by: Nikhil Devd
📧 Email: [devdnikhil5@gmail.com]
🌐 GitHub: github.com/Nikhil Devari

Feel free to fork, modify, and improve this project — contributions are always welcome!


💡 Future Enhancements

🔹 Add a Save Image feature to export the filtered result
🔹 Include custom slider controls for brightness and contrast
🔹 Add OpenCV integration for advanced effects
🔹 Improve layout with a modern theme (like ttkbootstrap)
🔹 Include a Reset Image button for reverting changes

⚙️ Troubleshooting

If the app doesn’t open or shows errors:

Ensure __init__ and __main__ are correctly typed in code

Make sure all dependencies are installed

Try running from the terminal instead of VS Code run button:

python PROJECTNEW.py


If matplotlib window doesn’t show, try:

pip install --upgrade matplotlib

🏁 Summary

This NumPy Image Filter App is a complete demonstration of how Python GUI development and matrix-based image processing can work together.
You can easily extend it with more filters, or integrate machine-learning models for smart effects.

🩵 License

This project is released under the MIT License — you’re free to use, modify, and share it for personal or educational use.
