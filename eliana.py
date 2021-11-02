import asyncio
import aiohttp
import re
from config import bot_token, owner_id, bot_id
from pyrogram import Client, filters

eliana = Client(
    ":memory:",
    bot_token="token Api here",
    api_id=2442183,
    api_hash="66c6799e1b784aff78bad680cd8362db",
)


async def chatbot(text):
    url = f"https://kazukoapi.herokuapp.com/kazuko/chatbot?text={text}&name=eliana"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            res = await res.json()
            text = res["message"]
            return text

@kazuko.on_message(filters.command("about") & ~filters.edited)
async def about(_, message):
    await message.reply_text(
        "[Kazuko Api](https://elianaapi.herokuapp.com/)"
        + " | [Owner](https://github.com/heyaaman/KazukoBot)", disable_web_page_preview=True)


@kazuko.on_message(filters.command("kazuko") & ~filters.edited)
async def start(_, message):
    await eliana.send_chat_action(message.chat.id, "typing")
    await message.reply_text(
        "**I Am Kazuko an advanced Group managing bot and a chatbot**"
    )



@kazuko.on_message(
    ~filters.private 
    & ~filters.command("help")
    & ~filters.edited
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user.id == bot_id:
            return
        await kazuko.send_chat_action(message.chat.id, "typing")
        if not message.text:
            query = "Hello"
        else:
            query = message.text
        if len(query) > 50:
            return
        try:
            res = await chatbot(query)
            await asyncio.sleep(1)
        except Exception as e:
            res = str(e)
        await message.reply_text(res)
        await kazuko.send_chat_action(message.chat.id, "cancel")
    else:
        if message.text:
            query = message.text
            if len(query) > 50:
                return
            if re.search("[.|\n]{0,}[l|L][u|U][n|N][a|A][.|\n]{0,}", query):
                await kazuko.send_chat_action(message.chat.id, "typing")
                try:
                    res = await chatbot(query)
                    await asyncio.sleep(1)
                except Exception as e:
                    res = str(e)
                await message.reply_text(res)
                await kazuko.send_chat_action(message.chat.id, "cancel")


@kazuko.on_message(
    filters.private
    & ~filters.command("help")
    & ~filters.edited
)
async def chatpm(_, message):
    if not message.text:
        return
    await kazuko.send_chat_action(message.chat.id, "typing")
    query = message.text
    if len(query) > 50:
        return
    try:
        res = await chatbot(query)
        await asyncio.sleep(1)
    except Exception as e:
        res = str(e)
    await message.reply_text(res)
    await kazuko.send_chat_action(message.chat.id, "cancel")


print(
    """
  Kazuko Started
"""
)


kazuko.run()
