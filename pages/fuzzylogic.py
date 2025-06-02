import streamlit as st
import numpy as np
import skfuzzy as fuzz
from typing import List, Dict, Tuple
import plotly.graph_objects as go


# ——— Configuration ———
VALUE_RANGE = (0, 100)
WEIGHT_RANGE = (0.0, 2.0)
FUZZY_DOMAIN = np.arange(VALUE_RANGE[0], VALUE_RANGE[1] + 1, 1)

# ——— Membership Functions ———
membership_functions = {
    "taste": {
        "sweet": fuzz.trimf(FUZZY_DOMAIN, [0, 0, 25]),
        "salty": fuzz.trimf(FUZZY_DOMAIN, [20, 35, 50]),
        "spicy": fuzz.trimf(FUZZY_DOMAIN, [40, 55, 70]),
        "sour": fuzz.trimf(FUZZY_DOMAIN, [60, 75, 85]),
        "bitter": fuzz.trimf(FUZZY_DOMAIN, [80, 100, 100]),
    },
    "price": {
        "cheap": fuzz.trimf(FUZZY_DOMAIN, [0, 0, 40]),
        "medium": fuzz.trimf(FUZZY_DOMAIN, [30, 50, 70]),
        "expensive": fuzz.trimf(FUZZY_DOMAIN, [60, 100, 100]),
    },
    "temperature": {
        "cold": fuzz.trimf(FUZZY_DOMAIN, [0, 0, 40]),
        "warm": fuzz.trimf(FUZZY_DOMAIN, [30, 50, 70]),
        "hot": fuzz.trimf(FUZZY_DOMAIN, [60, 100, 100]),
    },
    "prep_time": {
        "fast": fuzz.trimf(FUZZY_DOMAIN, [0, 0, 40]),
        "medium": fuzz.trimf(FUZZY_DOMAIN, [30, 50, 70]),
        "long": fuzz.trimf(FUZZY_DOMAIN, [60, 100, 100]),
    },
    "calories": {
        "low": fuzz.trimf(FUZZY_DOMAIN, [0, 0, 40]),
        "medium": fuzz.trimf(FUZZY_DOMAIN, [30, 50, 70]),
        "high": fuzz.trimf(FUZZY_DOMAIN, [60, 100, 100]),
    },
    "availability": {
        "common": fuzz.trimf(FUZZY_DOMAIN, [0, 0, 40]),
        "seasonal": fuzz.trimf(FUZZY_DOMAIN, [30, 50, 70]),
        "rare": fuzz.trimf(FUZZY_DOMAIN, [60, 100, 100]),
    },
    "satiety": {
        "light": fuzz.trimf(FUZZY_DOMAIN, [0, 0, 40]),
        "medium": fuzz.trimf(FUZZY_DOMAIN, [30, 50, 70]),
        "filling": fuzz.trimf(FUZZY_DOMAIN, [60, 100, 100]),
    },
}

# ——— Dishes (scaled 0–100) ———
raw_dishes = {
    "Burger": {
        "taste": 40,
        "price": 50,
        "temperature": 90,
        "prep_time": 10,
        "calories": 90,
        "availability": 10,
        "satiety": 90,
    },
    "Ice Cream": {
        "taste": 0,
        "price": 10,
        "temperature": 10,
        "prep_time": 10,
        "calories": 50,
        "availability": 10,
        "satiety": 10,
    },
    "KFC Wings": {
        "taste": 60,
        "price": 50,
        "temperature": 90,
        "prep_time": 10,
        "calories": 90,
        "availability": 10,
        "satiety": 50,
    },
    "Sushi": {
        "taste": 40,
        "price": 90,
        "temperature": 10,
        "prep_time": 50,
        "calories": 10,
        "availability": 50,
        "satiety": 10,
    },
    "Pancakes": {
        "taste": 10,
        "price": 10,
        "temperature": 50,
        "prep_time": 50,
        "calories": 50,
        "availability": 10,
        "satiety": 50,
    },
    "Pasta": {
        "taste": 40,
        "price": 50,
        "temperature": 90,
        "prep_time": 50,
        "calories": 50,
        "availability": 10,
        "satiety": 90,
    },
    "Pizza": {
        "taste": 40,
        "price": 50,
        "temperature": 90,
        "prep_time": 50,
        "calories": 90,
        "availability": 10,
        "satiety": 90,
    },
    "Dumplings": {
        "taste": 40,
        "price": 10,
        "temperature": 50,
        "prep_time": 50,
        "calories": 50,
        "availability": 10,
        "satiety": 50,
    },
    "Pork Chop": {
        "taste": 40,
        "price": 50,
        "temperature": 90,
        "prep_time": 50,
        "calories": 90,
        "availability": 10,
        "satiety": 90,
    },
    "Fries": {
        "taste": 40,
        "price": 10,
        "temperature": 90,
        "prep_time": 10,
        "calories": 90,
        "availability": 10,
        "satiety": 10,
    },
    "Zapiekanka": {
        "taste": 40,
        "price": 10,
        "temperature": 90,
        "prep_time": 10,
        "calories": 50,
        "availability": 10,
        "satiety": 50,
    },
    "Hunter's Stew": {
        "taste": 40,
        "price": 50,
        "temperature": 90,
        "prep_time": 90,
        "calories": 90,
        "availability": 50,
        "satiety": 90,
    },
    "Sour Rye Soup": {
        "taste": 80,
        "price": 10,
        "temperature": 90,
        "prep_time": 50,
        "calories": 50,
        "availability": 10,
        "satiety": 50,
    },
    "Kebab": {
        "taste": 60,
        "price": 50,
        "temperature": 90,
        "prep_time": 10,
        "calories": 90,
        "availability": 10,
        "satiety": 90,
    },
    "Caesar Salad": {
        "taste": 40,
        "price": 50,
        "temperature": 10,
        "prep_time": 10,
        "calories": 10,
        "availability": 10,
        "satiety": 10,
    },
    "Tacos": {
        "taste": 60,
        "price": 50,
        "temperature": 50,
        "prep_time": 10,
        "calories": 50,
        "availability": 50,
        "satiety": 50,
    },
    "Donuts": {
        "taste": 10,
        "price": 10,
        "temperature": 50,
        "prep_time": 50,
        "calories": 90,
        "availability": 10,
        "satiety": 10,
    },
    "Hot Dog": {
        "taste": 40,
        "price": 10,
        "temperature": 90,
        "prep_time": 10,
        "calories": 90,
        "availability": 10,
        "satiety": 50,
    },
    "Potato Dumplings": {
        "taste": 40,
        "price": 10,
        "temperature": 90,
        "prep_time": 50,
        "calories": 50,
        "availability": 10,
        "satiety": 50,
    },
    "Cheesecake": {
        "taste": 10,
        "price": 50,
        "temperature": 10,
        "prep_time": 90,
        "calories": 90,
        "availability": 10,
        "satiety": 50,
    },
}


# ——— Functions ———
def to_title(title: str) -> str:
    result = title.capitalize().replace("_", " ")
    return result


def map_slider_to_label(value: int, labels: List[str]) -> str:
    index = min(value * len(labels) // 101, len(labels) - 1)
    return labels[index]


def render_sliders(feature: str, labels: List[str]) -> Tuple[int, float]:
    value = st.slider(
        f"{feature.capitalize()} preference", *VALUE_RANGE, 50, help=", ".join(labels)
    )
    st.caption(f"Selected: {map_slider_to_label(value, labels)}")
    weight = st.slider(
        f"{feature.capitalize()} importance", *WEIGHT_RANGE, 1.0, step=0.1
    )
    return value, weight


def fuzzify_preferences(
    preferences: Dict[str, Dict[str, float]],
) -> Dict[str, Dict[str, float]]:
    return {
        feat: {
            cat: fuzz.interp_membership(FUZZY_DOMAIN, mf, preferences[feat]["value"])
            * preferences[feat]["weight"]
            for cat, mf in membership_functions[feat].items()
        }
        for feat in preferences
    }


def calculate_scores(
    user_fuzzy: Dict[str, Dict[str, float]],
    total_weight: float,
) -> List[Tuple[str, float]]:
    results = []

    for dish, features in raw_dishes.items():
        score = 0.0
        for feat in user_fuzzy:
            dish_val = features.get(feat, 0)
            dish_fuzzy = {
                cat: fuzz.interp_membership(FUZZY_DOMAIN, mf, dish_val)
                for cat, mf in membership_functions[feat].items()
            }
            for cat in user_fuzzy[feat]:
                score += user_fuzzy[feat][cat] * dish_fuzzy.get(cat, 0.0)
        normalized_score = score / total_weight
        results.append((dish, normalized_score))

    return sorted(results, key=lambda x: x[1], reverse=True)


def plot_membership_plotly(feature: str) -> go.Figure:
    """
    Plots membership functions for a given feature using Plotly.
    """
    x = FUZZY_DOMAIN
    labels = membership_functions[feature]

    fig = go.Figure()
    for label, mf in labels.items():
        fig.add_trace(
            go.Scatter(
                x=x,
                y=mf,
                mode="lines",
                name=label.capitalize(),
                line=dict(width=3),
            )
        )

    fig.update_layout(
        title=f"Fuzzy Categories: {to_title(feature)}",
        xaxis_title="Value (0-100)",
        yaxis_title="Membership",
        template="plotly_white",
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation="h", x=0, y=1.1),
    )
    return fig


def plot_dish_scores_percent(ranking: List[Tuple[str, float]]) -> go.Figure:
    """
    Creates a horizontal bar chart of dish scores converted to percentages.
    Input scores are assumed to be in [0, 1] range.
    """
    if not ranking:
        return go.Figure()

    # Convert scores to percentages
    dish_names = [dish for dish, _ in ranking]
    scores_percent = [score * 100 for _, score in ranking]

    fig = go.Figure(
        data=[
            go.Bar(
                x=scores_percent,
                y=dish_names,
                orientation="h",
                text=[f"{p:.1f}%" for p in scores_percent],
                textposition="auto",
                marker=dict(
                    color=scores_percent,
                    colorscale="Blues",
                    line=dict(color="rgba(0,0,0,0.6)", width=1),
                ),
            )
        ]
    )

    fig.update_layout(
        title="📊 Dish Scores as Percentage Match",
        title_font_size=24,
        xaxis_title="Score (%)",
        yaxis=dict(autorange="reversed"),
        xaxis=dict(range=[0, 100], tickfont=dict(size=14)),
        yaxis_tickfont=dict(size=14),
        template="plotly_white",
        height=800,
        margin=dict(l=40, r=40, t=60, b=40),
    )

    return fig


# ——— Streamlit UI ———
st.title("🍽️ Fuzzy Food Recommender")

st.markdown(
    "This app recommends dishes based on your taste and dietary preferences using fuzzy logic. "
    "Adjust your preferences below and click the button to see your top matches."
)


user_raw = {}
st.header("Your Preferences")
for feature in membership_functions:
    st.subheader(to_title(feature), divider=True)

    with st.container(border=True):
        categories = list(membership_functions[feature])
        val, wgt = render_sliders(feature, categories)
        user_raw[feature] = {"value": val, "weight": wgt}

        with st.expander(f"📊 Membership functions for {to_title(feature)}"):
            st.plotly_chart(plot_membership_plotly(feature), use_container_width=True)


with st.expander("🔍 Raw Input Data"):
    st.json(user_raw)

if st.button(
    "🔍 Generate Recommendations",
    type="primary",
    help="Click to match your preferences with the best dishes.",
):
    user_fuzzy = fuzzify_preferences(user_raw)
    total_weight = sum(user_raw[feat]["weight"] for feat in user_raw) or 1.0

    st.toast("✅ Recommendations generated successfully!", icon="🎉")

    tab_results, tab_debug = st.tabs(["🍽️ Recommended Dishes", "🧪 Fuzzy Details"])

    with tab_results:
        ranking = calculate_scores(user_fuzzy, total_weight)

        st.subheader("🍽️ Your Top 3 Matches", divider=True)

        top3 = ranking[:3]

        if top3:
            medals = ["🥇", "🥈", "🥉"]
            cols = st.columns(3)

            for i, (dish, score) in enumerate(top3):
                with cols[i]:
                    st.metric(
                        label=f"{medals[i]} {dish}",
                        value=f"{score * 100:.1f}%",
                        help="Fuzzy match score",
                    )

        st.plotly_chart(plot_dish_scores_percent(ranking), use_container_width=True)

    with tab_debug:
        st.json(user_fuzzy)
