import tailer
import re


class LogMonitor:
    def __init__(self, log_file_path, error_patterns):
        self.log_file_path = log_file_path
        self.previous_position = 0
        self.error_patterns = error_patterns

    def get_new_log_entries(self):
        with open(self.log_file_path, "r") as log_file:
            log_file.seek(self.previous_position)
            new_entries = list(tailer.follow(log_file))
            self.previous_position = log_file.tell()
            return new_entries

    def check_for_error(self, log_entry):
        for pattern in self.error_patterns:
            if re.search(pattern, log_entry):
                return True
        return False


if __name__ == "__main__":
    log_file_path = "log_monitor.log"
    error_patterns = [
        "error",
        "exception",
        "critical",
    ]

    log_monitor = LogMonitor(log_file_path, error_patterns)

    try:
        while True:
            new_log_entries = log_monitor.get_new_log_entries()

            for log_entry in new_log_entries:
                if log_monitor.check_for_error(log_entry):
                    print(f"Error detected: {log_entry}")

    except KeyboardInterrupt:
        print("Monitoring stopped.")
