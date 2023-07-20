devs_money = 100
dev_can_play_smash = False
if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament!")

elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")

mark = float(input("Enter what marks you recived "))

if mark >85:
    print("Distinction")
elif 65<= mark <=85:
    print("pass")
else:
    print ("fail")
if mark >85:
    print("Distinction")
    if 65<= mark <=85:
        print("pass")
else:1
    print ("fail")
