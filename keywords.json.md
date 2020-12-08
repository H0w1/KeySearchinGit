A description for keywords.json
## 
[{The direct keywords}, {The cross keywords}, {target keywords}]


```
[ 
    {// The direct keywords
        // CCs and opti
        "gcc","clang","compiler","optimiz","CCs","CCs+Op",
        // high level security
        "security": "[Ss]ecurity|[Dd]anger", "attack": "[Aa]ttack",       
        // certain threats       
        "ub", "side-channel", "race": "[Rr]ace condition", "struct-padding",
        "cfi", "info-leak", "UAF", "access-control",
        // compiler do something
        "reorder": "[Rr]eorder",
            // the numbers of cross cases of these keywords are still too large: (assum, break, introduc) X ccs+op : (852, 687, 2030) in 5.7-rc5
        "compiler.*assum", "(cc+opti ).* break", "(cc+opti ).*introduc"
    },

    {// The cross keywords
        "compilerXoptimiz": ["compiler", "optimiz"],
        "securityX(CCs+op)": ["security","CCs+Op"],
        "attackX(CCs+op)": ["attack","CCs+Op"],
        "raceX(CCs+op)": ["race","CCs+Op"],
        "cfiX(CCs+op)": ["cfi","CCs+Op"],
        "info-leakX(CCs+op)": ["info-leak","CCs+Op"],
        "access-controlX(CCs+op)": ["access-control","CCs+Op"],
        "UAFX(CCs+op)": ["UAF", "CCs+Op"],
        "reorderX(CCs+op)": ["[Rr]eorder","CCs+Op"]
    },
    {// target keywords
        "targetKeys": ["compilerXoptimiz", "securityX(CCs+op)", "attackX(CCs+op)", "raceX(CCs+op)", "cfiX(CCs+op)",
            "info-leakX(CCs+op)", "access-controlX(CCs+op)", "UAFX(CCs+op)"," reorderX(CCs+op)", 
            "compiler.*assum", "(cc+opti ).* break", "(cc+opti ).*introduc",
            "ub", "side-channel", "struct-padding"
        ]
    }

]
```