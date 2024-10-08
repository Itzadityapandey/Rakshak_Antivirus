import sys
import os
import yara

from datetime import datetime

# Class will instantiate a RakshakScanner object with a rule path and malicious file path as attributes
class RakshakScanner:

    # Constructor for RakshakScanner object
    def __init__(self, rule_path, mal_path):
        self.rule_path = rule_path
        self.mal_path = mal_path
        # Format the log file with the current date and time
        date_curr = datetime.now()
        dt_str = date_curr.strftime("%d-%m-%Y_%H:%M:%S")
        output_filename = dt_str + ".txt"
        self.log = "logs/" + output_filename
        return

    # To string method for printing info of RakshakScanner object
    # Input: - None
    # Returns - None
    def __str__(self):
        return ("Your rule path is: " + str(self.rule_path) + "\nYour mal_path is: " + str(self.mal_path))

    # Function will take the file path to the directory with rule files and create a dictionary so we can compile them
    # Input: rule_path - file path to the directory of rule files
    # Returns: rule_dict - dictionary of all rule files
    def make_dict(self):
        # Will take the directory containing all rule files and create a dictionary with the keys as the filenames, and values as their path values
        try:
            rule_dict = {}
            for file in os.listdir(self.rule_path):
                filepath = os.path.join(self.rule_path, file)
                rule_dict[file] = filepath
            return rule_dict
        except Exception as e:
            print("Directory for rule files is invalid, please try again")
            exit(0)

    # Function will write result string to the current log file
    # Input: string - string result to write to log
    # Returns: None (results written to the log file)
    def write_log(self, string):
        with open(self.log, "a+") as output_file:
            output_file.write(string)
        return

    # Function will take the file to scan, along with our compiled rules, and check for matching criteria
    # Input: file - file to scan
    #        rules - compiled Rakshak rules
    # Returns: file - file if hit, none if not hit
    def rakshak_sig_check(self, file, rules):
        try:
            # Will scan the file for 60 seconds, any longer it will move on to the next file
            matches = rules.match(file, 60)
            if len(matches) > 0:
                # Grab proper filename not directory
                filename = os.path.splitext(os.path.basename(file))[0]
                matches = list(matches.values())
                rule = matches[0][0].get('rule')
                # Logging functionality
                string = "File was hit: " + filename + " with rule: " + str(rule) + "\n"
                self.write_log(string)
                return file
        except:
            pass

    # Function will scan files within the directory given a dictionary of rule files
    # Input: rule_dict - dictionary of rule files
    # Returns: hit_files - all files hit by Rakshak rules
    def scan_files(self, rule_dict):
        hit_files = []
        # Compile Rakshak rules before starting scan
        rules = yara.compile(filepaths=rule_dict)
        for filename in os.listdir(self.mal_path):
            print("Scanning file: " + filename)
            # Call function to check file with Rakshak signatures
            file_path = os.path.realpath(os.path.join(self.mal_path, filename))
            print(file_path)
            scanned_file = self.rakshak_sig_check(file_path, rules)
            # Don't add the file to the list if it wasn't flagged/was already added
            if scanned_file and scanned_file not in hit_files:
                scanned_file = os.path.splitext(os.path.basename(scanned_file))[0]
                hit_files.append(scanned_file)
        return hit_files
