import discord
import asyncio
import random


import re

COR = 0x690FC3

msg_id = None
msg_user = None
qntdd = int


def toint(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

client = discord.Client()



@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="-Digite ?ajuda"))
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('-----TheLopes-----')

@client.event
async def on_message(message):

     if  message.author.id == '334359138110799872':

       if message.content.lower().startswith('?delete'):
          qntdd = message.content.strip('?delete ')
          qntdd = toint(qntdd)
          if qntdd <= 100:
              msg_author = message.author.mention
              await client.delete_message(message)
              # await asyncio.sleep(1)
              deleted = await client.purge_from(message.channel, limit=qntdd)
              botmsgdelete = await client.send_message(message.channel,
                                                       'Deletei {} mensagens '.format(
                                                           len(deleted),  msg_author))
              await asyncio.sleep(5)
              await client.delete_message(botmsgdelete)

          else:
              botmsgdelete = await client.send_message(message.channel,
                                                       'Utilize o comando digitando ?delete <numero de 1 a 100>')
              await asyncio.sleep(5)
              await client.delete_message(message)
              await client.delete_message(botmsgdelete)

     if message.content.lower().startswith('?ajuda'):
         user = message.author
         server = message.server
         embedinfo = discord.Embed(
             title='📌Comandos',
             color=COR,
             description='\n'
                         '\n'
         )
         embedinfo.set_thumbnail(url='https://cdn.discordapp.com/attachments/425891735059824673/426953764084383755/J.A.R.V.I.S._Rank_5_Icon.png')

         embedinfo.add_field(name='?avatar',value='Mostra o seu avatar', inline=False)
         embedinfo.add_field(name='?jarvis',value='Chama o BOT', inline=False)
         embedinfo.add_field(name='?contato',value='Envia o contato do programador', inline=False)
         embedinfo.add_field(name='?cadastro',value='Abre o menu de cadastro', inline=False)
         embedinfo.add_field(name='?enviardados', value='Envie Dados ao BOT', inline=False)
         embedinfo.add_field(name='?registro',value='Abre o menu de registro', inline=False)
         embedinfo.add_field(name='?convite',value='Mostra o convite do F SOCIETY', inline=False)
         embedinfo.add_field(name='?moeda',value='Joga uma moeda.',inline=False)
         embedinfo.add_field(name='?perfil',value='Abre o menu para definir seus cargos', inline=False)
         embedinfo.add_field(name='?rlol',value='Escolhe Entre:|Top|Jungle|Mid|Adc|Suporte|', inline=False)
         embedinfo.add_field(name='?cblol',value='Mostra o Link do Canal no Youtube da CBLOL.',inline=False)
        
         await client.send_message(message.author, embed=embedinfo)
         print('Alguem usou o ?ajuda')



     if message.content.lower().startswith('?dance'):
   
     
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/289891525918195712/428189193919922179/tenor.gif")
        await client.delete_message(message)

     if message.content.lower().startswith('?midiacad'):
      embed50 = discord.Embed(
      title='Realize o Cadastro.',
      color=COR,
      description=
                 'Para ter acesso as salas de jogos.\n'
         ' \n'
         ' \n'
          '-Digite **?cadastro**',)

      embed50.set_thumbnail(
         url='https://cdn.discordapp.com/attachments/392746066555961345/429135327274336266/0f3ed952323519.5608d8fce47b2.png')
      await client.send_message(message.channel, embed=embed50)
        
      if message.content.lower().startswith('?midiaperfil'):
        embed510 = discord.Embed(
        title='-Escolha seus Cargos!',
        color=COR,
        description=
                 'Digite **?perfil**\n'
         ' \n'
         ' \n'
          '**OBS:** Esse comando só funciona pra quem já fez o cadastro.',)
        embed510.set_thumbnail(
          url='https://cdn.discordapp.com/attachments/392746066555961345/429135327274336266/0f3ed952323519.5608d8fce47b2.png')
        await client.send_message(message.channel, embed=embed510)
          
        
     if message.content.lower().startswith('?avatar'):
        avatarembed = discord.Embed(
            title="",
            color=COR,
            description="[Clique aqui](" + message.author.avatar_url + ") para acessar o link de seu avatar!"
        )
        avatarembed.set_author(name=message.author.name)
        avatarembed.set_image(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=avatarembed)
        await client.delete_message(message)



     if message.content.lower().startswith('?jarvis'):
        msgjarvis= 'Olá {}, Cheguei!'.format(message.author.mention)
        await client.send_message(message.channel, msgjarvis)
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/289891525918195712/428189193919922179/tenor.gif")
        await client.delete_message(message)

        
     if message.content.lower().startswith('?cblol'):
        link2 = 'https://www.youtube.com/channel/UC48rkTlXjRd6pnqqBkdV0Mw'
        embedcblol = discord.Embed(
        title='LoL eSports BR',
        color=COR,
        description= "[Clique aqui]("+ link2 +") Para acessar o Canal No Youtube!\n"   
        
        embedcblol.set_thumbnail(url='https://cdn.discordapp.com/attachments/392746066555961345/429423972862656522/CBLOL_2017_Logo.png')
        await client.send_message(message.channel, embed=embedcblol)
        await client.delete_message(message)
        
        
        

     if message.content.lower().startswith("?contato"):
       embed2 = discord.Embed(

        title="Contato do Programador",
        color=COR,
        description=
        "\n"
        "Discord:  TheLopes#5834 \n"
        "\n"
        "Email: jefersonlopes.sjn@hotmail.com"


         ,)
       embed2.set_image(url=message.author.avatar_url)
       botmsg = await client.send_message(message.author, embed=embed2)
       await client.delete_message(message)


     elif message.content.lower().startswith('?diz'):
       if not message.author.id == '334359138110799872':
           return await client.send_message(message.channel, "```Você Não tem permissão.```")
       await client.send_message(message.channel, message.content[4:])
       await client.delete_message(message)

     elif message.content.lower().startswith('?dizavisos'):
       if not message.author.id == '334359138110799872':
           return await client.send_message(message.channel, "```Você Não tem permissão.```")
       await client.send_message(message.channel, message.content[4:])
       await client.delete_message(message)



     if message.content.lower().startswith('?registro'):
        await client.send_message(message.channel, '```Digite seu numero de Registro.```')

        msg1 = await client.wait_for_message(author=message.author, content='0001')

        embed0001= discord.Embed(

           title="",
           color=COR,
           description=
                    "**Nome**: Jeferson Lopes\n"
                    "\n"
                    "**Email**: jefersonlopes.sjn@hotmail.com\n"
                    "\n"
                    "**Nome Online**: TheLopes\n"
                    "\n"
                    "**Plataforma**: PS3| PS4| PC\n"
                    "\n"
                    "**Jogo**: GTA 5| FORTNITE| LOL",)
        await client.send_message(message.channel, embed=embed0001)
        embed0001.set_thumbnail(url='https://cdn.discordapp.com/attachments/392746066555961345/429160893377544203/Coroa-Dourada-16.png')

        msg2 = await client.wait_for_message(author=message.author, content='0002')
        embed0002 = discord.Embed(

            title="",
            color=COR,
            description=
            "**Nome**: Anthony \n"
            "\n"
            "**Email**: _ \n"
            "\n"
            "**Nome Online**: Anthonyalmeida50\n"
            "\n"
            "**Plataforma**: PS3\n"
            "\n"
            "**Jogo**: GTA 5", )
        await client.send_message(message.channel, embed=embed0002)



     elif message.content.lower().startswith('?rv'):



       avisos= client.get_channel("392711722172940298")
       canalbots= client.get_channel("400703461068374017")
       msgvr= "-Digite ** `` ?perfil `` ** no canal {} para escolher seus cargos!".format(canalbots.mention)
       await client.send_message(avisos, message.content[3:])

       await client.send_message(avisos, msgvr)
       await client.delete_message(message)

        
        
     if message.content.lower().startswith('?rlol'):
        choice = random.randint(1, 5)
        if choice == 1:
            await client.send_message(message.channel, '```Top```')
        if choice == 2:
            await client.send_message(message.channel, ' ```Jungle``` ')
        if choice == 3:
            await client.send_message(message.channel,' ```Mid``` ')
        if choice == 4:
            await client.send_message(message.channel,' ```Adc``` ')
        if choice == 5:
            await client.send_message(message.channel, ' ```Suporte``` ') 
        
        
        

     if message.content.lower().startswith('?cadastro'):
      link= 'https://discord.gg/43Zf9XK'

      embed3 = discord.Embed(
            title="Realização do Cadastro do server **F SOCIETY**",
            color=COR,
            description="\n"
                        "\n"
            "[Clique aqui]("+ link +")   Para entrar no server!\n" 
             "\n"
              "\n"
            "```Nome:\n"
            "Email:\n"
            "Nome Online:\n"
            "Plataforma:\n"
            "Jogo:```\n"
            "\n"
            
            
            "-Digite **?enviardados** *Seus Dados*"
          ,)
      botmsg = await client.send_message(message.channel, embed=embed3)

      await client.delete_message(message)
      print('Alguem Usou o comando de cadastro!')


     elif message.content.lower().startswith('?enviardados'):
         canal= client.get_channel("425150435725279253")
         avisos= client.get_channel("392711722172940298")
         msgdados= "{} Aguarde a confirmação do Registro.\n" \
                           "Ela irá aparecer em {}".format(message.author.mention, avisos.mention)


         await client.send_message(canal, "<@334359138110799872>")
         await client.send_message(canal, message.content[12:])
         await client.send_message(message.channel, msgdados)
         await client.delete_message(message)




     if message.content.lower().startswith('?convite'):
      await client.send_message(message.channel,"https://discord.gg/43Zf9XK")
      await client.delete_message(message)

     if message.content.lower().startswith('?moeda'):
      choice = random.randint(1,2)
      if choice == 1:
         await client.add_reaction(message, '😀')
      if choice == 2:
         await client.add_reaction(message, '👑')

     if message.content.lower().startswith("?lol"):
         user = message.author
         server = message.server
         embedlol = discord.Embed(
             title='Escolha Seu Elo e Lane',
             color=COR,
             description='\n'
                         '\n')
         embedlol.set_thumbnail(
             url='https://cdn.discordapp.com/attachments/392746066555961345/429129366291873814/resize.png')

         embedlol.add_field(name='Unranked', value='<:Unranked:428031343918710794>', inline=True)
         embedlol.add_field(name='Top', value='<:top:428031683544219671>', inline=True)
         embedlol.add_field(name='Bronze', value='<:bronze:428031523502030848>', inline=True)
         embedlol.add_field(name='Jungle', value='<:jungle:428031580116877312>', inline=True)
         embedlol.add_field(name='Prata', value='<:prata:428031631069282304>', inline=True)
         embedlol.add_field(name='Mid', value='<:mid:428031598517288962>', inline=True)
         embedlol.add_field(name='Ouro', value='<:ouro:428031561825386496>', inline=True)
         embedlol.add_field(name='Adc', value='<:adc:428037272923930644>', inline=True)
         embedlol.add_field(name='Platina', value='<:platina:428031671632134156>', inline=True)
         embedlol.add_field(name='Suporte', value='<:suporte:428031644046458890>', inline=True)
         embedlol.add_field(name='Diamante', value='<:diamante:428031544473550859>', inline=True)

         botmsglol = await client.send_message(message.channel, embed=embedlol)

         await client.add_reaction(botmsglol, ":Unranked:428031343918710794")
         await client.add_reaction(botmsglol," :top:428031683544219671")
         await client.add_reaction(botmsglol, ":bronze:428031523502030848 ")
         await client.add_reaction(botmsglol, ":jungle:428031580116877312 ")
         await client.add_reaction(botmsglol, " :prata:428031631069282304")
         await client.add_reaction(botmsglol, ":mid:428031598517288962 ")
         await client.add_reaction(botmsglol, ":ouro:428031561825386496 ")
         await client.add_reaction(botmsglol, ":adc:428037272923930644 ")
         await client.add_reaction(botmsglol, ":platina:428031671632134156 ")
         await client.add_reaction(botmsglol, ":suporte:428031644046458890")
         await client.add_reaction(botmsglol, ":diamante:428031544473550859")





     if message.content.lower().startswith("?perfil"):
        if not message.author.id == '334359138110799872'and '335531697858674688':
             return await client.send_message(message.channel, "```Faça nosso Cadastro para ter acesso as salas de Jogos.```")
        embed1 =discord.Embed(

           title="Defina seu Perfil!",
           color=COR,
           description="🔫 - GTA       \n"
                    "⚔ - LOL       \n"
                    "🛡 - FORTNITE  \n"
                    "👦 - MEMBRO    ",)
        botmsg = await client.send_message(message.channel, embed=embed1)
        await client.delete_message(message)
        await client.add_reaction(botmsg, "🔫")
        await client.add_reaction(botmsg, "⚔")
        await client.add_reaction(botmsg, "🛡")
        await client.add_reaction(botmsg, "👦")

        global msg_id
        msg_id = botmsg.id
        global msg_user
        msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🔫" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "GTA", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚔" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "LOL", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🛡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "FORTNITE", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "👦" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Membro", msg.server.roles)
     await client.add_roles(user, role)
     print("add")





@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🔫" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "GTA", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚔" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "LOL", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🛡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "FORTNITE", msg.server.roles)
     await client.remove_roles(user,role)

    if reaction.emoji == "👦" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Membro", msg.server.roles)
     await client.remove_roles(user,role)
     print("remove")


client.run('NDIzNzM4OTEzODc4OTY2Mjgz.DZw-vQ.C6c71fWztCIdQDvMTwxoI_Wvnb8')
