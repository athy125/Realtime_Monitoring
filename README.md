# 🚀 Real-time Log Monitoring and Error Detection 📊

## Overview

This Python project provides a versatile and powerful solution for real-time log monitoring and error detection in log files. Whether you're managing server logs, application logs, or any other type of log data, this tool allows you to monitor logs continuously and receive notifications when specific error patterns are detected.

**Key Features:**

- **Real-time Log Monitoring:** 🕒 The project uses the `tailer` library to monitor log files in real-time, ensuring that you stay up-to-date with the latest log entries.

- **Flexible Error Detection:** 🕵️ Customize the error patterns you want to detect by providing a list of keywords or regular expressions that match your specific use case.

- **Email and Slack Notifications:** 📧💬 When an error is detected, the tool can send email and Slack notifications to alert you or your team, allowing for rapid response to issues.

- **Configuration File:** 📝 Configure email and Slack settings, log file paths, and error patterns via a JSON configuration file, making it easy to adapt the tool to your needs without modifying the code.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Customization](#customization)
- [Contributions](#contributions)
- [License](#license)
- [Disclaimer](#disclaimer)

## Installation 🛠️

1. **Clone the Repository** 📦
   ```bash
   git clone https://github.com/athy125/Realtime_Monitoring.git


2. Navigate to the Project Directory 📂

   ```bash
   cd Realtime_Monitoring
   ```

3. Install the required dependencies using `pip` ⚙️

   ```bash
   pip install -r requirements.txt
   ```

## Usage 🚀

1. Create a configuration file named `config.json` in the project directory. Use the provided `config_example.json` as a template and fill in your email and Slack credentials, log file paths, and error patterns. 

2. Run the `main.py` script to start real-time log monitoring and error detection: 

   ```bash
   python main.py
   ```

3. The tool will continuously monitor the specified log files and send notifications when it detects error patterns.

## Configuration  🛠️

The `config.json` file allows you to customize the behavior of the log monitoring tool:

- `"sender_email"`: Your email address for sending email notifications.
- `"sender_password"`: Your email password (ensure security and consider using environment variables).
- `"smtp_server"`: The SMTP server address for your email provider.
- `"smtp_port"`: The SMTP server's port (587 for TLS, adjust based on your provider).
- `"slack_token"`: Your Slack API token for sending Slack notifications.
- `"log_file_path"`: The path to the log file you want to monitor.
- `"error_patterns"`: A list of error patterns (keywords or regular expressions) to detect in log entries.

## Customization 🧰

- Customize error patterns in the `config.json` file to match specific log patterns relevant to your application.

- Extend the tool to support additional notification methods or integrate with other communication platforms.

## Contributions 🤝

Contributions and enhancements to this project are welcome! If you have ideas for improvements or new features, please fork the repository and submit pull requests to contribute to its development.

## License 📄

This project is open-source and available under the [MIT License](LICENSE).

## Disclaimer 🚨

Please use this tool responsibly and ensure that you have appropriate permissions to access and monitor log files.
