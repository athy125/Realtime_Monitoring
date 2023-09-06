from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json


class SlackNotifier:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)
        self.client = WebClient(token=self.config["slack_token"])

    def load_config(self, config_file):
        try:
            with open(config_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception("Config file not found.")
        except json.JSONDecodeError as e:
            raise Exception(f"Error parsing config file: {e}")

    def send_slack_message(self, channel, message):
        try:
            response = self.client.chat_postMessage(channel=channel, text=message)
            if response["ok"]:
                print("Slack notification sent successfully.")
            else:
                print(f"Slack notification failed. Error: {response['error']}")

        except SlackApiError as e:
            print(f"Slack API error: {e.response['error']}")


if __name__ == "__main__":
    config_file = "slack_config.json"  # Replace with your configuration file path
    notifier = SlackNotifier(config_file)

    channel = "#general"  # Replace with the desired Slack channel
    message = "Error Detected: An error occurred in the application."

    notifier.send_slack_message(channel, message)
