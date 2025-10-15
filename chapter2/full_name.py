first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

# before python3.5
print("{} {}".format(first_name, last_name))

message = f"Hello, {full_name.title()}!"
print(message)