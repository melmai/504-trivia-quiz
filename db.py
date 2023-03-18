# import sqlite3
#
# conn = sqlite3.connect('questions.db')
#
# c = conn.cursor()
#
# c.execute("""CREATE TABLE IF NOT EXISTS "SAquestions" (
# 	"Type"	TEXT NOT NULL,
# 	"Question"	TEXT NOT NULL,
# 	"Choices"	TEXT,
# 	"Answer"	TEXT NOT NULL
#           ); """)
#
# c.execute("""CREATE TABLE IF NOT EXISTS "MCquestions" (
# 	"Type"	TEXT,
# 	"Question"	TEXT,
# 	"Choices"	TEXT,
# 	"Answer"	TEXT
# ); """)
# c.execute(""" CREATE TABLE IF NOT EXISTS "TFquestions" (
# 	"Type"	TEXT,
# 	"Question"	TEXT,
# 	"Choices"	TEXT,
# 	"Answer"	TEXT
# );""")
#
# #these below are short answer questions.
# c.execute(
#     """INSERT INTO SAquestions VALUES ('SA','In chess, what direction can
#     a bishop move?',NULL,'diagonally');""")
#
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','At a restaurant, you’ll see
#     deer meat on the menu under what name?',
#     NULL,'venison');""")
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','The Statue of Liberty was a
#     gift to the U.S. from what country?',NULL,
#     'france');""")
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','What alcoholic beverage is
#     made from juniper berries',NULL,'gin');""")
# c.execute("""INSERT INTO "SAquestions" VALUES ('SA','How many countries
# are in the European Union?',NULL,'27');""")
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','What musical artist played
#     27 different instruments on their debut
#     album, "For You"',NULL,'prince');""")
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','How many children are in
#     the Von Trapp family in The Sound of Music?',
#     NULL,'7');""")
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','What is the longest-running
#     band still featuring its original
#     lineup?',NULL,'u2');""")
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','How many keys are on a
#     modern, standard-sized piano?',NULL,'88');""")
# c.execute("""INSERT INTO "SAquestions" VALUES ('SA','For how many nights
# is Hanukkah celebrated?',NULL,'8');""")
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','Which famous art movement
#     did Pablo Picasso co-create?',NULL,
#     'cubism');""")
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','What is the most commonly
#     spoken language in Brazil?',NULL,
#     'portuguese');""")
# c.execute("""INSERT INTO "SAquestions" VALUES ('SA','How many bones do
# sharks have?',NULL,'0');""")
# c.execute("""INSERT INTO "SAquestions" VALUES ('SA','What is the human
# body’s largest organ?',NULL,'skin');""")
# c.execute("""INSERT INTO "SAquestions" VALUES ('SA','''Cynophobia'' is
# fear of what?',NULL,'dogs');""")
# c.execute("""INSERT INTO "SAquestions" VALUES ('SA','What is the rarest
# M&M color?',NULL,'brown');""")
# c.execute("""INSERT INTO "SAquestions" VALUES ('SA','What is the common
# name for dried plums?',NULL,'prunes');""")
# c.execute("""INSERT INTO "SAquestions" VALUES ('SA','Which country
# invented ice cream?',NULL,'china');""")
# c.execute("""INSERT INTO "SAquestions" VALUES ('SA','Dump, floater,
# and wipe are terms used in which team sport?
#
#
#
# ',NULL,'volleyball');""")
# c.execute(
#     """INSERT INTO "SAquestions" VALUES ('SA','What is the largest planet
#     in the solar system?',NULL,'jupiter');""")
#
#
# #these below are MC questions
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','What''s the largest
# bone in the human body?
#
# ','Femur, Humerus, Tibia, Sacrum','femur');""")
#
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','In the state of
# Georgia, it’s illegal to eat what with a fork?',
# 'Olives, Fried Chicken, Oreos, French Fries','fried chicken');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','What type of animal
# is a Flemish giant?','Dog, Rabbit, Bird,
# Rat','rabbit');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','Who painted "The
# Creation Of Adam"?','Monet, Rembrandt, Vermeer,
# Michelangelo', 'michelangelo');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','When was the iPhone
# released?','1999,
# 2004, 2007, 2009',  '2007');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','How many compartments
# are in a cow''s
# stomach?','2, 3, 4, 5',  '4');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','What''s a group of
# kittens called?','kindle,
# squiggle, murder, gurgle',  'kindle');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','What is the name of a
# coffee drink
# prepared by diluting espresso  with water?','americano, cortado,
# ristretto, macchiato','americano');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC', 'What type of nuts
# are a Hawaiian staple?','Peanuts, Walnuts, Macadamia nuts,
# Brazil nut','macadamia nuts');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','How many legs do
# cockroaches have? ','4, 6,
# 8, 10','6');""")
# c.execute("""INSERT INTO "MCquestions"  VALUES ('MC','How many degrees
# does the earth rotate each hour?','12, 15,
# 18, 20','15');""")
# c.execute("""INSERT INTO "MCquestions"  VALUES ('MC','What is the
# ''perfect score'' in a game of Ten Pin
# Bowling?','150, 200, 250, 300','300');""")
# c.execute("""INSERT INTO  "MCquestions" VALUES ('MC','Where were the 1920
# Olympics held?',
# 'France, Germany, Switzerland, Belgium','belgium');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','What famous character
# did Edgar Rice Burroughs create?','Tarzan,  Charlie Brown, Han Solo,
# James Bond','tarzan');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','Who was the first
# gymnast to  be awarded a perfect score of 10.0 at the Olympic Games?',
# 'Simone Biles, Larisa Latynina, Nadia Comaneci,  Beth Tweddle','nadia
# comaneci');""")
# c.execute("""INSERT INTO "MCquestions" VALUES (
# 'MC','During the American prohibition,  what was the name given to the
# illegal taverns?','Prohibition Pubs,
# Moonlighters, Speakeasies, Moonshines',  'speakeasies');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','What is the longest
# river in Ireland?','River Liffey,  Riber Shannon, River Nore,
# River Barrow','river shannon');""")
# c.execute("""INSERT INTO
# "MCquestions" VALUES ('MC','In which city can  you find JFK airport?',
# 'Johannesburg, New York, Singapore, Paris',
# 'new york');""")
# c.execute("""INSERT INTO "MCquestions" VALUES (  'MC','Which Pixar movie
# is about two robots who fall in love in
# space?','Wall-E, Finding Dory, Onward, Soul',  'wall-e');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','Which color is the
# ''E'' in the official Google logo?','Red,  Green, Blue, Yellow','red');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC',
# 'What is the highest grossing video game  franchise to date?','Pokemon,
# Pacman, Mario, Call of duty','pokemon');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC',  'Which coffee chain
# is named after a character in Moby Dick by Herman
# Melville','Starbucks, Dutch Bros, Pret, Nero',  'starbucks');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','Which fruit is
# at the top of the Wimbledon gentlemen''s singles  trophy?','Apple,
# Strawberry, Pineapple, Pear','pineapple');""")
# c.execute("""INSERT INTO "MCquestions" VALUES ('MC','In Home Alone,
# where were the McCallister flying to when they left Kevin?',
# 'France, Japan, England, Ireland','france');""")
# c.execute("""INSERT INTO  "MCquestions" VALUES ('MC','What''s Garfield
# favorite
# food?','Chicken, Spaghetti, Lasagna, Steak','lasagna');""")
#
# #below are TF questions
# c.execute("""INSERT  INTO "TFquestions" VALUES ('TF','True or False: New
# York City is composed of between 36 and 42 islands.','',  'true');""")
# c.execute("""INSERT INTO "TFquestions" VALUES ('TF',
# 'True or False: Aladdin''s character was based on Tom Cruise','',
# 'true');""")
# c.execute("""INSERT INTO "TFquestions" VALUES ('TF',
# 'True or False: Pixar''s first film was "A Bug''s Life"','',  'false');""")
# c.execute("""INSERT INTO "TFquestions" VALUES ('TF',
# 'True or False: Dumbo is the shortest Disney film','',  'true');""")
# c.execute("""INSERT INTO "TFquestions" VALUES ('TF',
# 'True or False: Pineapples grow on trees','','false');""")
# c.execute("""INSERT INTO  "TFquestions" VALUES ('TF','True or False: Every
# golf ball has the same number of dimples','','false');""")
# c.execute("""INSERT INTO  "TFquestions" VALUES ('TF','True or False: Three
# strikes in a row in bowling is called a chicken','','false');""")
# c.execute("""INSERT  INTO "TFquestions" VALUES ('TF',
# 'True or False: Fortune cookies were invented in China','','false');""")
# c.execute("""INSERT INTO  "TFquestions" VALUES ('TF',
# 'True or False: Every country in the world has a rectangular flag','',
# 'false');""")
# c.execute("""INSERT  INTO "TFquestions" VALUES (
# 'TF','True or False: The oldest soft drink in America is Dr. Pepper','',
# 'true');""")
# c.execute("""INSERT  INTO "TFquestions" VALUES (
# 'TF','True or False: An astronaut has played golf on the moon','',
# 'true');""")
# c.execute("""INSERT INTO  "TFquestions" VALUES ('TF',
# 'True or False: Saffron is the world''s most expensive spice?','',
# 'true');""")
# c.execute("""INSERT INTO  "TFquestions" VALUES ('TF',
# 'True or False: Bats are blind','','false');""")
# c.execute("""INSERT INTO "TFquestions" VALUES ('TF',  'True or False: The
# first tea
# bags were made of cotton.','','false');""")
# c.execute("""INSERT INTO "TFquestions" VALUES ('TF',  'True or False: The
# founding member
# of the English rock band The Beatles was Paul McCartney','','false');""")
# conn.commit()
# conn.close()
