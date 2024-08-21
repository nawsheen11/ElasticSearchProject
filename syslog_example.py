import logging
import logging.handlers

# Configure the syslog logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Set up syslog handler
syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')  # For Unix-like systems
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
syslog_handler.setFormatter(formatter)

logger.addHandler(syslog_handler)

def perform_task(task_id):
    try:
        # Simulate task processing
        if task_id % 2 == 0:
            # Simulate a success scenario
            logger.info(f"Task {task_id} completed successfully.")
        else:
            # Simulate a failure scenario
            raise ValueError(f"Task {task_id} failed due to an error.")
    except Exception as e:
        logger.error(e)

if __name__ == '__main__':
    for i in range(10):
        perform_task(i)

