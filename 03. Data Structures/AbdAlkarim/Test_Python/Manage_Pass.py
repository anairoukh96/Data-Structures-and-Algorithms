# def EncPass():
#     passwordList = [['moreb','password123','scme.edu.ps'],['ahmad','password2','mail.google.com'],['mdm992002','password2','facebook.com']]
#     print (passwordList)
#     search = input ("Enter user name to show password... ")
#     for i in range(len(passwordList)):
#         if passwordList[i][0] == search:
#             for j in range(len(passwordList[i])):
#                 print ( passwordList[i][j])

# EncPass()

Manager_Pass = []


def Manager():
    number_User_Row = int(input("Please Enter the number username: "))
    number_User_Column = 1
    for row in range(0,number_User_Row):
        Manager_Pass.append([])
        for column in range(0,number_User_Column):
            Username = str(input("Please Enter the username: "))
            Manager_Pass[row].append(f"UserName: {Username}")
            Password = str(input("Please enter the Password: "))
            Manager_Pass[row].append(f"Password: {Password}")
            Site = str(input("Please enter Site_Name: "))
            Manager_Pass[row].append(f"Website: {Site}")
    print("*" * 50)
    print(Manager_Pass)
    def Search_Pass():
        print("*" * 50)
        enter_user = str(input("Please enter the username: "))
        if Username == enter_user:
            print(f"Password: {Password}")
        
    Search_Pass()

Manager()