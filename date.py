import streamlit as st
import streamlit.components.v1 as components
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Virtual Love Game 💖",
    page_icon="💖",
    layout="centered"
)

# -----------------------------
# SESSION STATES
# -----------------------------
if "show_gift" not in st.session_state:
    st.session_state.show_gift = False

if "email_sent" not in st.session_state:
    st.session_state.email_sent = False


# -----------------------------
# EMAIL FUNCTION
# -----------------------------
def send_email():

    sender_email = st.secrets["EMAIL"]
    sender_password = st.secrets["EMAIL_PASSWORD"]
    receiver_email = st.secrets["RECEIVER_EMAIL"]

    subject = "💖 Someone Accepted Your Proposal!"

    body = f"""
Someone clicked YES ❤️

Time:
{datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}

Your Streamlit Love Game received a YES response.
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)


# -----------------------------
# TITLE
# -----------------------------
st.markdown(
    "<h1 style='text-align:center;color:red;'>💭 A Message for You 💭</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<p style='text-align:center;font-size:18px;color:#333;line-height:1.8;'>
Before I met you, I never knew what it was like to smile 😊 for no reason.<br>
Now that you're here, I think my entire life will fall into place. ☺️🫶
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;font-size:18px;color:#333;line-height:1.8;'>
I don't know how much you love me,<br>
but I love you with all my heart. ❤️🤌🙂
</p>
""", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align:center;color:#ff1493;'>
💖 Will you be mine 💗🫴 💖
</h2>
""", unsafe_allow_html=True)

# -----------------------------
# YES BUTTON
# -----------------------------
if st.button("YES !! ❤️"):

    st.session_state.show_gift = True
    st.balloons()

    if not st.session_state.email_sent:
        try:
            send_email()
            st.success("❤️ Your response has been recorded!")
            st.session_state.email_sent = True
        except Exception as e:
            st.error(f"Email Error: {e}")


# -----------------------------
# NO BUTTON (RUN AWAY)
# -----------------------------
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
top:120px;
left:55%;
transform:translateX(-50%);

background:#ff4da6;
color:white;

border:none;
padding:14px 28px;

border-radius:30px;

font-size:18px;

cursor:pointer;

transition:0.1s;

box-shadow:0 5px 15px rgba(0,0,0,.2);

}

</style>

</head>

<body>

<button id="noBtn">NO 😜</button>

<script>

const btn=document.getElementById("noBtn");

const texts=[
"NO 😜",
"Try Again 😂",
"Wrong Button 🤣",
"Catch Me 😎",
"Impossible 😝",
"Not Today 😆"
];

btn.addEventListener("mouseover",()=>{

const maxX=window.innerWidth-150;
const maxY=window.innerHeight-120;

btn.style.left=Math.random()*maxX+"px";
btn.style.top=Math.random()*maxY+"px";

btn.innerHTML=texts[Math.floor(Math.random()*texts.length)];

});

</script>

</body>

</html>

""",
height=250
)

# -----------------------------
# GIFT SECTION
# -----------------------------
if st.session_state.show_gift:

    st.markdown(
        """
<div style="
background:white;
padding:25px;
border-radius:20px;
text-align:center;
box-shadow:0 0 20px rgba(255,105,180,.4);
margin-top:20px;
">

<h2>💕 I knew it! 💕</h2>

<div style="font-size:90px;">
🎁 🎁 🎁
</div>

<h3>🌸 Here is your gift 🌸</h3>

<div style="font-size:70px;">
💐 🧸 🍫
</div>

<p style='font-size:18px;line-height:1.8;color:#333;'>

Loving ❤️ you has taught me what commitment truly means.<br>

Every version of my future includes your smile 😊.<br><br>

Thank you for making my world brighter every single day. 💕

</p>

<h2 style="color:#ff1493;">
You are Special ❤️
</h2>

</div>
""",
        unsafe_allow_html=True
    )
