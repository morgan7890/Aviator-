from flask import Flask, render_template
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def get_aviator_data():
    # Simulated Aviator odds data (replace with real data fetching logic later)
    return [1.2, 2.5, 1.8, 3.1, 1.1, 2.2, 1.9, 2.8]

def create_chart(data):
    # Ensure 'static' directory exists
    os.makedirs('static', exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(data, marker='o', linestyle='-', color='blue')
    plt.title("Aviator Odds History")
    plt.xlabel("Game Round")
    plt.ylabel("Multiplier (x)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('static/chart.png')
    plt.close()

@app.route('/')
def home():
    data = get_aviator_data()
    create_chart(data)
    return render_template('index.html', chart_url='static/chart.png')

if __name__ == '__main__':
    app.run(debug=True)
