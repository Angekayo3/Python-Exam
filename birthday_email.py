import smtplib  # Used to send emails using SMTP
from email.mime.text import MIMEText  # Used to create the email content
import datetime  # Used to get the current date
import csv  # Used to read the CSV file

# Function to send a birthday email
def send_birthday_email(name, email):
    sender_email = "akondipjerry.ebai"  # Your email address
    sender_password = "ckxexmuohugigbnu"  # Your email password (use environment variables for security)
    subject = "Happy Birthday!"  # Subject of the email
    body = f"Dear {name},\n\nHappy Birthday from ICT University\n\nBest Wishes,\nICT University"  # Email body

    # Create the email message
    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)  # Login to your email account
        server.sendmail(sender_email, email, msg.as_string())  # Send the email
        server.quit()  # Disconnect from the server
        print(f"Birthday email sent to {name} at {email}")
    except Exception as e:
        print(f"Failed to send email to {name}: {e}")

# Function to check and send birthday emails
def check_and_send_birthday_emails():
    today = datetime.datetime.now().strftime("%m-%d")  # Get today's date in MM-DD format
    with open('employees.csv', newline='') as csvfile:  # Open the CSV file
        reader = csv.DictReader(csvfile)  # Create a CSV dictionary reader
        for row in reader:  # Iterate over each row in the CSV file
            try:
                print(f"Processing row: {row}")  # Debugging statement to show the current row being processed
                birthdate = datetime.datetime.strptime(row["birthdate"], "%Y-%m-%d").strftime("%m-%d")  # Convert birthdate to MM-DD format
                if birthdate == today:  # Check if today is the employee's birthday
                    send_birthday_email(row["name"], row["email"])  # Send birthday email
            except KeyError as e:
                print(f"Skipping row due to missing key: {e}")  # Handle missing keys in the CSV file
            except ValueError as e:
                print(f"Skipping row due to invalid date format: {e}")  # Handle invalid date formats

# Main entry point of the script
if __name__ == "__main__":
    check_and_send_birthday_emails()  # Call the function to check and send birthday emails
