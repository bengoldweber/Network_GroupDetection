""" User interfacing command and control functions for the network generator """
# network_generator as ng
# Start command prompt, ask user what step to run
import sys


def user_input():
	exit_flag = False
	while exit_flag == False:
		try:
			run_selection = int(input("\nWhat step would you like to run:\n"
			                          "1 - Load emails \n"
			                          "2 - Generate network graph\n"
			                          "3 - Exit program\n"
			                          ">>> "))
			if run_selection == 1:
				print("hello\n")
			elif run_selection == 2:
				print("also hello\n")
			elif run_selection == 3:
				print("ending program\n")
				exit_flag = True
			else:
				print("Outside of bounds. Please enter 1,2 or 3")
		except ValueError as ve:
			print(f'\nValue error encountered. Please enter 1,2 or 3')



def main():
	""" main funciton """
	user_input()
	sys.exit(0)


if __name__ == "__main__":
	main()
