class Anime:
  def __init__(self, title, genre, status):
    self.title = title
    self.genre = genre
    self.status = status

  def displayHeader():
    print("===== Anime Watchlist =====")

  def displayInfo(self, displayHeader):
    print("Title:", self.title)
    print("Genre:", self.genre)
    print("Status:", self.status)

  def updateStatus(newStatus):
    pass

anime1 = Anime("Steins;Gate", "Drama, Sci-Fi", "Completed")
anime1.displayInfo()

anime2 = Anime("Kaguya-sama: Love is War -Ultra Romantic-", "Comedy, Romance", "Completed")
anime2.displayInfo()

anime3 = Anime("Fullmetall Alchemist: Brotherhood", "Action, Drama", "Plan to Watch")
anime3.displayInfo()