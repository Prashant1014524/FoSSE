import re
import requests

# My HuggingFace token for the AI chatbot (replace with your token)
HF_TOKEN = "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"

# Common error messages and what to do for each
my_error_fixes = {
    'unknown subckt': "Add '.include <library_file>' to include the subcircuit at the top of your netlist.",
    'unknown device': "Check spelling and if the device is present in your model/library.",
    'missing parameter': "Provide all required parameters (e.g. L, W for MOSFETs).",
    'floating node': "Make sure all pins are connected. No unconnected wires.",
    'device not found': "Define all devices using .model or .subckt.",
    'illegal': "Check your netlist syntax according to SPICE rules.",
    'singular matrix': "There's likely a floating node or missing ground. Check connections.",
    'no such model': "Check or add the .model statement for this device.",
    'too few nodes': "A part is missing node connections—check that all parts are connected.",
    'undefined': "Check all names, models, and parameters are defined and spelled right.",
    'open circuit': "There's an unconnected net somewhere.",
    'division by zero': "Don't use zero value for R, C, or L.",
    'temperature out of range': "Use a valid temperature value for your device.",
    'parameter out of range': "Use values recommended for your component.",
    'analysis not possible': "Make sure you have power sources and a valid simulation type.",
    'node not found': "Check spelling and case of all node names.",
    'ac analysis requires small signal model': "Add a suitable .model or use a compatible device for AC.",
    'no such parameter': "Parameter undefined—check .model or .param statements.",
    'unsupported parameter': "Remove or fix unrecognized parameters.",
    'not a number': "All number values must be valid, not text.",
    'illegal number of parameters': "Check parameter count/order for components.",
    'nmos not defined': "Add or include a .model for NMOS.",
    'could not set up circuit': "Check for errors in topology or missing parts.",
    'syntax error': "Check netlist lines and break them up if needed.",
    'element name expected': "Component/devices must have a valid name at line start.",
    'unknown model type': "Check .model syntax and type from manual.",
    'analysis setup failure': "Simulation setup incomplete—are sources and options set correctly?",
    'could not converge': "Try changing tolerances or adding initial conditions."
}

# ---------------------- AI Chatbot Function ----------------------
def get_ai_suggestion(msg, token):
    url = "https://api-inference.huggingface.co/models/google/flan-t5-base"
    headers = {"Authorization": f"Bearer {token}"}
    prompt = f"{msg}\nSuggest a fix for this circuit simulation error."
    try:
        resp = requests.post(url, headers=headers, json={"inputs": prompt}, timeout=30)
        data = resp.json()
        if isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
            return data[0]["generated_text"].strip()
        return str(data)
    except Exception as e:
        return f"AI Chatbot error: {e}"

# ---------------------- Error Log Analyzer ----------------------
def check_error_log(log_file):
    print("=" * 60)
    print("eSim Error Log Debugging Results:")
    print("=" * 60)
    found = False
    with open(log_file, 'r') as f:
        for i, line in enumerate(f, 1):
            if re.search(r'(error|warning|fatal|fail)', line, re.IGNORECASE):
                found = True
                print(f"\nLog line {i}:")
                print("  Message:", line.strip())
                print("  Suggestion:", get_rule_suggestion(line))
    if not found:
        print("No errors or warnings found in the provided log file.")
    print("=" * 60)

def get_rule_suggestion(line):
    for key, fix in my_error_fixes.items():
        if key in line.lower():
            return fix
    return "Check eSim/ngspice documentation or try the AI chatbot for this error."

# ---------------------- Netlist Analyzer ----------------------
def check_netlist(file_path):
    faults = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines, 1):
            parts = line.strip().split()
            if not parts or parts[0].startswith('.'):
                continue
            device = parts[0].upper()
            if device.startswith(('R', 'C', 'L')) and len(parts) < 4:
                faults.append((i, line.strip(), "Too few nodes/parameters for resistor/capacitor/inductor. Needed: 3 nodes + value."))
            elif device.startswith('M') and len(parts) < 6:
                faults.append((i, line.strip(), "Too few nodes/parameters for MOSFET. Needed: 4 nodes + model + params."))
            elif device.startswith('X') and len(parts) < 4:
                faults.append((i, line.strip(), "Too few nodes/parameters for subcircuit call."))
    if not faults:
        print("No obvious netlist mistakes found.")
    else:
        print("=" * 60)
        print("eSim Netlist Analysis Results:")
        print("=" * 60)
        for lineno, line, problem in faults:
            print(f"Line {lineno}: {line}\n  Suggestion: {problem}\n")
        print("=" * 60)

# ---------------------- Main Menu ----------------------
def main():
    print("eSim AI Debugging Tool by Prashant")
    print("1. Analyze error log (.out)")
    print("2. Analyze netlist file (.cir)")
    print("3. Chatbot: Get AI help for any error or netlist issue (HuggingFace)")
    choice = input("Choose option (1/2/3): ").strip()
    if choice == "1":
        fname = input("Enter error log filename (e.g. sample_errors.cir.out): ").strip()
        check_error_log(fname)
    elif choice == "2":
        fname = input("Enter netlist filename (e.g. sample_netlist.cir): ").strip()
        check_netlist(fname)
    elif choice == "3":
        print("Type your error or netlist issue (type 'exit' to quit):")
        while True:
            user_text = input(">> ").strip()
            if user_text.lower() == "exit":
                break
            print("AI Suggestion:", get_ai_suggestion(user_text, HF_TOKEN))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
