import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game Start")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter state name")

    if answer_state is None:
        break  # If user clicks Cancel, break the loop

    answer_state = answer_state.title()

    if answer_state=='Exit':
        missing_states=[]
        for state in data.state:
            if state not in guessed_states:
                missing_states.append(state)

            new_data = pandas.DataFrame(missing_states)

            new_data.to_csv("missing_states.csv")
    if answer_state in data.state.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(int(state.x.iloc[0]), int(state.y.iloc[0]))
        writer.write(answer_state)


