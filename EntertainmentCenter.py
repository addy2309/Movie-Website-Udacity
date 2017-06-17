import media
import fresh_tomatoes

# toy story object decleartion
toy_story = media.Movie(
    "Toy Stroy",
    "Andy's favourite toy, Woody, is worried that after Andy receives his \
    birthday gift, a new toy called Buzz Lightyear, his importance may get\
    reduced. He thus hatches a plan to eliminate Buzz.",
    "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ZZv1vki4ou4")  # NOQA

# batman v superman object decleartion
bvs = media.Movie(
    "Batman v Superman: Dawn of Justice",
    "Billionaire Bruce Wayne believes that Superman is a threat to humanity\
    as his power goes unchecked. Wayne decides to protect the world against\
    him in the guise of his superhero avatar, Batman.",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcS61fdKkVcQIKtObjNGAELqVwyzhwFoIfNGZVbC-rqta12xBfLa",  # NOQA
    "https://www.youtube.com/watch?v=0WWzgGyAH6Y")  # NOQA

# zindagi na milegi dobara object decleartion
znmd = media.Movie(
    "Zindagi Na Milegi Dobara",
    "Friends Kabir, Imran and Arjun take a vacation in Spain before \
    Kabir's marriage. The trip turns into an opportunity to mend fences,\
    heal wounds, fall in love with life and combat their worst fears.",
    "http://www.gstatic.com/tv/thumb/movieposters/8424501/p8424501_p_v7_aa.jpg",  # NOQA
    "https://www.youtube.com/watch?v=bQR_bxragHk")  # NOQA

# wonder woman object decleartion
wonder = media.Movie(
    "Wonder Woman",
    "Before she was Wonder Woman (Gal Gadot), she was Diana, princess\
    of the Amazons, trained to be an unconquerable warrior. Diana\
    leaves her home for the first time. Fighting alongside men in a war\
    to end all wars, she finally discovers her full powers and true destiny.",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",  # noqa
    "https://www.youtube.com/watch?v=INLzqh7rZ-U")  # noqa


movies = [znmd, wonder, bvs, toy_story]
fresh_tomatoes.open_movies_page(movies)
