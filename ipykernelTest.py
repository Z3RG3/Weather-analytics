import pandas as pd

print(1 + 2 + 3 + 4 + 5 + 6)


print(
    "Use shift + enter To run code in Jupyter interactive window, this way no need for ipynb"
)

data = {
    "Name": ["Jozsi", "Geri", "Hapci"],
    "Tucsok": ["cirip", "zrzZrr", "prprprr"],
    "Ret": ["Mezo", "Erdo", "Tisztas"],
}

df = pd.DataFrame(data)

df.head(2)
