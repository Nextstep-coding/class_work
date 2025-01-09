import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class TkinterDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Demo Application")
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        # PACK layout example
        frame_pack = tk.Frame(self.root, bg="SLATEGRAY", padx=20, pady=50)
        frame_pack.pack(side="top", fill="x", padx=5, pady=5)

        tk.Label(frame_pack, text="Pack Layout", font=("Arial", 14)).pack()
        tk.Button(frame_pack, text="Pack Button", command=self.show_message).pack(pady=5)

        # GRID layout example
        frame_grid = tk.Frame(self.root, bg="lightgreen", padx=10, pady=10)
        frame_grid.pack(side="top", fill="x", padx=5, pady=5)

        tk.Label(frame_grid, text="Grid Layout", font=("Arial", 14), bg="lightgreen").grid(row=0, column=0, columnspan=2)
        tk.Label(frame_grid, text="First Name:").grid(row=1, column=0, sticky="e")
        self.first_name_entry = tk.Entry(frame_grid)
        self.first_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_grid, text="Last Name:").grid(row=2, column=0, sticky="e")
        self.last_name_entry = tk.Entry(frame_grid)
        self.last_name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(frame_grid, text="Submit", command=self.show_entries).grid(row=3, column=0, columnspan=2, pady=10)

        # PLACE layout example
        frame_place = tk.Frame(self.root, bg="lightyellow", padx=10, pady=10, height=100, width=300)
        frame_place.pack(side="top", fill="x", padx=5, pady=5)

        tk.Label(frame_place, text="Place Layout", bg="lightyellow").place(x=10, y=10)
        tk.Button(frame_place, text="Click Me", command=self.show_message).place(x=100, y=40)

        # Canvas Example
        self.canvas = tk.Canvas(self.root, width=300, height=100, bg="white")
        self.canvas.pack(pady=10)
        self.canvas.create_rectangle(50, 20, 150, 80, fill="blue")
        self.canvas.create_text(200, 50, text="Canvas Example", fill="black", font=("Arial", 12))

    def create_menu(self):
        # Menu bar
        menu_bar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open File", command=self.open_file_dialog)
        file_menu.add_command(label="Save File", command=self.save_file_dialog)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about_dialog)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    def show_message(self):
        messagebox.showinfo("Information", "Button Clicked!")

    def show_entries(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        messagebox.showinfo("Entry Data", f"First Name: {first_name}\nLast Name: {last_name}")

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if file_path:
            messagebox.showinfo("File Selected", f"File: {file_path}")

    def save_file_dialog(self):
        file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt",
                                                 filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if file_path:
            messagebox.showinfo("File Saved", f"File saved at: {file_path}")

    def show_about_dialog(self):
        messagebox.showinfo("About", "Tkinter Demo Application\nVersion 1.0")


if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterDemoApp(root)
    root.mainloop()
