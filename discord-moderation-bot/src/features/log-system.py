import logging

class LogSystem:
    def __init__(self):
        self.log_file = 'moderation_log.txt'
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def log_action(self, action, user_id, reason):
        logging.info(f'{action} - User ID: {user_id} - Reason: {reason}')

    def read_logs(self):
        try:
            with open(self.log_file, 'r') as file:
                logs = file.readlines()
                for log in logs:
                    print(log)
        except FileNotFoundError:
            print('Log file not found.')

    def clear_logs(self):
        try:
            open(self.log_file, 'w').close()
            print('Logs cleared successfully.')
        except FileNotFoundError:
            print('Log file not found.')

# Testing the LogSystem class
# log = LogSystem()
# log.log_action('WARN', '123456789', 'Inappropriate language')
# log.log_action('MUTE', '987654321', 'Spamming')
# log.read_logs()
# log.clear_logs()