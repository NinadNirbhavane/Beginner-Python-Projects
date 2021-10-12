#string concatenation
#suppose we want to create a string that says "subscribe to ____" youtuber = " " 

# Youtuber = "BoomObsi"
# #few ways to do so
# print("Subscribe to " + Youtuber)
# print("subscribe to {}".format(Youtuber))
# print(f"subscribe to {Youtuber}")

adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because I love \
to {verb1}. Stay hydrated and {verb2} like you are {famous_person} "

print(madlib)