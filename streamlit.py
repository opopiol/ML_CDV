import streamlit as st
import seaborn as sns
import altair as alt
import pandas as pd
import numpy as np
from vega_datasets import data
import matplotlib.pyplot as plt

st.title("Penguins...not again")
penguins = sns.load_dataset("penguins")
st.write(penguins)

"""
## Data description

%d number of penguins
"""% penguins.shape[0]

species = penguins["species"].unique()
change_species = st.selectbox("Select species: ", species)

sex = penguins["sex"].dropna().unique()
change_sex = st.selectbox("Select sex: ", sex)

filtered_peng= penguins[(penguins['species']==change_species)&(penguins['sex']==change_sex)]
filtered_peng

linedata=pd.DataFrame(filtered_peng, columns=['bill_length_mm','bill_depth_mm',"flipper_length_mm"])
st.line_chart(linedata)

base = alt.Chart(penguins.dropna()).mark_circle().encode(
        alt.X("bill_depth_mm"),
        alt.Y("flipper_length_mm"),
        color="sex",
        tooltip=['sex','species',"bill_depth_mm", 'flipper_length_mm','body_mass_g'],
        size='body_mass_g'
).properties(
    width=700,
    height=400
).interactive()

st.altair_chart(base)