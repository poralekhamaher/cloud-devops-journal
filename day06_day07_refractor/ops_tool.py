def main():
	name = input("Enter your name : ").strip().title()
	raw_number = input("Enter your number : ").strip()

	try:
		number = int(raw_number)
	except ValueError:
		print("invalid number input")
		return 1 

	results = []
	results.append(f"User: {name}")
	
	for i in range(1,number+1):
		if i%2==0:
			results.append(str(i))
	with open("output.txt" , "w", encoding="utf-8") as file:
		file.write("\n".join(results)+"\n")

	print("even numbers written to output.txt")
	return 0

if __name__=="__main__":
	raise SystemExit(main())
		
	
	


	

