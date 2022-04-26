import time
import os
from wsgiref.simple_server import WSGIRequestHandler
num_circle = 6 
main_timer = 25
break_time = 5

DURATION = 1
i_circle = 0

silent_mode = True

def sound():
    duration = DURATION  # seconds
    freq = 440  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

def write_log():
    f = open("log.txt", "r+")
    n = int(f.read())
    n += 1
    f.seek(0)
    f.write(str(n))
    f.close()

from tkinter import * 
from tkinter import messagebox
def show_message(msg_title, msg_info):
    root = Tk()
    messagebox.showinfo(msg_title, msg_info)
    root.destroy()

def my_timer(ti, i_circle, s_name):
    global silent_mode
    print("-----------------------------------------------------")
    t = int(ti*60)
    print("id circle: "+str(i_circle))
    print(str(s_name))
    if silent_mode:
        print("Silent mode")
    else:
        print("Sound mode")
    i = 1
    while True:
        try:
            start = time.time()
            m =int((t-i)/60)
            s = t-i - m*60
            print("\t\t\t\t\t\t\t\t", end='\r')
            print("Time: "+str(m)+":"+str(s),end='\r')
            i += 1
            if i >= t:
                if silent_mode:
                    show_message(str(s_name), "Time is over")
                else:
                    sound()
                    show_message(str(s_name), "Time is over")
                
                break
            stop = time.time()
            time.sleep(abs(1-stop+start))
        except KeyboardInterrupt:
            print("\nPause")
            print("0: Switch mode")
            print("1: continue")
            print("2: quit")
            cmd = input("Command: ")
            if cmd == "1":
                continue
            if cmd == "0":
                silent_mode = not silent_mode
            if cmd == "2":
                exit(0)
    print("-----------------------------------------------------")

# show_message()
# exit(0)
while i_circle < num_circle:
    print("Number of circle left: "+str(num_circle - i_circle))
    my_timer(main_timer, i_circle, "Main Timer")
    write_log()
    print("Number of circle left: "+str(num_circle - i_circle))
    my_timer(break_time, i_circle, "Break time")
    i_circle += 1

show_message("Congratulation!!!", "You had finished!!!")

