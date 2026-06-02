class Anime:
  def __init__(self, title, genre, status):
    self.title = title
    self.genre = genre
    self.status = status

  def displayInfo(self):
    print("Title:", self.title)
    print("Genre:", self.genre)
    print("Status:", self.status)

  def updateStatus(newStatus):
    pass

a_user = Anime("Steins;Gate", "Drama", "Completed")
a_user.displayInfo()