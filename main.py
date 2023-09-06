# main.py
import time
import argparse
from log_monitoring import LogMonitor
from email_notifications import send_email
from slack_notifications import send_slack_message
from logger import log_event


def main():
    parser = argparse.ArgumentParser(
        description="Real-time Log Monitoring and Analysis"
    )
    parser.add_argument(
        "--log-file", help="Path to the log file to monitor", required=True
    )

    parser.add_argument(
        "--error-patterns", nargs="+", help="List of error patterns to detect"
    )
    parser.add_argument("--email", help="Email address for notifications")
    parser.add_argument("--slack-token", help="Slack API token for notifications")
    parser.add_argument(
        "--interval", type=int, default=60, help="Monitoring interval in seconds"
    )

    args = parser.parse_args()

    # Initialize the log monitor
    log_monitor = LogMonitor(args.log_file)

    try:
        while True:
            # Check for new log entries
            new_log_entries = log_monitor.get_new_log_entries()

            # Check for error patterns
            for log_entry in new_log_entries:
                if log_monitor.check_for_error(log_entry, args.error_patterns):
                    # Log the error
                    log_event(f"Error detected: {log_entry}")

                    # Send email notification if email is provided
                    if args.email:
                        send_email(args.email, "Error Detected", log_entry)

                    # Send Slack notification if Slack token is provided
                    if args.slack_token:
                        send_slack_message(
                            args.slack_token, "Error Detected", log_entry
                        )
            time.sleep(args.interval)

    except KeyboardInterrupt:
        print("Monitoring stopped.")


if __name__ == "__main__":
    main()
