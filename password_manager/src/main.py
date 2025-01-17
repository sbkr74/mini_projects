access = "Denied"
while True:
    mstr_pwd = input("Enter Master Password [0000] to Access Password Manager: ")

    if mstr_pwd.isdigit():
        if int(mstr_pwd) == 0000:
            access = "Accepted"
            break
        else:
            break
    else:
        try:
            mstr_pwd=int(mstr_pwd)
            continue
        except ValueError as e:
            print("ERROR: ",e)
            print("Accept only digits!!!\n")        

print(access)