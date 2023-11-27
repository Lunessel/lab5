from file import File
from folder import Folder


root = Folder("Root")
personal = Folder("Personal")
movies = Folder("Folder2")
songs = Folder("Folder3")
my_notes = File("My_notes", "txt", 100)
cat = File("Image", "jpg", 200)
backlog = File("Spreadsheet", "xlsx", 150)
the_avengers = File("Video", "mp4", 500)
patriotic_song = File("Audio", "mp3", 300)


personal.add(my_notes)
personal.add(cat)
movies.add(backlog)
movies.add(the_avengers)
movies.add(songs)
songs.add(patriotic_song)
root.add(personal)
root.add(movies)

print("tree of files:")
root.print_tree()

longest_path = root.find_longest_path()
print(f"longest way to object: {longest_path}")