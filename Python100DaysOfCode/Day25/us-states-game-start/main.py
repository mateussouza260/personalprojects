import turtle
import pandas
import states

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
new_state = states.States()

df = pandas.read_csv("50_states.csv")
state_names = df.state.to_list()
print(state_names)
guessed_states = []
not_guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name")
    answer_state = str(answer_state).title()
    if answer_state == "Exit":
        for st in state_names:
            if st not in guessed_states:
                not_guessed_states.append(st)
        data = pandas.DataFrame(not_guessed_states)
        data.to_csv("not_guessed_states.csv")
        print("break")
        break
    for s in state_names:
        if s == answer_state:
            guessed_states.append(s)
            state = df[df["state"] == answer_state]
            x_cor_state = int(state["x"])
            y_cor_state = int(state["y"])
            new_state.create_state(name=answer_state, x=x_cor_state, y=y_cor_state)



screen.exitonclick()
