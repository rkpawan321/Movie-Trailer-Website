""" This is main file where we create the instances of Class Movie.
    This python file is run to view the Movie Website Trailer."""
 
""" Importing  media and fresh_tomatoes python files """
import fresh_tomatoes
import media

""" Creating a list of instances of Class Movie and assign it to movies variable"""
toy_story = media.Movie("Toy Story" ,
                        "A story of a boy and his toys that come to life" ,
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/d1_JBMrrYw8")
                     

venom = media.Movie("Venom",
                    "Venom tries to control the new and dangerous abilities that Eddie finds so intoxicating.",
                    "https://upload.wikimedia.org/wikipedia/en/0/05/Venom_poster.jpg",
                    "https://youtu.be/xLCn88bfW1o")

aquaman = media.Movie("Aquaman" ,
                      "Arthur Curry learns that he is the heir to the underwater kingdom of Atlantis, and must step forward to lead his people and be a hero to the world.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3a/Aquaman_poster.jpg",
                      "https://youtu.be/WDkg3h8PCVU")
					  
infinity = media.Movie("Infinity War",
                       "All your heros die",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

thor = media.Movie("Thor Ragnarok",
                   "Thor looses his favourite tool",
                   "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                   "https://youtu.be/ue80QwXMRHg")

movies = [toy_story , avatar ,venom, aquaman, infinity , thor]

""" Calling open_movies_page method to view movie website
 input : List including all the instances """
fresh_tomatoes.open_movies_page(movies)



