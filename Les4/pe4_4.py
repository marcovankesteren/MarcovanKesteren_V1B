def new_password(oldpassword, newpassword):
    return newpassword != oldpassword and len(newpassword) >= 6 and len([figure for figure in newpassword if figure.isnumeric()]) > 0

print(new_password("bloemen", "winkel"))

print(new_password("bloemen", "Bloem1st"))