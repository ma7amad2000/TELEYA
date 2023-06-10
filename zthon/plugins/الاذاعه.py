import base64
import contextlib
from asyncio import sleep

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from zthon import zedub

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper import broadcast_sql as sql
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البوت"
LOGS = logging.getLogger(__name__)

ZED_BLACKLIST = [
   -1001904354189,
    -1001904354189,
    ]

DEVZ = [
    6275847466,
    6275847466,
]
#

"𓆩 [ 𓏺𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝗭𝗧𝗵𝗼𝗻𝙃𝘼𝙔𝘼- اوامـر الاذا؏ـــة](t.me/HL_BG) 𓆪\n\n"
    "**⎞𝟏⎝** `.للقروبات`  / `.للمجموعات`\n"
    "**رد الرساله لي تبي توجهها**\n"
    "**- لاذاعة رساله ولا ميديا للقروبات لي انت قاعد فيها**\n\n\n"
    "**⎞𝟐⎝** `.للخاص`\n"
    "**رد عالرساله لي تبي توجهها للي عندك فالخاص**\n"
    "**- كلامي واضح فوق🙂**\n\n\n"
    "**⎞𝟑⎝** `.خاص`\n"
    "**الامـر + معرف الشخص + الرسـاله . .**\n"
    " **عشان تدز رساله لحد معين بدون ماتخشله فالخاص**\n\n\n"
    "**⎞4⎝** `.للكل`\n"
    "**ترد على رساله ولا ميديا في تحتها كلام**\n"
    " **الامر هذا داخل المجموعه توجه رساله للكل **\n\n"
    "**⎞5⎝** `.زاجل`\n"
    "**بالــࢪد ؏ــلى ࢪســالة نصيــه او وسـائــط تحتهــا نــص**\n"
    " **عشان تدز رساله لحد معين 🕊. .**\n\n"
    "\n 𓆩 [𓏺𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝗭𝗧𝗵𝗼𝗻𝙃𝘼𝙔𝘼](t.me/HL_BG) 𓆪"
)


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="الاذاعه")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalPRO_cmd)


@zedub.zed_cmd(pattern=f"للقروبات(?: |$)(.*)")
async def gcast(event):
    zedthon = event.pattern_match.group(1)
    if zedthon: #Write Code By T.me/zzzzl1l
        await edit_or_reply(event, "**𖢿╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        zelzal = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**𖢿╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zzz = await edit_or_reply(event, "**𖢿╎جـاري الاذاعـه في المجموعـات ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if zelzal.text: #Write Code By T.me/zzzzl1l
                    try:
                        await borg.send_message(chat, zelzal, link_preview=False)
                        done += 1
                    except BaseException:
                        er += 1
                else:
                    try: #Write Code By T.me/zzzzl1l
                        await borg.send_file(
                            chat,
                            zelzal,
                            caption=zelzal.caption,
                            link_preview=False,
                        )
                        done += 1
                    except BaseException:
                        er += 1
            except BaseException:
                er += 1
    await zzz.edit(
        f"**𖢿╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من المجموعـات** \n**𖢿╎خطـأ في الارسـال الـى ** `{er}` **من المجموعـات**"
    )

@zedub.zed_cmd(pattern=f"للمجموعات(?: |$)(.*)")
async def gcast(event):
    zedthon = event.pattern_match.group(1)
    if zedthon: #Write Code By T.me/zzzzl1l
        await edit_or_reply(event, "**𖢿╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        zelzal = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**𖢿╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zzz = await edit_or_reply(event, "**𖢿╎جـاري الاذاعـه في المجموعـات ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if zelzal.text: #Write Code By T.me/zzzzl1l
                    try:
                        await borg.send_message(chat, zelzal, link_preview=False)
                        done += 1
                    except BaseException:
                        er += 1
                else:
                    try: #Write Code By T.me/zzzzl1l
                        await borg.send_file(
                            chat,
                            zelzal,
                            caption=zelzal.caption,
                            link_preview=False,
                        )
                        done += 1
                    except BaseException:
                        er += 1
            except BaseException:
                return
    await zzz.edit(
        f"**𖢿╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من المجموعـات ، خطـأ في الارسـال الـى ** `{er}` **من المجموعـات**"
    )
    
@zedub.zed_cmd(pattern=f"للخاص(?: |$)(.*)")
async def gucast(event):
    zedthon = event.pattern_match.group(1)
    if zedthon: #Write Code By T.me/zzzzl1l
        await edit_or_reply(event, "**𖢿╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        zelzal = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**𖢿╎بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zzz = await edit_or_reply(event, "**𖢿╎جـاري الاذاعـه في الخـاص ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if zelzal.text: #Write Code By T.me/zzzzl1l
                    try:
                        await borg.send_message(chat, zelzal, link_preview=False)
                        done += 1
                    except BaseException:
                        return
                else:
                    try: #Write Code By T.me/zzzzl1l
                        await borg.send_file(
                            chat,
                            zelzal,
                            caption=zelzal.caption,
                            link_preview=False,
                        )
                        done += 1
                    except BaseException:
                        er += 1
            except BaseException:
                return
    await zzz.edit(
        f"**𖢿╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من الخـاص**\n**𖢿╎خطـأ في الارسـال الـى ** `{er}` **من الخـاص**"
    )
    

@zedub.zed_cmd(pattern="خاص ?(.*)")
async def pmto(event):
    r = event.pattern_match.group(1)
    p = r.split(" ")
    chat_id = p[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    zelzal = ""
    for i in p[1:]:
        zelzal += i + " "
    if zelzal == "":
        return
    try:
        await zedub.send_message(chat_id, zelzal)
        await event.edit("**𖢿╎تـم ارسال الرسـالة بنجـاح ✅**\n**𖢿╎بـدون الدخـول للخـاص**")
    except BaseException:
        await event.edit("**𖢿╎اووبس .. لقـد حدث خطـأ مـا .. اعـد المحـاوله**")

