import streamlit as st
import base64

# ---------- BACKGROUND ----------
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)),
                              url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("workshop.png")

# ---------- SESSION STATE ----------
if "level" not in st.session_state:
    st.session_state.level = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "perfect" not in st.session_state:
    st.session_state.perfect = True

if "mode" not in st.session_state:
    st.session_state.mode = "Learn Mode"

# ---------- STYLE ----------
st.markdown(
    """
    <style>
    .block-container {
        background-color: rgba(0, 0, 0, 0.30);
        padding: 2rem;
        padding-top: 120px;
        border-radius: 12px;
        backdrop-filter: blur(6px);
    }

    h1, h2, h3, p, label, div {
        color: white !important;
    }

    div.stButton > button {
        background-color: #d4a017;
        color: black !important;
        border-radius: 10px;
        height: 3em;
        width: 240px;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write(f"⭐ Score: {st.session_state.score}")
st.write("**Bezalel:** Every detail matters. This is sacred work.")

# ---------- HELPER ----------
def wrong_answer():
    st.session_state.perfect = False
    st.warning("Not quite. Try again or review the Builder Notes.")

# =========================================================
# START SCREEN
# =========================================================
if st.session_state.level == 0:

    st.title("The Ark of the Covenant: Build and Learn")
    st.write("Step into Bezalel’s workshop and follow the Bible’s instructions to build and understand the Ark of the Covenant.")

    st.session_state.mode = st.radio(
        "Choose your game mode:",
        ["Learn Mode", "Challenge Mode"],
        index=0
    )

    if st.session_state.mode == "Learn Mode":
        st.info("Learn Mode includes Scripture, images, and Builder Notes.")
    else:
        st.warning("Challenge Mode still teaches, but you are trying for a Perfect Run!")

    if st.button("Start Game"):
        st.session_state.level = 1
        st.session_state.score = 0
        st.session_state.perfect = True
        st.rerun()

# =========================================================
# LEVEL 1 — ACACIA WOOD
# =========================================================
elif st.session_state.level == 1:

    st.subheader("Level 1: The Right Material")

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        st.info("Make an ark of acacia wood. — Exodus 25:10")

        choice = st.radio(
            "Which material should Bezalel use first?",
            ["Acacia wood", "Iron", "Clay", "Pine wood"],
            index=None
        )

        if st.button("Check Answer"):
            if choice is None:
                st.warning("Choose an answer.")
            elif choice == "Acacia wood":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.level = 2
                st.rerun()
            else:
                wrong_answer()

    with col2:
        st.image("acacia wood.jpg", caption="Preparing the wood for the Ark")

    with col3:
        st.markdown("### Builder Notes")
        st.caption("Acacia wood: Strong, durable wood used for sacred furniture.")
        st.caption("Iron: Strong, but not the commanded material.")
        st.caption("Clay: Useful for pottery, but too weak for this purpose.")
        st.caption("Pine wood: Common wood, but not what was commanded.")

# =========================================================
# LEVEL 2 — GOLD OFFERING
# =========================================================
elif st.session_state.level == 2:

    st.subheader("Level 2: The Gold Offering")

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        st.info("All whose hearts moved them brought articles of gold. — Exodus 35:22")

        choice = st.radio(
            "Where did the gold come from?",
            [
                "It appeared by itself",
                "The people brought it as an offering",
                "It was taken from another nation",
                "It was found in the ground"
            ],
            index=None
        )

        if st.button("Continue"):
            if choice is None:
                st.warning("Choose an answer.")
            elif choice == "The people brought it as an offering":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.level = 3
                st.rerun()
            else:
                wrong_answer()

    with col2:
        st.image("gold.jpg", caption="Gold brought as an offering")

    with col3:
        st.markdown("### Builder Notes")
        st.caption("Offering: The people gave willingly for the work.")
        st.caption("Appeared by itself: Not what happened here.")
        st.caption("Taken from another nation: Not the correct answer.")
        st.caption("Found in the ground: Gold can be mined, but this step is about giving.")

# =========================================================
# LEVEL 3 — GOLD OVERLAY
# =========================================================
elif st.session_state.level == 3:

    st.subheader("Level 3: Overlay with Gold")

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        st.info("You shall overlay it with pure gold, inside and out. — Exodus 25:11")

        choice = st.radio(
            "What should Bezalel do next?",
            [
                "Wrap it in cloth",
                "Paint it blue",
                "Overlay it with pure gold",
                "Leave it as wood"
            ],
            index=None
        )

        if st.button("Finish Gold Level"):
            if choice is None:
                st.warning("Choose an answer.")
            elif choice == "Overlay it with pure gold":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.level = 4
                st.rerun()
            else:
                wrong_answer()

    with col2:
        st.image("gold.png", caption="Overlaying and refining the Ark with gold")

    with col3:
        st.markdown("### Builder Notes")
        st.caption("Gold overlay: The Ark was covered with pure gold inside and out.")
        st.caption("Paint it blue: Blue was used elsewhere, but not as paint for the Ark.")
        st.caption("Wrap it in cloth: The Ark was covered for transport, not construction.")
        st.caption("Leave it as wood: The work would not be complete.")

# =========================================================
# LEVEL 4 — MERCY SEAT
# =========================================================
elif st.session_state.level == 4:

    st.subheader("Level 4: The Mercy Seat")

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        st.info("You shall make a mercy seat of pure gold. — Exodus 25:17–20")

        choice = st.radio(
            "Which sacred piece was placed above the Ark of the Covenant?",
            [
                "A cloth covering",
                "A wooden lid",
                "The Mercy Seat with cherubim",
                "A crown of bronze"
            ],
            index=None
        )

        if st.button("Continue"):
            if choice is None:
                st.warning("Choose an answer.")
            elif choice == "The Mercy Seat with cherubim":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.level = 5
                st.rerun()
            else:
                wrong_answer()

    with col2:
        st.image("mercy_seat.jpg", caption="The Mercy Seat with cherubim above the Ark")

    with col3:
        st.markdown("### Builder Notes")
        st.caption("Mercy Seat: The pure gold cover placed above the Ark.")
        st.caption("Cherubim: Angelic figures with wings stretched upward.")
        st.caption("Wooden lid: Not correct.")
        st.caption("Bronze crown: Not the commanded piece.")

# =========================================================
# LEVEL 5 — CONTENTS OF THE ARK
# =========================================================
elif st.session_state.level == 5:

    st.subheader("Level 5: What Was Connected with the Ark")

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        st.info("A golden jar holding the manna, Aaron’s rod which budded, and the tablets of the covenant. — Hebrews 9:4")

        choice = st.radio(
            "Which items were connected with the Ark of the Covenant?",
            [
                "Bread, incense, and sandals",
                "Coins, oil, and a crown",
                "Scrolls, stones, and a sword",
                "Tablets, manna, and Aaron’s rod"
            ],
            index=None
        )

        if st.button("Continue"):
            if choice is None:
                st.warning("Choose an answer.")
            elif choice == "Tablets, manna, and Aaron’s rod":
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.level = 6
                st.rerun()
            else:
                wrong_answer()

    with col2:
        st.image("ark_contents.jpg", caption="The contents connected with the Ark")

    with col3:
        st.markdown("### Builder Notes")
        st.caption("Tablets: God’s covenant commandments.")
        st.caption("Manna: God’s provision in the wilderness.")
        st.caption("Aaron’s rod: God’s chosen leadership.")
        st.caption("Other choices: Not listed as the Ark’s contents.")

# =========================================================
# BONUS LEVEL — HOLY OF HOLIES (ENHANCED)
# =========================================================
elif st.session_state.level == 6:

    st.subheader("Final Level: The Most Holy Place")

    st.markdown(
        """
        ✨ The work is complete.

        The Ark has been built exactly as instructed.

        Now, where will it rest?
        """
    )

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col1:
        st.info("Exodus 26:33 — The veil shall separate for you the holy place from the most holy.")

        choice = st.radio(
            "Where was the Ark of the Covenant placed?",
            [
                "The courtyard",
                "The entrance of the tent",
                "The Holy of Holies",
                "Outside the camp"
            ],
            index=None
        )

        if st.button("Place the Ark"):
            if choice is None:
                st.warning("Choose an answer.")
            elif choice == "The Holy of Holies":
                st.success("Correct.")

                st.session_state.score += 1
                st.session_state.level = 7

                st.balloons()

                st.write("✨ The Ark has been placed in the Most Holy Place.")

                st.rerun()
            else:
                st.session_state.perfect = False
                st.warning("Not quite. This place was set apart above all others.")

    with col2:
        st.image("holy_of_holies.jpg", caption="The Ark in the Most Holy Place (artist’s rendering)")

    with col3:
        st.markdown("### Builder Notes")
        st.caption("Holy of Holies: The most sacred place in the Tabernacle.")
        st.caption("Only the high priest could enter, and only once a year.")
        st.caption("This is where God's presence was revealed above the Mercy Seat.")
# =========================================================
# FINAL SCREEN — ENHANCED
# =========================================================
elif st.session_state.level == 7:

    st.success("🏆 You completed The Ark of the Covenant: Build and Learn!")

    st.write(f"Final Score: {st.session_state.score} out of 6")

    if st.session_state.perfect:
        st.success("🌟 Perfect Run! Every step was completed with precision.")
        st.balloons()
    else:
        st.info("Well done. Try again for a Perfect Run.")

    st.markdown("### What You Built")

    st.write("• Acacia wood — strength and endurance")
    st.write("• Gold overlay — purity and holiness")
    st.write("• Mercy Seat — the place of atonement")
    st.write("• Sacred contents — covenant, provision, and leadership")
    st.write("• Holy of Holies — the dwelling place of God’s presence")

    st.markdown("### Final Reflection")

    st.write(
        "The Ark of the Covenant was not just a sacred object. "
        "It represented God's presence among His people, His covenant, "
        "and His holiness."
    )

    st.write("🙏 You have followed the instructions faithfully.")
    
    st.caption("© 2026 Debbie Strauch. All rights reserved.")