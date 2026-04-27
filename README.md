<div align="center">

# 🖼️ Discord PFP Saver

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=5865F2&center=true&vCenter=true&width=435&lines=Fetch+any+Discord+PFP+%26+Banner;Fast.+Simple.+Clean." alt="Typing SVG" />

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0+-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discordpy.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Made by nrx](https://img.shields.io/badge/Made%20by-nrx-ff6b6b?style=for-the-badge)](https://github.com)

> **Fetch and save any Discord user's profile picture and banner in seconds.**

</div>

---

## 🚀 How to Use

**Step 1 —** Get your bot token from the [Discord Developer Portal](https://discord.com/developers/applications) and paste it in `.env`:

```env
DISCORD_TOKEN=your_token_here
```

**Step 2 —** Open `main.py` and swap in the target user's Discord ID:

```python
BOT_USER_ID = 123456789012345678
```

**Step 3 —** Run the bot:

```bash
python main.py
```

**Step 4 —** Check the `pfps/` folder ✅

```
pfps/
├── 123456789012345678_pfp.png
└── 123456789012345678_banner.png
```

> 💡 No commands. No setup. Just set your token, swap the ID, and run.

---

## 📁 Project Structure

```
discord-pfp-saver/
├── main.py          # Bot logic
├── .env             # Your secret token (never commit this!)
├── .gitignore       # Keeps sensitive files off GitHub
├── requirements.txt
├── README.md
└── pfps/            # Saved images land here
```

---

## 📦 Requirements

```bash
pip install -r requirements.txt
```

| Package | Purpose |
|---------|---------|
| `discord.py` | Discord bot framework |
| `requests` | Downloading images |
| `python-dotenv` | Loading `.env` token |

---

## 👨‍💻 About the Developer

<div align="center">

### **nrx**
*Student developer. Always experimenting, always shipping.*

Ranging from Discord bots to whatever comes next — still early, already dangerous. 🚀

</div>

---

<div align="center">

## 🙏 Thanks for checking this out!

If you found it useful, drop a ⭐ on GitHub — it means a lot and keeps the motivation going.

[![Star on GitHub](https://img.shields.io/badge/⭐%20Star%20on-GitHub-181717?style=for-the-badge&logo=github)](https://github.com)

</div>
