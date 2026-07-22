import streamlit as st
import requests

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Date Proposal ❤️",
    page_icon="❤️",
    layout="centered"
)

# -----------------------
# Android Friendly CSS
# -----------------------
st.markdown("""
<style>

.block-container{
    max-width:500px;
    padding-top:2rem;
}

div.stButton > button{
    width:100%;
    height:60px;
    font-size:22px;
    font-weight:bold;
    border-radius:15px;
    border:none;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# Telegram Function
# -----------------------
BOT_TOKEN = "8954289020:AAHZaBvcwLhPruZbHO7fH7VZwD02ufQKvAM"
CHAT_ID = "6746692749"

def send_telegram(date, time, place):

    message = f"""
❤️ New Date Confirmation ❤️

Someone accepted your proposal! 🥳

📅 Date: {date}

⏰ Time: {time}

📍 Place: {place}

💖 Congratulations!
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

# -----------------------
# Session State
# -----------------------
if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "no_count" not in st.session_state:
    st.session_state.no_count = 0

# -----------------------
# Title
# -----------------------
st.markdown(
"""
<h1 style="text-align:center;color:#ff4b4b;">
❤️ A Special Question ❤️
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<h3 style="text-align:center;">
Every moment with you feels special. 😊
</h3>

<h2 style="text-align:center;color:#ff1493;">
What if we went out? 🙂🫴
</h2>
""",
unsafe_allow_html=True
)

# -----------------------
# YES Button
# -----------------------
if st.button(
    "❤️ YES ❤️",
    use_container_width=True
):

    st.session_state.accepted = True
    st.balloons()

# -----------------------
# Android Friendly NO Button
# -----------------------

no_messages = [

    "🙈 No",

    "🥺 Are you sure?",

    "😔 Think once again...",

    "💔 Don't say no yet...",

    "🥹 Give me one chance?",

    "❤️ Please reconsider...",

    "🌹 I promise it'll be special...",

    "😊 I'm still hoping...",

    "💖 Last chance?",

    "🥲 Okay... I respect your choice."
]

if not st.session_state.accepted:

    if st.button(
        no_messages[
            min(
                st.session_state.no_count,
                len(no_messages)-1
            )
        ],
        use_container_width=True
    ):

        if st.session_state.no_count < len(no_messages)-1:

            st.session_state.no_count += 1

        st.rerun()

# -----------------------
# After YES
# -----------------------
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

    st.write("")

    # -----------------------
    # Date
    # -----------------------
    date = st.date_input(
        "📅 Select a Date"
    )

    # -----------------------
    # Time
    # -----------------------
    time = st.time_input(
        "⏰ Select Time"
    )

    # -----------------------
    # Place
    # -----------------------
    place = st.selectbox(
        "📍 Where should we go?",
        [
            "🌸 Iskcon Temple (Kharghar)",
            "🙏 Siddhivinayak Mandir (Dadar)",
            "🛕 Ganpati Mandir (Titwala)",
            "🌿 Manas Mandir (Shahapur)",
            "💖 Iskcon Temple (Thane)",
            "✨ Birla Mandir (Shahad)"
        ]
    )

    st.write("")

    # -----------------------
    # Confirm Button
    # -----------------------
    if st.button(
        "😊 Confirm Our Date ❤️",
        use_container_width=True
    ):

        try:
            send_telegram(
                date,
                time,
                place
            )

            st.success(
                "❤️ Our date is officially confirmed!"
            )

        except Exception as e:
            st.error(
                f"Telegram Error: {e}"
            )

        st.markdown(
            f"""
## 💌 See You Soon 😊

### 📅 Date
**{date}**

### ⏰ Time
**{time}**

### 📍 Place
**{place}**

---

❤️ Can't wait to meet you!

Thank you for saying YES. 🥹🌹
"""
        )

        st.balloons()
        st.snow()

        st.markdown(
            """
---
<center>

<h3 style="color:#ff1493;">
🌸 Have a Beautiful Day 🌸
</h3>

</center>
""",
            unsafe_allow_html=True,
        )
