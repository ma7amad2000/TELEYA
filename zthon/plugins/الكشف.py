import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers import get_user_from_event, sanga_seperator
from ..helpers.utils import _format

plugin_category = "العروض"


@zedub.zed_cmd(
    pattern="كشف(المعرف)?(?:\s|$)([\s\S]*)",
    command=("الاسماء", plugin_category),
    info={
        "header": "To get name history of the user.",
        "flags": {
            "u": "That is sgu to get username history.",
        },
        "usage": [
            "{tr}كشف <username/userid/reply>",
            "{tr}كشف المعرف <username/userid/reply>",
        ],
        "examples": "{tr}sg @missrose_bot",
    },
)
async def _(event):  # sourcery no-metrics
    "To get name/username history."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "`reply to  user's text message to get name/username history or give userid/username`",
        )
    user, rank = await get_user_from_event(event, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMata_BOT"
    zedevent = await edit_or_reply(event, "**𖢿╎جـارِ الكشـف ...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await edit_delete(zedevent, "**- اضغط ستارت هنـا @SangMata_BOT ثم اعد ارسال الامر**")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(zedevent, "**- الامـر في وضع الصيانه حاليـاً ...**")
    if "No data available" in responses:
        await edit_delete(zedevent, "**𖢿╎المستخدم ليس لديه أي سجل اسمـاء بعـد ...**")
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    sandy = None
    check = usernames if cmd == " المعرف" else names
    for i in check:
        if sandy:
            await event.reply(i, parse_mode=_format.parse_pre)
        else:
            sandy = True
            await zedevent.edit(i, parse_mode=_format.parse_pre)



@zedub.zed_cmd(
    pattern="الاسماء(المعرف)?(?:\s|$)([\s\S]*)",
    command=("الاسماء", plugin_category),
    info={
        "header": "To get name history of the user.",
        "flags": {
            "u": "That is sgu to get username history.",
        },
        "usage": [
            "{tr}كشف <username/userid/reply>",
            "{tr}كشف المعرف <username/userid/reply>",
        ],
        "examples": "{tr}sg @missrose_bot",
    },
)
async def _(event):  # sourcery no-metrics
    "To get name/username history."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "`reply to  user's text message to get name/username history or give userid/username`",
        )
    user, rank = await get_user_from_event(event, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMata_BOT"
    zedevent = await edit_or_reply(event, "**𖢿╎جـارِ الكشـف ...**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await edit_delete(zedevent, "**- اضغط ستارت هنـا @SangMata_BOT ثم اعد ارسال الامر**")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(zedevent, "**- الامـر في وضع الصيانه حاليـاً ...**")
    if "No data available" in responses:
        await edit_delete(zedevent, "**𖢿╎المستخدم ليس لديه أي سجل اسمـاء بعـد ...**")
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    sandy = None
    check = usernames if cmd == " المعرف" else names
    for i in check:
        if sandy:
            await event.reply(i, parse_mode=_format.parse_pre)
        else:
            sandy = True
            await zedevent.edit(i, parse_mode=_format.parse_pre)