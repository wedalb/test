import os
import tkinter as tk
from tkinter import messagebox, NW, Label
from tkinter import ttk
import subprocess
import threading
import time
from keyauth import api
import hashlib
from datetime import datetime
from PIL import Image, ImageTk

def getchecksum():
    md5_hash = hashlib.md5()
    try:
        with open(__file__, "rb") as file:
            md5_hash.update(file.read())
            digest = md5_hash.hexdigest()
            return digest
    except FileNotFoundError:
        return "file not found"

# Initialize KeyAuth with your application details
keyauthapp = api(
    name="Spooftest",
    ownerid="iNmkUchuKR",
    secret="626713143e7969d9d7455ffbde8294c836b4a222b7a215471c0922801977c19f",
    version="1.0",
    hash_to_check=getchecksum()
)

def check_license():
    key = license_entry.get()
    if not key:
        messagebox.showerror("Error", "No key entered. Please enter a valid key.")
        return

    try:
        keyauthapp.license(key)
    except keyauthapp.exceptions.KeyAuthError as e:
        print(f"Caught KeyAuthError: {e}")
        messagebox.showerror("Error", "This license is incorrect or missing")

    except Exception as e:
        print(f"Caught Exception: {e}")
        if "invalid license key" in str(e).lower():
            messagebox.showerror("Error", "This license is incorrect or missing")
        else:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


    show_user_data()
    run_batch_script()

def show_user_data():
    try:
        user_data_str = (
            f"Username: {keyauthapp.user_data.username}\n"
            f"IP address: {keyauthapp.user_data.ip}\n"
            f"Hardware-Id: {keyauthapp.user_data.hwid}\n"
        )
        subs = keyauthapp.user_data.subscriptions
        for i in range(len(subs)):
            sub = subs[i]["subscription"]
            expiry = datetime.utcfromtimestamp(int(subs[i]["expiry"])).strftime('%Y-%m-%d %H:%M:%S')
            timeleft = subs[i]["timeleft"]
            user_data_str += f"[{i + 1} / {len(subs)}] | Subscription: {sub} - Expiry: {expiry} - Timeleft: {timeleft}\n"

        user_data_str += (
            f"Created at: {datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Last login at: {datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Expires at: {datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        messagebox.showinfo("User Data", user_data_str)
    except AttributeError as e:
        print(f"Caught AttributeError: {e}")
        messagebox.showerror("Error", "Failed to load user data. Please ensure you are logged in.")
    except Exception as e:
        print(f"Caught Exception: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def run_batch_script():
    threading.Thread(target=execute_batch_with_progress).start()

def execute_batch_with_progress():
    try:
        command = r'''@echo off
            Setlocal EnableDelayedExpansion
            Set _RNDLength=2

            Set _Alphanumeric=0123456789ABCDEF
            Set _Str=%_Alphanumeric%987654321
            :_LenLoop
            IF NOT "%_Str:~18%"=="" SET _Str=%_Str:~9%& SET /A _Len+=9& GOTO :_LenLoop
            SET _tmp=%_Str:~9,1%
            SET /A _Len=_Len+_tmp
            Set _count=0
            SET _RndAlphaNum=
            :_loop
            Set /a _count+=1
            SET _RNDCS=%Random%
            Set /A _RNDCS=_RNDCS%%%_Len%

            SET _RNDBS=%Random%
            Set /A _RNDBS=_RNDBS%%%_Len%

            SET _RNDPSN=%Random%
            Set /A _RNDPSN=_RNDPSN%%%_Len%

            SET _RNDSS=%Random%
            Set /A _RNDSS=_RNDSS%%%_Len%

            SET _RNDSU=%Random%
            Set /A _RNDSU=_RNDSU%%%_Len%

            SET _RndAlphaNumCS=!_RndAlphaNumCS!!_Alphanumeric:~%_RNDCS%,1!
            SET _RndAlphaNumBS=!_RndAlphaNumBS!!_Alphanumeric:~%_RNDBS%,1!
            SET _RndAlphaNumPSN=!_RndAlphaNumPSN!!_Alphanumeric:~%_RNDPSN%,1!
            SET _RndAlphaNumSS=!_RndAlphaNumSS!!_Alphanumeric:~%_RNDSS%,1!
            SET _RndAlphaNumSU=!_RndAlphaNumSU!!_Alphanumeric:~%_RNDSU%,1!

            If !_count! lss %_RNDLength% goto _loop

            @echo off
            @echo ----------------------------------------------------------------------------------------------------------------
            @echo ----------------------------------------------------------------------------------------------------------------

            @echo  .----..---.  .--.  .----. .-. .-..-. . .-..-..----.
            @echo { {__ {_   _}/ {} \ | {}  }| {_} || |/ \| || || {}  \
            @echo .-._} } | | /  /\  \| .-. \| { } ||  .'.  || ||     /
            @echo `----'  `-' `-'  `-'`-' `-'`-' `-'`-'   `-'`-'`----'
            cd .\\source
            @echo ----------------------------------------------------------------------------------------------------------------
            @echo ----------------------------------------------------------------------------------------------------------------
            @echo CHANGING ALL HWIDs
            @echo CS will be changed to !_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!
            @echo BS will be changed to !_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSU!!_RndAlphaNumBS!
            @echo PSN will be changed to !_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSS!
            @echo SS will be changed to !_RndAlphaNumSS!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!
            @echo SU will be changed Automatically
            cd .\\source
            AMIDEWINx64.EXE /CS > nul !_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!
            AMIDEWINx64.EXE /BS > nul !_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSU!!_RndAlphaNumBS!
            AMIDEWINx64.EXE /PSN > nul !_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSS!
            AMIDEWINx64.EXE /SS > nul !_RndAlphaNumSS!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!
            AMIDEWINx64.EXE /SU > nul AUTO
            @echo CS successfully changed to !_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!
            @echo BS successfully changed to !_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSU!!_RndAlphaNumBS!
            @echo PSN successfully changed to !_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!!_RndAlphaNumPSN!!_RndAlphaNumSS!
            @echo SS successfully changed to !_RndAlphaNumSS!!_RndAlphaNumPSN!!_RndAlphaNumCS!!_RndAlphaNumBS!
            @echo SU changed Automatically
            @echo ALL HWID IDs Have Been Changed
            '''
        with open("temp_batch_file.bat", "w") as f:
            f.write(command)

        process = subprocess.Popen("temp_batch_file.bat", shell=True)

        while process.poll() is None:
            time.sleep(0.1)

        messagebox.showinfo("Success", "HWIDs have been successfully changed.")
    except Exception as e:
        print(f"Caught Exception: {e}")
        messagebox.showerror("Error", str(e))
    finally:
        os.remove("temp_batch_file.bat")

app = tk.Tk()
app.title("starHWID")
app.geometry("800x600")
bg_color = "#000000"

app.configure(bg=bg_color)

# Open the image using Pillow
img_path = 'hwid-logo.png'
image = Image.open(img_path)

small_image = image.resize((200, 150), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(small_image)
img_label = tk.Label(app, image=img, bg=bg_color)
img_label.grid(row=0, column=6, padx=10, pady=10)

license_label = tk.Label(app, text="Enter your license:", font=("Arial", 14), bg=bg_color)
license_label.grid(row=3, column=4, padx=10, pady=10)

license_entry = tk.Entry(app, font=("Arial", 14))
license_entry.grid(row=3, column=6, padx=10, pady=10)

submit_button = tk.Button(app, text="Submit", command=check_license, font=("Arial", 14), bg=bg_color)
submit_button.grid(row=4, column=4, columnspan=4, pady=20)

app.mainloop()
