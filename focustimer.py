import time
import os

def focus_timer(focus_minutes, break_minutes):
    while True:
        # Focus time
        print(f"Focus for {focus_minutes} minutes.")
        time.sleep(focus_minutes * 60)  # Convert minutes to seconds

        # Break time
        print(f"Take a break for {break_minutes} minutes.")
        time.sleep(break_minutes * 60)

        # Clear the console screen (works on Windows, macOS, Linux)
        os.system('cls' if os.name == 'nt' else 'clear')

# 设置专注时间和休息时间（以分钟为单位）
focus_time = 25
break_time = 5

# 启动专注时钟
focus_timer(focus_time, break_time)
