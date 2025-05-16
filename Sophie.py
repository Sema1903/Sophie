import random
import telebot
f = open('/content/drive/MyDrive/Colab Notebooks/Sophy/text.txt', 'r').read().split()
words1 = {}
keys1 = []
for i in range(1, len(f)):
  if f[i - 1] not in keys1:
    keys1.append(f[i - 1])
    words1.update({f[i - 1]: {f[i]: 1}})
  else:
    here = False
    for j in words1[f[i - 1]]:
      if j == f[i]:
        words1[f[i - 1]][j] += 1
        here = True
    if not here:
      words1[f[i - 1]].update({f[i]: 1})
words2 = {}
keys2 = []
for i in range(2, len(f)):
  if f[i - 2] + ' ' + f[i - 1] not in keys2:
    keys2.append(f[i - 2] + ' ' + f[i - 1])
    words2.update({f[i - 2] + ' ' + f[i - 1]: {f[i]: 1}})
  else:
    here = False
    for j in words2[f[i - 2] + ' ' + f[i - 1]]:
      if j == f[i]:
        words2[f[i - 2] + ' ' + f[i - 1]][j] += 1
        here = True
    if not here:
      words2[f[i - 2] + ' ' + f[i - 1]].update({f[i]: 1})
words3 = {}
keys3 = []
for i in range(3, len(f)):
  if f[i - 3] + ' ' + f[i - 2] + ' ' + f[i - 1] not in keys3:
    keys3.append(f[i - 3] + ' ' + f[i - 2] + ' ' + f[i - 1])
    words3.update({f[i - 3] + ' ' + f[i - 2] + ' ' + f[i - 1]: {f[i]: 1}})
  else:
    here = False
    for j in words3[f[i - 3] + ' ' + f[i - 2] + ' ' + f[i - 1]]:
      if j == f[i]:
        words3[f[i - 3] + ' ' + f[i - 2] + ' ' + f[i - 1]][j] += 1
        here = True
    if not here:
      words3[f[i - 3] + ' ' + f[i - 2] + ' ' + f[i - 1]].update({f[i]: 1})
def answer(b, words):
  text = ''
  max = 0
  variasnts = []
  for i in words[b]:
    if words[b][i] > max:
      max = words[b][i]
      variants = [i]
    elif words[b][i] == max:
      variants.append(i)
  return variants[random.randint(0, len(variants) - 1)]
def transform(a):
  if len(a) == 1:
    if a[0] in keys1:
      return answer(a[0], words1)
    else:
      a[0] = keys1[random.randint(0, len(keys1))]
      return answer(a[0], words1)
  elif len(a) == 2:
    if (a[0] + ' ' + a[1]) in keys2:
      return answer(a[0] + ' ' + a[1], words2)
    else:
      return transform([a[1]])
  else:
    here = False
    for i in range(len(a) - 1, 1, -1):
      if a[i - 2] + ' ' + a[i - 1] + ' ' + a[i] in keys3:
        here = True
        return answer(a[i - 2] + ' ' + a[i - 1] + ' ' + a[i], words3)
    if not here:
      for i in range(len(a) - 1, 0, -1):
        if a[i - 1] + ' ' + a[i] in keys2:
          here = True
          return answer(a[i - 1] + ' ' + a[i], words2)
      if not here:
        for i in range(len(a) - 1, -1, -1):
          return transform([a[i]])
def give(a):
  a = a.split()
  text = '  '
  while text[-2] != '.':
    res = transform(a)
    text += res + ' '
    a.append(res)
  return text[2:len(text)].replace('.', '')
bot = telebot.TeleBot('7283857646:AAFMUEH97xAwbqAQoliG7KYUHiZITEdftpc')
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет✌️ Поговорим? Просто напиши мне")
@bot.message_handler(content_types = 'text')
def chats(message):
  bot.send_message(message.chat.id, give(message.text.lower()))
bot.polling(none_stop=True)