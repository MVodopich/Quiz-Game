answer = input("Welcome to my quiz!! Do you want to play? ")
if answer != "yes":
    print("Ok, maybe next time. Bye!")
    quit()

print("Let's continue then!")
answer = input("What year did the United States declare independence from Great Britain? ")
number_correct = 0
if answer == "1776":
    print("Correct!")
    number_correct = 0 + 1
if answer != "1776":
    print("Incorrect. Next question")

answer = input("Are cows ruminants? Yes or No: ")
if answer == "yes":
    print("Correct!")
    number_correct = number_correct + 1
else:
    print("Incorrect. Next Question")

answer = input("How many bones are there in the adult human body? ")
if answer == "206":
    print("Correct!")
    number_correct = number_correct + 1
else:
    print("Incorrect. Next Question")

answer = input("What's the biggest state in the United States? ")
if answer == "Alaska":
    print("Correct!")
    number_correct = number_correct + 1
else:
    print("Incorrect. Next question")

print("Congrats!! You got " +str(number_correct)+ " out of 4 questions correct!")
print("Please play again sometime. Bye!")


