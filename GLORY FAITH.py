#3-4 guest list
guest_list=['flora', 'bella', 'tians']
print(guest_list)
print(guest_list[0], 'you are invited to my dinner on january 12')
print(guest_list[1], 'you are invited to my dinner on january 12')
print(guest_list[2], 'you are invited to my dinner on january 12')

#3-5 chamging the guest list
guest_list.pop(1)
print(guest_list)
guest_list.insert(1, 'tina')
print(guest_list)
print(guest_list[0], 'you are invited to my dinner')
print(guest_list[1], 'you are invited to my dinner')
print(guest_list[2], 'you are invited to my dinner')

#3-6 more guests
print('dear guests we have found a bigger table so we shall be inviting more guests')
guest_list.insert(0, 'leah')
guest_list.insert(1, 'beatrice')
guest_list.append('bertha')
print(guest_list)
print(guest_list[0], 'you are invited to my dinner')
print(guest_list[1], 'you are invited to my dinner')
print(guest_list[2], 'you are invited to my dinner')
print(guest_list[3], 'you are invited to my dinner')
print(guest_list[4], 'you are invited to my dinner')
print(guest_list[5], 'you are invited to my dinner')

#3-8 seeing the world
travel=['bora bora', 'cote dívoire', 'australia', 'belguim', 'canada']
print(travel)
travel.sort()

print (travel)
travel.sort(reverse=True)
print(travel)

travel.reverse()
print(travel)

travel.sort()
print(travel)

travel.sort(reverse=True)
print(travel)
