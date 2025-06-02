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

    bar_height = max(300, 40 * len(ranking))

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
        yaxis_tickfont=dict(size=16),
        template="plotly_white",
        height=bar_height,
        margin=dict(l=40, r=40, t=60, b=40),
    )

    return fig


def plot_top3_radar(
    user_profile: Dict[str, float], top_dishes: List[Tuple[str, Dict[str, float]]]
) -> go.Figure:
    """
    Compares user preferences with top 3 dishes on a radar chart (modern design).
    By default shows user and first-ranked dish only.
    """
    categories = list(user_profile.keys())
    categories.append(categories[0])  # Close radar

    fig = go.Figure()
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

    # User preferences (always visible)
    user_values = [user_profile[cat] for cat in user_profile]
    user_values.append(user_values[0])
    fig.add_trace(
        go.Scatterpolar(
            r=user_values,
            theta=categories,
            fill="toself",
            name="You",
            line=dict(color=colors[0], width=3, dash="dash"),
            marker=dict(size=6),
            opacity=0.8,
            visible=True,
        )
    )

    # Dishes: only first one visible by default
    for i, (dish_name, dish_profile) in enumerate(top_dishes):
        values = [dish_profile.get(cat, 0) for cat in user_profile]
        values.append(values[0])
        fig.add_trace(
            go.Scatterpolar(
                r=values,
                theta=categories,
                fill="toself",
                name=dish_name,
                line=dict(color=colors[i + 1], width=2),
                marker=dict(size=5),
                opacity=0.7,
                visible=True if i == 0 else "legendonly",
            )
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True, range=[0, 100], gridcolor="lightgrey", gridwidth=1
            ),
            angularaxis=dict(tickfont=dict(size=12)),
            bgcolor="white",
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            font=dict(size=12),
        ),
        template="plotly_white",
        height=600,
        margin=dict(l=30, r=30, t=80, b=80),
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

    tab_results, tab_radar, tab_debug = st.tabs(
        ["🍽️ Recommendations", "📊 Comparison Radar", "🧪 Details"]
    )

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

    with tab_radar:
        st.subheader("🔎 Compare Preferences with Top 3 Dishes")

        # Create user profile (only raw values)
        user_profile = {k: v["value"] for k, v in user_raw.items()}

        # Get top3 dish names
        top3_dishes = [name for name, _ in top3]

        # Get top3 raw profiles
        top3_profiles = [(dish, raw_dishes[dish]) for dish in top3_dishes]

        st.plotly_chart(
            plot_top3_radar(user_profile, top3_profiles), use_container_width=True
        )

    with tab_debug:
        st.json(user_fuzzy)
