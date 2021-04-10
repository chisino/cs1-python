print("This program leads a person through the steps of fixing a bad WiFi connection")

print("\nReboot the computer and try to connect.")

ans = input("\nDid that fix the problem? ")

if (ans == "no"):
    print("\nReboot the router and try to connect.")
    ans = input("\nDid that fix the problem? ")
    if (ans == "no"):
        print("\nMake sure the cables between the router and modem are plugged in firmly.")
        ans = input("\nDid that fix the problem? ")
        if (ans == "no"):
            print("\nMove the router to a new location.")
            ans = input("\nDid that fix the problem? ")
            if (ans == "no"):
                print("\nGet a new router.")
