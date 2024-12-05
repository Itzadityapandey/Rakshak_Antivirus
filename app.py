from flask import Flask, render_template, request
import os
import hashlib

app = Flask(__name__)

# Malware signatures
MALWARE_SIGNATURES = set()  # Use a set for faster lookups

def load_signatures(file_path):
    """
    Load malware signatures into a set for quick lookups.
    """
    try:
        with open(file_path, 'r') as f:
            for line in f:
                hash_value = line.strip()  # Remove whitespace or newline characters
                if hash_value:  # Ensure no blank lines
                    MALWARE_SIGNATURES.add(hash_value)
        print(f"Loaded {len(MALWARE_SIGNATURES)} malware signatures.")
    except FileNotFoundError:
        print(f"Signature file not found: {file_path}")
    except Exception as e:
        print(f"Error loading signatures: {e}")

def calculate_hash(file_path):
    """
    Calculate the MD5 hash of a file.
    """
    try:
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None

def scan_directory(directory):
    """
    Scan a directory for files matching malware signatures.
    """
    infected_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            if file_hash and file_hash in MALWARE_SIGNATURES:
                infected_files.append(file_path)
    return infected_files

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Flask route for the home page.
    """
    if request.method == "POST":
        directory = request.form.get("directory")
        if os.path.isdir(directory):
            infected_files = scan_directory(directory)
            return render_template("result.html", infected_files=infected_files)
        else:
            return render_template("index.html", error="Invalid directory path.")
    return render_template("index.html")

if __name__ == "__main__":
    signature_file = "md5_hashes_3.txt"  # Path to your MD5 hash file
    load_signatures(signature_file)
    app.run(debug=True)
