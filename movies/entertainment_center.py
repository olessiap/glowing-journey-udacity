import media

ivan_movie = media.Movie("Ivan Vasilievich: Back to the Future","Ivan the terrible travels to the future",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNDQ3NDM2NjM5MF5BMl5BanBnXkFtZTYwNTg1OTc5._V1_.jpg",
                         "https://www.youtube.com/watch?v=nDWPKqXDNq8")

moscow_movie = media.Movie("Moscow Does Not Believe in Tears", "Story about a Moscow woman and her rise in society",
                           "https://images-na.ssl-images-amazon.com/images/I/51-6zxtejTL.jpg",
                           "https://www.youtube.com/watch?v=69ellPkReh0")

fate_movie = media.Movie("The Irony of Fate or Enjoy Your Bath", "A man accidently ends up in the wrong apartment on NYE and changes the fate of 2 people",
                         "https://www.podnapisi.net/thumbnails/moviedb/normal/VDc.jpg",
                         "https://www.youtube.com/watch?v=nNrFdBvBYWg")
#print toy_story.storyline
#print moscow_movie.storyline

fate_movie.show_trailer()
