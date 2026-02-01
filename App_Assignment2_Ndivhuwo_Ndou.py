# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 22:37:55 2026

@author: Ndivhuwo.Ndou
"""

import streamlit as st
import pandas as pd

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Research Profile | Dr Ndivhuwo Ndou",
    page_icon="📘",
    layout="wide"
)

# ------------------ SIDEBAR ------------------
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Profile",
        "Education",
        "Certificates",
        "Experience",
        "Teaching",
        "Administration",
        "Research",
        "Supervision",
        "Publications",
        "Grants",
        "Skills",
        "References"
    ]
)

# ------------------ HEADER ------------------
st.title("Research Profile")
st.subheader("Dr Ndivhuwo Ndou")

st.markdown("""
**Lecturer | Applied Mathematics | Data Science**  
University of Venda, South Africa  

📧 ndivhuwo.ndou@univen.ac.za  
🔗 [Google Scholar](https://scholar.google.com/citations?user=6QvTXAMAAAAJ&hl=en)  
🔗 [ORCID](https://orcid.org/0000-0002-0515-344X)  
🔗 [GitHub](https://github.com/ndoundivhuwo)
""")

st.divider()

# ------------------ PROFILE ------------------
if section == "Profile":
    st.header("👤 Profile")
    st.write("""
I am a Lecturer in the Department of Mathematical and Computational Sciences
at the University of Venda. My research interests include **numerical analysis,
finite difference methods, computational fluid dynamics, and machine learning
applications to PDEs**.
    """)

# ------------------ EDUCATION ------------------
elif section == "Education":
    st.header("🎓 Educational Qualifications")

    data = [
        ["2020–2024", "PhD Applied Mathematics", "University of Johannesburg"],
        ["2016–2018", "MSc Applied Mathematics", "University of Venda"],
        ["2014–2015", "BSc Honours Applied Mathematics", "University of Venda"],
        ["2011–2013", "BSc Mathematics & Physics", "University of Venda"],
    ]

    df = pd.DataFrame(data, columns=["Period", "Qualification", "Institution"])
    st.table(df)

    st.markdown("""
**PhD Thesis:**  
*Solving Advection Diffusion Reaction Equations Using Families of Finite Difference Methods*  
[Thesis Link](https://hdl.handle.net/10210/517998)
""")

# ------------------ CERTIFICATES ------------------
elif section == "Certificates":
    st.header("📜 Certificates & Training")

    st.markdown("""
- Certificate in Data Science with Python – University of Cape Town  
- MATLAB Onramp, Optimization Onramp, ODEs with MATLAB  
- WOCCO Computational Mathematics Workshop  
- NASSP Winter School  
- AIMS Mathematics & Computing Workshops
""")

# ------------------ EXPERIENCE ------------------
elif section == "Experience":
    st.header("💼 Professional Experience")

    st.markdown("""
**Lecturer** – University of Venda *(2021–Present)*  
**Junior Lecturer** – University of Venda *(2019–2021)*  
**Educator** – TVET College *(2018–2019)*  
**Intern & Tutor** – University of Venda *(2013–2016)*
""")

# ------------------ TEACHING ------------------
elif section == "Teaching":
    st.header("📘 Modules Taught")

    modules = [
        "Numerical Analysis",
        "Vector Analysis",
        "Financial Mathematics",
        "Engineering Mathematics",
        "ODEs (Honours)",
        "Programming (Honours)",
        "Stability & Optimization (Honours)"
    ]

    for m in modules:
        st.markdown(f"- {m}")

# ------------------ ADMINISTRATION ------------------
elif section == "Administration":
    st.header("🏛 University Administrative Duties")

    st.markdown("""
- Chairperson: Departmental Timetable Committee  
- Faculty Champion: Research Open Day  
- Honours Coordinator (Applied Mathematics)  
- Procurement & Purchasing Officer  
- Curriculum Review Committee Member
""")

# ------------------ RESEARCH ------------------
elif section == "Research":
    st.header("🔬 Research Interests")

    st.markdown("""
- Advection–Diffusion–Reaction Equations  
- Finite Difference Methods  
- Computational Fluid Dynamics  
- Machine Learning for PDEs  
- Numerical Stability & Positivity Preservation
""")

# ------------------ SUPERVISION ------------------
elif section == "Supervision":
    st.header("🎓 Postgraduate Supervision")

    st.markdown("""
- **12 Honours projects** completed  
- **3 MSc students** currently supervised  
- Research areas: PDEs, Machine Learning, Computational Mathematics
""")

# ------------------ PUBLICATIONS ------------------
elif section == "Publications":
    st.header("📚 Selected Publications")

    st.markdown("""
1. Ndou N. et al. *Axioms* (2024)  
2. Ndou N. et al. *Mathematics* (2024)  
3. Ndou N. et al. *Mathematics* (2022)  
4. Hocking G. et al. *PDEs in Applied Mathematics* (2025)
""")

    st.markdown("[Full Google Scholar Profile](https://scholar.google.com/citations?user=6QvTXAMAAAAJ&hl=en)")

# ------------------ GRANTS ------------------
elif section == "Grants":
    st.header("💰 Grants & Funding")

    grant_data = [
        ["NRF", "R160 000", "MSc Funding"],
        ["Capacity Development Grant", "R125 000", "PhD Research"],
        ["Community Engagement Grant", "R98 000", "Maths Olympiad"],
        ["Research Incentives", "R31 878", "Publications"],
    ]

    df = pd.DataFrame(grant_data, columns=["Grant", "Amount", "Purpose"])
    st.dataframe(df, use_container_width=True)

# ------------------ SKILLS ------------------
elif section == "Skills":
    st.header("🛠 Technical Skills")

    st.markdown("""
**Programming & Software**
- Python, MATLAB, Mathematica
- LaTeX, MS Office

**Platforms**
- Moodle, Blackboard, Microsoft Teams

**Operating Systems**
- Windows, Linux
""")

# ------------------ REFERENCES ------------------
elif section == "References":
    st.header("📞 References")

    st.markdown("""
**Dr Kizito Muzhinji**  
Senior Lecturer, University of Venda  
📧 kizito.muzhinji@univen.ac.za  

**Dr Vhutshilo Nekhubvi**  
Senior Lecturer, University of Venda  
📧 vhutshilo.nekhubvi@univen.ac.za  

**Dr Simiso Moyo**  
Former HoD, University of Venda  
📧 misomoyo60@gmail.com
""")

# ------------------ FOOTER ------------------
st.divider()
st.caption("© Dr Ndivhuwo Ndou | Academic CV | Built with Streamlit")
