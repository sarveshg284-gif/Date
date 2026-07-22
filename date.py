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
# Moving NO Button (Android Touch Friendly)
# -----------------------

import streamlit.components.v1 as components


components.html(
"""
<!DOCTYPE html>

<html>

<head>

<style>

body{
    margin:0;
    height:150px;
    overflow:hidden;
    background:transparent;
}


#noBtn{

position:absolute;

top:50px;
left:50%;

transform:translateX(-50%);

background:#ff4da6;

color:white;

border:none;

padding:15px 35px;

border-radius:30px;

font-size:20px;

font-weight:bold;

box-shadow:0px 5px 15px rgba(255,0,100,0.3);

transition:0.25s;

}


</style>

</head>


<body>


<button id="noBtn">
🙈 NO
</button>



<script>


const btn=document.getElementById("noBtn");


const messages=[

"🙈 NO",

"🥺 Are you sure?",

"😔 Think again",

"💔 Don't say no yet...",

"🥹 One chance?",

"❤️ Please reconsider",

"🌹 I'll make it special",

"😊 I'm still hoping...",

"💖 Last chance",

"🥲 Okay... I respect your choice."

];



let count=0;



function moveButton(){


let x=Math.random()*220;

let y=Math.random()*70;


btn.style.left=x+"px";

btn.style.top=y+"px";


btn.innerHTML=
messages[Math.min(count,messages.length-1)];


count++;


}



btn.addEventListener(
"touchstart",
function(e){

e.preventDefault();

moveButton();

}
);



btn.addEventListener(
"click",
function(){

moveButton();

}
);



</script>


</body>

</html>
""",
height=160,
)

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


Thank you for saying YES. 🥹🌸
"""
        )

        st.balloons()
        st.snow()

        st.markdown(
            """
---
<center>

</center>
""",
            unsafe_allow_html=True,
        )
