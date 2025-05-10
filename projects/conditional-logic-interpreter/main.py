# Should I play DnD tonight?

print("Answer these questions with y/n:")

answer = input("Do you feel like playing? ")
if answer == 'y':
    feel_like_playing = True
else:
    feel_like_playing = False

answer = input("Is the session scheduled for today? ")
if answer == 'y':
    session_today = True
else:
    session_today = False

answer = input("Do you have time? ")
if answer == 'y':
    have_time = True
else:
    have_time = False

answer = input("Do you need to do homework? ")
if answer == 'y':
    have_homework = True
else:
    have_homework = False

answer = input("Are all your friends ready? ")
if answer == 'y':
    friends_ready = True
else:
    friends_ready = False

answer = input("Is the session prepared? ")
if answer == 'y':
    session_prepared = True
else:
    session_prepared = False

if (feel_like_playing or session_today) and (have_time and not have_homework) and (friends_ready and session_prepared):
    print("You should play DnD tonight!")
else:
    print("You should not play DnD tonight!")