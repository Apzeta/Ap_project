import pygame  # Import the pygame library for audio playback
import os  # Import the os module for interacting with the filesystem

def list_songs():
    """Function to list available songs in the 'songs' directory."""
    print("Available songs:")
    for i, song in enumerate(os.listdir("songs")):
        print(f"{i+1}. {song}")

def play_song(song):
    """Function to play the specified song."""
    pygame.mixer.music.load(os.path.join("songs", song))  # Load the song
    pygame.mixer.music.play()  # Start playing the song

def stop_song():
    """Function to stop the currently playing song."""
    pygame.mixer.music.stop()  # Stop the playback

def main():
    """Main function to run the MP3 player."""
    pygame.init()  # Initialize pygame
    pygame.mixer.init()  # Initialize the mixer for audio playback

    while True:
        print("\nMP3 Player Menu:")
        print("1. List Songs")
        print("2. Play Song")
        print("3. Stop Song")
        print("4. Exit")

        choice = input("Enter your choice: ")  # Get user input for menu selection

        if choice == "1":
            list_songs()  # List available songs
        elif choice == "2":
            song_number = int(input("Enter the song number to play: "))  # Prompt for song selection
            songs = os.listdir("songs")  # Get the list of available songs
            if 1 <= song_number <= len(songs):  # Check if the selected song number is valid
                play_song(songs[song_number - 1])  # Play the selected song
            else:
                print("Invalid song number!")  # Print error message for invalid selection
        elif choice == "3":
            stop_song()  # Stop the currently playing song
        elif choice == "4":
            pygame.quit()  # Quit pygame and exit the program
            print("Goodbye!")  # Print farewell message
            break
        else:
            print("Invalid choice!")  # Print error message for invalid menu selection

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly

