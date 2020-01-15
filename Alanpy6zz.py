#
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
import os
iirange = (2, 3, 4, 5, 6, 7)
for ii in range(2, 13):
    if (ii % 3 == 0):
        print("triple: " + str(ii))
    else:
        print(ii)

pass


def Alanpy6zz():
    '''
    Print a bunch of stuff breaking
    down the __file__ magic value
    '''

    str1 = "Name {}.  File {}"
    str2 = str1.format(__name__, __file__)
    print("Name, File: " + str2)
    bn = os.path.basename(__file__)
    lenbn = len(bn)
    lenfile = len(__file__)
    p3 = (__file__)[0:lenfile-lenbn]
    p4 = (__file__)

    print(p3)
    if True:
        zz = p4+'10'
        print(zz)
    return str2


if __name__ == "__main__":
    # // comment
    Alanpy6zz()
    # // comment
