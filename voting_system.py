candidate1 = input(" Enter 1st condidate name ! " )
candidate2 = input(" Enter 2nd condidate name ! " )
candi1_count = 0
candi2_count = 0
voter_id = [101,102,103,104 ,105,106]
no_of_voters = len(voter_id)
print("number of voters :",no_of_voters)
voted = []
while True:
    if voter_id == []:
        print("voting is over ")
        if candi1_count>candi2_count:
            print(f"{candidate1} won the election with {candi1_count}")
        elif candi2_count>candi1_count:
            print(f"{candidate2} won the election with {candi2_count}")
        else:
            print(" tied !!!!")
        break
    else:
        
        voter = int(input(" enter your id ! " ))
        if voter in voted:
            print(" you alredy voted ")
        else:
            if voter in voter_id:
                print(f"1.{candidate1}\n 2.{candidate2}")
                ch= int(input("enter your choice "))
                if ch == 1:
                    candi1_count +=1
                    print(f"you voted {candidate1}")
                elif ch == 2:
                    candi2_count += 1
                    print(f"you voted {candidate2}")
                voter_id.remove(voter)
                voted.append(voter)
            else:
                print(" you are not allow to vote ")
    





