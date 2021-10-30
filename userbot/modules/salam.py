from time import sleep
from platform import uname
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Assalamualaikum.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Assalamualaikum.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Waallaikumsalam......`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Waallaikumsalam.....`")
# Owner @Si_Dian


CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
