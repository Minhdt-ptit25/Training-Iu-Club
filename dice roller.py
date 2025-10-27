import random
#"\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518"
#● ┌ ─ ┐ │ └ ┘
'┌─────────┐'
'│         │'        
'│         │'  
'│         │'  
'└─────────┘'

dice_art ={
    1: ('┌─────────┐',
        '│         │',
        '│    ●    │',
        '│         │',
        '└─────────┘'),
    2: ('┌─────────┐',
        '│  ●      │',
        '│         │',
        '│      ●  │',
        '└─────────┘'),
    3: ('┌─────────┐',
        '│  ●      │',
        '│    ●    │',
        '│      ●  │',
        '└─────────┘'),
    4: ('┌─────────┐',
        '│  ●   ●  │',
        '│         │',
        '│  ●   ●  │',
        '└─────────┘'),
    5: ('┌─────────┐',
        '│  ●   ●  │',
        '│    ●    │',
        '│  ●   ●  │',
        '└─────────┘'),
    6: ('┌─────────┐',
        '│  ●   ●  │',
        '│  ●   ●  │',
        '│  ●   ●  │',
        '└─────────┘'),

}
dice = []
total = 0
num_of_dice = 3
Guess = input("TÀI HAY XỈU?: ")

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

#for die in range(num_of_dice):
 #   for line in dice_art.get(dice[die]):
  #      print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end = "")
    print()

for die in dice:
    total += die
print(f'KẾT QUẢ: {total}')
if 4<=total<=10:
    check = "XỈU"
    print("XỈU")
elif 11 <=total <= 17:
    check = "TÀI"
    print("TÀI")
if Guess == check:
    print("BẠN ĐÃ ĂN ĐƯỢC NHÀ CÁI :333")
else:
    print("SAO MÀ ĂN ĐƯỢC NHÀ CÁI HEHE =)))")