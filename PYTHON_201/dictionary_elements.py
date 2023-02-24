sozluk={"reg":"regresyon modeli"
        ,"loj":"lojistik regresyon"
        ,"cart":"classification and reg"}

print(sozluk["reg"])

sozluk={"reg":{"RMS":10
        ,"MSE":20
        ,"SSE":30},
        
        "loj":{"RMS":10
        ,"MSE":20
        ,"SSE":30},

        "cart":{"RMS":10
        ,"MSE":20
        ,"SSE":30}}

print(sozluk["reg"]["SSE"])