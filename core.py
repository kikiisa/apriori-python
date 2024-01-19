from apriori_python import apriori

itemSetList = [['eggs', 'bacon', 'soup'],
                ['eggs', 'banana', 'apple'],
                ['soup', 'banana', 'banana'],
                ['Mangga', 'Banana', 'Rol'],
                ['soup', 'Banana', 'apple'],
                ['soup', 'bacon', 'banana'],
                ]
freqItemSet, rules = apriori(itemSetList, minSup=0.5, minConf=0.5)
# print(freqItemSet)
for(k, v) in freqItemSet.items():
    print(k, v)