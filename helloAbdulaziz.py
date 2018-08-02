name = input("You'r name : ")
admins = ["ABDULAZIZ", "AZIZ"]
cicleNum = len(admins) - 1 
while cicleNum != -1 :
	result = ("Hi asshole")
	access = ("What is your problem asshole? : ")
	if name.upper() == admins[cicleNum]:
		result = ("Hello my Boss!")
		access = ("What is your problem my boss? : ")
		cicleNum = 0 
	cicleNum -= 1
print(result)
input(access)
if access.upper() != "":
	print("I'll solve that!")
