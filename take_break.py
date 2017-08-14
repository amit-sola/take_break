import time
import webbrowser

total_breaks = 3
break_count = 0

print("Execution started on " + time.ctime())

# Helps you to take a break every 30 minutes

while(break_count < total_breaks):
    time.sleep(30*60)
    webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
    break_count += 1