unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("verifying:"+current_user.title())
	confirmed_users.append(current_user)
print("111")
for confirmed_user in confirmed_users:
	print(confirmed_user)	
