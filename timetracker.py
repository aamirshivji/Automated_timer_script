import time as tm 
import datetime
import atexit 
import argparse
import json
from pathlib import Path

def hello_world():
    print("Hello! Welcome to my time tracker. The activity you have entered is now being timed :) ")
    print(" If you wish to stop timing, simply press 'ctrl + C' ")
    print("The activity will be added to your file 'learning_times.json' ")
    

time_file = Path("learning_times.json") #create a path object pointing to the json file

def load_learning_times():
    if time_file.exists():
        with open(time_file, "r") as file:
            return json.load(file)
    else:
        # Create the file with an empty dictionary
        with open(time_file, "w") as file:
            json.dump({}, file)
        
        return {}


    
def save_learning_times(learning_times):
    with open(time_file, "w") as file:
        json.dump(learning_times, file)
        print("time updated successfully!")
        

def show_total_time(activity):
    learning_times = load_learning_times()
    if activity in learning_times:
        total_seconds = learning_times[activity]
        total_duration = datetime.timedelta(seconds=total_seconds)
        hours, remainder = divmod(total_duration.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Total time for '{activity}': {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds.")
    else:
        print(f"No time recorded for activity '{activity}'.")

        
def track_activity(activity):
    hello_world()
    #initialize time data
    start_time = tm.time()
    time = load_learning_times()
    
    def stop_tracking():
        end_time = tm.time()
        session_time = end_time - start_time
        session_duration = datetime.timedelta(seconds = session_time) #turning the tracked time into something more readable 
        
        if activity in time:
            total_time = datetime.timedelta(seconds = time[activity]) #convert existing time in file for activity into human readable 
            total_time += session_duration #update the existing time to include latest tracking data. 
            
        else:
            total_time = session_duration
            
        #save the time in seconds so it increments more easily 
        time[activity] = total_time.total_seconds()
        save_learning_times(time)
        
        #display tracked for user
        hours, remainder = divmod(total_time.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"\nActivity '{activity}' - Total time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds.")
        print(f"Session time: {session_duration}")

        
    atexit.register(stop_tracking)
    print(f"Tracking activity '{activity}'. Press Ctrl+C to stop.")
    
    while True:
        try:
            tm.sleep(1)
        except KeyboardInterrupt:
            print("stopping tracker")
            break

def main():
    
    parser = argparse.ArgumentParser("track time spent on various activities")
    parser.add_argument("activity", type=str, help = "name of activity to track e.g HTML foundations, DHCP Installation")
    parser.add_argument("--show", action="store_true", help="Show the total time for the specified activity without tracking")
    args = parser.parse_args()
    
    if args.show:
        show_total_time(args.activity)
    else:
        track_activity(args.activity)
    
if __name__=="__main__":
    main()
            
