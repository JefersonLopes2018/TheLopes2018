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
    await client.change_presence(game=discord.Game(name="?ajuda"))
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
         embedinfo.set_thumbnail(url='https://cdn.discordapp.com/avatars/423738913878966283/3eae6e8f5be338604dbf4a21ad96a34c.webp?size=1024')

         embedinfo.add_field(name='🔷Comandos de interação',value='.', inline=False)
       
         embedinfo.add_field(name='?jarvis',value='Chama o BOT', inline=False)
         embedinfo.add_field(name='?avatar',value='Mostra o seu avatar', inline=False)
         embedinfo.add_field(name='t?avatar *@user*',value='Mostra o avatar do user.', inline=False)
         embedinfo.add_field(name='?enquete',value='Cria uma enquete', inline=False)
         embedinfo.add_field(name='?contato',value='Envia o contato do programador', inline=False)
         embedinfo.add_field(name='?rlol',value='Escolhe Entre:|Top|Jungle|Mid|Adc|Suporte|', inline=False)
         embedinfo.add_field(name='?cblol',value='Mostra o Link do Canal no Youtube da CBLOL',inline=False)
         embedinfo.add_field(name='?moeda',value='Joga uma moeda.',inline=False)
         embedinfo.add_field(name='?convite',value='Mostra o convite do F SOCIETY', inline=False)
        
         embedinfo.add_field(name='🔷Comandos de registros',value='.', inline=False)
        
         embedinfo.add_field(name='?perfil',value='Abre o menu para definir seus cargos', inline=False)
         embedinfo.add_field(name='?cadastro',value='Abre o menu de cadastro', inline=False)
         embedinfo.add_field(name='?enviardados', value='Envie Dados ao BOT', inline=False)
         embedinfo.add_field(name='?registro',value='Abre o menu de registro', inline=False)
         embedinfo.add_field(name='?relist',value='Mostra a lista de usuarios registrados', inline=False)
         
      
         embedinfo.set_footer(text="-Digite ok para receber a lista no privado.")
         await client.send_message(message.channel, embed=embedinfo)
         await client.add_reaction(message, '😄')
         msg1 = await client.wait_for_message(author=message.author, content='ok')
         await client.send_message(message.author, embed=embedinfo)
         

       
    
      #sistema_de_enquete


     if message.content.lower().startswith("?enquete"):
      menssagem = message.content[9:]
      msp = await client.send_message(message.channel, menssagem)

      await client.delete_message(message)
      await client.add_reaction(msp, ':sim:444562578639945728')
      await client.add_reaction(msp, ':nao:444562647799562261')
   


     #lixo
    
     if message.content.lower().startswith('?dance'):
   
     
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/289891525918195712/428189193919922179/tenor.gif")
        await client.delete_message(message)

        
     if message.content.lower().startswith('?cadinfo'):
      embed50 = discord.Embed(
      title='Realize o Cadastro.',
      color=COR,
      description=
                 '-Para ter Seu Registro no Banco de dados do <@423738913878966283>.\n'
         ' \n'
         ' \n'
          '-Digite **?cadastro**',)
         
      await client.send_message(message.channel, embed=embed50)
      await client.add_reaction(message, '📑')  
        
        
        
        
        
        
        
      #sistema_de_avatar
       
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


     if message.content.lower().startswith('t?avatar'):
        try:
            embederro = discord.Embed(
                title='Erro',
                color=COR,
                description='Este nick não existe ou saiu do servidor',
            )
            embederro.set_thumbnail(url=client.user.avatar_url)
            user = message.mentions[0]

            avatarembed = discord.Embed(
                title="",
                color=COR,
                description='Aqui está o avatar de **{}**! '.format(user.name),
            )

            avatarembed.set_image(url=user.avatar_url)
            botmsg = await client.send_message(message.channel, embed=avatarembed)

        except IndexError:
            await client.send_message(message.channel, embed=embederro)
        except:
            await client.send_message(message.channel, embed=embederro)
        finally:
            pass
        

        
        
        
        
        
        #jarvis_online
        
     if message.content.lower().startswith('?jarvis'):
        msgjarvis= 'Olá {}, Cheguei!'.format(message.author.mention)
        await client.send_message(message.channel, msgjarvis)
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/289891525918195712/428189193919922179/tenor.gif")
        await client.delete_message(message)

        
        
        
        
        #contato
        
     if message.content.lower().startswith("?contato"):
       embed2 = discord.Embed(

        title="Contato do Programador",
        color=COR,
        description=
        "\n"
        "Whatsapp: (53) 9-9909-6291 \n"
        "Discord: <@334359138110799872> \n"
        "\n"
        "Email: jefersonlopes.sjn@hotmail.com"


         ,)
       embed2.set_image(url=message.author.avatar_url)
       botmsg = await client.send_message(message.author, embed=embed2)
       await client.add_reaction(message,'👊'
        
        
        
        
     #sistema_de_controle(mensagem)
        
        
   

      
        
        
        #lol
        
        
     if message.content.lower().startswith('?cblol'):
        link2 = 'https://www.youtube.com/channel/UC48rkTlXjRd6pnqqBkdV0Mw'
        embedcblol = discord.Embed(
         title='LoL eSports BR',
         color=COR,
         description= "\n"
            "[Clique aqui]("+ link2 +") Para acessar o Canal No Youtube!\n")   
        
        embedcblol.set_thumbnail(url='https://cdn.discordapp.com/attachments/425141386266935296/431610785207418901/CBLOL_2017_Logo.png')
        await client.send_message(message.channel, embed=embedcblol)
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
        
        
        
     #Banco_de_dados
    
     if message.content.lower().startswith('?relist'):

       embedlist= discord.Embed(
        title='Lista de Registrados',
        color=COR,
        description='**001**: Jeferson Lopes\n'
                   '**002**: Anthony Almeida'
                   '\n'
                   '\n'
                   '-Digite ** `` ?cadastro `` ** para entrar nos registros do <@423738913878966283>')

       embedlist.set_thumbnail(url='https://cdn.discordapp.com/attachments/425141386266935296/435928628908523520/book_stack_pc_1600_clr_3258.png')
       await client.send_message(message.channel, embed=embedlist)

    
    
    
     if message.content.lower().startswith('?registro'):

        await client.send_message(message.channel, '```Digite seu numero de Registro.```')
        embed001 = discord.Embed(

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
            "**Jogo**: GTA 5| FORTNITE| LOL", )

        embed002 = discord.Embed(

            title="",
            color=COR,
            description="**Nome**: Anthony \n"
            "\n"
            "**Email**: _ \n"
            "\n"
            "**Nome Online**: Anthonyalmeida50\n"
            "\n"
            "**Plataforma**: PS3\n"
            "\n"
            "**Jogo**: GTA 5", )

        embed003 = discord.Embed(

            title="Registro Invalido!",
            color=COR,
            description="")
        embed004 = discord.Embed(

            title="Registro Invalido!",
            color=COR,
            description="")

        embed005 = discord.Embed(

            title="Registro Invalido!",
            color=COR,
            description="")

        embed006 = discord.Embed(

            title="Registro Invalido!",
            color=COR,
            description="")

        embed007 = discord.Embed(

            title="Registro Invalido!",
            color=COR,
            description="")

        embed008 = discord.Embed(

            title="Registro Invalido!",
            color=COR,
            description="")

        embed009 = discord.Embed(

            title="Registro Invalido!",
            color=COR,
            description="")
        embed010 = discord.Embed(

            title="Registro Invalido!",
            color=COR,
            description="")


        msg1 = await client.wait_for_message(author=message.author, content='001')
        embed001.set_thumbnail(url='https://cdn.discordapp.com/avatars/334359138110799872/e9500cf1d03931f465dab3bcdf9eb527.webp?size=1024')
        await client.send_message(message.channel, embed=embed001)
        msg2 = await client.wait_for_message(author=message.author, content='002')
        embed002.set_thumbnail(url='https://cdn.discordapp.com/avatars/335531697858674688/28f47a3ce62ae9b3be26914e07311437.webp?size=1024')
        await client.send_message(message.channel, embed=embed002)
        msg3 = await client.wait_for_message(author=message.author, content='003')
        await client.send_message(message.channel, embed=embed003)
        msg4 = await client.wait_for_message(author=message.author, content='004')
        await client.send_message(message.channel, embed=embed004)
        msg5 = await client.wait_for_message(author=message.author, content='005')
        await client.send_message(message.channel, embed=embed005)
        msg6 = await client.wait_for_message(author=message.author, content='006')
        await client.send_message(message.channel, embed=embed006)
        msg7 = await client.wait_for_message(author=message.author, content='007')
        await client.send_message(message.channel, embed=embed007)
        msg8 = await client.wait_for_message(author=message.author, content='008')
        await client.send_message(message.channel, embed=embed008)
        msg9 = await client.wait_for_message(author=message.author, content='009')
        await client.send_message(message.channel, embed=embed009)
        msg10 = await client.wait_for_message(author=message.author, content='010')
        await client.send_message(message.channel, embed=embed010)





     elif message.content.lower().startswith('?rv'):



       avisos= client.get_channel("392711722172940298")
       canalbots= client.get_channel("400703461068374017")
       msgvr= "-Digite ** `` ?perfil `` ** no canal {} para escolher seus cargos!".format(canalbots.mention)
       await client.send_message(avisos, message.content[3:])

       await client.send_message(message.author, msgvr)
       await client.delete_message(message)

                
        
     if message.content.lower().startswith('?cadastro'):
      link= 'https://discord.gg/RXNTwcW'

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
         evd = await client.send_message(message.channel, msgdados)
         await client.add_reaction(evd, ':sim:444562578639945728')



            
            
            
           
        #interação

     if message.content.lower().startswith('?convite'):
      convic = await client.send_message(message.channel,"https://discord.gg/RXNTwcW")
      await client.delete_message(message)
      await client.add_reaction(convic, '😀')

        
     if message.content.lower().startswith('?moeda'):
      choice = random.randint(1,2)
      if choice == 1:
         await client.add_reaction(message, '😀')
      if choice == 2:
         await client.add_reaction(message, '👑')

            
   

    #Sistema_de_cargos

     if message.content.lower().startswith("?perfil"):
        
        embed1 =discord.Embed(

           title="Defina seu Perfil!",
           color=COR,
           description="🔫 - GTA       \n"
                    "⚔ - LOL       \n"
                    "🛡 - FORTNITE  \n"
                    ,)
             
        botmsg = await client.send_message(message.channel, embed=embed1)
        
        await client.add_reaction(botmsg, "🔫")
        await client.add_reaction(botmsg, "⚔")
        await client.add_reaction(botmsg, "🛡")
        

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

    if reaction.emoji == "🍗" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Coxinha Peculiar 🍗", msg.server.roles)
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

    if reaction.emoji == "🍗" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Coxinha Peculiar 🍗", msg.server.roles)
     await client.remove_roles(user, role)
     print("add")



client.run('NDIzNzM4OTEzODc4OTY2Mjgz.DZw-vQ.C6c71fWztCIdQDvMTwxoI_Wvnb8')
