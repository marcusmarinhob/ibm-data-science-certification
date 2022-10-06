import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

print('matplotlib version: ', mpl.__version__)

india_china = {'year':[1980, 1981, 1982, 1983, 1984], 'India':[8080, 8670, 8147, 7338, 5704], 'China':[5123, 6682, 3308, 1863, 1527]}
india_china_df = pd.DataFrame(data=india_china)

# print(india_china_df)

ax = plt.gca()
india_china_df.plot(kind="line", x='year', y='India', ax=ax)
india_china_df.plot(kind="line", x='year', y='China', ax=ax)

plt.show()