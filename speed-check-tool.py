import time  # Built-in timer

def check_start_speed(message, ai_tool_path):
    start_time = time.time()
    # Hook your AI tool here (like a simple command)
    end_time = time.time()
    speed_ms = (end_time - start_time) * 1000  # In milliseconds
    return speed_ms

# Run 64 tests like this:
speeds = []
for i in range(64):
    speed = check_start_speed("Your message here", "path/to/your/ai")
    speeds.append(speed)
print("Average speed:", sum(speeds) / len(speeds))
