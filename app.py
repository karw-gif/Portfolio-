import streamlit as st

st.set_page_config(
    page_title="Joy Mwenda | Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- LOAD CSS ----------

with open("styles/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# ---------- NAVIGATION ----------

st.markdown("""
<div class="navbar">

<a href="#home">Home</a>

<a href="#about">About</a>

<a href="#projects">Projects</a>

<a href="#skills">Skills</a>

<a href="#certifications">Certifications</a>

<a href="#contact">Contact</a>

</div>
""", unsafe_allow_html=True)

# ===============================
# HERO
# ===============================

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

left,right=st.columns([1,2])

with left:

    st.image(
        "assets/profile.jpg",
        width=260
    )

with right:

    st.markdown("""
<div class="hero-title">

Hi, I'm Joy Mwenda 👋

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="hero-subtitle">

AI | Cybersecurity | Software Development

</div>
""",unsafe_allow_html=True)

    st.write("")

    st.markdown("""
With hands on experience in  developing AI-powered,
cybersecurity, mobile, and web applications.

I enjoy creating intelligent systems that solve real-world challenges through
machine learning, secure software development, and modern technologies.
""")

    c1,c2,c3,c4=st.columns(4)

    with c1:

        with open("assets/resume.pdf","rb") as pdf:

            st.download_button(
                "📄 Resume",
                pdf,
                "Joy_Mwenda_Resume.pdf"
            )

    with c2:

        st.link_button(
            "💻 GitHub",
            "https://github.com/karw-gif"
        )

    with c3:

        st.link_button(
            "💼 LinkedIn",
            "https://linkedin.com/in/joy-karwitha-2640a82b7"
        )

    with c4:

        st.link_button(
            "📧 Email",
            "mailto:mjoykarwitha@gmail.com"
        )

st.write("")
st.divider()

# ===============================
# ABOUT
# ===============================

st.markdown('<div id="about"></div>',unsafe_allow_html=True)

st.markdown("""
<h2 class="section-title">
About Me
</h2>
""",unsafe_allow_html=True)

st.write("""

I'm a final year Computer Science student specializing in Artificial Intelligence, Cybersecurity, and Software Development. I build intelligent applications that enhance security, automate processes, and solve real-world challenges using modern technologies.

My interests lie in developing intelligent applications that improve
security, automate processes, and solve real-world problems.

I'm continuously expanding my expertise in machine learning, cloud
computing, and secure software engineering while building projects that
combine practical software development with emerging technologies.

""")

st.divider()

# ===============================
# HIGHLIGHTS
# ===============================

st.markdown("""
<h2 class="section-title">
Highlights
</h2>
""",unsafe_allow_html=True)

a,b,c=st.columns(3)

with a:

    st.metric(
        "🥇 Cyber Shujaa",
        "First Prize"
    )

with b:

    st.metric(
        "🤖 AI Model Accuracy",
        "90%"
    )

with c:

    st.metric(
        "🚀 Featured Projects",
        "3"
    )

st.divider()

# ===============================
# PROJECTS
# ===============================

st.markdown('<div id="projects"></div>',unsafe_allow_html=True)

st.markdown("""
<h2 class="section-title">

Featured Engineering Projects

</h2>
""",unsafe_allow_html=True)

# HERO PROJECT

st.markdown("""
<div class="project-card">
<h2>🤖 AI Integrated Smart Packet Analyzer</h2>

<p>
An AI-powered intrusion detection system that monitors
network traffic, identifies malicious packet flows,
and explains predictions using Explainable AI.
</p>

</div>
""",unsafe_allow_html=True)

m1,m2,m3,m4=st.columns(4)

m1.metric("Accuracy","90%")
m2.metric("Analysis Modes","3")
m3.metric("Explainable AI","Enabled")
m4.metric("Reports","PDF")

tabs=st.tabs([
"Overview",
"Features",
"Screenshots",
"Technologies",
"Results"
])

with tabs[0]:

    st.write("""

The AI Integrated Smart Packet Analyzer combines Machine Learning,
real-time packet analysis, and Explainable AI to detect malicious
network traffic.

It supports:

• Live Capture

• Offline PCAP Analysis

• Simulation Mode

while providing downloadable analysis reports and model evaluation.

""")

with tabs[1]:

    st.markdown("""

✅ Live Capture Mode

✅ Offline PCAP Mode

✅ Simulation Demo

✅ Explainable AI

✅ Downloadable Reports

✅ Model Evaluation Dashboard

✅ Threat Classification

✅ Interactive Visualizations

""")

with tabs[2]:

    st.subheader("AI Smart Packet Analyzer Screenshots")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "assets/ai/dashboard.png",
            caption="Main Dashboard",
            use_container_width=True
        )

    with col2:
        st.image(
            "assets/ai/xai.png",
            caption="Explainable AI",
            use_container_width=True
        )
           
with tabs[3]:

    st.subheader("Technologies Used")

    tech1, tech2 = st.columns(2)

    with tech1:

        st.markdown("""
### Programming

- Python

### Machine Learning

- XGBoost
- Scikit-learn
- Explainable AI (SHAP)

### Data Processing

- Pandas
- NumPy
""")

    with tech2:

        st.markdown("""
### Network Analysis

- NFStream

### Frontend

- Streamlit

### Development

- Git
- GitHub
- VS Code
""")

with tabs[4]:

    st.success("Final Model Accuracy: 90%")

    st.progress(90)

    st.markdown("""

### Performance Highlights

- Machine Learning accuracy of **90%**

- Supports three network analysis modes

- Explainable AI for transparent predictions

- Downloadable PDF Network Analysis Report

- Dedicated Model Evaluation Dashboard

""")

st.write("")

github1, report = st.columns(2)

with github1:

    st.link_button(
 "💻 View GitHub Repository",
    "https://github.com/karw-gif/AI-Integrated-Smart-Packet-Analyzer-.git"
)

with report:

    st.button("📄 Download Sample Report")

st.divider()

# ===================================
# NOVAMEDIX
# ===================================

st.markdown("""
<div class="project-card">
<h2>🏥 NovaMediX</h2>

<p>
A telemedicine platform developed to improve healthcare accessibility by
enabling appointment booking, emergency assistance, accident reporting,
and health monitoring through a mobile application.
</p>

</div>
""", unsafe_allow_html=True)

left, right = st.columns([1,1])

with left:

    st.image(
        "assets/novamedix/mockup.png",
        use_container_width=True
    )

with right:

    st.subheader("Key Features")

    st.markdown("""

✅ User Authentication

✅ Appointment Booking

✅ Emergency Booking

✅ Accident Reporting

✅ Blood Pressure Monitoring

✅ Responsive Healthcare Website

""")

    st.subheader("Technologies")

    st.markdown("""

- Flutter

- Dart

- HTML5

- CSS3

- Material Design

""")

    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/karw-gif/NovaMedix-.git"
    )

st.divider()

# ===================================
# CAMPUSCONNECT
# ===================================

st.markdown("""
<div class="project-card">
<h2>📱 CampusConnect</h2>

<p>
CampusConnect is a mobile application built with Kotlin that enhances
communication and engagement within universities by delivering
real-time campus events and notifications.
</p>

</div>
""", unsafe_allow_html=True)

st.subheader("Core Features")

st.markdown("""

📅 Event Management

🔔 Push Notifications

☁ Firebase Realtime Database

📱 Material Design Interface

🔒 Reliable Data Synchronization

""")

st.subheader("Technology Stack")

st.markdown("""

- Kotlin

- Android XML

- Firebase Realtime Database

- Firebase Cloud Messaging

- Gradle

""")

st.link_button(
    "💻 GitHub Repository",
    "https://github.com/karw-gif/CampusConnect-_App"
)

st.divider()

# ===================================
# SKILLS
# ===================================

st.markdown('<div id="skills"></div>', unsafe_allow_html=True)

st.markdown("""
<h2 class="section-title">

Skills & Technologies

</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.subheader("🧠 AI & Machine Learning")

    st.markdown("""

- Python

- XGBoost

- Scikit-learn

- Pandas

- NumPy

- Explainable AI

""")

    st.subheader("🛡 Cybersecurity")

    st.markdown("""

- NFStream

- Threat Detection

- Packet Analysis

- Network Analysis

- Intrusion Detection

""")

with col2:

    st.subheader("💻 Software Development")

    st.markdown("""

- Flutter

- HTML5

- CSS3

- JavaScript

- Kotlin

- Git & GitHub

""")

    st.subheader("☁ Cloud")

    st.markdown("""

- Oracle Cloud Infrastructure

- AWS Fundamentals

""")

st.divider()
# ===================================
# CERTIFICATIONS
# ===================================

st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)

st.markdown("""
<h2 class="section-title">
📜 Certifications
</h2>
""", unsafe_allow_html=True)

certifications = [
    "Oracle Cloud Infrastructure 2025 AI Foundations Associate",
    "Certified in Cybersecurity (CC) — ISC2 (In Progress)",
    "Ethical Hacking — Cisco Networking Academy",
    "Threat Management — Cisco Networking Academy",
    "Introduction to Cybersecurity — Cisco Networking Academy",
    "Networking Basics — Cisco Networking Academy",
    "Software Development — Power Learn Project (PLP)"
]

for cert in certifications:
    st.markdown(f"""
    <div class="certificate-card">
        ✅ {cert}
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ===================================
# CONTACT
# ===================================

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

st.markdown("""
<h2 class="section-title">
📬 Let's Connect
</h2>
""", unsafe_allow_html=True)

left, right = st.columns([1,1])

with left:

    st.markdown("""
### Contact Information
""")

    st.write("📧 **Email:** mjoykarwitha@gmail.com")

    st.write("📱 **Phone:** +254 745 856 192")

    st.write("📍 **Location:** Kiambu, Kenya")

    st.write("")

    st.link_button(
        "💻 GitHub",
        "https://github.com/karw-gif"
    )

    st.link_button(
        "💼 LinkedIn",
        "https://linkedin.com/in/joy-karwitha-2640a82b7"
    )

with right:

    st.markdown("""
### Send a Message
""")

    name = st.text_input("Your Name")

    email = st.text_input("Your Email")

    message = st.text_area(
        "Message",
        height=180
    )

    if st.button("Send Message"):

        st.success(
            "Thank you! Your message has been recorded."
        )

st.divider()

# ===================================
# FOOTER
# ===================================

st.markdown("""
<div class="footer">

<h2>Thanks for visiting my portfolio 👋</h2>

<p>

Currently seeking internship opportunities in

<b>Artificial Intelligence</b>,
<b>Cybersecurity</b>,
<b>Software Engineering</b>,
and <b>Cloud Computing</b>.

</p>

<p>

"Great software solves real problems."

</p>

<hr>

<p>

© 2026 Joy Karwitha Mwenda

</p>

</div>
""", unsafe_allow_html=True)

# ===================================
# OPTIONAL SIDEBAR
# ===================================

with st.sidebar:

    st.image(
        "assets/profile.jpg",
        width=120
    )

    st.markdown("## Joy Mwenda")

    st.caption("AI • Cybersecurity • Software Engineering")

    st.divider()

    st.write("### Quick Stats")

    st.metric(
        "Projects",
        "3"
    )

    st.metric(
        "Model Accuracy",
        "90%"
    )

    st.metric(
        "Certifications",
        "7"
    )

    st.divider()

    st.write("### Currently Learning")

    st.write("• AWS")

    st.write("• Advanced Machine Learning")

    st.write("• Cloud Security")

    st.divider()

    st.info(
        "Open to internship opportunities."
    )
