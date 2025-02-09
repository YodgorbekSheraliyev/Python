from flask import Flask, render_template
import random
import os
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = my_list[2::3]
print(new_list)
# app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

# @app.route("/")
# def get_home():
#     return render_template('index.html', name="MY TEMPLATE")


# def my_func(num):
    
#     random_num = random.Random(0, 9)
#     if num > random_num:
#         return f"{num} is too high"
#     elif num < random_num:
#         return f"{num} is lower"
#     else:
#         return f"You found me "

#         pass

# app.run(port=5000, debug=True)
