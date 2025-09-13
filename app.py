import streamlit as st
import json
import random
from pathlib import Path
from streamlit_lottie import st_lottie

# ----------------------------
# Helper functions
# ----------------------------
def load_lottiefile(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def load_text(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def load_quiz(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Happy Anniversary ❤️", page_icon="💖", layout="centered")

# ----------------------------
# CSS (page + quiz redesign)
# ----------------------------
st.markdown(
    """
    <style>
    /* Page fonts + background */
    body {
        background: linear-gradient(135deg, #fff8fb, #fff6f9);
        font-family: 'Trebuchet MS', sans-serif;
    }

    .main-title {
        font-size: 56px;
        font-weight: 800;
        color: #e60073;
        text-align: center;
        margin-top: 18px;
        letter-spacing: 0.4px;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #800040;
        margin-top: -4px;
    }
    .one-liner {
        font-size: 18px;
        text-align: center;
        color: #ff3385;
        font-style: italic;
        margin-top: 6px;
    }
    .shayari {
        font-size: 18px;
        text-align: center;
        color: #b30059;
        font-style: italic;
        margin-top: 15px;
        padding: 14px;
        background: rgba(255, 230, 245, 0.6);
        border-radius: 14px;
        display: inline-block;
    }

    /* QUIZ - wrapper + card */
    .quiz-wrapper {
        max-width: 820px;
        margin-left: auto;
        margin-right: auto;
        padding-top: 6px;
        padding-bottom: 6px;
    }

    .quiz-card {
        background: linear-gradient(90deg, rgba(255,230,245,0.85), rgba(255,245,250,0.85));
        border-radius: 16px;
        padding: 18px 20px;
        margin: 16px 0;
        box-shadow: 0 8px 24px rgba(216, 68, 133, 0.06);
        border: 1px solid rgba(255, 200, 230, 0.6);
    }

    .question {
        font-size: 18px;
        font-weight: 700;
        color: #c2185b;
        margin-bottom: 12px;
    }

    /* Style the Streamlit radio container to look like part of the card.
       This is a global rule for radio widgets, but visually it makes the
       options sit inside a white block inside the pink card. */
    .stRadio > div {
        background: #fff;
        border: 1px solid #ffd6e6;
        border-radius: 12px;
        padding: 12px;
        margin-top: 6px;
    }

    /* style individual options inside radio when hovered/checked */
    .stRadio input[type="radio"] + label {
        padding: 8px 10px;
        border-radius: 10px;
    }
    .stRadio input[type="radio"]:checked + label {
        background: linear-gradient(90deg, #ff9bbf, #ff5b97);
        color: white !important;
        box-shadow: 0 6px 16px rgba(255, 75, 140, 0.18);
    }

    /* center the quiz title */
    .quiz-title {
        text-align: center;
        font-size: 26px;
        color: #e60073;
        font-weight: 800;
        margin-top: 6px;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Background Music (Autoplay + Loop with Base64)
# ----------------------------
import base64
music_path = "assets/music/background.mp3"
if Path(music_path).exists():
    with open(music_path, "rb") as f:
        st.audio(f.read(), format="audio/mp3", loop=True)
else:
    st.info("Add your background music file at assets/music/background.mp3")

# ----------------------------
# 1. Landing Section
# ----------------------------
st.markdown(f'<div class="main-title">Happy Anniversary ❤️ My Love</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">Four years of love, laughter, and a lifetime to go...</div>', unsafe_allow_html=True)
st.markdown(f'<div class="one-liner">Tere bina life ekdum adhoori hai, tu hai toh har din poori hai ❤️</div>', unsafe_allow_html=True)

# Floating hearts Lottie (optional)
try:
    hearts = load_lottiefile("assets/lottie/hearts.json")
    st_lottie(hearts, height=180, key="hearts")
except Exception:
    # don't break the page if missing
    pass

# ----------------------------
# Hero Image + Shayari (centered)
# ----------------------------
hero_path = "assets/images/hero.jpg"
if Path(hero_path).exists():
    st.markdown("<div style='text-align:center;margin-top:6px;'>", unsafe_allow_html=True)
    st.image(hero_path, width=420, caption="💞 Our Special Moment 💞")
    st.markdown("</div>", unsafe_allow_html=True)

# Shayari block
st.markdown(
    """
    <div style="text-align:center; margin-top:12px;">
        <p class="shayari">
        Har pal mein teri yaad bas jaati hai,<br>
        Teri muskaan meri duniya roshan kar jaati hai,<br>
        Anniversary par sirf yeh kehna hai tumse,<br>
        Meri zindagi tumse hi, tum pe hi ruk jaati hai ❤️
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ----------------------------
# Special Combined Shayari Section (Smooth Animations + Background)
# ----------------------------
from streamlit.components.v1 import html

animated_shayari = """
<style>
  body {
    margin: 0;
    padding: 0;
  }

  /* Background gradient animation */
  .shayari-bg {
    background: linear-gradient(270deg, #ffe6f0, #fff0f5, #ffe6ff);
    background-size: 600% 600%;
    animation: gradientShift 12s ease infinite;
    padding: 30px;
    border-radius: 20px;
    display: inline-block;
    box-shadow: 0 6px 20px rgba(200,60,120,0.25);
  }

  @keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

  /* Shayari text styles */
  #shayari-box p {
    font-size: 20px;
    color: #a8005a;
    font-style: italic;
    margin: 6px 0;
    opacity: 0;
    animation: fadeIn 1s forwards;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>

<div style="text-align:center; margin-top:20px;">
  <div class="shayari-bg" id="shayari-box">
  </div>
</div>

<script>
  const lines = [
    "Main Chup Rahoon Toh Samajh Jaati Ho,",
    "Main Hasi Bikhraoon Toh Saath Hasaati Ho,",
    "Zindagi Ki Raahon Mein Har Mod Par,",
    "Mujhe Apna Humsafar Banaati Ho.",
    "",
    "Meri Har Subah Tumse Roshan Hoti Hai,",
    "Meri Har Raat Tumse Khamosh Hoti Hai,",
    "Kya Kahein Kaise Bataayein,",
    "Meri Duniya Tumse Hi Poorn Hoti Hai.",
    "",
    "Chhoti Chhoti Baton Mein Khushi Dhoond Laati Ho,",
    "Mere Andheron Mein Roshni Ban Jaati Ho,",
    "Kabhi Nakhron Se Kabhi Pyaar Se,",
    "Meri Zindagi Ko Khubsurat Banaati Ho. ❤️"
  ];

  let i = 0;
  function showLine() {
    if (i < lines.length) {
      let box = document.getElementById("shayari-box");
      let p = document.createElement("p");
      p.textContent = lines[i];
      p.style.animationDelay = (i * 1.3) + "s";  // smooth staggered timing
      box.appendChild(p);
      i++;
      setTimeout(showLine, 1200);
    }
  }
  showLine();
</script>
"""

html(animated_shayari, height=750)


# ----------------------------
# 2. Photo Memories Carousel
# ----------------------------
st.subheader("📸 Our Memories Together")
images = list(Path("assets/images").glob("*.jpg")) + list(Path("assets/images").glob("*.png"))

if len(images) > 1:
    index = st.slider("Slide through our memories 💕", 1, len(images))
    st.image(str(images[index - 1]), caption=f"Memory {index}", use_container_width=True)
elif len(images) == 1:
    st.image(str(images[0]), caption="Our first memory 💕", use_container_width=True)
else:
    st.info("Add some photos in assets/images/ (jpg/png)")

st.divider()

# ----------------------------
# 3. Why You're My Lucky Charm
# ----------------------------
st.markdown(
    """
    <style>
        .lucky-section {
            text-align: center;
            margin: 30px auto;
            max-width: 720px;
        }
        .lucky-title {
            font-size: 28px;
            font-weight: 800;
            color: #e60073;
            margin-bottom: 20px;
            position: relative;
        }
        .lucky-title::after {
            content: "";
            display: block;
            width: 80px;
            height: 3px;
            background: linear-gradient(90deg, #ff85a2, #ff3385);
            margin: 10px auto 0;
            border-radius: 2px;
        }
        .lucky-item {
            font-size: 20px;
            margin: 12px 0;
            color: #800040;
            font-weight: 500;
            transition: transform 0.2s ease, color 0.2s ease;
        }
        .lucky-item:hover {
            transform: scale(1.05);
            color: #e60073;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='lucky-section'>", unsafe_allow_html=True)
st.markdown("<div class='lucky-title'>🍀 Why You're My Lucky Charm</div>", unsafe_allow_html=True)

lucky_points = [
    "✨ You bring me peace when I’m restless",
    "🌷 You make even boring days beautiful",
    "🤗 You turn every fight into a reason to hug",
    "❤️ You remind me daily that love is real"
]

for point in lucky_points:
    st.markdown(f"<div class='lucky-item'>{point}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ----------------------------
# 4. Love Letter Section
# ----------------------------
st.subheader("💌 A Letter For You")
letter_file = "content/love_letter.txt"
if Path(letter_file).exists():
    letter = load_text(letter_file)
    with st.expander("Click to read my letter ❤️", expanded=False):
        st.write(letter)
else:
    st.info("Add your love letter in content/love_letter.txt")

st.divider()

# ----------------------------
# 5. Cute Quiz (stable + styled)
# ----------------------------
st.markdown('<div class="quiz-title">💖 Cute Quiz For You 💖</div>', unsafe_allow_html=True)
quiz_file = "content/quiz.json"

if Path(quiz_file).exists():
    quiz = load_quiz(quiz_file)

    # lock an order once so questions don't re-order on reruns
    if "quiz_order" not in st.session_state:
        order = list(range(len(quiz)))
        random.shuffle(order)
        st.session_state.quiz_order = order
    order = st.session_state.quiz_order

    # init answer keys (stable keys based on original index)
    for orig_idx in range(len(quiz)):
        key = f"quiz_{orig_idx}"
        if key not in st.session_state:
            st.session_state[key] = None

    # use a form so intermediate interactions don't cause re-runs that disturb layout
    with st.form(key="quiz_form"):
        # quiz wrapper (centered)
        st.markdown('<div class="quiz-wrapper">', unsafe_allow_html=True)

        for display_pos, orig_idx in enumerate(order):
            q = quiz[orig_idx]

            # card with question header (the radio will visually appear right below and styled)
            st.markdown(f'<div class="quiz-card"><div class="question">Q{display_pos+1}. {q["question"]}</div>', unsafe_allow_html=True)

            # some Streamlit versions accept index=None to avoid pre-selection; fallback below if TypeError
            try:
                st.radio("Choose an option:", q["options"], key=f"quiz_{orig_idx}", index=None, label_visibility="collapsed")
            except TypeError:
                # fallback for older streamlit: use selectbox with placeholder and mirror into quiz_{orig_idx}
                choices_with_placeholder = ["-- Select --"] + q["options"]
                sel = st.selectbox("", choices_with_placeholder, key=f"quiz_{orig_idx}_sb")
                if sel == "-- Select --":
                    st.session_state[f"quiz_{orig_idx}"] = None
                else:
                    st.session_state[f"quiz_{orig_idx}"] = sel

            st.markdown("</div>", unsafe_allow_html=True)  # close quiz-card

        st.markdown('</div>', unsafe_allow_html=True)  # close wrapper

        submit_clicked = st.form_submit_button("Submit My Answers 💌")

    # process submission
    if submit_clicked:
        st.session_state.quiz_submitted = True

    if st.session_state.get("quiz_submitted", False):
        score = 0
        total = len(quiz)
        for orig_idx, q in enumerate(quiz):
            user_ans = st.session_state.get(f"quiz_{orig_idx}")
            if user_ans is not None and user_ans == q["answer"]:
                score += 1

        st.markdown(f"### 🎉 You scored **{score}/{total}** 💖")

        if score >= 8:
            st.balloons()
            st.success("Wahh! Tum mujhe itna acche se jaanti ho 😍")
        elif score >= 5:
            st.info("Bahut achha kiya! Tum toh meri jaan ho hi ❤️")
        else:
            st.warning("Aree.. thoda revise karna padega humari kahani 😛")

        if st.button("Restart Quiz 🔁"):
            # Clear quiz keys and order so quiz can be replayed
            for orig_idx in range(len(quiz)):
                st.session_state.pop(f"quiz_{orig_idx}", None)
                st.session_state.pop(f"quiz_{orig_idx}_sb", None)
            st.session_state.pop("quiz_order", None)
            st.session_state.pop("quiz_submitted", None)
            st.rerun()
else:
    st.info("Add your quiz in content/quiz.json")

st.divider()

# ----------------------------
# 6. Final Surprise
# ----------------------------
st.subheader("🎁 Final Surprise")

if st.button("Click here for your surprise 💖"):
    try:
        balloons = load_lottiefile("assets/lottie/balloons.json")
        fireworks = load_lottiefile("assets/lottie/fireworks.json")
        st_lottie(balloons, height=200, key="balloons")
        st_lottie(fireworks, height=300, key="fireworks")
        st.success("Forever yours, Soham ❤️")
    except Exception:
        st.error("Animations missing. Add balloons.json and fireworks.json in assets/lottie/")

