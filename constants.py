import random

token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
prekol=['https://tenor.com/view/suspense-suspicious-evil-look-evillook-gif-20187691','https://tenor.com/view/dance-happy-cat-reaction-rainbow-gif-19368130','https://tenor.com/view/funny-silly-wtf-crazy-kitty-gif-12896137','https://tenor.com/view/discord-cat-cat-cat-bell-cat-rings-bell-cat-rings-bell-for-service-gif-22647044','https://tenor.com/view/gatto-cibo-cat-bread-hungry-cat-gif-15925702','https://tenor.com/view/cat-asleep-asleep-on-keyboard-keyboard-computer-gif-15396270']
otmazki = ['колобок повесился','рыба утонула','кощей застрелился','солнце загорело','Буратино утанул ','Чебурашка оглох','русалака села на шпогат','ёжик с автоматом','маятник заколебался']
random_message = lambda: random.choice(otmazki)
random_message2 = lambda: random.choice(prekol)