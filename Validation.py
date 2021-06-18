def checkValidefields(Phone):
    validPhone = 0
    Error_Occured =0
    if Phone.isnumeric() and len(Phone)==10:
        validPhone += 1
        print(f"Number of valid phone {validPhone}")
        pass
    else:
        validPhone = 0
        Error_Occured +=1
        print(f"Invalide Phone Number{Error_Occured} , :{Phone} ")

def Check_message_content(Message):
        valid_msg = 0
        invalid_msg = 0
        if len(Message) > 1 and len(Message)<160:
            valid_msg +=1
            print("valid message sent  ")
        else:
            valid_msg = 0
            invalid_msg +=1
            print(f"Invalide message whose lenth equal 1 - 160 :  {invalid_msg}")