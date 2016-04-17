"""

This module provides the movie title, link to the poster image
and link to the movie trailer for each of Tony's favorite movies.

"""

import fresh_tomatoes

import media

jurassic_world = media.Movie("Jurassic World",
                             "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",  # NOQA
                             "https://youtu.be/RFinNxS5KN4")

neighbors = media.Movie("Neighbors",
                        "https://upload.wikimedia.org/wikipedia/en/3/32/Neighbors_%282013%29_Poster.jpg",  # NOQA
                        "https://youtu.be/KrAf5ALLxGI")

forty_virgin = media.Movie("The 40-Year-Old Virgin",
                           "https://upload.wikimedia.org/wikipedia/en/4/43/40-Year-OldVirginMoviePoster.jpg",  # NOQA
                           "https://youtu.be/KUT64PctyNw")

knocked_up = media.Movie("Knocked Up",
                         "https://upload.wikimedia.org/wikipedia/en/5/51/Knockedupmp.jpg",  # NOQA
                         "https://youtu.be/xlBR-T8gdFo")

minions = media.Movie("Minions",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",  # NOQA
                      "https://youtu.be/8smpu0Hg424")

spy = media.Movie("Spy",
                  "https://upload.wikimedia.org/wikipedia/en/5/5d/Spy2015_TeaserPoster.jpg",  # NOQA
                  "https://youtu.be/WUiNU_H8Xeg")

heat = media.Movie("The Heat",
                   "https://upload.wikimedia.org/wikipedia/en/b/bf/The_Heat_poster.jpg",  # NOQA
                   "https://youtu.be/fbDictI7xiU")

identity_thief = media.Movie("Identity Thief",
                             "https://upload.wikimedia.org/wikipedia/en/a/a7/Identity_Thief_Poster.jpg",  # NOQA
                             "https://youtu.be/NW_60YDUj7Q")

skyfall = media.Movie("Skyfall",
                      "https://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg",  # NOQA
                      "https://youtu.be/6kw1UVovByw")

movies = [jurassic_world, neighbors, forty_virgin, knocked_up,
          minions, spy, heat, identity_thief, skyfall]
fresh_tomatoes.open_movies_page(movies)
