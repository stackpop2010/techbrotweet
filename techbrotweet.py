#This is a silly twitter bot I programmed from what I learned in CS 161 and 162, and from reading the tweepy documentation.
#The bot takes random tech buzzwords, latin, silly hashtags, etc and mashes them together into a nonsense tweet
#Bot's hijinks can be viewed at https://x.com/_techbrobot
#Recommend implementing with gunicorn


import tweepy
import random
import time
import schedule


api_key = #"YOUR_API_KEY"
api_secret = #'YOUR_API_SECRET'
access_token = #'YOU_ACCESS_TOKEN'
access_token_secret = #'YOUR_ACCESS_TOKEN_SECRET'
client_id = #your_client_id
client_secret = #your_secret
bearer_token = #your_bearer_token

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)



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
             "qualatively bad", "quantum mechanics", "QC", "quality assurance", "algorithm", "kotaku", "MCU", "MAANG",
             "Bitcoin", "Luna", "monero", "Snowden", "crapware", "malware", "bloatware", "Outlook", "GMAIL", "chicky nuggy",
             "defi", "App", "Star my repo please", "Fintech", "Data Science?!", "Data Science, I guess", "Deeplearning",
             "FAANG", "Web3", "Multiexperience", "Google", "Cloud-Native Platforms", "Big Data", "Social Media",
             "Platform as a Service", "ASIC miner", "X", "idiocracy", "ELON MUSK!!!", "The Zuck", "WIRED", "tech",
             "retrospective", "bug report", "integration", "lead time",
             "Chatbots", "Cloud Computing", "Cryptocurrency", "Data Mining", "scams", "Python", "Digitization",
             "Digital Transformation", "Distributed Cloud", "Sustainable Technology", "Solar Powered", "mecha",
             "Digital Disruption", "Agile", "Internet of Things", "Machine Learning", "RAM", "Actionable Analytics",
             "Microservices", "Raspberry Pi", "Boot Strapping", "AWS", "BASIC", "Fortran era", "Older than COBOL",
             "User Experience", "Infrastructure as a Service", "AMD", "Intel", "NVIDIA", "Linux", "Planning Poker",
             "Backlog", "Fungible", "FIFO", "Fiduciary", "Password Manager", "High Powered GPU", "META", "Metaverse",
             "ISO 9000", "Clean Room", "High Spec Hardware", "Middle Out Compression", "Boolean Logic", "Logic Gates"
             "Bottleneck", "Gantt Charts", "Iteration", "Kanban", "Configuration", "Release Planning", "Windows Vista",
             "RGB Lighting", "TWITCH", "Live Stream", "Encapsulation", "P2P Network", "Open Source", "Scripted",
             "SNAFU", "Laptop", "Client", "E2E Encryption", "Leaked", "Techno Wizard", "Flask",]

convo_starter = ["Get this", "So I was talking to my colleagues", "Today I", "I can't believe my mom doesn't know",
                 "Once upon a time", "DUDE!", "You know...", "OK, so:", "OMG", "", "LOL", "I'm literally",
                 "Why can't we be friends", "I was today years old when I learned that", "Ever wonder why,"
                 "Do you ever feel like a plastic bag Drifting through the wind, wanting to start again?", "Tech Bros Be Like:",
                 "RIP all my gains", "Tech stocks are", "Wait so this is X now??", "No really, where does MicRib go every year?",
                 "Do you ever feel, feel so paper-thin Like a house of cards, one blow from cavin' in?",
                 "If you want sick gains in the gym", "Today my macos were", "I'd NEVER use a Mac because",
                 "My roommate is driving me nuts", "I can't find my protein shaker",
                 "I will ONLY use a Mac because", "God these Linux guys", "I asked my girlfriend if", "bro",
                 "so I was telling my scrum master", "our idiot QA tester", "I have to refactor my code base because",
                 "Pair programming is aesome because", "Pair programming sucks because", "Please, please, please star my repo bro",
                 "I need a new job because", "I deserve a raise because", "The other day I read", "Thoughts and prayers for",
                 "maybe I'm the problem but", "Game of Thrones season six be like", "I was helping my 80 year old grandfather set up Linux and"
                 "Last week while I was waiting in line for street tacos", "You ever hear a Kpop song and wonder if it's about",
                 "I just saw", "I can't get a girlfriend because", "I can't believe nobody at this party", "What year is it",
                 "Quit calling me a techo bro just because", "Bond, James Bond", "Backstreet's Back Boys!", "It's so lit that",
                 "I programed a bot to", "My brother used his raspberry pi to", "How can I help my sister understand",
                 "Last night my tinder date said", "I'm moving off this platform because", "At my hackathon over the weekend",
                 "haters think", "quit hatin' just because", "so this is normal right?", "Has anyone really ever been as far decided to",
                 "to the bots in my replies:", "to the haters in my mentions:", "You should immediately invest in crypto because",
                 "I'm not sold on this new tech", "For the 100th time, I am not a bot!", "I have a CS degree but wouldn't need one to tell you",
                 "Get a raspberry pi they say, it's only $35 they say", "LOL Zuck really thinks", "Listen, I actually like sports.",
                 "yo get this", "No I do not watch Big Bang Theory but", "Hello World:", "hey Twitter heyyyy:",
                 "I trained a bot to read", "I'm very employable because I understand", "Don't go chasing waterfalls",
                 "Hear me out, Vista was actually good", "M@stad0n isn't even that good", "Let me explain the Godfather to you",
                 "The central theme in the original Gundam series was about the future of", "ever wonder why", "Why does",
                 "Call me crazy, but I think middle out compression could work", "What is my dog thinking when",
                 "I'm not even that drunk but", "I'm drunk AMA about:", "He was a punk, she did ballet, what more can I say",
                 "I'm an Elon stan because", "Bezos isn't evil, he's just misunderstood", "What if", "Hey Alexa", "OK Google",
                 "SIRI HELP!!!", "Jackie Chan could take Bruce Lee in a fight if", "Anyone know how to fix my toaster's wifi",
                 "My Tesla stock", "Why invest in S&P500 when bitcoin is doing numbers", "It's so mid when", "I only just noticed",
                 "Some of my coworkers don't even game. What are they doing in tech??", "You guys", "Well", "Hot take:",
                 "I almost got fired because my boss thinks", "I'm definitely the Wayne Gretsky of coding", "This goes hard",
                 "What if I told you I'm the Michael Jordan of Ruby on Rails", "I had to break up with my girlfriend because",
                 "Why get redpilled when you could drink another Red Bull and write more code", "It's hard to be humble when",
                 "Damn I just found some MtG cards in my", "Bezos, Zuck, and Musk walk into a bar", "Let it be known",
                 "Bezos, Zuck, and Musk walk into a sewer", "I wonder how Bill Gates feels about being poor", "I'm absolutely on fire today, but like a dumpster fire",
                 "Crap, I can't tell which of these 30 white Teslas in the Best Buy Parking Lot is mine", "God bless this mess!",
                 "I never wear a black hoodie to work because I don't want to be mistaken for a hacker", "I'm back",
                 "Pizza is great, but have you heard about", "I lost my M@sta0n password so I'm back on Twitter",
                 "I'm really sick of all the resturants by my work", "I'm really sick of all the resturants near my condo",
                 "It has to be said - The Snyder cut is overrated. Doesn't even account for", "this may age poorly...",
                 "My mom kicked me off her Netflix account so I have to", "It's Wednesday my dudes", "RT if",
                 "I may not understand women, but at least I know", "Did you know?", "Unbelievable:", "Spread the word:",
                 "LMFAO why are you all choosing to be poor when Luna is basically free right now", "TFW...",
                 "If you enjoy this content, you can support me on Patreon where I:", "I'm so high [on life] right now...",
                 "Please star my repo! I've added features that", "we're doomed...", "JavaScript is actually good because"]

sign_off = ["!", "", "!!!", " :)", "...", " >:[", "!?", "???", ".", " lol!", " heck", " SAD!", "Huh?", "8)", "thanks Obama", "It just goes hard",
            " And that's a wrap", " Mic drop", " Good night.", " Don't forget to star my repo!", "we're doomed!", "I mean... bruh"]

hash_tag = ["#lol", "#techlife", "#corporatehell", "#wtfm8", "#epicfail", "#fail", "#epicwin", "#owned", "#whatsmyageagain",
            "#wtf", "#freebritney", "#player", "#whoisjohngalt", "#crypto", "#linux", "#macos", "#california", "#anime",
            "#marchmadness", "#communism", "#FML", "#TIFU", "#WoW", "#AOC", "#AC", "#javascript", "#seaoftheives", "#MtG",
            "#iphone", "#greenday", "#friday", "#cats", "#tbt", "#mcm", "#wcw", "#giveaway", "#contest", "#qa", "#sad",
            "#funny", "#vegan", "#blockcain", "#fintech", "#datascience", "#goals", "#blessed", "#notabot", "#android",
            "#badnews", "#goodnews", "#fakenews", "#programming", "#java", "#showerthoughts", "#python"  "#webdev", "#pooping",
            "#app", "#defi", "#winning", "#NBA", "#NFL", "#NHL", "#NBL", "#NHRA", "#NASCAR", "#yourmom", "#dadbod",
            "#techbro", "#windowsinsider", "#flipphone", "#craftbeers", "#reddit", "#twitter", "#metaverse", "#alexa",
            "#siri", "#google", "#tesla", "#mid", "#lit", "#rgb", "#emo", "#astronomy", "#agronomy", "#hackathon",
            "#hacking", "#github", "#twitch", "#youtube", "#superbowl", "#MCU", "#startrek", "#starwars", "#100daysofcode",
            "#fitintech", "#micdrop", "#ufc", "#tft", "#fortnight", "#fps", "#overwatch", "#pupg", "#valorant",
            "#apex", "#halo", "#doom", "#onion", "#tacos", "#hottake", "#spread the word", "#pleaseretweet"]


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

    print_string = print_string[0:250]
    print_string = str(print_string + (random.choice(sign_off)) + (" " +random.choice(hash_tag)))

    #return print_string
    return client.create_tweet(text=print_string)

#print(gibberish())


#schedules hourly tweet
#change return statement to return client.create_tweet(text=print_string)


schedule.every().hour.do(gibberish)
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

#sends text tweet, works
client.create_tweet(text=gibberish())

#reply to tweets, works
#client.create_tweet(in_reply_to_tweet_id=1759334988875776342, text=gibberish())
