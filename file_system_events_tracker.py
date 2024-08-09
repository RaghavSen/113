import sys
import time
import random

import os
import shutil
import logging

from Watchdog.observers import Observer 
from Watchdog.events import FileSystemEventHandler 

from_dir = "C:/Users/BHUVNESH/Downloads"


class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print("hey someone created ,{event.src_path}")
    def on_modified(self,event):
        print("Hey There, {event.src_path} has been modified")
    def on_deleted(self,event):
        print("Hey there {event.src_path} has been deleted")
    def on_moved(self,event):
        print("Somone moved {event.src_path} to {event.dest.path}")        
    #1_on_created

    #2_on_deleted

    #3_on_modified

    #4_on_moved

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:  
  while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()