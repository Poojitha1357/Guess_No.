from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for session management (if needed)

# Initialize secret number between 1 and 100 for guessing
secret_number = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def index():
    global secret_number
    message = None  # Feedback message for user
    win = False    # Flag to indicate if user won

    if request.method == 'POST':
        guess = request.form.get('guess')  # Get user input from form
        if guess:
            try:
                guess = int(guess)  # Convert input to integer
                if guess == secret_number:
                    message = "🎉 Correct! You win!"
                    win = True
                    # Reset the secret number for a new game
                    secret_number = random.randint(1, 100)
                elif guess < secret_number:
                    message = "Too low! Try again."
                else:
                    message = "Too high! Try again."
            except ValueError:
                message = "Please enter a valid number."  # Handle non-integer input
        else:
            message = "Please enter a valid number."  # Handle empty input

    # Render HTML template with message and win status
    return render_template('index.html', message=message, win=win)

if __name__ == '__main__':
    app.run(debug=True)  # Run Flask app in debug mode for development
