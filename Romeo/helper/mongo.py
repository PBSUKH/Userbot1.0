from Romeo.helper import dbb
Rbun = dbb["RBAN"]
async def rraid(user, reason="#MC"):
    await Rbun.insert_one({"user": user, "reason": reason})
async def runraid(user):
    await Rbun.delete_one({"user": user})
async def rban_list():
    return [lo async for lo in Rbun.find({})]
async def raidub_info(user):
    kk = await Rbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]

Lbun = dbb["LBAN"]
async def rlove(user, reason="#MYLOVER"):
    await Lbun.insert_one({"user": user, "reason": reason})
async def runlove(user):
    await Lbun.delete_one({"user": user})
async def lban_list():
    return [lo async for lo in Lbun.find({})]
async def loveub_info(user):
    um = await Lbun.find_one({"user": user})
    if not um:
        return False
    else:
        return um["reason"]
