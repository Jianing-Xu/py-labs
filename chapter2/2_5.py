# “找一句你钦佩的名人说的名言，将其姓名和名言打印出来。输出应类似于下面这样（包括引号）。
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

# “用变量famous_person表示名人的姓名，再创建要显示的消息并将其赋给变量message，然后打印这条消息。”
name = "Albert Einstein"
dictum = "A person who never made a mistake never tried anything new."
print(f"{name} once said, \"{dictum}\"")

# “剔除人名中的空白 用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"和"\n"各一次。”
name = " Albert Einstein  "
print(f"\t{name}\n")
print(f"{name}")
print(f"{name}\t")
print(f"{name}\n")
print(f"{name}\t\n")