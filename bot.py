import discord
import asyncio
import data

client = discord.Client()

COR =0x11283B
msg_id = None
msg_user = None
server_token = data.get_token()


def get_channel(server, channel_name):
    for channels in server.channels :
        if channels == channel_name :
            return channels

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_member_join(member):

    embed1 =discord.Embed(
        title="Seja muito bem vindo ao server da UnB dos Brothers\n\n- Não esqueça de olhar o canal de texto #boas-vindas\n\n- Nos ajude a te identificar, o que você faz ? (Sem mentir, não prejudique o servidor)",
        color=COR,
        description="\n- Estudante de Ciência da Computação - UnB = 💻\n"
        "- Estudo na UnB =  🎓 \n"
        "- Não estudo na UnB = 🤷",)

    server = member.server
    channel = get_channel(server, "geral")
    botmsg = await client.send_message(member, embed=embed1)

    await client.add_reaction(botmsg, "💻")
    await client.add_reaction(botmsg, "🎓")
    await client.add_reaction(botmsg, "🤷")
    
    global msg_id
    msg_id = botmsg.id

@client.event
async def on_reaction_add(reaction, user):
    
    server = client.get_server(data.get_server_id())
    member = server.get_member(user.id)
    msg = reaction.message

    if reaction.emoji == "💻" and msg.id == msg_id: 
        role = discord.utils.find(lambda r: r.name == "Calouro Burro", server.roles)

    elif reaction.emoji == "🎓" and msg.id == msg_id: 
        role = discord.utils.find(lambda r: r.name == "UnB", server.roles)

    else:
        role = discord.utils.find(lambda r: r.name == "Disney", server.roles)

    await client.add_roles(member, role)

@client.event
async def on_reaction_remove(reaction, user):

    server = client.get_server(data.get_server_id())
    member = server.get_member(user.id)
    msg = reaction.message

    if reaction.emoji == "💻" and msg.id == msg_id: 
        role = discord.utils.find(lambda r: r.name == "Calouro Burro", server.roles)

    elif reaction.emoji == "🎓" and msg.id == msg_id: 
        role = discord.utils.find(lambda r: r.name == "UnB", server.roles)

    else:
        role = discord.utils.find(lambda r: r.name == "Disney", server.roles)

    await client.remove_roles(member, role)

client.run(server_token)