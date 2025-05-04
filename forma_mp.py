import customtkinter as ctk
from tkinter import filedialog, messagebox
from moviepy import *
import os


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def mp4_to_mp3(mp4, mp3):
    audio = AudioFileClip(mp4)
    audio.write_audiofile(mp3)
    audio.close()

def mp4_to_gif(mp4, gif):
    video = VideoFileClip(mp4)
    video.write_gif(gif)
    video.close()

def mp4_to_avi(mp4, avi):
    video = VideoFileClip(mp4)
    video.write_videofile(avi, codec='png')
    video.close()

def browse_file():
    file_path.set(filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")]))

def convert():
    path = file_path.get()
    if not path.lower().endswith(".mp4"):
        messagebox.showerror("Ошибка", "Выберите файл с расширением .mp4")
        return
    
    choice = format_choice.get()
    if choice == "mp3":
        output = path[:-4] + ".mp3"
        mp4_to_mp3(path, output)
    elif choice == "gif":
        output = path[:-4] + ".gif"
        mp4_to_gif(path, output)
    elif choice == "avi":
        output = path[:-4] + ".avi"
        mp4_to_avi(path, output)
    else:
        messagebox.showerror("Ошибка", "Выберите формат конвертации!")
        return

    messagebox.showinfo("Готово", f"Файл сохранён как:\n{output}")
    open_folder(output)

def open_folder(output_path):
    """Открывает папку с результатом"""
    folder_path = os.path.dirname(output_path)
    os.startfile(folder_path)


# --- GUI ---
app = ctk.CTk()
app.title("🎬 MP4 Конвертер")
app.geometry("400x320")
app.resizable(False, False)

file_path = ctk.StringVar()
format_choice = ctk.StringVar(value="mp3")

ctk.CTkLabel(app, text="Выберите MP4 файл", font=("Tahoma", 14)).pack(pady=(20, 5))
ctk.CTkEntry(app, textvariable=file_path, width=260).pack()
ctk.CTkButton(app, text="Обзор...", command=browse_file).pack(pady=10)

ctk.CTkLabel(app, text="Формат конвертации", font=("Tahoma", 14)).pack(pady=(10, 5))

ctk.CTkRadioButton(app, text="🎵 MP3", variable=format_choice, value="mp3").pack()
ctk.CTkRadioButton(app, text="🎞 GIF", variable=format_choice, value="gif").pack()
ctk.CTkRadioButton(app, text="📺 AVI", variable=format_choice, value="avi").pack()

ctk.CTkButton(app, text="Конвертировать", command=convert, fg_color="#1f6aa5", hover_color="#144e75").pack(pady=20)

app.mainloop()

