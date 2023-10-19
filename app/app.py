from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data storage. Replace this with a database in production.
users = []

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_confirmation = request.form['password_confirmation']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_of_birth = request.form['date_of_birth']
        height = request.form['height']
        city = request.form['city']
        province = request.form['province']
        country = request.form['country']
        biography = request.form['biography']
        hobbies = request.form['hobbies']
        likes = request.form['likes']
        
        # Save the user data to the storage (for demo purposes)
        users.append({
            'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'height': height,
            'city': city,
            'province': province,
            'country': country,
            'biography': biography,
            'hobbies': hobbies,
            'likes': likes,
        })

        # Redirect the user to the login page after successful registration
        return redirect(url_for('login'))

    return render_template('register.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Perform user authentication here (e.g., check if the user exists in the database)
        # For this example, we assume that the user exists and log them in directly.

        # Redirect the user to their profile page after successful login
        return redirect(url_for('profile', username=username))

    return render_template('login.html')

# Route for user profile page
@app.route('/profile/<username>')
def profile(username):
    # Fetch the user data from the database based on the provided username
    # For this example, we use the dummy user data storage.
    user_data = next((user for user in users if user['username'] == username), None)

    if user_data:
        return render_template('profile.html', user=user_data)
    else:
        return "User not found."

# Route for logging out
@app.route('/logout')
def logout():
    # Perform logout functionality here (e.g., clear user session)
    # For this example, we simply redirect the user to the home page.
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)