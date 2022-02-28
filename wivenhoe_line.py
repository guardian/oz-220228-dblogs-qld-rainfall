# %%
import pandas as pd 
# pd.set_option("display.max_rows", 100)

# testo = "-testo"
testo = ''
chart_key = f"oz-datablogs-220228-wivenhoe-dam-levels-{testo}"

fillo = 'input/Wivenhoe.csv'
#%%

data = pd.read_csv(fillo)

#%%

df = data.copy()
# 'Name', 'Date', 'Last Observation (%)', 'Last Observation (ML)'
df['Last Observation (ML)'] = pd.to_numeric(df['Last Observation (ML)'])


df = df[['Date', 'Last Observation (%)']]
# df = df[['Date', 'Last Observation (ML)']]


df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Date'] = df['Date'].dt.strftime("%Y-%m-%d")

# df['Last Observation (%)'] = pd.to_numeric(df['Last Observation (%)'])
# 
df = df[['Date', 'Last Observation (%)']]
df.columns = ['Date', 'Water level']

final = df.to_dict(orient='records')


p = df

# p = p.sort_values(by=['Last Observation (%)'], ascending=False)

# vchecker = 'Last Observation (ML)'
# print(p.loc[p[vchecker].isna()])

print(p)
print(p.columns.tolist())

# #%%

from yachtcharter import yachtCharter
template = [
    {
    "title": f"Wivenhoe dam capacity over time",
    "subtitle": f"Showing the actual dam level as a percentage of dam capacity since 2008.",
    "footnote": "",
    "dateFormat": "%Y-%m-%d",
    "source": "SEQ Water",
    "margin-left": "35",
    "margin-top": "30",
    "margin-bottom": "20",
    "margin-right": "10",
#     "tooltip":"<strong>{{#formatDate}}{{Date}}{{/formatDate}}</strong><br/> In ICU: {{ICU}}<br/>"
    }
]

yachtCharter(template=template, 
            data=final,
            chartId=[{"type":"linechart"}],
            options=[{"colorScheme":"guardian", "lineLabelling":"TRUE"}],
            chartName=f"{chart_key}{testo}")

# # #%%