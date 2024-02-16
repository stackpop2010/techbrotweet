"""
This should push a gibberish tech speak tweet. Need to create a developer Twitter and uncomment daily or single tweet.
"""

import random
#from command line need to type "pip install tweepy"
import tweepy
import schedule
import time

consumer_key = "YOUR_API_KEY"
consumer_secret = 'YOUR_API_SECRET'
access_token = 'YOU_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

#double check if this is an oh or zero
auth =tweepy.OAuthHandler()(consumer_key, consumer_secret)
auth.set_acess_token(access_token, access_token_secret)
api =tweepy.API(auth)

latin_list = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eius",
              "modi", "tempor", "incididunt", "ut",
              "labore", "et", "dolore", "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrumd",
              "exercitation",
              "ullam", "co", "pariatur", "exceptur", "sint", "obcaecati", "cupidtat", "non", "pro", "ident", "sunt",
              "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laboru", "et", "harum", "de", "re",
              "ud", "facilis", "est", "er",
              "expedi", "disi", "nam", "liber", "tempor", "cum", "soluta", "nobis", "elige", "quod", "maxim", "placeat",
              "facer",
              "possim", "omins", "volupt", "assumenda", "est", "omnis", "dolor", "repellenda"]

tech_list = ["Datafication", "Net Neutrality", "Non-Fungible Tokens", "Metaverse", "Digital Divide", "Bezos, more like Bozos",
             "Everything As A Service", "API", "Token", "Reddit", "use old.reddit instead", "Anime", "dox", "dynamic",
             "Hyper-Personalization", "Gamification", "Wantrepreneur", "SQL", "C#", "Front End", "Full Stack",
             "Web Dev", "lean", "accelerator", "venture capital", "C++", "Java", "Rust", "Janky old flash animation",
             "Augmented Reality", "Virtual reality", "Robotics", "Smart Industry 4.0", "Robotic Process Automation",
             "Neural Networks", "scalability", "burn rate", "RIP twitter", "Perl", "Barons", "Wall Street Journal",
             "Blockchain", "Technological Unemployment", "Computer Vision", "Cyber Crime", "Security", "Hackathon",
             "Distributed Cloud", "Artificial Intelligence", "Large Language Models", "Hyperautomation", "Chat GPT",
             "Quantum Computing", "5G Connectivity", "Standing Desk,", "Scrum Master", "Techno Jesus", "sprint",
             "qualatively bad", "quantum mechanics", "QC", "quality assurance", "algorithm", "kotaku", "MCU",
             "Bitcoin", "Luna", "monero", "Snowden", "crapware", "malware", "bloatware", "Outlook", "GMAIL",
             "defi", "App", "Star my repo please",
             "FAANG", "Web3", "Multiexperience", "Google", "Cloud-Native Platforms", "Big Data", "Social Media",
             "Platform as a Service", "ASIC miner", "X", "idiocracy", "ELON MUSK!!!", "The Zuck", "WIRED", "tech",
             "Chatbots", "Cloud Computing", "Cryptocurrency", "Data Mining", "scams", "Python", "Digitization",
             "Digital Transformation", "Distributed Cloud", "Sustainable Technology", "Solar Powered", "mecha",
             "Digital Disruption", "Agile", "Internet of Things", "Machine Learning", "RAM", "Actionable Analytics",
             "Microservices", "Raspberry Pi", "Boot Strapping", "AWS", "BASIC", "Fortran era", "Older than COBOL",
             "User Experience", "Infrastructure as a Service"]

convo_starter = ["Get this", "So I was talking to my colleagues", "Today I", "I can't belive my mom doesn't know",
                 "Once upon a time", "DUDE!", "You know...", "OK, so:", "OMG", "", "LOL", "I'm literally",
                 "Why can't we be friends", "I was today years old when I learned that", "Ever wonder why,"
                 "Do you ever feel like a plastic bag Drifting through the wind, wanting to start again?",
                 "Do you ever feel, feel so paper-thin Like a house of cards, one blow from cavin' in?",
                 "If you want sick gains in the gym", "Today my macos were", "I'd NEVER use a Mac because",
                 "I will ONLY use a Mac because", "God these Linux guys", "I asked my girlfriend if",
                 "I need a new job because", "I deserve a raise because", "The other day I read",
                 "maybe I'm the problem but", "Game of Thrones season six be like",
                 "I just saw", "I can't get a girlfriend becuase", "I can't believe nobody at this party",
                 "Quit calling me a techo bro just because", "Bond, James Bond", "Backstreet's Back Boys!",
                 "I programed a bot to", "My brother used his raspberry pi to", "How can I help my sister understand",
                 "Last night my tinder date said", "I'm moving off this platform because","Quit calling me a techo bro just because",
                 "haters think", "quit hatin' just because", "so this is normal right?", "Has anyone really ever been as far decided to",
                 "to the bots in my replies:", "to the haters in my mentions:", "You should immediately invest in crypto because",
                 "I'm not sold on this new tech", "For the 100th time, I am not a bot!", "I have a CS degree but wouldn't need one to tell you",
                 "Get a raspberry pi they say, it's only $35 they say", "LOL Zuck really thinks", "Listen, I actually like sports."]

sign_off = ["!", "", "!!!", " :)", "...", " >:[", "!?", "???", ".", " lol!", " heck"]


def gibberish():
    len = random.choice(range(5,101))

    # makes your string 70% latin and 30% buzz words
    k = float(len) * 0.7
    j = float(len) * 0.3

    # creates and concatinates latin and buzz words
    new_list = list(random.choices(latin_list, k=int(k))) + (random.choices(tech_list, k=int(j)))
    # shuffles the order
    random.shuffle(new_list)
    # add "conversation starter"
    greeting = (random.choice(convo_starter))
    greeting = str(greeting)
    # converts to string
    print_string = ""
    for word in new_list:
        print_string += " " + word
    print_string = greeting + print_string

    print_string = print_string[0:195]
    print_string = str(print_string + random.choice(sign_off))

    return print_string

"""
def tweet_at_scheduled_time(tweet):
    api.update_status(tweet)

#one time tweet:

try:
    api.uodate_status(gibberish())
    print("tweet sucessfully sent, you can verify at {}") #need to add twitter url here
except Exception as e:
    print("Error:", e)

####

#daily tweet
schedule.every().day.at("10:00").do(tweet_at_scheduled_time, tweet = (gibberish())
while True:
    schedule.run_pending()
    time.sleep(1)

"""



