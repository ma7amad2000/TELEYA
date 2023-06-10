import re

from telethon.utils import get_display_name

from zthon import zedub

from ..core.managers import edit_or_reply
from ..sql_helper import blacklist_sql as sql
from ..utils import is_admin
from . import BOTLOG_CHATID


@zedub.zed_cmd(incoming=True, groups_only=True)
async def on_new_message(event):
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    zthonadmin = await is_admin(event.client, event.chat_id, event.client.uid)
    if not zthonadmin:
        return
    for snip in snips:
        pattern = f"( |^|[^\\w]){re.escape(snip)}( |$|[^\\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"**𖢿╎عـذراً عـزيـزي مـالك البـوت\n𖢿╎ليست لدي صلاحية الحذف في** {get_display_name(await event.get_chat())}.\n**𖢿╎لذا لن يتم إزالة الكلمات الممنوعـه في تلك الدردشـه ؟!**",
                )
                for word in snips:
                    sql.rm_from_blacklist(event.chat_id, word.lower())
            break


@zedub.zed_cmd(
    pattern="منع(?:\s|$)([\s\S]*)",
    require_admin=True,
)
async def _(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await edit_or_reply(
        event,
        f"**𖢿╎تم اضافة (** {len(to_blacklist)} **)**\n**𖢿╎الى قائمة الكلمـات الممنوعـه هنـا .. بنجـاح ✓**",
    )


@zedub.zed_cmd(
    pattern="الغاء منع(?:\s|$)([\s\S]*)",
    require_admin=True,
)
async def _(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )
    successful = sum(
        bool(sql.rm_from_blacklist(event.chat_id, trigger.lower()))
        for trigger in to_unblacklist
    )
    await edit_or_reply(
        event, f"**𖢿╎تم حذف (** {successful} / {len(to_unblacklist)} **(**\n**𖢿╎من قائمة الكلمـات الممنوعـه هنـا .. بنجـاح ✓**"
    )


@zedub.zed_cmd(
    pattern="قائمة المنع$",
    require_admin=True,
)
async def _(event):
    all_blacklisted = sql.get_chat_blacklist(event.chat_id)
    OUT_STR = "**𖢿╎قائمة الكلمـات الممنوعـه هنـا هـي :\n**"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"- {trigger} \n"
    else:
        OUT_STR = "**𖢿╎لم يتم اضافة كلمـات ممنوعـة هنـا بعـد ؟!**"
    await edit_or_reply(event, OUT_STR)
