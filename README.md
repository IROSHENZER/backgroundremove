# Image Background Remover GUI - Python

## Overview
The Image Background Remover GUI is a Python application that allows users to remove the background from images easily using a graphical user interface (GUI). It uses the `rembg` library to perform background removal and `Pillow` (PIL) for image handling, along with `tkinter` for the GUI components.

## Installation

To install the necessary dependencies and run the application, follow these steps:

1. Install the required packages:

```bash
pip install rembg Pillow tkinter
```

2. Run the application by executing the following command:

```bash
python bgremove.py
```

## File Structure

```
background-remover/
│
├── bgremove.py           # Main application file
├── README.md           # Documentation for the project
└── requirements.txt    # Project dependencies
```

## Requirements

- Python 3.6 or higher
- rembg
- Pillow (PIL)
- tkinter (usually comes pre-installed with Python)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) for the background removal functionality.
- [U2Net](https://github.com/xuebinqin/U-2-Net) for the underlying AI model used for background removal.



