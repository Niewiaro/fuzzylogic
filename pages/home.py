import streamlit as st


st.title("👋 Welcome to the Fuzzy Food Recommender")

st.markdown(
    """
    This interactive app helps you **discover the best dishes** based on your **personal preferences** 
    using the power of fuzzy logic. 🍽️🧠
    """
)

with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/1046/1046784.png", width=120)
    with col2:
        st.success("Ready to find your ideal meal? Let’s get started!")
        st.page_link(
            "pages/fuzzylogic.py", label="🍽️ Go to Fuzzy Logic Recommender", icon="➡️"
        )


st.divider()

st.subheader("🧭 How to Use This App")

st.markdown(
    """
1. Go to the **Fuzzy Logic** page from the sidebar or via the button below.
2. Adjust sliders for each food feature like taste, price, calories, etc.
3. Set how important each feature is to you.
4. Click the **Generate Recommendations** button.
5. See your **top matching dishes**, explore fuzzy data, and compare meals on a **radar chart**.
"""
)

st.divider()

st.subheader("🧠 About Fuzzy Logic")

st.markdown(
    """
Unlike traditional logic, fuzzy logic allows **partial membership**.  
This means a dish can be **somewhat spicy and slightly sweet at the same time** — just like real food.

By combining your preferences with fuzzy evaluation, we compute a **match score** for every dish.
"""
)

st.page_link("pages/fuzzylogic.py", label="🍽️ Go to Fuzzy Logic Recommender", icon="➡️")

st.divider()
st.caption("Made with ❤️ using Streamlit & fuzzy logic.")
