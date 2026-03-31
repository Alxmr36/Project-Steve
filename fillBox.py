def fillBox():
    items = 60
    box = 0

    if items >= 60:
        print("Box is full")
        box += 1
        print("you now have", box, "box")
    else:
        print("Continue to fill the box")
        print("You now have", items, "items in the box")

print(fillBox())

def createPallet():
    boxes = 5
    pallet = 0

    if boxes >= 10:
        print("Pallet is full")
        pallet += 1
        print("you now have", pallet, "pallet")
    else:
        print("Continue to fill the pallet")
        print("You now have", boxes, "boxes on the pallet")

print (createPallet())        

