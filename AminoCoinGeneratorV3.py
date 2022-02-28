from json import load
from tabulate import tabulate
from utils import aminoboi, menu_configs

accounts = [ ]
with open("accounts.json") as data:
	accounts_list = load(data)
	for account in accounts_list:
		accounts.append(account)

def authorize(email: str, password: str, client: aminoboi.Client):
	try:
		print(f"-- deviceID::: {client.device_Id}")
		client.auth(email=email, password=password)
		print(f"-- Logged in::: {email}...")
	except Exception as e:
		print(f"-- Error in auth::: {e}")
	
def play_lottery(ndc_id: int, client: aminoboi.Client):
	try:
		client.join_community(ndc_id=ndc_id)
		lottery = client.lottery(ndc_id=ndc_id)
		print(f"-- Lottery::: {lottery['api:message']}")
	except Exception as e:
		print(f"-- Error in play lottery::: {e}")
		
def watch_ad(client: aminoboi.Client):
	try:
		watch_ad = client.watch_ad()
		print(f"-- Watch Ad::: {watch_ad['api:message']}")
	except Exception as e:
		print(f"-- Error in watch ad::: {e}")
		
		# -- transfer coins and main function for generating coins -- 
		
def transfer_coins():
    link_info = aminoboi.Client().get_from_link(input("-- Blog link::: "))["linkInfoV2"]["extensions"]["linkInfo"]
    ndc_id, blog_id = link_info["ndcId"], link_info["objectId"]
    for account in accounts:
    	try:
    		client = aminoboi.Client()
    		email, password = account["email"], account["password"]
    		authorize(email=email, password=password, client=client)
    		client.join_community(ndc_id=ndc_id)
    		total_coins = client.get_wallet_info()["wallet"]["totalCoins"]
    		print(f"-- {email} have::: {total_coins} coins...")
    		if total_coins != 0:
    			transfer = client.send_coins_blog(ndc_id=ndc_id, blog_Id=blog_id, coins=total_coins)
    			print(f">> {email} transfered {total_coins} coins - {transfer['api:message']}...")
    	except Exception as e:
    		print(f"-- Error in transfer coins::: {e}")

def main_process():
    link_info = aminoboi.Client().get_from_link(input("-- Community link::: "))["linkInfoV2"]["extensions"]["community"]
    ndc_id = link_info["ndcId"]
    for account in accounts:
    	try:
    		client = aminoboi.Client()
    		email, password = account["email"], account["password"]
    		authorize(email=email, password=password, client=client)
    		play_lottery(ndc_id=ndc_id, client=client)
    		watch_ad(client=client)
    	except Exception as e:
    		print(f">> Error in main process - {e}")

           
		# -- transfer coins and main function for generating coins --      

def main():
	print("""\u001b[32m
Script by deluvsushi
Github : https://github.com/deluvsushi
╔═══╗╔═╗╔═╗╔══╗╔═╗─╔╗╔═══╗╔═══╗╔═══╗╔══╗╔═╗─╔╗     
║╔═╗║║║╚╝║║╚╣─╝║║╚╗║║║╔═╗║║╔═╗║║╔═╗║╚╣─╝║║╚╗║║     
║║─║║║╔╗╔╗║─║║─║╔╗╚╝║║║─║║║║─╚╝║║─║║─║║─║╔╗╚╝║     
║╚═╝║║║║║║║─║║─║║╚╗║║║║─║║║║─╔╗║║─║║─║║─║║╚╗║║     
║╔═╗║║║║║║║╔╣─╗║║─║║║║╚═╝║║╚═╝║║╚═╝║╔╣─╗║║─║║║     
╚╝─╚╝╚╝╚╝╚╝╚══╝╚╝─╚═╝╚═══╝╚═══╝╚═══╝╚══╝╚╝─╚═╝     
╔═══╗╔═══╗╔═╗─╔╗╔═══╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗╔╗──╔╗╔═══╗
║╔═╗║║╔══╝║║╚╗║║║╔══╝║╔═╗║║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║║╚╗╔╝║║╔═╗║
║║─╚╝║╚══╗║╔╗╚╝║║╚══╗║╚═╝║║║─║║╚╝║║╚╝║║─║║║╚═╝║╚╗║║╔╝╚╝╔╝║
║║╔═╗║╔══╝║║╚╗║║║╔══╝║╔╗╔╝║╚═╝║──║║──║║─║║║╔╗╔╝─║╚╝║─╔╗╚╗║
║╚╩═║║╚══╗║║─║║║║╚══╗║║║╚╗║╔═╗║──║║──║╚═╝║║║║╚╗─╚╗╔╝─║╚═╝║
╚═══╝╚═══╝╚╝─╚═╝╚═══╝╚╝╚═╝╚╝─╚╝──╚╝──╚═══╝╚╝╚═╝──╚╝──╚═══╝
""")
	print(tabulate(menu_configs.main_menu, tablefmt="fancy_grid"))
	select = int(input("-- Select::: "))
	
	if select == 1:
		main_process()
	
	elif select == 2:
		transfer_coins()

main()
