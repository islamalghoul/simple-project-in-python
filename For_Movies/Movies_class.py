import requests
import pprint

class Movies:
    def __init__(self,name) :
        self.name=name
        self.titles=[]  
        self.overview=[]
        self.vote_average=None
        self.date=None
        self.vote_count=None
        self.r=None
    def get_data(self):
        url=f"https://api.themoviedb.org/3/search/multi?api_key=4cdf972d28239e8f8ad1b28527b46f03&&query={self.name}"
        self.r = requests.get(url).json()
        return 1
    def get_title(self):
        titles=[]
        for i in self.r["results"]:
            if "title"in i:
                titles.append(i["title"])
        self.titles=titles
        return titles[0]
    def get_overview(self):
        description=[]
        for i in self.r["results"]:
            if "overview"in i:
                description.append(i["overview"])
        self.overview=description 
        return self.overview[0][0:200]
        
    def get_rating(self):
        rating=[]
        for i in self.r["results"]:
            if "vote_average"in i:
                rating.append(i["vote_average"])
        self.vote_average=rating 
        return self.vote_average[0]
    
    def get_vote_count(self):
        vote_count=[]
        for i in self.r["results"]:
            if "vote_count"in i:
                vote_count.append(i["vote_count"])
        self.vote_count=vote_count 
        return self.vote_count[0]

    def get_date(self):
        date=[]
        for i in self.r["results"]:
            if "release_date"in i:
                date.append(i["release_date"])
        self.date=date
        return self.date[0]
    

       
    def format_data(self):
        for i in range(10):
             pprint.pprint("The Title for this version : "+ self.titles[i])
             print("\n")
             pprint.pprint("The Description for this version : "+self.overview[i][0:200]+"...")
             print("\n")
             pprint.pprint(f"The Rating for this version  : {self.vote_average[i]}")
             pprint.pprint(f"The Number of Voters for this version : { self.vote_count[i]}")
             pprint.pprint(f"The Date for this version : {self.date[i]}")
             
             print("\n"*2)

class Movie(Movies):
    def __init__(self,name):
        self.name=name
        self.titles=[]  
        self.overview=[]
        self.vote_average=None
        self.date=None
        self.vote_count=None
        self.r=None
        super().__init__(name)

    def format_data(self):
             pprint.pprint("The Title for this version : "+ self.titles[0])
             print("\n")
             pprint.pprint("The Description for this version : "+self.overview[0][0:200]+"...")
             print("\n")
             pprint.pprint(f"The Rating for this version  : {self.vote_average[0]}")
             pprint.pprint(f"The Number of Voters for this version : { self.vote_count[0]}")
             pprint.pprint(f"The Date for this version : {self.date[0]}")
             print("\n"*2)



spider_man=Movie("spiderman")
spider_man.get_data()
print(spider_man.get_date())

