import pygame
from tkinter import Tk, filedialog, Button, Label, Scale

class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("Python MP3 Player")

        self.music_folder = ""
        self.file_path = ""

        # Create labels
        self.label_folder = Label(root, text="Music Folder:")
        self.label_folder.pack()

        self.label_volume = Label(root, text="Volume:")
        self.label_volume.pack()

        # Create buttons
        self.button_select_folder = Button(root, text="Select Folder", command=self.select_folder)
        self.button_select_folder.pack()

        self.button_select_song = Button(root, text="Select Song", command=self.select_song)
        self.button_select_song.pack()

        self.button_play = Button(root, text="Play", command=self.play_music)
        self.button_play.pack()

        self.button_pause = Button(root, text="Pause", command=self.pause_music)
        self.button_pause.pack()

        self.button_stop = Button(root, text="Stop", command=self.stop_music)
        self.button_stop.pack()

        # Create volume control
        self.volume_slider = Scale(root, from_=0, to=100, orient="horizontal", command=self.set_volume)
        self.volume_slider.set(50)  # Initial volume
        self.volume_slider.pack()

        # Initialize Pygame mixer
        pygame.mixer.init()

    def select_folder(self):
        self.music_folder = filedialog.askdirectory(title="Select Music Folder")
        self.label_folder.config(text=f"Music Folder: {self.music_folder}")

    def select_song(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        self.label_folder.config(text=f"Selected Song: {self.file_path}")

    def play_music(self):
        if self.file_path:
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume) / 100)

def main():
    root = Tk()
    mp3_player = MP3Player(root)
    root.mainloop()

if __name__ == "__main__":
    main()

