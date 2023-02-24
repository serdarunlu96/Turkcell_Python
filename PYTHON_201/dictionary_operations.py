sozluk={"reg":"regresyon modeli"
        ,"loj":"lojistik regresyon"
        ,"cart":"classification and reg"}

sozluk["gbm"]="gradient boosting mac"
print(sozluk)

sozluk["reg"]="coklu dogrusal regresyon"
print(sozluk)

sozluk[1]="yapay sinir agları"
print(sozluk)

t=("tuple",) # add tuple into dictionary
sozluk[t]="yeni bir sey"
print(sozluk)