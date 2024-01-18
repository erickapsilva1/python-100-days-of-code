import turtle, pandas

screen = turtle.Screen()
screen.setup(725,491)
screen.title("U. S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
turtle.tracer(False)

data = pandas.read_csv("50_states.csv")
correct_guess = []

us_states = data["state"]
us_states_count = len(data["state"])

title_phrase = "Guess the State"

while not len(correct_guess) == us_states_count:
    answer_state = screen.textinput(title=title_phrase, prompt="What's another state's name?")
    answer_state = answer_state.title()
    check = len(data[data["state"] == answer_state])

    if check == 1:
        correct_guess.append(answer_state)
        title_phrase = f'{len(correct_guess)}/{us_states_count} States Correct'
        coord = data[data['state'] == answer_state][['x', 'y']].values.flatten()
        turtle.penup()
        turtle.setposition(coord)
        turtle.write(answer_state)
        turtle.setposition(0, 0)

screen.exitonclick()
