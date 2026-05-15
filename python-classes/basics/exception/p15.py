class InvalidVoter(Exception):
    pass
try: 
    age = int(input("Enter age : "))
    if(age < 18):
      raise InvalidVoter("Not eligible for voting...")
    else:
      print("You can vote....")

except InvalidVoter as e:
    print(f"Invalid Voter Exception : {e}")

except Exception as e:
   print(e)        
   