import turtle  
import pandas
from state import State

states_data = pandas.read_csv('./50_states.csv')

states_data_list = states_data['state'].values.tolist()
state_coor_list = states_data.values.tolist()
screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

for index in range(len(states_data_list)):
    states_data_list[index] = states_data_list[index].lower()


score_value = 0
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.penup()
score.goto(-screen.canvwidth + 50, screen.canvheight - 20)
score.color("green")
score.write(f"Score {score_value}/50", font=('Arial', 20, "italic"))
for i in range(50):
    guess_state = screen.textinput("Enter the state name: ", "Enter the state name: ").lower()
    if guess_state == "exit":
        exit()
    if guess_state in states_data_list:
        score_value +=1
        score.clear()
        score.write(f"Score {score_value}/50", font=('Arial', 20, "italic"))
        index = states_data_list.index(guess_state)
        x_cor = state_coor_list[index][1]
        y_cor = state_coor_list[index][2]
        State((x_cor, y_cor), guess_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()