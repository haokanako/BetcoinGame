from flask import Flask, render_template, request
import random

app = Flask(__name__)

motivational_quotes = [
    "「不赌你就赢了，你赌，你就输定了，而要想不输，只有一个办法，就是远离赌博。」——赌徒",
    "「小赌怡情，大赌要命，其实，大赌就是从小赌开始的。」——赌徒",
    "「澳门过三关，还不是想吃啥吃啥。」——赌徒",
    "「十个赌徒九个输，倾家荡产不如猪。」——戒赌吧",
    "「小赌怡情，大赌要命”，其实，大赌就是从小赌开始的。」——赌徒",
    ""
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    initial_balance = float(request.form['initial_balance'])
    num_rounds = int(request.form['num_rounds'])

    # Game logic
    balance = initial_balance
    game_results = []

    for _ in range(num_rounds):
        result = random.choice(['正面', '反面'])
        if result == '正面':
            balance *= 0.5
        else:
            balance *= 2
        game_results.append((result, balance))

    final_balance = game_results[-1][1]

    total_profit_loss = final_balance - initial_balance
    percentage_change = (total_profit_loss / initial_balance) * 100

    random_quote = random.choice(motivational_quotes)

    return render_template('play.html',
                           initial_balance=initial_balance,
                           num_rounds=num_rounds,
                           game_results=game_results,
                           final_balance=final_balance,
                           total_profit_loss=total_profit_loss,
                           percentage_change=percentage_change,
                           random_quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True)
