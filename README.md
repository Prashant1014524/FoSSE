eSim AI Debugging Tool
Overview
The eSim AI Debugging Tool is a Python-based platform designed to help users debug electronic circuit netlists and simulation error logs for projects in eSim/ngspice or similar EDA tools.
It combines powerful rule-based suggestions with an integrated AI chatbot (using HuggingFace) for interactive, human-like troubleshooting.

##Features
Rule-Based Error & Netlist Analysis:

Instantly analyzes .cir netlist and .out simulation log files.

Provides clear, actionable suggestions for common issues (missing nodes, bad syntax, undefined devices, etc.)

Integrated AI Chatbot (HuggingFace):

FREE, no credit card required!

Ask any error message or netlist question and receive real-time, conversational advice.

Makes debugging more accessible—even for new or rarely-seen errors!

Modular, extensible code:

Easy to add new error patterns or analysis rules.

Cleanly separated functions for maintainability and scaling.

Beginner-friendly interface:

No advanced setup required.

Includes sample netlist and log files for testing/demo.

Installation & Getting Started
Python 3.7 or newer required.

Install dependencies:

text
pip install requests
Download this repository (or copy the all-in-one script and sample files).

Get your free HuggingFace API token:

Sign up at https://huggingface.co/

Go to Settings → Access Tokens → Create new token (choose "read")

Copy token (starts with hf_...)

Paste your token:

Replace the value in HF_TOKEN = "hf_..." at the top of the script.

Usage
bash
python ai_debug_tool_with_hfchatbot.py
You’ll see a menu:

text
eSim AI Debugging Tool
1. Analyze error log (.out)
2. Analyze netlist file (.cir)
3. Interactive AI Chatbot (FREE, HuggingFace; enter error or netlist issue)
Choose option (1/2/3):
Option 1: Analyze and get suggestions for a .out error log file.
Option 2: Analyze a .cir netlist for missing parameters and other structural bugs.
Option 3: Chat interactively with the AI—just type or paste any error message, and get a suggested fix immediately.

Sample Files
sample_errors.cir.out

sample_netlist.cir

You can create your own eSim test files and apply the tool as well.

Example Interaction
text
>> Error: unknown subckt: opamp
AI Suggestion: Add an .include statement for the opamp subcircuit in your netlist, or check that the subcircuit is defined above.
text
>> Warning: floating node detected at N002
AI Suggestion: Make sure all nodes are connected in your schematic and there are no unconnected pins at N002.
Extending and Customizing
Add your own rules for error detection in the error_fix_dict dictionary.

To collect user error history for personalization, add a simple log file or database.

You can swap the language model for more advanced HuggingFace models, or add OpenAI integration if you have an API key.

Design, Quality, and Submission Notes
Meets all FOSSEE/eSim internship screening requirements:

Netlist and log analysis

Useful suggestions for various errors

AI/ML chatbot integration

Extensible, well-documented design

Sample files and user documentation provided

Creativity:
The hybrid rule-based + AI chatbot approach ensures advice is always available, even when new errors appear.\

Author / Credits
Developed by [Prashant] for the eSim Semester Long Internship Autumn 2025
Mentor: FOSSEE eSim team

