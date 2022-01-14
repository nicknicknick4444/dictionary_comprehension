""""Build a dictionary from two lists using dictionary comprehension, with a little help from a zipped list!"""

def make_lists():
    list1=[i for i in range(1,5)]
    list2=["a","b","c","d"]
    print("Two lists...")
    print(list1)
    print(list2)
    return list1,list2

def zipup(list1,list2):
    return list(zip(list1,list2))

def comprehend_this(zippy):
    return {a:b for a,b in zippy}

def in_reverse(zippy):
    return {b:a for a,b in zippy}

def main():
    list1,list2=make_lists()
    zippy=zipup(list1,list2)
    comp_dict=comprehend_this(zippy)
    switch_up=in_reverse(zippy)
     
    print("\n...become one dict: ")
    print(comp_dict)
    print("\nLet's switch it up now: ")
    print(switch_up)
    print("\nNow THAT'S what I call dictionary comprehension!")

if __name__ == "__main__":
    main()
