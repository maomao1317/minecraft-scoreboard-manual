# import system function
import os
# import user dump
import json
# import delay
import time
# first run
try:
    with open("recentcommand.txt") as f_obj:
        total = f_obj.read()
except FileNotFoundError:
    print("You are first time to run this program!")
# list all scoreboard
def listall():
    print("This is the command: ")
    with open("commands/describe.plain.xml", 'r') as f_obj:
        cmd = f_obj.read()
        print(cmd)
    currentcmd = "/scoreboard objectives list"
    with open("recentcommand.txt", 'a') as f_obj:
        f_obj.write("\n")
        json.dump(currentcmd, f_obj)
        print("We saved it to your disk!")
# create scoreboard
def createsb():
    print("We will help you to create a scoreboard.")
    sbname = input("First, Enter your scoreboard's name(Not display name.Just your management name.): ")
    sbdisplayname = input("Next, Enter your scoreboard's display name: ")
    print("Choose the type: ")
    print("1. Dummy")
    print("2. Trigger")
    print("3. Death Count")
    print("4. playerKillCount")
    print("5. totalKillCount")
    print("6. Health")
    print("7. XP")
    print("8. XP Level")
    print("9. food")
    print("10. air")
    print("11. armor")
    print("Here is the instruction.")
    print("Dummy: Points can only be modified with commands, and are usually used to store scores, currencies, and more.")
    print("Trigger: Points can only be modified with commands, and are usually used to store scores, currencies, and more. Unlike the dummy, the administrator can control the switch that allows the score to be modified through the / trigger command.")
    print("deathCount: Points will be automatically increased when killed.")
    print("playerKillCount: When you defeat other players, you will automatically increase the score.")
    print("totalKillCount: Points are automatically increased when defeating creatures (including animals and monsters).")
    print("Health: The current health value, half a heart represents 1 point (the value is 0 before the first update of the health value).")
    print("XP: The current experience value.")
    print("XP Level: current level.")
    print("food: Current saturation (this value was 0 before the first health update).")
    print("air: The remaining air in the current dive is consistent with Air in NBT.")
    print("armor: Current armor value (this value was 0 before the armor value was first updated).")
    types = input("Option(1-11): ")
    print("Don't forget to display it!")
    if types == "1":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname +  " dummy " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "2":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname +  " trigger " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "3":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " deathCount "+ sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "4":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " playerKillCount " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "5":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " totalKillCount " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "6":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " health " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "7":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " xp " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "8":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " level " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "9":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " food " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "10":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " air " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    if types == "11":
        print("Converting...")
        currentcmd = "/scoreboard objectives add " + sbname + " armor " + sbdisplayname
        print("We are done! The command is " + currentcmd)
    with open("recentcommand.txt", 'a') as f_obj:
        f_obj.write("\n")
        json.dump(currentcmd, f_obj)
        print("We saved it to your disk!")
# show scoreboard
def displaysb():
    sbname = input("Enter the scoreboard name(Not display name, Leave blank to clear the selected display): ")
    print("Where do you want to put it?")
    print("1. Shown after TAB key player name")
    print("2. Show on the right side of the screen")
    print("3. Shown under player name (visible in multiplayer mode)")
    opt = input("Select some where(1-3): ")
    if opt == "1":
        print("Converting...")
        currentcmd = "/scoreboard objectives setdisplay list " + sbname
        print("We are done! The command is " + currentcmd)
    if opt == "2":
        print("Converting...")
        currentcmd = "/scoreboard objectives setdisplay sidebar " + sbname
        print("We are done! The command is " + currentcmd)
    if opt == "3":
        print("Converting...")
        currentcmd = "/scoreboard objectives setdisplay belowName " + sbname
        print("We are done! The command is " + currentcmd)
    with open("recentcommand.txt", 'a') as f_obj:
        f_obj.write("\n")
        json.dump(currentcmd, f_obj)
        print("We saved it to your disk!")
# modify scoreboard
def modifysb():
    print("This wizard will help you to modify your scoreboard.")
    sbname = input(" Enter your scoreboard's name: ")
    print("Who is the target?")
    print("1. Nearest player")
    print("2. Random player")
    print("3. All players")
    print("4. All Entities")
    print("5. The entity executing the current command")
    print("6. Furthest player")
    print("7. Player's Name")
    target = input("Choose one(1-7): ")
    if target == "1":
        who = "@p"
    if target == "2":
        who = "@r"
    if target == "3":
        who = "@a"
    if target == "4":
        who = "@e"
    if target == "5":
        who = "@s"
    if target == "6":
        who = "@p[c=-1]"
    if target == "7":
        who = input("Target's name: ")
    print("What do you want to do?")
    print("1. set")
    print("2. add")
    print("3. sub")
    print("4. reset")
    udo = input("Choose one(1-4): ")
    if udo == "1":
        values = input("Set to: ")
    if udo == "2":
        values = input("Add: ")
    if udo == "3":
        values = input("Sub: ")
    if udo == "4":
        pass
    print("Start Converting...")
    if udo != "4":
        if udo == "1":
            currentcmd = "/scoreboard players set " + who +  " " + sbname + " " + values
        if udo == "2":
            currentcmd = "/scoreboard players add "   + who + " " + sbname + " " + values
        if udo == "3":
            currentcmd = "/scoreboard players remove "  + who + " " + sbname + " " + values
    if udo == "4":
        currentcmd = "/scoreboard players reset " + who + " " + sbname
    print("We are done! The command is " + currentcmd)
    with open("recentcommand.txt", 'a') as f_obj:
        f_obj.write("\n")
        json.dump(currentcmd, f_obj)
        print("We saved it to your disk!")
# delete a scoreboard
def deletesb():
    sbname = input("Scoreboard name: ")
    print("Converting...")
    currentcmd = "/scoreboard objectives remove " + sbname + " "
    print("We are done! The command is " + currentcmd)
    with open("recentcommand.txt", 'a') as f_obj:
        f_obj.write("\n")
        json.dump(currentcmd, f_obj)
        print("We saved it to your disk!")
# endsbfunction
# begin export function
def exptojson():
    print("We are exporting...")
    print("Opening recentcommand.txt")
    try:
        with open("recentcommand.txt") as f_obj:
            export = f_obj.read()
            with open("export.json", 'w') as json_obj:
                dump = json.dump(export)
                print("Exported! Saved to export.json")
    except FileNotFoundError:
        print("recentcommand.txt Did not found!")



while True:
    # user run
    print("\n")
    print("\n")
    print("\n")
    print("Adjust you can execute commands: ")
    print("1. List all exist scoreboards")
    print("2. Create a scoreboard")
    print("3. Display a scoreboard")
    print("4. Modify a scoreboard")
    print("5. Delete a scoreboard")
    print("6. Export All Recent Command to json")
    print("q. Quit")
    print("Tips: Your all command will save to your local disk! Named 'recentcommand.txt'")

    # user input
    options = input("Option Number: ")

    # judge options
    if options == "1":
        listall()
    if options == "2":
        createsb()
    if options == "3":
        displaysb()
    if options == "4":
        modifysb()
    if options == "5":
        deletesb()
    if options == "6":
        exptojson()
    else:
        exit()
