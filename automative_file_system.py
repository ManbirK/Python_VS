import sys
import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



from_dir = "C:/Users/meenu/Downloads/OsTest"
to_dir ="C:/Users/meenu/Downloads/OsTest2"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
         name, extension = os.path.splitext(event.src_path)
         print(name)
         print(extension)
         print(event)

         for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg   C:\Users\meenu\Downloads\OsTest\ttest.png      
                path2 = to_dir + '/' + key                     # Example path2 : D:/My Files/Image_Files      
                path3 = to_dir + '/' + key + '/' + file_name   # Example path3 : D:/My Files/Image_Files/ImageName1.jpg
                print("path1 " , path1)
                print("path3 ", path3)

                time.sleep(3)
                if os.path.exists(path2):
                    print("Directory Exists")
                    print("Moving " + file_name + ".....")

                    # Move from path1 ---> path3
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print(" Creating Directory")
                    os.makedirs(path2)
                    print("Moving " + file_name + ".....")
                    shutil.move(path1, path3)
                    time.sleep(1)



#initialize Event handler Class
event_handler = FileMovementHandler()

#Initialize Observer
observer = Observer()


#Schedule the Observer
observer.schedule(event_handler,from_dir,recursive=True)

#start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()


