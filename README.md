# Antivirus Scanner

A web-based antivirus scanner application that scans directories for malware using a predefined list of MD5 hash signatures. Built with Python and Flask, the application allows users to input a directory path and checks for infected files by comparing their hashes against known malware signatures.

## Features

- **Efficient Malware Detection**: Quickly scans files in a directory for potential malware by comparing file hashes.
- **Interactive Web Interface**: User-friendly interface with options to input directory paths and view scan results.
- **Customizable UI**: Modern, responsive, and futuristic UI design that includes:
  - Background customization
  - Animated buttons
  - Error and success notifications
- **Secure and Lightweight**: Minimal dependencies and fast operations.

## Technologies Used

- **Python**: Core application logic.
- **Flask**: Web framework to handle routes and templates.
- **HTML & CSS**: Frontend design with a responsive and futuristic layout.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/antivirus-scanner.git
   cd antivirus-scanner
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Malware Signatures**:
   - Ensure you have a file named `md5_hashes_3.txt` in the project root containing known malware MD5 hashes, one per line.

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Web Interface**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Enter the directory path you wish to scan.
2. Click on the **Start Scan** button.
3. View results:
   - A list of infected files (if any) will be displayed.
   - If no malware is detected, a success message will appear.

## File Structure

```
antivirus-scanner/
|-- app.py
|-- templates/
|   |-- index.html
|   |-- result.html
|-- static/
|   |-- style.css
|-- md5_hashes_3.txt
|-- requirements.txt
|-- README.md
```



## Customization

- **Background Image**: Replace the `background.jpg` file in `static/` to update the background.
- **Styling**: Modify `style.css` for further design tweaks.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with your improvements.



Happy Scanning! 🚀
