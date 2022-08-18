go=input("enter link of google account")
if go=="account.google.com":
    print("crate a google account")
    name=input("please enter your first name")
    if name>="A" or name<="Z" and name>="a"or name<="z" :
        print(name)
        name2=input("please enter your last name")
        if name2>="A" or name2<="Z" and name2>="a" or name2<="z":
            print(name2)
            psd=input("create your password")
            if psd>="A" or psd<="Z"and psd>="a" or psd<="z" or psd>=1 or psd<=9 and psd=="#" or psd=="@":
                print("create psd",psd)
                num=int(input("enter the number"))
                if num>=1 or num<=10:
                    print(num)
                    year=input("enter the year")
                    month=input("enter the month")
                    day=input("enter the day")
                    if year>="1980" or year<="2022" or month>="1" or month<="12" or day>="1" or day<="31":
                        print("birthdate",year+"/"+month+"/"+day)
                        gender=input("enter the gender")
                        if gender=="male" and gender=="female":
                            print("gender")
                            email=input("enter your email")
                            if email<="a" or email<="z" or email>="1" or email<="9" or email=="@":
                                print("email")
                                print("gmail successfully")
                            else:
                                print("wrong gmail ")
                        else:
                            print("incorrect gender")
                    else:
                        print("incorrect birthdate")
                else:
                    print("incorrect number")
            else:
                print("incorrect password")
        else:
            print("incorrect last name")
    else:
        print("incorrect first name")
else:
    print("wrong gmail account")