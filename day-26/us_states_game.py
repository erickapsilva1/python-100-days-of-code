import turtle, pandas

screen = turtle.Screen()
screen.setup(725,491)
screen.title("U. S. States Game")
image = "files/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
turtle.tracer(False)

data = pandas.read_csv("files/50_states.csv")
correct_guess = []

us_states = data.state.to_list()
us_states_count = len(data["state"])

title_phrase = "Guess the State"

while not len(correct_guess) == us_states_count:
    answer_state = screen.textinput(title=title_phrase, prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in us_states if state not in correct_guess]

        df = pandas.DataFrame(missing_states)
        df.to_csv("game_result.csv")

        break

    if answer_state in us_states:
        correct_guess.append(answer_state)
        title_phrase = f'{len(correct_guess)}/{us_states_count} States Correct'
        coord = data[data['state'] == answer_state][['x', 'y']].values.flatten()
        turtle.penup()
        turtle.setposition(coord)
        turtle.write(answer_state)
        turtle.setposition(0, 0)


screen.exitonclick()
