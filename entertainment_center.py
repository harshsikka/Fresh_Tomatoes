import media
import fresh_tomatoes  # importing file provided by Udacity to render responsive webpage

toy_story = media.Movie("Toy Story",
                        "A story about the dark, twisted, secret lives of some toys.",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Space marine with loyalty issues",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

pacific_rim = media.Movie("Pacific Rim",
                          "Giant Robots vs Godzilla's cousins. What isn't to like?",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcT24u-kDNdX_vpwbAkMyXGKDIz7m-h_QorA_o6m0q36GPHDgJmU",
                          "https://www.youtube.com/watch?v=5guMumPFBag")

bourne_identity = media.Movie("The Bourne Identity",
                              "The human swiss army knife.",
                              "http://www.gstatic.com/tv/thumb/movieposters/28900/p28900_p_v8_ai.jpg",
                              "https://www.youtube.com/watch?v=cD-uQreIwEk")
skyfall = media.Movie("Skyfall",
                      "Guns, Gadgets, and Naomi Harris",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcTSNSk0M1z_CZ1UKTnfE2nHmk4Oxqh_gKO0dAHZHwrfLX6D9Y4s",
                      "https://www.youtube.com/watch?v=6kw1UVovByw")
            
movies = [toy_story, avatar, pacific_rim, bourne_identity, skyfall]  # storing in list for fresh_tomatoes.py open method

fresh_tomatoes.open_movies_page(movies)

