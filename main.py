import subprocess

DASHED_LINE="\033[91m"+"--------------------"+"\033[0m"

print("Welcome to Fleet Risk Simulator! Please choose which risk scores you would like to know about, and what model you want to try out.")
print("As this is a test run, we will be using sample data sets to display the usage of the model, although you can put your own csv files in the appropriate directories instead")
print(DASHED_LINE)
print("1: Drivers")
print("2: Vehicles")
print("3: Routes")
print(DASHED_LINE)

choice=input()
if choice not in ["1", "2", "3"]:
    print("Invalid choice!")
elif choice=="1":
    subprocess.Popen("cd servers && python3 server_driver.py")
    subprocess.Popen("cd clients/client_driver && python3 client1.py")
    subprocess.Popen("cd clients/client_driver && python3 client2.py")
elif choice=="1":
    subprocess.Popen("cd servers && python3 server_vehicle.py")
    subprocess.Popen("cd clients/client_vehicle && python3 client1.py")
    subprocess.Popen("cd clients/client_vehicle && python3 client2.py")
elif choice=="1":
    subprocess.Popen("cd servers && python3 server_route.py")
    subprocess.Popen("cd clients/client_route && python3 client1.py")
    subprocess.Popen("cd clients/client_route && python3 client2.py")

print("Thanks for visiting!")
