from Movies_classs import Movies,Movie
from Series_classs import Series,Seriess
print('''
         |**********************************|
         |                                  |
         |    Welcome to Rhythms  Cinema    |
         |                                  |
         |                                  |
         |**********************************|
         ''')
print("\n"*2)
try:
    x= input("What are you looking for(Movies OR Series) ?")
    if x.lower()=="movies":
        
        movie_name=input("enter the movie name: ")
        movie=Movie(movie_name)
        movie.get_data()
        movie.get_title()
        movie.get_overview()
        movie.get_rating()
        movie.get_vote_count()
        movie.get_date()
        movie.format_data()
        show_more_info=input(f"do you want more information about any movie related to this movie {movie_name}...(Yes or  No)")
        if show_more_info.lower()=="yes" or show_more_info.lower()=="y":
            movie=Movies(movie_name)
            movie.get_data()
            movie.get_title()
            movie.get_overview()
            movie.get_rating()
            movie.get_vote_count()
            movie.get_date()
            movie.format_data()
    elif x.lower()=="series":
        series_name=input(" ** Enter the Series name: ")
        series=Series(series_name)
        series.get_data()
        series.get_title()
        series.get_overview()
        series.get_rating()
        series.get_vote_count()
        series.get_date()
        series.format_data()
        show_more_info=input(f"do you want more information about any Seriess related to this Series     {series_name}...(Yes or  No)")
    if show_more_info.lower()=="yes" or show_more_info.lower()=="y":
        series=Seriess(series_name)
        series.get_data()
        series.get_title()
        series.get_overview()
        series.get_rating()
        series.get_vote_count()
        series.get_date()
        series.format_data() 
except NameError:
    print("you should enter Series or Movies")
except IndexError as err:
    print(f"the {movie_name} that you entered dose not exist on our list")