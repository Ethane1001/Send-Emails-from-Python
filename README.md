# Python Email Sender

## Description
This Python script enables users to send emails using the SMTP protocol with SSL encryption. Designed for simplicity and ease of use, it's configured for Gmail by default but can be adapted for other email providers. The script is ideal for automating email sending tasks, whether for personal reminders, automated notifications, or as part of a larger Python project.

## How to Use

1. **Set Email Credentials**: For security, do not hard-code your email credentials. Instead, use environment variables or other secure methods to store your email address and password.

2. **Modify the Script**: Update the `email_sender`, `email_receiver`, `subject`, and `body` variables in the script to match your sending and receiving details.

3. **Run the Script**: Execute the script using Python. If set up correctly, it will send an email to the specified recipient.

## Note on Security
The script uses SSL for security during email transmission. Be cautious with your email credentials; avoid storing them directly in the script or in public repositories.
