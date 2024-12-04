import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox
from yt_dlp import YoutubeDL

def download_video():
    url = url_var.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube video URL.")
        return

    try:
        # Ask the user to select a download directory
        download_folder = filedialog.askdirectory(title="Select Download Folder")
        if not download_folder:
            messagebox.showerror("Error", "Please select a folder to save the video.")
            return

        # Download the video using yt-dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_title = info.get('title', 'Unknown')

        # Update GUI with download info
        result_var.set(f"Downloaded: {video_title}\nLocation: {download_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create main GUI window
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("500x300")
root.resizable(False, False)

# URL Entry
Label(root, text="Enter YouTube URL:", font=("Arial", 12)).pack(pady=10)
url_var = StringVar()
Entry(root, textvariable=url_var, width=50, font=("Arial", 12)).pack(pady=10)

# Download Button
Button(root, text="Download", command=download_video, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

# Result Display
result_var = StringVar()
Label(root, textvariable=result_var, font=("Arial", 10), wraplength=400, justify="center").pack(pady=20)

# Run the application
root.mainloop()
