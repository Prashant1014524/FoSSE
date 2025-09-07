# **eSim AI Debugging Tool**

## **Overview**

The **eSim AI Debugging Tool** is a Python-based platform designed to help users debug electronic circuit netlists and simulation error logs for projects in eSim, ngspice, or similar EDA tools.

It combines powerful **rule-based suggestions** with an integrated **AI chatbot (using HuggingFace)** for interactive, human-like troubleshooting.

---

## **Features**

- **Rule-Based Error & Netlist Analysis**
  - Instantly analyzes `.cir` netlist and `.out` simulation log files.
  - Provides clear, actionable suggestions for common issues (missing nodes, bad syntax, undefined devices, etc.)

- **Integrated AI Chatbot (HuggingFace)**
  - **FREE**, no credit card required!
  - Ask any error message or netlist question and receive real-time, conversational advice.
  - Makes debugging more accessible—even for new or rarely-seen errors!

- **Modular, Extensible Code**
  - Easy to add new error patterns or analysis rules.
  - Cleanly separated functions for maintainability and scaling.

- **Beginner-Friendly Interface**
  - No advanced setup required.
  - Includes sample netlist and log files for testing/demo.
 

  
---

## **Extending and Customizing**

- Add your own rules for error detection in the `error_fix_dict` dictionary.
- To collect user error history for personalization, add a simple log file or database.
- You can swap the language model for more advanced HuggingFace models, or add OpenAI integration if you have an API key.

---
## **pip install requests
3. **Download this repository** (or copy the all-in-one script and sample files).
4. **Get your free HuggingFace API token:**
- Sign up at [https://huggingface.co/](https://huggingface.co/)
- Go to **Settings → Access Tokens → Create new token** (choose "read")
- Copy the token (starts with `hf_...`)
5. **Paste your token:**
- Replace the value in `HF_TOKEN = "hf_..."` at the top of the script.

---

## **Usage**

You’ll see a menu:


- **Option 1:** Analyze and get suggestions for a `.out` error log file.
- **Option 2:** Analyze a `.cir` netlist for missing parameters and other structural bugs.
- **Option 3:** Chat interactively with the AI—just type or paste any error message, and get a suggested fix immediately.

---

## **Sample Files**

- `sample_errors.cir.out`
- `sample_netlist.cir`

You can also create your own eSim test files and apply the tool as well.

---

## **Example Interaction**



---

## **Extending and Customizing**

- Add your own rules for error detection in the `error_fix_dict` dictionary.
- To collect user error history for personalization, add a simple log file or database.
- You can swap the language model for more advanced HuggingFace models, or add OpenAI integration if you have an API key.

---

## **Design, Quality, and Submission Notes**

**Meets all FOSSEE/eSim internship screening requirements:**
- Netlist and log analysis
- Useful suggestions for various errors
- AI/ML chatbot integration
- Extensible, well-documented design
- Sample files and user documentation provided

**Creativity:**
- The hybrid rule-based + AI chatbot approach ensures advice is always available, even when new errors appear.

---

## **Author / Credits**

Developed by **Prashant** for the eSim Semester Long Internship Autumn 2025  
Mentor: **FOSSEE eSim team**

---

**Thank You**



