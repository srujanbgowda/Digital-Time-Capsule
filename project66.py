from datatime import datetime

message  = input("enter your message:")

unlock_date =  input("Enter unlock date (DD-MM-YYYY) : ")

try:
    unlock_date = datetime.strptime(unlock_date,"%d-%m-%Y")
except ValueError:    
    print("Invalid date format. Please use DD-MM-YYYY.")
    exit()

print("\n🔐 Your digital time capsule is ready!")    
print(f"Message: {message}") print(f"Unlock Date: {unlock_date.strftime('%d-%m-%Y')}")