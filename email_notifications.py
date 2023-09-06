import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailNotifier:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        try:
            with open(config_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception("Config file not found.")
        except json.JSONDecodeError as e:
            raise Exception(f"Error parsing config file: {e}")

    def send_email(self, to_email, subject, message):
        try:
            smtp_server = smtplib.SMTP(
                self.config["smtp_server"], self.config["smtp_port"]
            )
            smtp_server.starttls()
            smtp_server.login(
                self.config["sender_email"], self.config["sender_password"]
            )

            msg = MIMEMultipart()
            msg["From"] = self.config["sender_email"]
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            smtp_server.sendmail(self.config["sender_email"], to_email, msg.as_string())
            print("Email notification sent successfully.")
        except (smtplib.SMTPException, ConnectionRefusedError) as e:
            print(f"Email sending error: {e}")
        finally:
            smtp_server.quit() if "smtp_server" in locals() else None


if __name__ == "__main__":
    config_file = "email_config.json"  # Replace with your configuration file path
    notifier = EmailNotifier(config_file)

    to_email = "recipient@example.com"
    subject = "Error Detected"
    message = "An error occurred in the application."

    notifier.send_email(to_email, subject, message)
