import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
#screen.title.goto()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
country_list = data["state"].to_list()
cor_x = data["x"].to_list()
cor_y = data["y"].to_list()
score = 0
game_on = True
correct_guesses = []

while game_on:

    answer_state = screen.textinput(title = f"{len(correct_guesses)}/ 50, guess the state", prompt = "What's another state's name?,").title()



    """if answer_state == "Exit":
        missing_states = []
        for state in country_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_on = False"""

    if answer_state == "Exit":
        missing_states = [state for state in country_list if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_on = False

    if answer_state == country:
        #correct_answer = screen.textinput(title= {country})
        new_country = turtle.Turtle("square")
        new_country.hideturtle()
        #screen.update(0.1)
        new_country.penup()
        new_country.goto(x=cor_x[country_list.index(country)], y=cor_y[country_list.index(country)])
        new_country.write(country)
        score += 1
        correct_guesses.append(country)
        if score == len(country_list):
            game_on = False



print("You win!")
screen.exitonclick()



