from flask import Flask, render_template, request
from app.game_logic import get_computer_choice, determine_winner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        player_choice = request.form.get('choice')
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        return render_template('index.html', player_choice=player_choice, computer_choice=computer_choice, result=result)
    return render_template('index.html', player_choice=None, computer_choice=None, result=None)