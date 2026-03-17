# COMP1797: Wireless and Mobile Technologies
## Coursework Logbook

**Student Name:** [Insert Name]  
**Student ID:** [Insert ID]  
**Module:** COMP1797: Wireless and Mobile Technologies  
**Academic Year:** [Insert Year]  
**Instructor:** [Insert Instructor Name]  

---

## Introduction

This logbook provides a structured record of my practical and theoretical learning throughout the COMP1797 module. Its purpose is to document the development of my understanding across laboratory exercises and quizzes, while also reflecting on technical progress and areas for improvement.

The module covers core principles of wireless and mobile technologies, including cellular communication, wireless sensor networks (WSNs), cyber-physical systems (CPS), and network security. Through hands-on lab tasks and knowledge-based quizzes, I developed both conceptual understanding and applied technical skills relevant to modern communication systems.

---

## Weekly and Task-Based Record

### Week 1 - Lab 1
**Lab Title:** Introduction to Wireless Communication Fundamentals  
**Objective:** To understand the basic architecture of wireless systems and compare guided versus unguided transmission media.  
**Description of Task:** I reviewed key communication concepts (frequency, bandwidth, latency, and signal attenuation), examined wireless standards, and completed short practical activities involving basic signal calculations and link-budget interpretation.  
**Tools/Technologies Used:** Lecture slides, MATLAB/Python for simple calculations, online spectrum references.  
**Results/Observations:** I was able to identify how propagation loss increases with distance and frequency, and I observed that wireless link quality is highly environment-dependent.  
**Reflection:** This lab established foundational terminology and concepts used throughout the module. The main challenge was interpreting technical parameters in practical terms, but repeated worked examples improved my confidence.

### Week 2 - Lab 2
**Lab Title:** Cellular Communication and Mobility Management  
**Objective:** To understand cellular network structure, handover mechanisms, and frequency reuse.  
**Description of Task:** I analyzed a simplified cellular deployment model, studied cell splitting and sectoring, and reviewed mobility events such as handover and location update procedures.  
**Tools/Technologies Used:** Cellular planning diagrams, simulation worksheets, network architecture notes (2G/3G/4G/5G overview).  
**Results/Observations:** I observed that reducing cell size can improve capacity but also increases handover overhead. I also identified trade-offs between coverage, interference, and quality of service.  
**Reflection:** I understood the relationship between user mobility and network control signaling more clearly. The most difficult part was balancing theoretical equations with real deployment constraints.

### Week 3 - Lab 3
**Lab Title:** Wireless Sensor Networks: Node Deployment and Performance Metrics  
**Objective:** To evaluate WSN behavior under different node densities and measure performance outcomes.  
**Description of Task:** I implemented a WSN simulation in Python for a 100m x 100m area with a central base station. I tested three densities (10, 50, and 100 nodes), ran repeated iterations, and calculated average energy consumption and packet delivery ratio (PDR).  
**Tools/Technologies Used:** Python, NumPy, Matplotlib.  
**Results/Observations:** Results showed stable average per-node energy near similar values across densities and PDR converging around the expected geometric coverage ratio for the chosen success threshold.  
**Reflection:** This lab strengthened my data analysis and simulation skills. A key challenge was ensuring reproducibility and correctly averaging results over multiple iterations.

### Week 4 - Lab 4
**Lab Title:** Cyber-Physical Systems and Real-Time Data Flow  
**Objective:** To understand CPS architecture and timing constraints in sensor-actuator systems.  
**Description of Task:** I modeled a simple CPS pipeline: sensing, communication, processing, and actuation. I examined timing delays, packet loss effects, and control reliability under constrained wireless links.  
**Tools/Technologies Used:** CPS design diagrams, event-timing tables, Python-based latency calculations.  
**Results/Observations:** I observed that small communication delays can propagate into significant control instability when feedback loops require strict timing. Reliability and bounded latency were critical for safe operation.  
**Reflection:** I gained a stronger understanding of why CPS design must integrate communication and control jointly. The challenge was linking networking metrics to physical system behavior.

### Week 5 - Lab 5
**Lab Title:** Wireless Network Security and Threat Mitigation  
**Objective:** To evaluate common wireless threats and identify practical defense mechanisms.  
**Description of Task:** I studied attack scenarios including eavesdropping, spoofing, replay, and denial-of-service in wireless contexts. I then mapped each threat to mitigation strategies such as encryption, authentication, key management, and intrusion monitoring.  
**Tools/Technologies Used:** Security case studies, protocol analysis notes, risk assessment matrix.  
**Results/Observations:** I found that multi-layer security is essential because no single mechanism is sufficient. Strong authentication and proper key handling significantly reduce attack surface.  
**Reflection:** This lab improved my awareness of security-by-design principles. The main challenge was assessing how to balance security overhead with performance in constrained wireless environments.

---

## Quiz Record

### Quiz 1
**Topic:** Wireless Communication Basics  
**Content Covered:** Spectrum use, modulation overview, propagation effects, and signal quality metrics.  
**What I Learned:** I consolidated core terminology and improved my ability to interpret communication scenarios using technical vocabulary.  
**Reflection on Performance:** Performance was satisfactory; I answered conceptual questions well but need faster recall of formula-based definitions.

### Quiz 2
**Topic:** Cellular Networks and Handover  
**Content Covered:** Cell architecture, reuse patterns, mobility management, and handover triggers.  
**What I Learned:** I developed clearer understanding of how mobility influences resource allocation and continuity of service.  
**Reflection on Performance:** I performed well on architecture questions but made minor errors in applying reuse calculations under time pressure.

### Quiz 3
**Topic:** Wireless Sensor Networks  
**Content Covered:** WSN topologies, base station communication, energy models, and packet delivery metrics.  
**What I Learned:** I improved in interpreting WSN performance outputs and understanding the impact of spatial node distribution on reliability.  
**Reflection on Performance:** Results were strong overall. I need to improve precision when explaining assumptions in simulation-based questions.

### Quiz 4
**Topic:** Cyber-Physical Systems  
**Content Covered:** CPS components, feedback loops, timing constraints, and reliability considerations.  
**What I Learned:** I learned how communication delay and packet loss directly affect control quality in physical systems.  
**Reflection on Performance:** Performance was good, though I need deeper practice in analyzing failure propagation in multi-stage CPS pipelines.

### Quiz 5
**Topic:** Wireless Security  
**Content Covered:** Threat models, encryption fundamentals, authentication methods, and secure protocol practices.  
**What I Learned:** I strengthened my understanding of practical defenses and the importance of layered security in wireless environments.  
**Reflection on Performance:** I performed consistently and showed improved analytical reasoning; however, I should revise specific protocol details for full accuracy.

---

## Screenshots of Quiz Results

[Insert Screenshot of Quiz 1 Result Here]

[Insert Screenshot of Quiz 2 Result Here]

[Insert Screenshot of Quiz 3 Result Here]

[Insert Screenshot of Quiz 4 Result Here]

[Insert Screenshot of Quiz 5 Result Here]

---

## Conclusion

Overall, this module provided a comprehensive understanding of wireless and mobile technologies through integrated theory and practice. I developed skills in analyzing wireless communication systems, modeling WSN performance, evaluating CPS timing behavior, and assessing security risks in mobile environments.

The combination of laboratory exercises and quizzes strengthened both my technical competency and academic reporting ability. I can now approach wireless system problems with improved analytical structure, evidence-based reasoning, and clearer awareness of engineering trade-offs between performance, reliability, and security.
