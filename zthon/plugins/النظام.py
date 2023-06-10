"""Get the info your system. Using .neofetch then .sysd"""

# .spc command is ported from  alfianandaa/ProjectAlf

import platform
import sys
from datetime import datetime

import psutil
from telethon import __version__

from zthon import zedub

from ..core.managers import edit_or_reply
from ..helpers.utils import _zedutils

plugin_category = "الادوات"


def get_size(inputbytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if inputbytes < factor:
            return f"{inputbytes:.2f}{unit}{suffix}"
        inputbytes /= factor


@zedub.zed_cmd(
    pattern="النظام$",
    command=("النظام", plugin_category),
    info={
        "header": "To show system specification.",
        "الاستـخـدام": "{tr}النظام",
    },
)
async def psu(event):
    "shows system specification"
    uname = platform.uname()
    softw = "** 𓆩 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝗭𝗧𝗵𝗼𝗻𝙃𝘼𝙔𝘼 @HL_BG المطور @BP_BP 𓆪 **\n"
    softw += f"**𖢿︙╎النظام : ** `{uname.system}`\n"
    softw += f"**𖢿︙╎المرجع  : ** `{uname.release}`\n"
    softw += f"**𖢿︙╎الاصدار  : ** `{uname.version}`\n"
    softw += f"**𖢿︙╎النـوع  : ** `{uname.machine}`\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"**𖢿︙╎تاريـخ التنصيب : **\n**- التاريـخ 📋:**\t`{bt.day}/{bt.month}/{bt.year}`\n**- الـوقت ⏰:**\t`{bt.hour}:{bt.minute}`\n"
    # CPU Cores
    cpuu = "**- معلومات المعالـج :**\n"
    cpuu += "**𖢿︙╎الماديـه   :** `" + str(psutil.cpu_count(logical=False)) + "`\n"
    cpuu += "**𖢿︙╎الكليـه      :** `" + str(psutil.cpu_count(logical=True)) + "`\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"**𖢿︙╎اعلـى تـردد    : ** `{cpufreq.max:.2f}Mhz`\n"
    cpuu += f"**𖢿︙╎اقـل تـردد    : ** `{cpufreq.min:.2f}Mhz`\n"
    cpuu += f"**𖢿︙╎التـردد الإفتـراضـي : ** `{cpufreq.current:.2f}Mhz`\n\n"
    # CPU usage
    cpuu += "**- استخدامات المعالج لكل وحده :**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"**𖢿︙╎كـور {i}  : ** `{percentage}%`\n"
    cpuu += "**- استخدامات المعالج الكليـه :**\n"
    cpuu += f"**𖢿︙╎الكـليه : ** `{psutil.cpu_percent()}%`\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**- استخدامـات الذاكـره :**\n"
    memm += f"**𖢿︙╎الكـليه     : ** `{get_size(svmem.total)}`\n"
    memm += f"**𖢿︙╎الفعليـه : ** `{get_size(svmem.available)}`\n"
    memm += f"**𖢿︙╎المستخدمـه      : ** `{get_size(svmem.used)}`\n"
    memm += f"**𖢿︙╎المتاحـه: ** `{svmem.percent}%`\n"
    # Bandwidth Usage
    bw = "**- استخدامات الرفـع والتحميـل :**\n"
    bw += f"**𖢿︙╎الرفـع  : ** `{get_size(psutil.net_io_counters().bytes_sent)}`\n"
    bw += f"**𖢿︙╎التحميـل : ** `{get_size(psutil.net_io_counters().bytes_recv)}`\n"
    help_string = f"{str(softw)}\n"
    help_string += f"{str(cpuu)}\n"
    help_string += f"{str(memm)}\n"
    help_string += f"{str(bw)}\n"
    help_string += "**- إصـدار بايثــون & سبـارك :**\n"
    help_string += f"**𖢿︙╎بايثـون : ** `{sys.version}`\n"
    help_string += f"**𖢿︙╎تيليثـون : ** `{__version__}`"
    await event.edit(help_string)


@zedub.zed_cmd(
    pattern="cpu$",
    command=("cpu", plugin_category),
    info={
        "header": "To show cpu information.",
        "الاستـخـدام": "{tr}cpu",
    },
)
async def cpu(event):
    "shows cpu information"
    cmd = "zed /proc/cpuinfo | grep 'model name'"
    o = (await _zedutils.runcmd(cmd))[0]
    await edit_or_reply(
        event, f"**[Tepthon](tg://need_update_for_some_feature/) CPU Model:**\n{o}"
    )


@zedub.zed_cmd(
    pattern="نظامي$",
    command=("sysd", plugin_category),
    info={
        "header": "Shows system information using neofetch",
        "الاستـخـدام": "{tr}نظامي",
    },
)
async def sysdetails(sysd):
    "Shows system information using neofetch"
    zedevent = await edit_or_reply(sysd, "`Fetching system information.`")
    cmd = "git clone https://github.com/dylanaraps/neofetch.git"
    await _zedutils.runcmd(cmd)
    neo = "neofetch/neofetch --off --color_blocks off --bold off --cpu_temp C \
                    --cpu_speed on --cpu_cores physical --kernel_shorthand off --stdout"
    a, b, c, d = await _zedutils.runcmd(neo)
    result = str(a) + str(b)
    await edit_or_reply(zedevent, f"**Neofetch Result:** `{result}`")
