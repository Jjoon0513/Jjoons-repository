import discord
from datetime import datetime
import random, math

now = datetime.now()
a = 0
bot = discord.Bot()
token = "bot_token"
updatetime = now.strftime('%Y-%m-%d %H:%M:%S')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("사람인척"))
    print("아찌 온라인")

@bot.event
async def on_member_join(member):
    await member.send(
        f'어서오시오, {member.mention}여 이곳에 온걸 환영하오.'
    )

@bot.slash_command(description="쭌의 현재 행동을 알려줍니다 (아마?)")
async def 쭌은지금(ctx):
    print('쭌은지금 실행됨')
    embed = discord.Embed(title="쭌은지금 게임하는중!", colour=discord.Colour.purple())
    await ctx.respond(embed=embed)

@bot.slash_command(description="아찌의 대한 알림을 보여줍니다")
async def 알림(ctx):
    print('알림')
    embed = discord.Embed(title="구버전 아찌 섭종 알림!", description=f"아찌는 이번에 최적화를 이후로 새로은 뉴! 아찌로 도라올꺼에요! 기다려 주실수 있죠?", colour=discord.Colour.blue())
    await ctx.respond(embed=embed)



@bot.slash_command(description="응 아니야")
async def 응아니야(ctx):
    print('응 아니야 실행됨')
    embed = discord.Embed(title="응 아니야", colour=discord.Colour.red())
    await ctx.respond(embed=embed)

@bot.slash_command(description="아찌한테 간식을 줍니다")
async def 간식주기(ctx):
    print(f'간식주기 {a}번 실행됨')
    if a < 150:
        embed = discord.Embed(title="암냠냠!", description=f"아찌는 총 {a}번 간식을 먹었습니다", colour=discord.Colour.blue())
        await ctx.respond(embed=embed)
    elif 300 > a > 150:
        embed = discord.Embed(title="그 그만!", description=f"아찌는 총 {a}번 간식을 먹었습니다 조금 배불러하네요", colour=discord.Colour.blue())
        await ctx.respond(embed=embed)
    elif 600 > a > 300:
        embed = discord.Embed(title="300개를 넘었구나!", description=f"아찌는 총 {a}번 간식을 먹었습니다 살려주세요", colour=discord.Colour.blue())
        await ctx.respond(embed=embed)
    elif 1000 > a >= 600:
        embed = discord.Embed(title="진짜 그만해요!", description=f"아찌가 무려 {a}번 간식을 먹었습니다... 진짜 그만!", colour=discord.Colour.red())
        await ctx.respond(embed=embed)
    elif 2000 > a >= 1000:
        embed = discord.Embed(title="제발 그만해 이러다 다 죽어!", description=f"아찌가 이제 {a}번이나 그만그만그만그만", colour=discord.Colour.red())
        await ctx.respond(embed=embed)


@bot.slash_command(description="아찌가 먹을 라면을 선택해줍니다")
async def 라면고르기(ctx):
    ra = random.randint(1,8)
    print('라면고르기 실행됨')
    if ra == 1:
        myon = '진라면'
    elif ra == 2:
        myon = '진라면 큰 컵'
    elif ra == 3:
        myon = '육개장'
    elif ra == 4:
        myon = '육개장 큰 컵'
    elif ra == 5:
        myon = '김치사발면'
    elif ra == 6:
        myon = '김치사발면 큰 컵'
    elif ra == 7:
        myon = '참깨라면'
    elif ra == 8:
        myon = '참께라면 큰 컵'
    embed = discord.Embed(title=myon, colour=discord.Colour.blue())
    await ctx.respond(embed=embed)

@bot.slash_command(description='몸짱아찌')
async def 몸짱아찌(ctx):
    await ctx.respond('https://cdn.discordapp.com/attachments/1024634333241278505/1026775742597566496/IMG_20221003_170909_038.jpg')

@bot.slash_command(description='shows the status of the azzi bot')
async def azzistate(ctx):
    ping = round(bot.latency * 1000)
    if ping < 230:
        colour = discord.Colour.green()
    if 300 > ping >= 230:
        colour = discord.Colour.orange()
    if ping >= 300:
        colour = discord.Colour.red()
    embed = discord.Embed(title="status==online", description=f"ping: {ping}ms", colour=colour)
    await ctx.respond(embed=embed)


@bot.slash_command(description="주사위를 굴립니다")
async def 주사위(ctx):
    dice = random.randint(1,6)
    print('주사위 실행됨')
    if dice == 1:
        dicee = ':one:'
    elif dice == 2:
        dicee = ':two:'
    elif dice == 3:
        dicee = ':three:'
    elif dice == 4:
        dicee = ':four:'
    elif dice == 5:
        dicee = ':five:'
    elif dice == 6:
        dicee = ':six:'

    await ctx.respond(dicee)

@bot.slash_command(description="동전을 던집니다")
async def 동전던지기(ctx):
    coin = random.randint(1,2)
    print('동전 던지기 실행됨')
    if coin == 1:
        cooin = '앞면'
        colourset = discord.Colour.green()
    else:
        cooin = '뒷면'
        colourset = discord.Colour.blue()
    await ctx.respond(embed=discord.Embed(title=cooin, colour=colourset))

@bot.slash_command(description="어쩔티비")
async def 어쩔티비(ctx):
    print('어쩔티비 실행됨')
    embed = discord.Embed(title="어쩔티비", colour=discord.Colour.red())
    await ctx.respond(embed=embed)

@bot.slash_command(description="아찌의 사진을 아무거나 하나 보여줍니다")
async def 아찌사진첩(ctx):
    pic = random.randint(1,7)
    if pic == 1:
        await ctx.respond('https://cdn.discordapp.com/attachments/918823938136633347/1025728823397982218/5ca976ce854e810f.jpg')
    elif pic == 2:
        await ctx.respond('https://cdn.discordapp.com/attachments/918823938136633347/1025726369432338452/20221001_2008310.jpg')
    elif pic == 3:
        await ctx.respond('https://cdn.discordapp.com/attachments/918823938136633347/1025729912168005632/1663756116474.jpg')
    elif pic == 4:
        await ctx.respond('https://cdn.discordapp.com/attachments/918823938136633347/1025728381184135188/20_20221001201727.png')
    elif pic == 5:
        await ctx.respond('https://cdn.discordapp.com/attachments/918823938136633347/1048815903162236988/20221202_220536.jpg')
    elif pic == 6:
        await ctx.respond('https://cdn.discordapp.com/attachments/918823938136633347/1048815925920538714/20221202_220417.jpg')
    elif pic == 7:
        await ctx.respond('https://cdn.discordapp.com/attachments/1024634333241278505/1026775742597566496/IMG_20221003_170909_038.jpg')

@bot.slash_command(description="저쩔티비")
async def 저쩔티비(ctx):
    print('저쩔티비 실행됨')
    embed = discord.Embed(title="저쩔티비", colour=discord.Colour.red())
    await ctx.respond(embed=embed)

@bot.slash_command(description="아찌가 10면 주사위를 굴립니다")
async def 십면주사위(ctx):
    print('10면주사위 실행됨')
    tendice = random.randint(1,10)
    if tendice == 1:
        tendiceq = ':one:'
    elif tendice == 2:
        tendiceq = ':two:'
    elif tendice == 3:
        tendiceq = ':three:'
    elif tendice == 4:
        tendiceq = ':four:'
    elif tendice == 5:
        tendiceq = ':five:'
    elif tendice == 6:
        tendiceq = ':six:'
    elif tendice == 7:
        tendiceq = ':seven:'
    elif tendice == 8:
        tendiceq = ':eight:'
    elif tendice == 9:
        tendiceq = ':nine:'
    elif tendice == 10:
        tendiceq = ':keycap_ten:'
    await ctx.respond(tendiceq)

@bot.slash_command(description="뻐큐")
async def 뻐큐(ctx):
    print('뻐큐 실행됨')
    await ctx.respond(':middle_finger:')

@bot.slash_command(description="응 맞아")
async def 응맞아(ctx):
    print('응 맞아 실행됨')
    embed = discord.Embed(title="응 맞아", colour=discord.Colour.red())
    await ctx.respond(embed=embed)

@bot.slash_command(description="여긴 어디죠?")
async def 여긴어디죠(ctx):
    print('여긴 어디죠 실행됨')
    embed = discord.Embed(title="여긴어디죠?", colour=discord.Colour.red())
    await ctx.respond(embed=embed)

@bot.slash_command(description="sus")
async def sus(ctx):
    print('sus 실행됨')
    suss = random.randint(1,5)
    if suss == 1:
        await ctx.respond('https://i.imgflip.com/5f9ob7.gif')
    if suss == 2:
        await ctx.respond('https://i.imgflip.com/55lrtj.gif')
    if suss == 3:
        await ctx.respond('https://th.bing.com/th/id/OIP.NpCK1q0EdTYmpXGF7YD0PAHaJ4?pid=ImgDet&rs=1')
    if suss == 4:
        await ctx.respond('https://i.pinimg.com/originals/51/f1/60/51f160dd5838823c94a7a7e08ec8061d.jpg')
    if suss == 5:
        await ctx.respond('https://i.imgflip.com/57q6a0.jpg')

@bot.slash_command(description="rock sus")
async def rocksus(ctx):
    print('rocksus 실행됨')
    rocksuss = random.randint(1,7)
    if rocksuss == 1:
        await ctx.respond('https://i.ytimg.com/vi/Z9jGJPjHUm8/hqdefault.jpg')
    if rocksuss == 2:
        await ctx.respond('https://i.ytimg.com/vi/a5xX6DCDCYo/maxresdefault.jpg')
    if rocksuss == 3:
        await ctx.respond('https://www.igrupos.com/imagenes/436145057.jpg')
    if rocksuss == 4:
        await ctx.respond('https://entrelineas.com.mx/wp-content/uploads/2016/08/THEROCK.jpg')
    if rocksuss == 5:
        await ctx.respond('https://i1.wp.com/www.sopitas.com/wp-content/uploads/2016/05/the-rock2-e1462234259943.jpg')
    if rocksuss == 6:
        await ctx.respond('https://qph.fs.quoracdn.net/main-qimg-d80c7c62524471c58effff6ed63a773f')
    if rocksuss == 7:
        await ctx.respond('https://eay8xzxp7gq.exactdn.com/wp-content/uploads/2021/07/The-Rock-stares-at-Steve-Austin-2001-Royal-Rumble-1536x1164.jpg?strip=all&lossy=1&ssl=1')

@bot.slash_command(description="스팀 신규 및 인기 신제품을 보여줍니다")
async def 스팀추천게임(ctx):
    print('스팀추천게임 실행됨')
    await ctx.respond('https://store.steampowered.com/app/824000/Hokko_Life/')
    await ctx.respond('2022년 9월 28일 기준')

@bot.slash_command(description="업데이트가 된 시각을 보여줍니다")
async def 업데이트시각(ctx):
    print('업데이트 시각 실행됨')
    embed = discord.Embed(title=updatetime, colour=discord.Colour.green())
    await ctx.respond(embed=embed)

@bot.slash_command(description="아찌를 서버에 초대할수있는 링크를 보여줍니다")
async def 우리서버에도아찌를(ctx):
    print('우리 서버에도 아찌를 실행됨')
    embed = discord.Embed(title='여기!', description='https://discord.com/api/oauth2/authorize?client_id=1020863208472444938&permissions=8&scope=bot', colour=discord.Colour.blue())
    await ctx.respond(embed=embed)

@bot.slash_command(description="아찌더미봇에 대해 말해줍니다")
async def 아찌더미봇에대해(ctx):
    print('아찌 더미봇에 대해 실행됨')
    embed = discord.Embed(title='아찌더미봇이란', description='아찌가 정식적으로 릴리즈 되기 전 테스트 봇입니다', color=discord.Colour.blue())
    await ctx.respond(embed=embed)

@bot.slash_command(description="짖습니다")
async def 짖어(ctx):
    print('짖어 실행됨')
    woolf = random.randint(1,3)
    if woolf == 1:
        wooolf = '월'
    elif woolf == 2:
        wooolf = '컹'
    elif woolf == 3:
        wooolf = '멍'
    embed = discord.Embed(title=wooolf, colour=discord.Colour.red())
    await ctx.respond(embed=embed)

@bot.slash_command(description="아찌가 금지된 장난감인 마법의 소라고동을 건듭니다")
async def 마법의소라고동(ctx):
    print('마법의 소라고동 실행됨')
    so = random.randint(1, 6)
    if so == 1:
        ra = '아니'
    elif so == 2:
        ra = '당연하지'
    elif so == 3:
        ra = '당연히 아니지'
    elif so == 4:
        ra = '그래야만해'
    elif so == 5:
        ra = '그러지 않아야만해'
    elif so == 6:
        ra = '어'
    embed = discord.Embed(title=ra, colour=discord.Colour.red())
    await ctx.respond(embed=embed)

@bot.slash_command(description="아찌가 찍기를 도와줍니다")
async def 오지선다찍기(ctx):
    print('오지선다찍기 실행됨')
    oge = random.randint(1,5)
    if oge == 1:
        sun = '1번'
    elif oge == 2:
        sun = '2번'
    elif oge == 3:
        sun = '3번'
    elif oge == 4:
        sun = '4번'
    elif oge == 5:
        sun = '5번'
    embed = discord.Embed(title=sun, colour=discord.Colour.green())
    await ctx.respond(embed=embed)

@bot.slash_command(description="아찌가 몸짱이 될때 먹었던 프로틴을 선택해줍니다")
async def 프로틴고르기(ctx):
    print('프로틴고르기 실행됨')
    pro = random.randint(1,6)
    if pro == 1:
        tin = '초코맛 프로틴'
    elif pro == 2:
        tin = '바나나맛 프로틴'
    elif pro == 3:
        tin = 'Just 프로틴'
    elif pro == 4:
        tin = '딸기맛 프로틴'
    elif pro == 5:
        tin = '쥬스맛 프로틴'
    elif pro == 6:
        tin = '스낵맛 프로틴'
    embed = discord.Embed(title=tin, colour=discord.Colour.green())
    await ctx.respond(embed=embed)

bot.run('token')
