toc = {
    "name": "Aditya Tummala",
    "age": 30,
    "is_verified": True
}

print(toc["name"])

phone_number = input("Enter phone number: ")
num_2_alp = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
phone_output = ""
for ch in phone_number:
    print(num_2_alp.get(ch,"!"))
    phone_output += num_2_alp.get(ch, "!") + " "
print("\n" + phone_output)


random_message = input(">")
random_msg_output = random_message.split(' ')
print(random_msg_output)