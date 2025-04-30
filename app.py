from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Load plant data
with open('plants.json', 'r') as f:
    plants = json.load(f)

# Daily fact
def get_daily_fact():
    facts = [p['fact'] for p in plants if 'fact' in p]
    return random.choice(facts) if facts else "No fact available."

@app.route('/')
def home():
    return render_template('home.html', plants=plants, fact=get_daily_fact())

@app.route('/plant/<name>')
def plant_details(name):
    plant = next((p for p in plants if p["name"].lower() == name.lower()), None)
    if plant:
        return render_template('plant_details.html', plant=plant)
    return "Plant not found"

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)
