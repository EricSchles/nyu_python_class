forloop_list = []
for i in range(10):
    forloop_list.append(i)

# equivalent to

comprehension_list = [i for i in range(10)]

slightly_complex_forloop = []
for i in range(10):
    if i % 2 != 0:
        slightly_complex_forloop.append(i)

# equivalent to

slightly_complex_comprehension = [i for i in range(10) if i % 2 !=0]

complex_forloop = []
for i in range(100):
    if i % 2 == 0:
        if i in [2,4,6,8]:
            complex_forloop.append(i)
        else:
            complex_forloop.append(i+1)


to_process = ["thing","stuff","vals"] 
multi_index = []
for index,value in enumerate(to_process):
    multi_index.append((index,value))

# equvalent to

multi_index_comp = [(i,v) for i,v in enumerate(to_process)]
