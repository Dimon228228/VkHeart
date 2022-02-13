import vk_api
import time
from threading import Thread
from Heart import *


def captcha_handler(captcha):

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


access_token = "df21f6d20dfeb77dd17f630232eec56e629b1b00f9a6d3640191e6417758b2fa2642c90651d40fa1a0017"
session = vk_api.VkApi(token = access_token, captcha_handler=captcha_handler)
vk = session.get_api()


def editing(message_id,message,people):
  edit = vk.messages.edit(peer_id=people, message=message1, random_id=0,message_id=message_id)
  time.sleep(0.5)
  edit = vk.messages.edit(peer_id=people, message=message2, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message3, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message4, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message5, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message6, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message7, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message8, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message9, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message10, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message11, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message12, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message13, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message14, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message15, random_id=0,message_id=message_id)
  time.sleep(0.4)
  #edit = vk.messages.edit(peer_id=people, message=message16, random_id=0,message_id=message_id)
  #time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message17, random_id=0,message_id=message_id)
  time.sleep(0.4)
  edit = vk.messages.edit(peer_id=people, message=message18, random_id=0,message_id=message_id)
  time.sleep(2)
  edit = vk.messages.edit(peer_id=people, message='Сreated by @FROTZY ❤', random_id=0,message_id=message_id)

x=1

while x==1:
  #---------------------------------------Get_People_Id----------------------------------------------------
  people_id = vk.messages.getConversations(count='1', out='1', filter ='all', offset = "0")
  people_id1 = people_id['items']
  people_id2 = people_id1[0]
  people_id3 = people_id2['conversation']
  people_id4 = people_id3['peer']
  people = int(people_id4['id'])
  #---------------------------------------------------------------------------------------------------------

  #---------------------------------------Get_Message_Id----------------------------------------------------
  id = vk.messages.getConversations(count='1', out='1', filter ='all', offset = "0")
  id1 = id['items']
  id2 = id1[0]
  id3 = id2['conversation']
  message_id = int(id3['last_message_id'])
  #---------------------------------------------------------------------------------------------------------

  #---------------------------------------Get_Message_Text--------------------------------------------------
  message_text = vk.messages.getConversations(count='1', out='1', filter ='all', offset = "0")
  message_text1 = message_text['items']
  message_text2 = message_text1[0]
  message_text3 = message_text2['last_message']
  message = message_text3['text']
  #---------------------------------------------------------------------------------------------------------
  if message == '❤':
    editing(message_id,message,people)
    x=0 
  else:
    x=1



























#all_friends = []

#def get_friends():
  #friends = session.method("friends.get" , {"user_id":481326048})

  #for friend in friends["items"]:
      #users = session.method("users.get" , {"user_id":friend})
      #all_friends.append(f'{users[0]["first_name"]} {users[0]["last_name"]}\n')
      #print(users)
    
  #for i in range(10):
    #thread = Thread(target=count, args=())
    #thread.start()

#get_friends()

#print("".join(all_friends))

#585206895