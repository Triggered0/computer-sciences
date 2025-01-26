no = input("Phone Number: ")
if len(no) != 10:
    print("Wrong number")
else:
    no = [*no]
    no.insert(0, "(")
    no.insert(4, ")")
    no.insert(5, " ")
    no.insert(9, "-")
    print("".join(no))
