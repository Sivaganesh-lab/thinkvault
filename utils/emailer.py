import smtplib
from email.message import EmailMessage

def send_certificate(email_to, file_path):
    msg = EmailMessage()
    msg["Subject"] = "Your ThinkVault Certificate"
    msg["From"] = "your_email@gmail.com"
    msg["To"] = email_to
    msg.set_content("Your idea certificate is attached.")

    with open(file_path, "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename="certificate.pdf")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("your_email@gmail.com", "your-app-password")  # Use Gmail App Password
        smtp.send_message(msg)
