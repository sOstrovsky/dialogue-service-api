import time

from datetime import datetime


def generate_openai_prompt(prompt: str) -> str:
    time.sleep(5)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f'current time: {current_time}'