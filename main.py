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
async def on_member_join(member):
  canal = client.get_channel("393451272034058241")
  regras = client.get_channel("424026852097654794")
  bots = client.get_channel("392697933562118144")
  msg = "Bem Vindo {}\n leia as {}".format(member.mention, regras.mention)
  msg2 = "Olá {},Esse é o canal de Chat, Para liberar Outras salas digite ** ``?perfil`` ** em {}".format(member.mention, bots.mention) 
  await client.send_message(member, msg) #substitua canal por member para enviar a msg no DM do membro
  await client.send_message(canal, msg2)
@client.event
async def on_member_remove(member):
   canal = client.get_channel("423328604911304708")
   msg = "Adeus garotinho(a) juvenil {}".format(member.mention)
   await client.send_message(member, msg) #substitua canal por member para enviar a msg no DM do membro    
    
    
    
    
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

        
         embedinfo.add_field(name='jarvis',value='Pergunta algo ao Jarvis!', inline=False)
         embedinfo.add_field(name='?staff +mensagem',value='Envia uma mensagem a staff do F SOCIETY.', inline=False)
         embedinfo.add_field(name='?link',value='Pega o link para add o BOT no seu server', inline=False)
         embedinfo.add_field(name='?avatar',value='Mostra o seu avatar', inline=False)
         embedinfo.add_field(name='t?avatar *@user*',value='Mostra o avatar do user.', inline=False)
         embedinfo.add_field(name='?dance',value='Bota o jarvis para dançar.', inline=False)
         embedinfo.add_field(name='?enquete',value='Cria uma enquete', inline=False)
         embedinfo.add_field(name='?contato',value='Envia o contato do programador', inline=False)
         embedinfo.add_field(name='?rlol',value='Escolhe Entre:|Top|Jungle|Mid|Adc|Suporte|', inline=False)
         embedinfo.add_field(name='?cblol',value='Mostra o Link do Canal no Youtube da CBLOL',inline=False)
         embedinfo.add_field(name='?moeda',value='Joga uma moeda.',inline=False)
         embedinfo.add_field(name='?convite',value='Mostra o convite do F SOCIETY', inline=False)
         embedinfo.add_field(name='?perfil',value='Abre o menu para definir seus cargos', inline=False)
        
         
      
         embedinfo.set_footer(text="-Digite ok para receber a lista no privado.")
         await client.send_message(message.channel, embed=embedinfo)
         await client.add_reaction(message, '😄')
         msg1 = await client.wait_for_message(author=message.author, content='ok')
         await client.send_message(message.author, embed=embedinfo)
         
      
    
    
    
    
       
    
      #sistema_de_enquete


     if message.content.lower().startswith("?enquete"):
       menssagem2 = message.content[9:]
       embedeq= discord.Embed(
          title=menssagem2,
          color=COR,
          description="",
                 )
       embedeq.set_thumbnail(url='https://cdn.discordapp.com/avatars/423738913878966283/3eae6e8f5be338604dbf4a21ad96a34c.webp?size=1024')
       embedeq.set_footer(text='-Obrigado por responder!')
       msp55 = await client.send_message(message.channel, embed=embedeq)


       await client.delete_message(message)
       await client.add_reaction(msp55, ':sim:444562578639945728')
       await client.add_reaction(msp55, ':nao:444562647799562261')
   


     #lixo
    
     if message.channel == client.get_channel('392746066555961345'):
       canalhe = client.get_channel("492158366622285835")
       BV = '{}'.format(message.content[0:])
       await client.send_message(canalhe, BV)
       await asyncio.sleep(3)
       await client.delete_message(message)
    
    
    
    
     if message.content.lower().startswith('?dance'):
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/289891525918195712/428189193919922179/tenor.gif")
        await client.delete_message(message)

    
        
        
        
        
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
        
     if message.content.lower().startswith('?coxinha'):
        canal= client.get_channel("442860201503227904")
        await client.send_message(canal, message.content[7:])
        
        

        
        
        
        
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
       await client.add_reaction(message,'👊')
        
        
        
        
     #sistema_de_controle(mensagem)
        
     if message.content.lower().startswith('?diz'):
       if not message.author.id == '334359138110799872':
         return await client.send_message(message.channel, "```Você Não tem permissão!```")
       await client.send_message(message.channel, message.content[4:])
       await client.delete_message(message)

        
     if message.content.lower().startswith('?avisos'):
       avisos= client.get_channel("392711722172940298")
       if not message.author.id == '334359138110799872':
         return await client.send_message(message.channel, "```Você Não tem permissão!```")
       await client.send_message(avisos, message.content[8:])
       await client.delete_message(message)  
   

     if message.content.lower().startswith('jarvis'):
       staff = client.get_channel("425150435725279253")
       sos = '<@&463052822175285268> vocês foram solitados por {},em **{}**'.format(message.author.mention,message.server.name)
       javai = '{} Vou analisar sua duvida e lhe responder assim que possivel!'.format(message.author.mention)
       await client.send_message(staff, sos)
       
       await client.send_message(staff, message.content[7:])
       await client.send_message(message.channel, javai)
      
        
        
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
  
       


     elif message.content.lower().startswith('?staff'):
         canal= client.get_channel("425150435725279253")
         avisos= client.get_channel("392711722172940298")
         sos1 = '<@&425144881049239553> O usuário {} Mandou uma menssagem de **{}** para o **F SOCIETY**'.format(message.author.mention,message.server.name)
         CON = '```{}```'.format(message.content[7:])
         await client.delete_message(message)
         foi=await client.send_message(message.channel, "```Mensagem Enviada com Sucesso!```")
         await client.add_reaction(foi, ':sim:444562578639945728')
         await client.send_message(canal, sos1) 
         
         await client.send_message(canal, CON)
         
        


     if message.content.lower().startswith('?link'):
        link2 = 'https://discordapp.com/oauth2/authorize?client_id=423738913878966283&scope=bot&permissions=8'
        embedlinkbot = discord.Embed(
         title='Leve o Jarvis com Você!',
         color=COR,
         description= "\n"
            "[Clique aqui]("+ link2 +") Para Adicionar o BOT ao seu Server\n")   
        embedlinkbot.set_thumbnail(url='https://cdn.discordapp.com/avatars/423738913878966283/3eae6e8f5be338604dbf4a21ad96a34c.webp?size=1024')
        await client.send_message(message.channel, embed=embedlinkbot)
        await client.delete_message(message)
        

            
            
            
           
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
                    "⚔  - LOL       \n"
                    "🛡  - FORTNITE  \n" 
                    "🛠 - UNTURNED  \n"
                    ,)
             
        botmsg = await client.send_message(message.channel, embed=embed1)
        
        await client.add_reaction(botmsg, "🔫")
        await client.add_reaction(botmsg, "⚔")
        await client.add_reaction(botmsg, "🛡")
        await client.add_reaction(botmsg, "🛠")

        global msg_id
        msg_id = botmsg.id
        global msg_user
        msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🔫": 
     role = discord.utils.find(lambda r: r.name == "GTA", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚔":
     role = discord.utils.find(lambda r: r.name == "LOL", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🛡":
     role = discord.utils.find(lambda r: r.name == "FORTNITE", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🛠" :
     role = discord.utils.find(lambda r: r.name == "Unturned", msg.server.roles)
     await client.add_roles(user, role)
     print("add")





@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🔫":
     role = discord.utils.find(lambda r: r.name == "GTA", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚔":
     role = discord.utils.find(lambda r: r.name == "LOL", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🛡":
     role = discord.utils.find(lambda r: r.name == "FORTNITE", msg.server.roles)
     await client.remove_roles(user,role)

    if reaction.emoji == "🛠":
     role = discord.utils.find(lambda r: r.name == "Unturned", msg.server.roles)
     await client.remove_roles(user, role)
     print("add")



client.run('NDIzNzM4OTEzODc4OTY2Mjgz.DZw-vQ.C6c71fWztCIdQDvMTwxoI_Wvnb8')
