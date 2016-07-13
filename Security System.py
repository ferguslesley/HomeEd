# Ferg's Personal Security System
def main():
    print("Name Verification Please.")
    name = input("> ")

    if name == "Fergus":
        print("Verification Accepted, Welcome, Fergus.")
    else:
        for t in range(0,10):
            print("INTRUDER ALERT. LEAVE NOW!!!")
        
main()
