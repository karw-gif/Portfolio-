# Portfolio

This is a beautiful, professional, and interactive portfolio application built using Streamlit and custom CSS styling.

## Portfolio Structure

```text
portfolio/
│
├── app.py                  # Streamlit application entrypoint
├── requirements.txt        # Application dependencies
├── README.md               # Documentation
│
├── assets/                 # Profile, resume, and project screenshot assets
│   ├── profile.jpg         # Profile picture
│   ├── resume.pdf          # Professional Resume
│   │
│   ├── ai/                 # AI Intrusion Detector Screenshots
│   │   ├── dashboard.png   # Simulator dashboard
│   │   └── xai.png         # Explainable AI/Model Evaluation report
│   │
│   ├── novamedix/          # NovaMediX project assets
│   │   └── mockup.png      # NovaMediX mobile app UI mockup
│   │
│   └── campusconnect/      # CampusConnect project assets
│       └── mockup.png      # CampusConnect mobile app UI mockup
│
└── styles/
    └── style.css           # Custom CSS styling for premium look & feel
```

## How to Run

1. Clone or copy this folder structure to your machine.
2. Install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
4. Open the displayed URL in your browser to view the portfolio.
