def userChoice(String answer) {
    if (answer.toLowerCase() == 'y') {
        return true
    } else {
        return false
    }
}

static void main(String[] args) {

    def console = System.console()

    def questions = ["Do you feel like playing?",
            "<Is the session scheduled for today?",
            "Do you have time?",
            "Do you need to do homework?", // Note: "yes" means you shouldn't play
            "Are all your friends ready?",
            "Is the session prepared?"
    ]

    def conditions = []

    println("Answer these questions with y/n:")

    for (question in questions) {
        def answer = console.readLine(question + " ")
        conditions.add(userChoice(answer))
    }

    def (feel_like_playing, session_today, have_time, have_homework, friends_ready, session_prepared) = conditions

    if ((feel_like_playing || session_today) && (have_time && !have_homework && friends_ready && session_prepared)) {
        println("You should play DnD tonight!")
    } else {
        println("You should not play DnD tonight!")
    }






}