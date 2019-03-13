import discord
import asyncio
import data

client = discord.Client()

COR =0x11283B
msg_id = None
msg_user = None
server_token = data.get_token()
bot_id = data.get_bot_id()


@client.event
async def direct_welcome_message(member):

    private_welcome_message =discord.Embed(
        title= "Seja muito bem vindo novamente ao server da UnB dos Brothers\n\n- Dê uma olhada no canal de texto #boas-vindas\n\n- Nos ajude a te identificar, o que você faz ? (Sem mentir, não prejudique o servidor)",
        color=COR,
        description="\n- Estudante de Ciência da Computação - UnB = 💻\n"
        "- Estudo na UnB =  🎓 \n"
        "- Não estudo na UnB = 🤷",)


    botmsg = await client.send_message(member, embed = private_welcome_message)
    await client.add_reaction(botmsg, "💻")
    await client.add_reaction(botmsg, "🎓")
    await client.add_reaction(botmsg, "🤷")


def get_channel(server, channel_name):
    for channels in server.channels :
        if channels.name == channel_name :
            return channels

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_member_join(member):

    welcome_message = member.mention + " , seja muito bem vindo ao server da UnB dos Brothers!\n\n- Não esqueça de olhar a mensagem no privado que te mandei!"
     
    server = member.server
    channel = get_channel(server, "general")

    await client.send_message(channel, welcome_message)

    await direct_welcome_message(member)
    
@client.event
async def on_reaction_add(reaction, user):
    
    server = client.get_server(data.get_server_id())
    member = server.get_member(user.id)
    bot_member = server.get_member(bot_id)
    owner = reaction.message.author.id
    message = reaction.message

    if owner != bot_id or user.id == bot_id:
        return

    if reaction.emoji == "💻" :

        await client.delete_message(message)

        private_computer_science_message = discord.Embed(
            title= "Seja muito bem vindo novamente ao server da UnB dos Brothers\n\n- Dê uma olhada no canal de texto #boas-vindas\n\n- Nos ajude a te identificar, em qual semestre você está ? (Sem mentir, não prejudique o servidor)",
            color=COR,
            description="\n- 3 º Semestre ou mais = 🥇\n"
            "- 2 º Semestre =  🥈 \n"
            "- 1 º Semestre = 🥉 \n"
            "- Voltar = ⬅",)


        botmsg = await client.send_message(member, embed = private_computer_science_message )

        await client.add_reaction(botmsg, "🥇")
        await client.add_reaction(botmsg, "🥈")
        await client.add_reaction(botmsg, "🥉")
        await client.add_reaction(botmsg, "⬅")


        return


    elif reaction.emoji == "🥇" :
        role = discord.utils.find(lambda r: r.name == "Veterano", server.roles)

    elif reaction.emoji == "🥈" :
        role = discord.utils.find(lambda r: r.name == "Calouro B", server.roles)

    elif reaction.emoji == "🥉" :
        role = discord.utils.find(lambda r: r.name == "Calouro Burro", server.roles)

    elif reaction.emoji == "⬅" :
        await client.delete_message(message)
        await direct_welcome_message(member)
        return

    elif reaction.emoji == "🎓" : 
        role = discord.utils.find(lambda r: r.name == "UnB", server.roles)

    elif reaction.emoji == "🤷":
        role = discord.utils.find(lambda r: r.name == "Disney", server.roles)
    
    else:
        return

    await client.add_roles(member, role)

@client.event
async def on_reaction_remove(reaction, user):

    server = client.get_server(data.get_server_id())
    member = server.get_member(user.id)
    owner = reaction.message.author.id

    if owner != bot_id or user.id == bot_id:
        return

    if reaction.emoji == "🥇" :
        role = discord.utils.find(lambda r: r.name == "Veterano", server.roles)

    elif reaction.emoji == "🥈" :
        role = discord.utils.find(lambda r: r.name == "Calouro B", server.roles)

    elif reaction.emoji == "🥉" :
        role = discord.utils.find(lambda r: r.name == "Calouro Burro", server.roles)

    elif reaction.emoji == "🎓" : 
        role = discord.utils.find(lambda r: r.name == "UnB", server.roles)

    elif reaction.emoji == "🤷" :
        role = discord.utils.find(lambda r: r.name == "Disney", server.roles)
    
    else:
        return

    await client.remove_roles(member, role)

client.run(server_token)