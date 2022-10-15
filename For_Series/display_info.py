from Series_class import Series, Seriess
print('''
         |******************************|
         |                              |
         |    Welcome to Series page    |
         |                              |
         |******************************|
         ''')

         
print("\n"*2)
try:
    series_name=input(" ** Enter the Series name: ")
    series=Series(series_name)
    series.get_data()
    series.get_title()
    series.get_overview()
    series.get_rating()
    series.get_vote_count()
    series.get_date()
    series.format_data()
    show_more_info=input(f"do you want more information about any Seriess related to this Series{series_name}...(Yes or  No)")
    if show_more_info.lower()=="yes" or show_more_info.lower()=="y":
        series=Seriess(series_name)
        series.get_data()
        series.get_title()
        series.get_overview()
        series.get_rating()
        series.get_vote_count()
        series.get_date()
        series.format_data() 
except IndexError as err:
    print(f"the {series_name} that you entered dose not exist on our list")