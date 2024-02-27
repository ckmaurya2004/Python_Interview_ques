

# try:
#     num = int(input("enter  a string "))
#     if num == 12:
#         print("match the string ")
#     else:
#         print("not match")

# except:
#     print("some exception occurred")


# def fun():
    
#     try:
#         num = int(input("enter a number "))
#         if num ==2:
#             print(f"correct input | {num}")
#         else:
#             print("invalid input | ")
#     except:
#         print("exception occurred ")
#     finally:
#         print(" I am execute all cases")

# fun()
    

class KiranName(Exception):
    pass
    # try:
    #     name = input(" Enter a name ")
    #     if name == "kiran":
    #         raise KiranName
    #     else:
    #         print(f"hello {name}")
    # except KiranName:
    #     print("Exception occurred ")





name = input(" Enter a name ")

if name == "kiran":
    raise KiranName(f"{name} blocked here ")
else:
    print(f"hello {name}")