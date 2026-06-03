class Anime:
  def __init__(self, title, genre, status, rating):
    self.title = title
    self.genre = genre
    self.status = status
    self.rating = rating

  def displayInfo(self):
    print("Title:", self.title)
    print("Genre:", self.genre)
    print("Status:", self.status)
    print("Rating:", self.rating)

  def updateStatus(self, newstatus):
    self.status = newstatus
    print("Updating Anime Status...")
    print("Title:", self.title)
    print("Genre:", self.genre)
    print("Status:", self.status)
    print("Rating:", self.rating)

anime1 = Anime("Steins;Gate", "Drama, Sci-Fi", "Completed", "10")
anime1.displayInfo()

anime2 = Anime("Kaguya-sama: Love is War -Ultra Romantic-", "Comedy, Romance", "Completed", "9")
anime2.displayInfo()

anime3 = Anime("Fullmetal Alchemist: Brotherhood", "Action, Drama", "Plan to Watch", "9")
anime3.displayInfo()

anime3.updateStatus("Watching")