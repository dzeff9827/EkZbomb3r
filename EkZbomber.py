from tools import tools
from termcolor import colored

tools.clear()
tools.ICC()
tools.clear()
tools.check_files()
tools.CFU()

while True:
	tools.clear()
	tools.banner_tools()

	tool = input(colored("\nEkZbomb3r>> ", "red"))
	if tool == "1":
		numb, ct, pr = tools.start_input()
		if numb != 0:
			tools.start(numb, ct, proxy_=pr)
	elif tool == "0":
		tools.clear()
		break
	elif tool == "6":
		tools.banner_info()
	elif tool == "2":
		tools.faq_proxy()
	elif tool == "3":
		tools.quick_guide()
	elif tool == "4":
		tools.disclaimer()
	elif tool == "5":
		tools.donate()
	elif tool.lower() == "clear logs":
		tools.clear_logs()
	else:
		pass
