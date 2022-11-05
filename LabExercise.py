#Gela Maricon B. Seño
#BSCOE 2-2

def main():
	print("")
	array = [0, 3, 5, 9, 10, 11, 17, 21, 26, 30]
	print("Array:", array)
	print("")
	print("************* MENU *************")
	print("(1) Add an element")
	print("(2) Insert an element")
	print("(3) Modify an element")
	print("(4) Delete an element")
	print("(5) Arrange in ascending order")
	print("(6) Arrange in descending order")
	print("(7) Find the index of an element")
	print("(8) Count an element")
	print("(9) Length of an array")
	print("(10) Reverse an array ")
	print("(11) Sum of an array")
	print("(12) Find the maximum")
	print("(13) Find the minimum")
	print("(14) Exit")
	print("********************************")
	print("")
	
	menu_option = int(input("What do you want to do? (1-14): "))
	print("")
	
	if menu_option == 1:
		add_element = int(input("Enter the number you want to add: "))
		array.append(add_element)
		print("The element", add_element, "has been added.")
		print("This is the new array: Array:", array)
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
			TryAgain()
			
	elif menu_option == 2:
		insert_element = int(input("Enter the number you want to insert: "))
		insert_index = int(input("Enter the index where you want to insert: "))
		array.insert(insert_index, insert_element)
		print("The element", insert_element, "has been inserted.")
		print("This is the new array: Array:", array)
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
		TryAgain()
			
	elif menu_option == 3:
			old_element = int(input("Enter the number you want to replace/modify: "))
			new_element = int(input("Enter the new number: "))
			index_old = array.index(old_element)
			array.remove(old_element)
			array.insert(index_old, new_element)
			print("The element", old_element, "has been replaced by", new_element, ".")
			print("This is the new array: Array:", array)
			print("")
			def TryAgain():
				try_again = str(input("Do you want to try again? (Y/N): ")).upper()
				if try_again == "Y":
					main()
				elif try_again == "N":
					exit()
				else:
					print("Invalid input! Enter (Y/N) only.")
					TryAgain()
			TryAgain()
			
	elif menu_option == 4:
			delete_element = int(input("Enter the number you want to delete: "))
			array.remove(delete_element)
			print("The element", delete_element, "has been deleted.")
			print("This is the new array: Array:", array)
			print("")
			def TryAgain():
				try_again = str(input("Do you want to try again? (Y/N): ")).upper()
				if try_again == "Y":
					main()
				elif try_again == "N":
					exit()
				else:
					print("Invalid input! Enter (Y/N) only.")
					TryAgain()
			TryAgain()
			
	elif menu_option == 5:
			array.sort()
			print("The array has been arranged in ascending order.")
			print("This is the new array: Array:", array)
			print("")
			def TryAgain():
				try_again = str(input("Do you want to try again? (Y/N): ")).upper()
				if try_again == "Y":
					main()
				elif try_again == "N":
					exit()
				else:
					print("Invalid input! Enter (Y/N) only.")
					TryAgain()
			TryAgain()
			
	elif menu_option == 6:
		array.sort()
		array.reverse()
		print("The array has been arranged in descending order.")
		print("This is the new array: Array:", array)
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
		TryAgain()
		
	elif menu_option == 7:
		index_element = int(input("Enter the number you want to find: "))
		idx = array.index(index_element)
		print("The index of", index_element, "is", idx, ".")
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
		TryAgain()
		
	elif menu_option == 8:
		count_element = int(input("Enter the number you want to count: "))
		counter = array.count(count_element)
		print("The count/number of occurrence of", count_element, "in the array is", counter, ".")
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
		TryAgain()
		
	elif menu_option == 9:
		length_element = len(array)
		print("The array has", length_element, "elements.")	
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
		TryAgain()
		
	elif menu_option == 10:
		array.reverse()
		print("The array has been reversed.")
		print("This is the new array: Array:", array)
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
		TryAgain()
		
	elif menu_option == 11:
		total = sum(array)
		print("The sum of the array is", total, ".")
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
		TryAgain()
		
	elif menu_option == 12:
		largest = max(array)
		print("The maximum number is", largest, ".")
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
		TryAgain()
		
	elif menu_option == 13:
		smallest = min(array)
		print("The minimum number is", smallest, ".")	
		print("")
		def TryAgain():
			try_again = str(input("Do you want to try again? (Y/N): ")).upper()
			if try_again == "Y":
				main()
			elif try_again == "N":
				exit()
			else:
				print("Invalid input! Enter (Y/N) only.")
				TryAgain()
		TryAgain()
			
	elif menu_option == 14:
		exit()
	else:
		print("Invalid input! Insert only (1-14).")
		main()
main()		