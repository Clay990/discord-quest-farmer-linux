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
