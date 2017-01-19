import media
import fresh_tomatoes

###calling the constructor media.movie() to initiate movie objects
ivan_movie = media.Movie("Ivan Vasilievich: Back to the Future","Ivan the terrible travels to the future",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNDQ3NDM2NjM5MF5BMl5BanBnXkFtZTYwNTg1OTc5._V1_.jpg",
                         "https://www.youtube.com/watch?v=nDWPKqXDNq8")

moscow_movie = media.Movie("Moscow Does Not Believe in Tears", "Story about a Moscow woman and her rise in society",
                           "https://images-na.ssl-images-amazon.com/images/I/51-6zxtejTL.jpg",
                           "https://www.youtube.com/watch?v=69ellPkReh0")

fate_movie = media.Movie("The Irony of Fate or Enjoy Your Bath", "A man accidently ends up in the wrong apartment on NYE and changes the fate of 2 people",
                         "https://www.podnapisi.net/thumbnails/moviedb/normal/VDc.jpg",
                         "https://www.youtube.com/watch?v=nNrFdBvBYWg")

brother_movie = media.Movie("Brother", "2 brothers turn into thugs",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNDMxNzkwNzkwNV5BMl5BanBnXkFtZTcwNTczNDkxMQ@@._V1_.jpg",
                         "https://www.youtube.com/watch?v=Zq55yxODJiA")

nineth_company_movie = media.Movie("9th company", "Russian boys become soldiers in the Afghan war & become bffs in tragic circumstances",
                         "https://i.jeded.com/i/the-9th-company-9-ya-rota.19239.jpg",
                         "https://www.youtube.com/watch?v=TcHD9VEQ7C8")

nightwatch_movie = media.Movie("Nightwatch", "Supernatural beings fight to protect their realms",
                         "http://images.moviepostershop.com/night-watch-movie-poster-2004-1010262173.jpg",
                         "https://www.youtube.com/watch?v=xDPLZW8MBW8")


movies = [ivan_movie, moscow_movie, fate_movie, brother_movie, nineth_company_movie, nightwatch_movie] ##storing movie objects in a list as input for open_movies_page function
fresh_tomatoes.open_movies_page(movies)
