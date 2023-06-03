

import pandas as pd 
import random


username = [
    "Marquisette",
    "Roustabout",
    "Metameric",
    "Rasmus2god",
    "Cromlech",
    "Hodgepodge",
    "Durometer",
    "Eructation",
    "Eutrapely",
    "Mellifluous",
    "Weirdward",
    "HoiPolloi",
    "Inurbanity",
    "Svengali",
    "Aurulent",
    "Contraband",
    "Affreux",
    "Webinar",
    "CocopErgo",
    "XxbluekJetsam",
    "Inviscate",
    "Scofflaw",
    "Aduncate",
    "Cantankerous",
    "Stigmatic",
    "Hothead",
    "Subduct",
    "Buckaroo",
    "Vitellary",
    "Umpteen",
    "ArcuatDiable",
    "Filibuster",
    "DickfarSley",
    "SfevansQuack",
    "Homiliary",
    "Roundabout",
    "Nickelodeon",
    "Curlicue",
    "WtgshadowsMulley",
    "Gallimaufry",
    "Belonoid",
    "Crescendo",
    "Bortna123",
    "Folderol",
    "Choller",
    "Blogosphere",
    "Samajni1700",
    "Flophouse",
    "Gypsography",
    "Cuirass",

]

random_date = [
    "1940-09-11",
    "1942-04-15",
    "1947-04-09",
    "1947-08-13",
    "1947-10-29",
    "1947-12-31",
    "1956-10-10",
    "1957-01-09",
    "1957-08-28",
    "1960-01-13",
    "1960-05-11",
    "1969-02-12",
    "1977-09-14",
    "1977-10-05",
    "1982-03-10",
    "1987-11-11",
    "1988-08-24",
    "1990-07-04",
    "1993-09-08",
    "1993-09-22",
    "1999-02-17",
    "1999-03-31",
    "1999-04-14",
    "2002-09-04",
    "2003-12-24",
    "1942-06-17",
    "1947-12-10",
    "1957-09-18",
    "1959-06-10",
    "1963-10-02",
    "1966-05-11",
    "1971-04-07",
    "1972-05-03",
    "1972-08-30",
    "1978-09-06",
    "1981-10-21",
    "1984-05-02",
    "1988-10-26",
    "1989-01-18",
    "1989-03-15",
    "1989-11-22",
    "1995-07-19",
    "1996-03-27",
    "1996-05-29",
    "1996-09-18",
    "1997-01-29",
    "1998-06-03",
    "2000-09-27",
    "2001-08-15",
    "2007-05-16"
]

company = [
    "google.com",
    "yahoo.com",
    "protonmail.com",
    "hotmail.com",
    "outlook.com"
]

passwd = [
    "y5=3]N-",
    "yk0-VzG",
    "tI60r+!",
    "L+B&n18",
    "S7m)9+M",
    "a=K5U0M",
    "A*hmS9g",
    "w_!W[6S",
    "aj'!L1j",
    "bHeB7&6",
    "M2&>Nu&",
    "A1>e?R]",
    "Hvf#e1s",
    "VA[7d'O",
    "t){5PYm",
    "cKSX!5e",
    "of5Y+vb",
    "Zj5)O%x",
    "G1>im}r",
    "qq_Q2*v",
    "Z]k6$K?",
    "M*z$C4Y",
    "D+6&xyu",
    "Mv!Jv2Z",
    "iN%0N9n",
    "Rp50f#|",
    "U[|1k'k",
    "P1@{g6_",
    "yx?1Px_",
    "sU4]_AA",
    "Cxo}7C8",
    "y5M_j{0",
    "Ai63I_r",
    "oA=a3#&",
    "Dp{9o[W",
    "b9C<(5{",
    "Y3%e7{*",
    "a!84D}H",
    "Yc}&0mk",
    "B%8mGHa",
    "g'9xT4J",
    "Zle5$zu",
    "n3+I-(*",
    "R@bm3lM",
    "T5%tjQ(",
    "SflZ%4g",
    "S|2d@ZG",
    "bU{%0d%",
    "K|3S]tm",
    "B*m5)Bh"
]


emails = []




data = pd.read_csv("data/userinfov1.csv")


for _,row in data.iterrows():
    
    comp = company[random.randint(0, 4)]  
    nb_fname = random.randint(1,3)

    email = f"{row['fname'][:nb_fname]}{row['lname']}@{comp}"

    emails.append(email.lower())


data["email"] = emails
data["bday"] = random_date
data["username"] = list(map(lambda x: x.lower(),username))
data["passwd"] = passwd 

data.to_csv("data/userinfov2.csv",index=False)

