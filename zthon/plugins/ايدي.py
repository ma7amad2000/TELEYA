# Zed-Thon - ZelZal
# Copyright (C) 2022 Zedthon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/main/LICENSE/>.

"""
ZThon - ZelZal
- كتـابـة الاضـافـات
 تطويرالوسكي الليبي وبرمجة زلزال اليمني - @BP_BP
- حقـوق زدثـــون @HL_BG
- تخمـط صيـر مطـور كفــوو واذكــر المصــدر
"""

import contextlib
import html
import os
import base64

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import MessageEntityMentionName

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest

from zthon import zedub
from zthon.core.logger import logging

from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id
from ..sql_helper.globals import gvarstatus
from . import spamwatch

plugin_category = "العروض"
LOGS = logging.getLogger(__name__)
# code by t.me/zzzzl1l
ZED_TEXT = gvarstatus("CUSTOM_ALIVE_TEXT") or "| : 𖢿"
ZEDM = gvarstatus("CUSTOM_ALIVE_EMOJI") or ""
ZEDF = gvarstatus("CUSTOM_ALIVE_FONT") or " [𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝗭𝗧𝗵𝗼𝗻𝙃𝘼𝙔𝘼](https://t.me/HL_BG) "
zed_dev = (6275847466, 6275847466)
zel_dev = (6275847466, 6275847466)
zelzal = (6275847466, 6275847466)


async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)
    )
    replied_user_profile_photos_count = "مــا عنــدش بـروفــايـل"
    dc_id = "Can't get dc id"
    with contextlib.suppress(AttributeError):
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    user_id = replied_user.id
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    zilzal = (await event.client.get_entity(user_id)).premium
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("ماعندش اسم اول ")
    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("ماعنــدش يــوزر")
    user_bio = "لا يـوجـد" if not user_bio else user_bio
# Copyright (C) 2021 Zed-Thon . All Rights Reserved
# الـرتب الوهميـه & البريميـوم كتـابـة الكـود - زلــزال الـهيبــه @zzzzl1l
    if user_id in zelzal: # code by t.me/zzzzl1l
        rotbat = "⌁ مطـور السـورس | : 𖢿 ⌁" 
    elif user_id in zel_dev:
        rotbat = "⌁ مطـور مسـاعـد | : 𖢿" 
    elif user_id == (await event.client.get_me()).id and user_id not in zed_dev:
        rotbat = "⌁ مـالك الحساب | : 𖢿" 
    else:
        rotbat = "⌁ العضـو | : 𖢿"
    caption = f"<b> {ZED_TEXT} </b>\n"
    caption += f"ٴ<b>{ZEDF}</b>\n"
    caption += f"<b>{ZEDM}اسمه   | : 𖢿 </b> "
    caption += f'<a href="tg://user?id={user_id}">{full_name}</a>'
    caption += f"\n<b>{ZEDM}معرفه| : 𖢿  {username}</b>"
    caption += f"\n<b>{ZEDM}ايديه  | : 𖢿</b> <code>{user_id}</code>\n"
    caption += f"<b>{ZEDM}رتبته | : 𖢿 {rotbat} </b>\n"
    if zilzal == True or user_id in zelzal: # code by t.me/zzzzl1l
        caption += f"<b>{ZEDM}حسابه | : 𖢿 عــــادي 🌟</b>\n"
    caption += f"<b>{ZEDM}صوره  | : 𖢿</b> {replied_user_profile_photos_count}\n"
    if user_id != (await event.client.get_me()).id: # code by t.me/zzzzl1l
        caption += f"<b>{ZEDM}قروبات مشتركه | : 𖢿 </b> {common_chat} \n"
    caption += f"<b>{ZEDM}بايو | : 𖢿  {user_bio}</b> \n"
    caption += f"ٴ<b>{ZEDF}</b>"
    return photo, caption
# Copyright (C) 2021 Zed-Thon . All Rights Reserved


@zedub.zed_cmd(
    pattern="ايدي(?: |$)(.*)",
    command=("ايدي", plugin_category),
    info={
        "header": "لـ عـرض معلومـات الشخـص",
        "الاستـخـدام": " {tr}ايدي بالـرد او {tr}ايدي + معـرف/ايـدي الشخص",
    },
)
async def who(event):
    "Gets info of an user"
    zed = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(zed, "**-تاكد من المعلومات ياطيب!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await zed.delete()
    except TypeError:
        await zed.edit(caption, parse_mode="html")


@zedub.zed_cmd(
    pattern="ا(?: |$)(.*)",
    command=("ا", plugin_category),
    info={
        "header": "امـر مختصـر لـ عـرض معلومـات الشخـص| : 𖢿",
        "الاستـخـدام": " {tr}ا بالـرد او {tr}ا + معـرف/ايـدي الشخص",
    },
)
async def who(event):
    "Gets info of an user"
    zed = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(zed, "**-تاكد من المعلومات ياطيب| : 𖢿!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await zed.delete()
    except TypeError:
        await zed.edit(caption, parse_mode="html")


@zedub.zed_cmd(
    pattern="صورته(?:\s|$)([\s\S]*)",
    command=("صورته", plugin_category),
    info={
        "header": "لـ جـلب بـروفـايـلات الشخـص| : 𖢿",
        "الاستـخـدام": [
            "{tr}صورته + عدد",
            "{tr}صورته الكل",
            "{tr}صورته",
        ],
    },
)
async def potocmd(event):
    "To get user or group profile pic"
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user and user.sender:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "**- ماعندش صوره لاعـاد تعرفـه بني آدم ولا حيوان؟ | : 𖢿**"
            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "الكل":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "**- ماعندش صوره لاعـاد تعرفـه بني آدم ولا حيوان؟ | : 𖢿**")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(
                    event, "**- رقـم غلط| : 𖢿. . .**"
                )
                return
        except BaseException:
            await edit_or_reply(event, "**- رقـم غلط| : 𖢿. . .**")
            return
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "**- ماعندش صوره لاعـاد تعرفـه بني آدم ولا حيوان؟ **"
            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()

