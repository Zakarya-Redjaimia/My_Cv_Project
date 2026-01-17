#WachDogFolders
import time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import ctypes

log_file_path = os.path.join(os.path.expanduser("F://file_events.log"))
print(log_file_path)

def notify_wind(message,title):
    try:
        ctypes.windll.user32.MessageBoxW(0,message,title,0)
    except:
        pass
def log_event(title,message):
# Open the log file in append mode and write the title and message
    with open(log_file_path, "a") as log_file:
        log_file.write(f"\n============================\n{title}: {time.ctime()}\n============================\n{message}")  # Combine title and message

def created(event):
    message = f"File {event.src_path} [CREATED]"
    title = "Warrning"
    log_event(title,message)
    #notify_wind(message,title)
def deleted(event):
    message = f"File {event.src_path} [DELETED]"
    title = "Warrning"
    log_event(title,message)
    #notify_wind(message,title)

def modified(event):
    message = f"File {event.src_path} [MODIFIED]"
    title = "Warrning"
    log_event(title,message)
    #notify_wind(message,title)
    
def moved(event):
    message = f"File {event.src_path} [MOVED TO] \n{event.dest_path}"
    title = "Warrning"
    log_event(title,message)
    #notify_wind(message,title)

if __name__ == "__main__":

    path = "C:\\Users\\Win\\Desktop\\"
    #path = "C:\\"
    evo = FileSystemEventHandler()
    evo.on_created = created
    evo.on_deleted = deleted
    evo.on_modified = modified
    evo.on_moved = moved

    observer = Observer()
    observer.schedule(evo,path,recursive=True)
    observer.start()

    try:        
        while True:
            time.sleep(1)
    except KeyboardInterrupt: # ctrl + c
        observer.stop()
    observer.join()