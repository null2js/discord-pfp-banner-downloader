import discord
import os
import requests

intents = discord.Intents.default()
client = discord.Client(intents=intents)

SAVE_DIR = "pfps"
os.makedirs(SAVE_DIR, exist_ok=True)

BOT_USER_ID = 1348887899185352715

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    try:
        user = await client.fetch_user(BOT_USER_ID)

        # 🔹 PFP
        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
        response = requests.get(avatar_url)

        with open(f"{SAVE_DIR}/{user.id}_pfp.png", "wb") as f:
            f.write(response.content)

        print(f"Saved PFP of {user} ✔️")

        # 🔹 BANNER (needs fetch_user, you already did that 👍)
        if user.banner:
            banner_url = user.banner.url
            response = requests.get(banner_url)

            with open(f"{SAVE_DIR}/{user.id}_banner.png", "wb") as f:
                f.write(response.content)

            print(f"Saved banner of {user} ✔️")
        else:
            print(f"{user} has no banner ❌")

    except Exception as e:
        print("Error:", e)

client.run("MTQ3ODA1NTk5MjQ5ODU4OTc2Nw.G-y8dq.ilOWW5Qm2sMMlJQenN-ZUNTY19IL7kPPrJc8Vc")