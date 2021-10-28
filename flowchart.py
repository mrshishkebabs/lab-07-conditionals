move = input("Does it move? [y/n] ")
if move == "y":
    should = input ("Should it? [y/n] ")
    if should == "y":
        print("No problem.")
    elif should == "n":
        print("DUCT TAPE TIME!")
    else:
        print("Answer my question! You didn't type y or n.")       
elif move == "n":
    should = input("Should it? [y/n] ")
    if should == "n":
        print("No problem.")
    elif should == "y":
        print("WD-40 TIME!")
    else:
        print("Answer my question! You didn't type y or n.")
else:
    print("Answer my question! You didn't type y or n.")