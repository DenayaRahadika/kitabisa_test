"""
Sort and combine these 2 lists and print the result
Input 1: 4,3,6,5,1,2
Input 2: F,C,D,B,A
Output : [1:A],[2:B],[3:C],[4:D],[5:F],[6:NULL]
Edited Output: (due to wrong output shape): [1,"A"],[2, "B"],[3, "C"],[4, "D"],[5, "F"],[6, "NULL"]
"""


class SortCombine(object):
    def sort_combine(self, list1, list2):
        list1 = sorted(list1)
        list2 = sorted(list2)

        n1 = len(list1)
        n2 = len(list2)
        output = []
        i = 0
        while n1 > 0 or n2 > 0:
            if n1 <= 0:
                output.append(["NULL", list2[i]])
            elif n2 <= 0:
                output.append([list1[i], "NULL"])
            else:
                output.append([list1[i], list2[i]])
            i += 1
            n1 -= 1
            n2 -= 1
        return output


if __name__ == "__main__":
    sc = SortCombine()
    list1 = []
    list2 = []

    output = sc.sort_combine(list1, list2)
    print(output)
