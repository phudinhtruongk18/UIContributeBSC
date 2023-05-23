import re

def get_num_of_holder(txt):
    pattern = re.compile(r"(.*) addr")

    timeitem = re.findall(pattern, txt)    

    if timeitem.__len__() < 1:
        return "--ERROR--"

    time_str = timeitem[0]
    return time_str


if __name__ == "__main__":
    # write a test case for this function
    test_case_1 = "1 address"
    test_case_2 = "1 addresses"
    test_case_3 = "1 addresss"
    test_case_4 = "1 addressss"
    test_case_5 = "71,358 addresses"
    list_test_case = [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5]
    for temp in list_test_case:
        print(get_num_of_holder(temp))
