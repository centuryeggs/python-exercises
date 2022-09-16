import random
import numpy

types = ['a','b','c','d']
nums = [2,3,4,5,6,7,8,9,10,11,12,13,14]
# 生成扑克牌
def create_cards ():
  cards = []
  for type in types:
    for num in nums:
      cards.append({
        'type': type,
        'num': num
      })
  return cards

# 发牌
def dealt_cards(cards, player_num):
  dealt_cards = random.sample(cards, player_num*3)
  return numpy.array_split(dealt_cards, player_num)

# 判断牌型 5:豹子 4:顺金 3:金花 2:顺子 1:对子 0:单张
def get_cards_type(combo):
  nums = [combo[0]['num'], combo[1]['num'], combo[2]['num']]
  if (combo[0]['num'] == combo[1]['num']  == combo[2]['num']):
    return 5
  elif (combo[0]['type'] == combo[1]['type'] == combo[2]['type']):
    if (min(nums) + 1 == numpy.median(nums) == max(nums) - 1):
      return 4
    else:
      return 3
  elif (min(nums) + 1 == numpy.median(nums) == max(nums) - 1):
    return 2
  elif (combo[0]['num'] == combo[1]['num'] or
    combo[0]['num'] == combo[2]['num'] or
    combo[1]['num'] == combo[2]['num']):
    return 1
  else:
    return 0
# 比较牌型大小 combo1 更大返回 True
def compare(combo1, combo2):
  comb1_type = get_cards_type(combo1)
  comb2_type = get_cards_type(combo2)
  if (comb1_type > comb2_type):
    return True
  elif (comb1_type < comb2_type):
    return False
  else:
    if (comb1_type == 5): #都是豹子
      if (combo1[0]['num'] > combo2[0]['num']):
        return True
      else:
        return False
    elif (comb1_type == 4): #都是顺金
      combo1_nums = [combo1[0]['num'],combo1[1]['num'],combo1[2]['num']]
      combo2_nums = [combo2[0]['num'],combo2[1]['num'],combo2[2]['num']]
      if (max(combo1_nums) > max(combo2_nums)):
        return True
      elif (max(combo1_nums) < max(combo2_nums)):
        return False
      else:
        if (combo1[0]['type'] > combo2[0]['type']):
          return True
        else:
          return False
    elif (comb1_type == 3): #都是金花
      return True
    # elif (comb1_type == 2): #都是顺子
    # elif (comb1_type == 1): #都是对子
    # elif (comb1_type == 0): #都是单张
      
def wrapper(dict):
  types = {'a': '♦️','b': '♣️', 'c':'♥️', 'd': '♠️' }
  nums = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
  return types[dict['type']] + nums[dict['num'] - 2]

# print(dealt_cards(create_cards(), 5))
# 从多组牌中，比较出最大的牌型，返回其索引
# def get_result(show_cards):
#   for 
# cards = create_cards()
# show_cards = dealt_cards(cards, 5)
# compare(show_cards)
# get_cards_type(['♦️2','♦️2','♦️2'])
# print(get_cards_type([{'type': 'a', 'num': 6},{'type': 'c', 'num': 7},{'type': 'd', 'num': 7}]))
# wrapper()
print(wrapper({'type': 'a', 'num': 14}))