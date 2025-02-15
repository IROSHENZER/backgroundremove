import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from rembg import remove
from pathlib import Path
import threading

class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover")
        self.root.geometry("600x400")
        
        self.input_folder = tk.StringVar()
        self.output_folder = tk.StringVar()
        
        self.create_widgets()
        
        self.processing = False
        
    def create_widgets(self):
        input_frame = tk.LabelFrame(self.root, text="Input Folder", padx=10, pady=5)
        input_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Entry(input_frame, textvariable=self.input_folder, width=50).pack(side="left", padx=5)
        tk.Button(input_frame, text="Browse", command=self.browse_input).pack(side="left", padx=5)
        
        output_frame = tk.LabelFrame(self.root, text="Output Folder", padx=10, pady=5)
        output_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Entry(output_frame, textvariable=self.output_folder, width=50).pack(side="left", padx=5)
        tk.Button(output_frame, text="Browse", command=self.browse_output).pack(side="left", padx=5)
        
        self.process_button = tk.Button(self.root, text="Process Images", command=self.process_images)
        self.process_button.pack(pady=10)
        
        self.progress_label = tk.Label(self.root, text="")
        self.progress_label.pack(pady=5)
        
        # Status list
        self.status_text = tk.Text(self.root, height=10, width=60)
        self.status_text.pack(padx=10, pady=5)
        
    def browse_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_folder.set(folder)
            
    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder.set(folder)
            
    def update_status(self, message):
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        
    def process_images(self):
        if self.processing:
            messagebox.showwarning("Warning", "Processing is already in progress!")
            return
            
        input_path = self.input_folder.get()
        output_path = self.output_folder.get()
        
        if not input_path or not output_path:
            messagebox.showerror("Error", "Please select both input and output folders!")
            return
            
        if not os.path.exists(input_path):
            messagebox.showerror("Error", "Input folder does not exist!")
            return
            
        os.makedirs(output_path, exist_ok=True)
        
        self.processing = True
        self.process_button.config(state="disabled")
        self.progress_label.config(text="Processing...")
        
        thread = threading.Thread(target=self.process_images_thread)
        thread.start()
        
    def process_images_thread(self):
        input_path = self.input_folder.get()
        output_path = self.output_folder.get()
        
        try:
            image_files = [f for f in os.listdir(input_path) 
                         if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp'))]
            
            if not image_files:
                self.update_status("No image files found in the input folder!")
                return
            
            total_files = len(image_files)
            processed_files = 0
            
            for image_file in image_files:
                input_image_path = os.path.join(input_path, image_file)
                output_image_path = os.path.join(output_path, 
                                               f"{Path(image_file).stem}_nobg.png")
                
                try:
                    with open(input_image_path, 'rb') as i:
                        input_image = i.read()
                        output_image = remove(input_image)
                        
                    with open(output_image_path, 'wb') as o:
                        o.write(output_image)
                        
                    processed_files += 1
                    self.update_status(f"Processed: {image_file}")
                    
                except Exception as e:
                    self.update_status(f"Error processing {image_file}: {str(e)}")
                
                self.progress_label.config(
                    text=f"Progress: {processed_files}/{total_files} images"
                )
                
            self.update_status("\nProcessing completed!")
            
        except Exception as e:
            self.update_status(f"Error: {str(e)}")
            
        finally:
            self.processing = False
            self.process_button.config(state="normal")
            self.progress_label.config(text="Ready")

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()
