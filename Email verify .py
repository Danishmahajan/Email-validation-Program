class Error(Exception):
    pass
class MissingSymbolError(Error):
    pass
class MissingDomainError(Error):
    pass
class AddressError(Error):
    pass
class NameBeforeDomain(Error):
    pass
class NameBeforeAtTheRate(Error):
    pass
print("\n          The Email Validation Program \n")
while True:
    #TRY BLOCK
    try:
        mail =input("\n Please , Enter Your mail  Address:" )
        email=mail.lower()
        list_domain=["com","org","co.in","ac.in","net"]
        userdomain = email.split(".",1)[-1] # Split for Domain
        split_name=email.split("@")   #Split for the Address
        count=0
        for i in email:
            if i == "@":
                count=count+1
                split_name2= split_name[1].split(".")  # split  for .
        #Checking The @ And The Domain
        if "@" not in email:
            raise MissingSymbolError
       
        # Chking for Double @
        elif count>1:
            raise AddressError

        elif userdomain not in list_domain:
            raise MissingDomainError
        
        #checking The Mail before @
        elif not split_name[0].isalnum():
            raise NameBeforeAtTheRate
        #checking The Mail before. 
        elif not split_name2[0].isalnum():
            raise NameBeforeDomain 
        else:
            print("\n  Your mail is valid  i.e ", email,"\n")
            break

    # EXCEPT BLOCK
    except MissingSymbolError:
        print("\n Enter Your Mail Again Containing @ ...... ")
    except MissingDomainError:
        print("\n Enter Your Mail Again Containing Domain ......  ")
    except AddressError:
        print("\n Enter Your Mail with valid Address  ......  ")
    except NameBeforeAtTheRate:
        print("\n Enter Your Mail with valid Address Before @  ......  ")
    except NameBeforeDomain:
        print("\n Enter Your Mail with valid Address Before Dot  ......  ")
