# 🐧 Linux Discord Quest Farmer

**Get Discord Quest rewards (Orbs, Decorations) on Linux without installing 100GB games.**

This tool completes Discord Quests by tricking the Discord Linux client into thinking you are playing a game. It spawns a lightweight, native Linux process (renamed to match the game's `.exe`) which satisfies Discord's detection system.

**✅ No Wine • ✅ No Proton • ✅ No 100GB Downloads • ✅ Open Source**

## 🚀 Features

* **One-Click Farming:** Pre-configured list of currently active quests (e.g., *Where Winds Meet*, *Arena Breakout*).
* **Smart Detection:** Automatically handles games that require specific folders (e.g., creating `Win64` for Unreal Engine games).
* **Native & Safe:** Uses your system's `sleep` command. No weird binaries or root permissions needed.
* **Lightweight:** The entire script is just a few KB.

## 📦 Installation & Usage

### 1. Clone the Repository and run
```bash
git clone https://github.com/Clay990/discord-quest-farmer-linux.git
cd discord-quest-farmer-linux
python quest.py

```

## ❓ How it Works

Discord on Linux detects games by checking your running **process names**. It does not verify if the file is a valid Windows PE executable.

1. This script creates a fake folder structure (e.g., `~/Games/Fake_Quests/Game/Win64/`).
2. It copies your native `/usr/bin/sleep` binary to that folder.
3. It renames `sleep` to the target executable (e.g., `UAGame.exe`).
4. It runs the process for 15+ minutes so Discord detects it.

## ⚠️ Disclaimer

This tool is for educational purposes. Use it responsibly. The maintainers are not responsible for any account actions taken by Discord (though this method is generally considered safe as it only spoofs local process names).
