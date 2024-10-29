'''brain-cracker generator'''
def all_variants(text):

    for index in range(len(text)):
        for sec_index in range(len(text) - index): # в каждой итерации j будет терять  индекс с конца
            yield text[sec_index:sec_index + index + 1]


a = all_variants("abc")
for i in a:
    print(i)

#
# b = all_variants('doggy')
# for i in b:
#     print(i)
