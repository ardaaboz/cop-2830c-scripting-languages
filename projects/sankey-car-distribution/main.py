import plotly.graph_objects as go

labels = [
    "All Cars",  # 0
    "Fiat",  # 1
    "Renault",  # 2
    "Ford",  # 3
    "Volkswagen",  # 4
    "Peugeot",  # 5
    "Citroën",  # 6
    "Hyundai",  # 7
    "Toyota",  # 8
    "Chery",  # 9
    "TOGG",  # 10
    "Nissan",  # 11
    "Egea",  # 12
    "Tipo",  # 13
    "Doblo",  # 14
    "Clio",  # 15
    "Megane",  # 16
    "Symbol",  # 17
    "Focus",  # 18
    "Courier",  # 19
    "Golf",  # 20
    "Passat",  # 21
    "208",  # 22
    "3008",  # 23
    "C-Elysée",  # 24
    "Berlingo",  # 25
    "i20",  # 26
    "Tucson",  # 27
    "Corolla",  # 28
    "Yaris",  # 29
    "Tiggo 8",  # 30
    "Omoda 5",  # 31
    "T10X",  # 32
    "Qashqai",  # 33
    "Micra"  # 34
]

sources = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # All Cars (0) > Brands (1-11)

    1, 1, 1,  # Fiat (1) > Models (12, 13, 14)
    2, 2, 2,  # Renault (2) > Models (15, 16, 17)
    3, 3,  # Ford (3) > Models (18, 19)
    4, 4,  # VW (4) > Models (20, 21)
    5, 5,  # Peugeot (5) > Models (22, 23)
    6, 6,  # Citroën (6) > Models (24, 25)
    7, 7,  # Hyundai (7) > Models (26, 27)
    8, 8,  # Toyota (8) > Models (28, 29)
    9, 9,  # Chery (9) > Models (30, 31)
    10,  # TOGG (10) > Model (32)
    11, 11  # Nissan (11) > Models (33, 34)
]

targets = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,  # All Cars > Brands

    12, 13, 14,  # Fiat > Models
    15, 16, 17,  # Renault > Models
    18, 19,  # Ford > Models
    20, 21,  # VW > Models
    22, 23,  # Peugeot > Models
    24, 25,  # Citroën > Models
    26, 27,  # Hyundai > Models
    28, 29,  # Toyota > Models
    30, 31,  # Chery > Models
    32,  # TOGG > Model
    33, 34  # Nissan > Models
]

values = [
    7, 7, 5, 5, 4, 3, 3, 3, 5, 3, 3,  # Values for All Cars > Brands (11 values)

    3, 2, 2,  # Fiat > Models (3 values)
    3, 2, 2,  # Renault > Models (3 values)
    3, 2,  # Ford > Models (2 values)
    3, 2,  # VW > Models (2 values)
    2, 2,  # Peugeot > Models (2 values)
    2, 1,  # Citroën > Models (2 values)
    2, 1,  # Hyundai > Models (2 values)
    3, 2,  # Toyota > Models (2 values)
    3, 2,  # Chery > Models (2 values)
    3,  # TOGG > Model (1 value)
    2, 1  # Nissan > Models (2 values)
]

# Define brand colors
brand_colors = [
    "rgb(105,105,105)",  # All Cars

    "rgb(178,34,34)",  # Fiat
    "rgb(139,0,0)",  # Renault
    "rgb(0,0,139)",  # Ford
    "rgb(0,100,0)",  # Volkswagen
    "rgb(160,82,45)",  # Peugeot
    "rgb(128,0,0)",  # Citroën

    "rgb(47,79,79)",  # Hyundai
    "rgb(107,142,35)",  # Toyota
    "rgb(139,69,19)",  # Chery
    "rgb(128,0,128)",  # TOGG
    "rgb(25,25,112)",  # Nissan
]

# Map models to their brand's color
node_colors = [None] * len(labels)
node_colors[0] = brand_colors[0]  # All Cars

# Brands (1-11)
for i in range(1, 12):
    node_colors[i] = brand_colors[i]

# Models (12-34)
# Fiat Models
node_colors[12] = brand_colors[1]
node_colors[13] = brand_colors[1]
node_colors[14] = brand_colors[1]

# Renault Models
node_colors[15] = brand_colors[2]
node_colors[16] = brand_colors[2]
node_colors[17] = brand_colors[2]

# Ford Models
node_colors[18] = brand_colors[3]
node_colors[19] = brand_colors[3]

# Volkswagen Models
node_colors[20] = brand_colors[4]
node_colors[21] = brand_colors[4]

# Peugeot Models
node_colors[22] = brand_colors[5]
node_colors[23] = brand_colors[5]

# Citroën Models
node_colors[24] = brand_colors[6]
node_colors[25] = brand_colors[6]

# Hyundai Models
node_colors[26] = brand_colors[7]
node_colors[27] = brand_colors[7]

# Toyota Models
node_colors[28] = brand_colors[8]
node_colors[29] = brand_colors[8]

# Chery Models
node_colors[30] = brand_colors[9]
node_colors[31] = brand_colors[9]

# TOGG Models
node_colors[32] = brand_colors[10]

# Nissan Models
node_colors[33] = brand_colors[11]
node_colors[34] = brand_colors[11]

# link colors same as source node colors but with transparency
link_colors = []
alpha_value = 0.4

for s in sources:
    rgb_color_string = node_colors[s]
    r, g, b = map(int, rgb_color_string.strip('rgb()').split(','))
    rgba_color_string = f"rgba({r},{g},{b},{alpha_value})"
    link_colors.append(rgba_color_string)

fig = go.Figure(data=[go.Sankey(
    arrangement="snap",
    node=dict(
        pad=15,
        thickness=15,
        line=dict(color="white", width=0.5),
        label=labels,
        color=node_colors
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=link_colors
    )
)])

fig.update_layout(
    title_text="Car Brand and Model Distribution in a Parking Lot in Turkey",
    font=dict(color="white", size=10),
    paper_bgcolor="black",
    plot_bgcolor="black",
    height=700,
    width=1000,
)

fig.show()