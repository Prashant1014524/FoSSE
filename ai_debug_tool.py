import re
import requests

# ------- Put your actual token with NO spaces before or after
HF_TOKEN = "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"  # <-- Your HuggingFace token here

# ------- Error Patterns -------
error_fix_dict = {
    'unknown subckt': "Add '.include <library_file>' with subcircuit definition at the top of your netlist.",
    'unknown device': "Check the spelling and presence of the device in the netlist/model library.",
    'missing parameter': "Provide all required parameters for your devices (e.g., VGS, L, W for MOSFETs).",
    'floating node': "Ensure all schematic pins are connected; avoid isolated points.",
    'device not found': "Verify that all devices are defined using .model or .subckt in your netlist.",
    'illegal': "Check syntax and ensure your netlist statements match SPICE conventions.",
    'singular matrix': "Likely a floating node or missing ground path. Double-check node connections and grounding.",
    'no such model': "Add or correct the .model statement for this device.",
    'too few nodes': "A component is missing node connections; ensure all components are fully specified.",
    'undefined': "Check spelling and ensure referenced models/nodes/parameters are defined.",
    'open circuit': "A net is unconnected. Check schematic for loose wires or missing links.",
    'division by zero': "Check components for zero value (e.g., resistor/capacitor/inductor = 0 is invalid).",
    'temperature out of range': "Set temperature values within device/model limits.",
    'parameter out of range': "Choose parameter values within recommended device limits.",
    'analysis not possible': "Review simulation setup; may lack voltage source, clock, or valid analysis type.",
    'node not found': "Check spelling/case of node names; must match schematic/netlist exactly.",
    'ac analysis requires small signal model': "Model must support AC analysis; add proper .model or use compatible device.",
    'no such parameter': "Check spelling and ensure parameter is defined in .model/.param statement.",
    'unsupported parameter': "Parameter does not exist for this device. Remove or correct.",
    'not a number': "Numerical parameter is missing or corrupted. Replace text with a valid number.",
    'illegal number of parameters': "Check component line for proper parameter count and order.",
    'nmos not defined': "Include a .model statement for NMOS or load PDK/model library correctly.",
    'could not set up circuit': "Check netlist for syntax errors, missing components or invalid topology.",
    'syntax error': "Check netlist formatting and line breaks; correct as per SPICE syntax.",
    'element name expected': "Line begins without a valid component/device name.",
    'unknown model type': "Refer to device manual; check .model syntax and available types.",
    'analysis setup failure': "Simulation setup is incomplete; check for required sources and valid options.",
    'could not converge': "Simulation failed to converge; adjust tolerances, add initial conditions, or check for circuit errors."
}

# ------- HuggingFace Chatbot (Free AI) -------
def hf_chatbot_response(user_message, hf_token):
    url = "https://api-inference.huggingface.co/models/google/flan-t5-base"
    headers = {"Authorization": f"Bearer {hf_token}"}
    prompt = f"{user_message}\nSuggest a fix for this circuit simulation error."
    payload = {"inputs": prompt}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        output = response.json()
        if isinstance(output, list) and len(output) > 0 and "generated_text" in output[0]:
            return output[0]["generated_text"].strip()
        return str(output)
    except Exception as e:
        return f"Chatbot error: {e}"

# ------- Error Log Analyzer -------
def suggest_fix(line):
    for key, fix in error_fix_dict.items():
        if key in line.lower():
            return fix
    return "Refer to the eSim or ngspice documentation for this error."

def analyze_error_log(log_file):
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
                print("  Suggestion:", suggest_fix(line))
    if not found:
        print("No errors or warnings found in the provided log file.")
    print("=" * 60)

# ------- Netlist Analyzer -------
def parse_netlist(file_path):
    issues = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines, 1):
            tokens = line.strip().split()
            if not tokens or tokens[0].startswith('.'):
                continue
            device = tokens[0].upper()
            if device.startswith(('R', 'C', 'L')) and len(tokens) < 4:
                issues.append((i, line.strip(), "Too few nodes/parameters for resistor/capacitor/inductor. Expected 3 nodes + value."))
            elif device.startswith('M') and len(tokens) < 6:
                issues.append((i, line.strip(), "Too few nodes/parameters for MOSFET. Expected 4 nodes + model + params."))
            elif device.startswith('X') and len(tokens) < 4:
                issues.append((i, line.strip(), "Too few nodes/parameters for subcircuit call."))
    if not issues:
        print("No obvious netlist issues found.")
    else:
        print("=" * 60)
        print("eSim Netlist Analysis Results:")
        print("=" * 60)
        for lineno, line, issue in issues:
            print(f"Line {lineno}: {line}\n  Suggestion: {issue}\n")
        print("=" * 60)

# ------- Main CLI -------
def main():
    print("eSim AI Debugging Tool")
    print("1. Analyze error log (.out)")
    print("2. Analyze netlist file (.cir)")
    print("3. Interactive AI Chatbot (FREE, HuggingFace; enter error or netlist issue)")
    choice = input("Choose option (1/2/3): ").strip()
    if choice == "1":
        file = input("Enter error log filename (e.g. sample_errors.cir.out): ").strip()
        analyze_error_log(file)
    elif choice == "2":
        file = input("Enter netlist filename (e.g. sample_netlist.cir): ").strip()
        parse_netlist(file)
    elif choice == "3":
        hf_token = HF_TOKEN
        print("Type your error or netlist issue (type 'exit' to quit):")
        while True:
            user_text = input(">> ").strip()
            if user_text.lower() == "exit":
                break
            print("AI Suggestion:", hf_chatbot_response(user_text, hf_token))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
