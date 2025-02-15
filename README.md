# Background Remover GUI

A Python desktop application that removes backgrounds from images using a simple graphical user interface. Process multiple images at once by selecting an input folder, and save the processed images with transparent backgrounds as PNG files.

![Background Remover GUI Screenshot](https://via.placeholder.com/600x400.png?text=Background+Remover+GUI)

## Features

- User-friendly graphical interface
- Batch processing of multiple images
- Supports various input formats (PNG, JPG, JPEG, BMP, WEBP)
- Saves processed images with transparent backgrounds as PNG
- Real-time progress tracking
- Multi-threaded processing to prevent GUI freezing
- Detailed status updates and error handling

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/background-remover.git
cd background-remover
```

2. Install the required dependencies:
```bash
pip install rembg
pip install Pillow
```

Note: On first run, the application will download the U2Net model (approximately 176MB). This is a one-time download.

## Usage

1. Run the application:
```bash
python app.py
```

2. Use the GUI to:
   - Click "Browse" to select an input folder containing images
   - Click "Browse" to select an output folder for processed images
   - Click "Process Images" to start background removal

3. Monitor progress:
   - The status window shows real-time processing updates
   - Progress counter shows number of processed images
   - Wait for the "Processing completed!" message

Processed images will be saved in the output folder with "_nobg" suffix.

## File Structure

```
background-remover/
│
├── app.py              # Main application file
├── README.md          # This documentation
└── requirements.txt   # Project dependencies
```

## Requirements

- Python 3.6 or higher
- rembg
- Pillow (PIL)
- tkinter (usually comes with Python)


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) for the background removal functionality
- [U2Net](https://github.com/xuebinqin/U-2-Net) for the underlying AI model


## Support

If you encounter any problems or have suggestions, please open an issue on the GitHub repository.
