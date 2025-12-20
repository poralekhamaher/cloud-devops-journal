
def main():
	name=input("enter your name : ").strip().title()
	raw_number= input("enter your number: ").strip()

	try:
		number= int(raw_number)
	except:
		print("enter a valid number")
	

	results=[]
	results.append(f"User: {name}")
	

	for i in range (1, number+1):
		if i%2==0:
			results.append(str(i))

	


	with open("output.txt","w",encoding="utf-8") as file:
		file.write("\n".join(results)+"\n")


	print("Even numbers written to output.txt")



if __name__=="__main__":
	main()


