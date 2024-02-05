import tkinter as tk
from PIL import Image, ImageTk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("480x320")
        root.iconbitmap("icon1.ico")
        self.root.title("Street-Sight-Navigator-Ai")
        self.root.configure(bg="#D3D3D3")

        self.is_running = False  

        image_path = "holes.jpg"
        image = Image.open(image_path)

        
        image_width, image_height = image.size
        window_width = 380
        window_height = 320

        
        ratio = min(window_width / image_width, window_height / image_height)
        resized_width = int(image_width * ratio)
        resized_height = int(image_height * ratio)

        
        image = image.resize((resized_width, resized_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(self.root, image=photo)
        self.image_label.image = photo
        self.image_label.place(x=0, y=0, width=380, height=320)

        label_font_size = 12
        label_font_weight = "bold"

        

        button_width = 90
        button_height = 45
        button_padding = 42
        button_font_size = 12
        button_font_weight = "bold"

        center_x_right = 380 + (480 - 380 - button_width) / 2

        self.status_label = tk.Label(self.root, text="Status:", font=("Arial", label_font_size, label_font_weight),bg="#D3D3D3")
        self.status_label.place(x=380, y=10, width=60, height=20)

        self.status_button = tk.Button(self.root, width=3, height=1, bg="#f36c60", borderwidth=0)
        self.status_button.place(x=450, y=10, width=25, height=24)
        
        
        self.toggle_button_text = tk.StringVar()
        self.toggle_button_text.set("Start" if not self.is_running else "Stop")
        self.toggle_button_color = "#72d572" if not self.is_running else "#EF7272"

        self.button1 = tk.Button(self.root, text="Save", width=button_width, height=button_height, bg="#2E8B57", fg="#fff", borderwidth=0, font=("Arial", button_font_size, button_font_weight))
        self.button1.place(x=center_x_right, y=button_padding, width=button_width, height=button_height)

        self.button2 = tk.Button(self.root, text="Export", width=button_width, height=button_height, bg="#ffd54f", fg="#fff", borderwidth=0, font=("Arial", button_font_size, button_font_weight))
        self.button2.place(x=center_x_right, y=2 * button_padding + button_height, width=button_width, height=button_height)

        self.button3 = tk.Button(self.root, textvariable=self.toggle_button_text, width=button_width, height=button_height, bg=self.toggle_button_color, fg="#fff", borderwidth=0, font=("Arial", button_font_size, button_font_weight), command=self.toggle_status)
        self.button3.place(x=center_x_right, y=3 * button_padding + 2 * button_height, width=button_width, height=button_height)

    def toggle_status(self):
        self.is_running = not self.is_running
        self.toggle_button_text.set("Start" if not self.is_running else "Stop")
        self.toggle_button_color = "#72d572" if not self.is_running else "#EF7272"
        self.button3.configure(bg=self.toggle_button_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
