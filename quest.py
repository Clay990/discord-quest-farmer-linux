#!/usr/bin/env python3
import os
import subprocess
import sys
import time

# ==========================================
# 🛠️ MAINTAINER ZONE (EDIT THIS LIST)
# ==========================================
# Add current Discord quests here.
# 'time': 1200 seconds = 20 minutes (safety buffer for 15 min quests)
# 'folder': Use "" for no subfolder, or "Win64" for games like Arena Breakout

ACTIVE_QUESTS = [
    {
        "name": "Where Winds Meet",
        "exe": "wwm.exe",
        "folder": "",
        "time": 1200
    },
    {
        "name": "Arena Breakout: Infinite",
        "exe": "UAGame.exe",
        "folder": "Win64",
        "time": 1200
    },
    {
        "name": "RAID: Shadow Legends",
        "exe": "Raid.exe",
        "folder": "",
        "time": 1200
    },
    {
        "name": "PUBG",
        "exe": "TslGame.exe",
        "folder": "",
        "time": 1200
    },
    {
        "name": "Valorant",
        "exe": "VALORANT-Win64-Shipping.exe",
        "folder": "Win64",
        "time": 1200
    }
]
# ==========================================

def run_fake_game(game_name, exe_name, subfolder, duration):
    home = os.path.expanduser("~")
    base_dir = os.path.join(home, "Games", "Fake_Quests", game_name.replace(" ", "_"))
    final_dir = os.path.join(base_dir, subfolder) if subfolder else base_dir
    fake_exe = os.path.join(final_dir, exe_name)

    print(f"\n[*] Setting up fake env: {final_dir}")
    os.makedirs(final_dir, exist_ok=True)

    try:
        subprocess.run(["cp", "/usr/bin/sleep", fake_exe], check=True)
    except Exception as e:
        print(f"Error: Could not copy /usr/bin/sleep. {e}")
        return

    print(f"[*] Running '{exe_name}' for {int(duration/60)} minutes...")
    print("\033[1;32m➜ Check Discord > User Settings > Gift Inventory for progress.\033[0m")
    print("\033[1;31m➜ Press Ctrl+C to stop early.\033[0m")

    try:
        proc = subprocess.Popen([fake_exe, str(duration)])
        proc.wait()
    except KeyboardInterrupt:
        print("\n[!] Stopping...")
        proc.terminate()
        # Cleanup
        try:
            os.remove(fake_exe)
            if subfolder: os.rmdir(final_dir)
            os.rmdir(base_dir)
        except: pass
        print("Cleaned up.")

def main():
    print("\033[1;36m=== 🐧 Linux Discord Quest Farmer ===\033[0m")
    print("Choose a current active quest:")

    # 1. Display the Curated List
    for i, quest in enumerate(ACTIVE_QUESTS):
        print(f"[{i+1}] {quest['name']}")

    print(f"[{len(ACTIVE_QUESTS)+1}] Custom / Search Manually")

    # 2. Get User Input
    try:
        choice = int(input("\nSelect number: ")) - 1
    except ValueError:
        print("Invalid input.")
        return

    # 3. Run the Selected Quest
    if 0 <= choice < len(ACTIVE_QUESTS):
        q = ACTIVE_QUESTS[choice]
        run_fake_game(q['name'], q['exe'], q['folder'], q['time'])

    # 4. Fallback to Manual Mode (Hidden option if you want to use it)
    elif choice == len(ACTIVE_QUESTS):
        print("\n--- Manual Mode ---")
        name = input("Game Name: ")
        exe = input("EXE Name (e.g. game.exe): ")
        folder = input("Subfolder (optional): ")
        run_fake_game(name, exe, folder, 1200)
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
