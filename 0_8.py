ban_words = ["N00B ", "N0ob ", "n00B ", "No0b ", "No0B ", "Noob ", "NoOb ", "NOob ", "NoOB ", "NOoB ", "noob"]
player = input()
player = player.replace("?", "")
player = player.replace("!", "")
player = player.replace(".", "")
player = player.replace(",", "")
word = player.lower().split()
if any(word in ban_words for word in word):
    print("Banned")
else:
    print("Great Player")