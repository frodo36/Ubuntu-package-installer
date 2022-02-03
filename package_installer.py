from os import system, path

system
if not path.exists("/usr/local/bin/zap"):
    print("Zap is not installed, press any key to install...")
    system("sudo apt install curl")
    system("sudo apt install grep")
    system("sudo apt install jq")
    system("sudo apt install wget")
    system("curl https://raw.githubusercontent.com/srevinsaju/zap/main/install.sh | sudo bash -s")
def start():
    query= input("Please enter the name of the package you wish to install: ")
    print("\n1 -Automatically use all install methods 1 by 1 to install package")
    print("2 -Install package with apt")
    print("3 -Install package with snap")
    print("4 -Install package with flatpak")
    print("5 -Install package with zap(appimage)")
    user = input("\nYour choice(1-5): ")
    if user.lower() == "1":
        pass
    elif user.lower() == "2":
        print("\n")
        system(f"sudo apt search {query}")
        query = input("Enter package to install or 'I' to install a different package: ")
        if query == "i":
            start()
        print("\n")
        system(f"sudo apt install {query}")
    elif user.lower() == "3":
        print("\n")
        system(f"sudo snap search {query}")
        query = input("Enter package to install or 'I' to install a different package: ")
        if query == "i":
            start()
        print("\n")
        system(f"sudo snap install {query}")
    elif user.lower() == "4":
        print("\n")
        system(f"sudo flatpak search {query}")
    elif user.lower() == "5":
        print("\n")
        system(f"sudo zap search {query}")
        query = input("Enter package to install or 'I' to install a different package: ")
        if query == "i":
            start()
        print("\n")
        system(f"sudo zap install {query}")
    
    print("\n")
    system(f"sudo apt search {query}")
    package = input("\nEnter package to install or enter to skip: ")
    print("\n")
    system(f"sudo apt install {package}")
    user = input("\nPress any key to continue to next install method(snap) or press 'I' to install a different package: ")
    if user.lower() == "i":
        start()
    print("\n")
    system(f"sudo snap search {query}")
    package = input("\nEnter package to install or enter to skip: ")
    print("\n")
    system(f"sudo snap install {package}")
    user = input("\nPress any key to continue to next install method(flatpak) or press 'I' to install a different package: ")
    if user.lower() == "i":
        start()
    print("\n")
    system(f"sudo flatpak search {query}")
    package = input("\nEnter package to install or enter to skip: ")
    print("\n")
    system(f"sudo flatpak install {package}")
    user = input("\nPress any key to continue to next install method(zap(appimage)) or press 'I' to install a different package: ")
    if user.lower() == "i":
        start()
    print("\n")
    system(f"sudo zap search {query}")
    package = input("\nEnter package to install or enter to skip: ")
    print("\n")
    system(f"sudo zap install {package}")
    input("Press any key to install a different package or ctr + c to cancel: ")
    start()
start()
