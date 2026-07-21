import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Date Proposal ❤️",
    page_icon="❤️",
    layout="centered"
)

if "accepted" not in st.session_state:
    st.session_state.accepted = False

# -----------------------
# Title
# -----------------------
st.markdown(
    """
    <h1 style="text-align:center;color:#ff4b4b;">
        ❤️ A Special Question ❤️
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h3 style="text-align:center;">
        Every moment with you feels special. 😊
    </h3>

    <h2 style="text-align:center;color:#ff1493;">
        🌹 Will you go on a date with me? 🌹
    </h2>
    """,
    unsafe_allow_html=True,
)

# -----------------------
# YES Button
# -----------------------
if st.button("YES ❤️"):
    st.session_state.accepted = True
    st.balloons()

# -----------------------
# NO Button (Runs Away)
# -----------------------
components.html(
    """
<!DOCTYPE html>
<html>
<head>

<style>

body{
    margin:0;
    overflow:hidden;
    background:transparent;
}

#noBtn{

position:absolute;

top:60px;
left:55%;

background:#ff4da6;

color:white;

border:none;

padding:14px 28px;

border-radius:30px;

font-size:18px;

cursor:pointer;

transition:0.1s;

}

</style>

</head>

<body>

<button id="noBtn">NO 😜</button>

<script>

const btn=document.getElementById("noBtn");

const texts=[
"No 😜",
"Catch Me 😂",
"Too Slow 😆",
"Try Again 😎",
"Impossible 🤣",
"Almost 😜"
];

btn.addEventListener("mouseover",()=>{

const maxX=window.innerWidth-150;
const maxY=window.innerHeight-100;

btn.style.left=Math.random()*maxX+"px";
btn.style.top=Math.random()*maxY+"px";

btn.innerHTML=texts[Math.floor(Math.random()*texts.length)];

});

</script>

</body>
</html>
""",
    height=180,
)

# -----------------------
# After YES
# -----------------------
if st.session_state.accepted:

    st.markdown(
        """
        <div style="
        background:#fff0f6;
        padding:25px;
        border-radius:20px;
        text-align:center;
        margin-top:20px;
        box-shadow:0px 0px 20px rgba(255,105,180,.4);
        ">

        <h2>🥳 Yay!! 🥳</h2>

        <h3>I'm so happy you said YES! ❤️</h3>

        <p style="font-size:18px;">
        Now choose our date. 🌹
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    date = st.date_input("📅 Select a date")

    time = st.time_input("⏰ Select a time")

    place = st.selectbox(
        "📍 Where should we go?",
        [
            "☕ Coffee Shop",
            "🍕 Pizza Date",
            "🎬 Movie",
            "🍽️ Dinner",
            "🌳 Park Walk",
            "🍦 Ice Cream",
            "🏖️ Beach",
        ],
    )

    if st.button("💖 Confirm Date"):

        st.success("Our date is officially fixed! ❤️")

        st.markdown(
            f"""
### 💌 Date Confirmed

**📅 Date:** {date}

**⏰ Time:** {time}

**📍 Place:** {place}

Can't wait to see you! 🥰🌹
"""
        )

        st.snow()
