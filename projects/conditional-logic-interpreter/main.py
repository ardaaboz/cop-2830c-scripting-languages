# Should I play DnD tonight?

questions = [
    "Do you feel like playing?",
    "Is the session scheduled for today?",
    "Do you have time?",
    "Do you need to do homework?",  # Note: "yes" means you shouldn't play
    "Are all your friends ready?",
    "Is the session prepared?"
]

def userChoice(answer):
    if answer.lower() == "y":
        return True
    else:
        return False

# List to store the answers
conditions = []

print("Answer these questions with y/n:")

for question in questions:
    answer = input(question + " ")
    conditions.append(userChoice(answer))

feel_like_playing, session_today, have_time, have_homework, friends_ready, session_prepared = conditions

if (feel_like_playing or session_today) and (have_time and not have_homework) and (friends_ready and session_prepared):
    print("You should play DnD tonight!")
else:
    print("You should not play DnD tonight!")