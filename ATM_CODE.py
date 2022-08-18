print("       welcome to state bank of india swipe your card    ")
print("please do not remove your card:-")
amount=100000
card=input("enter your card")
if card=="debit":
       lang=input("enter your language")
       if lang=="english":
              pin=input("enter your pin")
              if len(pin)==4:
                    trans=input("enter your transtion")
                    if trans=="withdrowl":
                            withdrowl=int(input("enter the withdrowl amount"))
                            if withdrowl<amount:
                                 print("you can take a cash")
                    elif trans=="transfer_money":
                            transfer_money=int(input("enter the transfer money"))
                            if transfer_money<=amount:
                                   print("your money successfully transfed")
                            else:
                                   print("enter valid amount")
                    elif trans=="change_pin":
                            change_pin=input("enter change pin")
                            if len(change_pin)==4:
                                   print("succesfuly change your pin")
                            else:
                                   print("enter valid change pin")
                    elif trans=="deposit":
                            deposit=int(input("enter yoyr deposit amount"))
                            if deposit>1000:
                                   print("your money is succesfuly deposit")
                            else:
                                   print("please enter valid amount")
              else:
                     print("enter valid pin")
       else:
              print("enter valid language")
else:
       print("please enter valid card")
	
