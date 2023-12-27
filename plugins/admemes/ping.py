"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ಸತ್ತಿಲ್ಲ 🥲😔 ಇಲ್ಲೇ ಇದ್ದೀನಿ😪.. ನಿನಗೆ ನನ್ನ ಮೇಲೆ ಮೊದಲಿನ ತರ ಪ್ರೀತಿ❤️ ಇಲ್ಲ😏. ಚೆನ್ನಾಗಿದೆ 😏.. ನೀನು ಮೊದಲಿನಂತಿಲ್ಲ ನೀನು ಬದಲಾಗೇ ಬಿಟ್ಟೇ..🥺" 
REPO = "<b>𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙰𝙳𝙼𝙸𝙽 𝙵𝙾𝚁 𝚁𝙴𝙿𝙾 ›› https://t.me/I_am_Mr_Abnormal</b>"
GROUP = "<b>𝙼𝚈 𝙽𝙰𝚃𝙸𝚅𝙴 𝙶𝚁𝙾𝚄𝙿 ›› https://t.me/+hHun54O4V0U2YzE1</b>"
CHANNEL = "<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> ›› https://youtube.com/@Ranibennur_fighting_sheeps\n\n<b>𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› t.me/About_Mr_Abnormal</b>"
ABNORMAL = "<b>𝙾𝚆𝙽𝙴𝚁 ›› https://t.me/I_am_Mr_Abnormal</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("abnormal", COMMAND_HAND_LER) & f_onw_fliter)
async def abnormal(_, message):
    await message.reply_text(ABNORMAL)


