# automated_timer_script

This is a simple python automated script that times how long a person spends learning a skill or doing a certain activity. I

## How does it work?
running *timetracker.py "activity"* starts a timer automatically. You can move to any other app on your laptop and carry on with your task until *ctrl + c* is pressed, which stops the timer and then saves the duration of that activity to a JSON File, *learning_times.json*.

running **timetracker.py "activity" --show** displays the total time you have spent on an activity by searching for it through the json file (why look for the activity and time yourself when you can automate it?)

### use case
The main goal behind this script was to automatically time and track my own CS journey. I am currently working on my web development and mobile development skills and wanted a way to time myself and store those figures in a file that i can look back at. I am also just testing my python programming akills and working on automation in general. 

### Future goal
A future goal is to use my own stats from the JSON File this script generates and compare that with online data to generate an analysis on how long it takes different people to acquire these same skills - perhaps using reddit API 
