import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
from pathlib import Path

def run_webcam():
    subprocess.Popen([sys.executable, str(Path(__file__).with_name("pose.py"))])

def run_video():
    path = filedialog.askopenfilename(
        title="Select a video",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
    )
    if path:
        subprocess.Popen([sys.executable, str(Path(__file__).with_name("pose.py")), path])

root = tk.Tk()
root.title("Ergonomic AI Launcher")
root.geometry("300x150")

tk.Button(root, text="Run with Webcam", width=25, command=run_webcam).pack(pady=10)
tk.Button(root, text="Run with Video File", width=25, command=run_video).pack(pady=10)

root.mainloop()
