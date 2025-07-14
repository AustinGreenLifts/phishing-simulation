from flask import Flask, render_template, request
from email_sender import send_email  # Importing the send_email function

app = Flask(__name__)

def generate_phishing_email(name):
    return f'''
    <html>
    <head></head>
    <body>
        <h2>Hello {name},</h2>
        <p>This is a simulated phishing email.</p>
        <p><a href="{Insert-Link}">Click here</a> to claim your bonus.</p>
    </body>
    </html>
    '''

@app.route('/')
def index():
    return render_template('index.html')  # Render the main page

@app.route('/send-phishing', methods=['POST'])
def send_phishing_email():
    recipient = request.form['email']
    subject = "Phishing Simulation"
    body = generate_phishing_email('Employee')  # Generate email content

    send_email(subject, 'Trevor Poe', [recipient], body)  # Send email
    return f"Phishing email sent to {recipient}!"

if __name__ == '__main__':
    app.run(debug=True)
