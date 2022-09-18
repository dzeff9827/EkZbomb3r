from tools import tools
from tools import proxy
from termcolor import colored
import requests

tools.clear()
tools.ICC()
tools.clear()

while True:
	tools.clear()
	tools.banner_tools()

	tool = input(colored("\nEkZoRtSiSt BOMBER ##>> ", "red"))
	if tool == "1":
		numb, ct, pr = tools.start_input()
		if numb != 0:
			tools.start(numb, ct, proxy_=pr)
	elif tool == "0":
		tools.clear()
		break
	elif tool == "99":
		tools.banner_info()
	elif tool == "2":
		tools.ip()
	elif tool == "3":
		tools.dos()
	elif tool == "4":
		tools.faq_proxy()
	elif tool == "5":
		tools.quick_guide()
	elif tool == "6":
		tools.disclaimer()
	elif tool.lower() == "clear logs":
		tools.clear_logs()
	else:
		pass
