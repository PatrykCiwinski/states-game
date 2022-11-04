import turtle
import pandas
screen=turtle.Screen()
screen.title("USA states")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

score=0
guessed_states=[]
game_is_on=True
while game_is_on:
    answer=screen.textinput(f"Score is {score}/50","name the state").title()

    if answer=="Exit":
        missing_states=[state for state in states if state not in guessed_states]
        missing_data=pandas.DataFrame(missing_states)
        missing_data.to_csv("missing_states.csv")
        break
    if answer in states:
        guessed_states.append(answer)
        score += 1
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer, align="center", font=("Arial", 14, "bold"))
        if score>50:
            game_is_on=False

