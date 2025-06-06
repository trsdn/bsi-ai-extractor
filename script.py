import csv
import re
import sys
import os

# Check for required dependencies
try:
    import fitz
except ImportError:
    print("Error: PyMuPDF library not found.")
    print("Please install it using one of the following commands:")
    print("  pip install -r requirements.txt")
    print("  pip install PyMuPDF")
    print("\nIf you're using a virtual environment, make sure it's activated first:")
    print("  python3 -m venv venv")
    print("  source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
    print("  pip install -r requirements.txt")
    sys.exit(1)

# Check if the PDF file exists
pdf_path = "AI-Finance_Test-Criteria.pdf"
if not os.path.exists(pdf_path):
    print(f"Error: PDF file '{pdf_path}' not found. Current directory: {os.getcwd()}")
    sys.exit(1)

try:
    # Open the PDF file
    doc = fitz.open(pdf_path)
    print(f"Successfully opened PDF with {len(doc)} pages.")
except Exception as e:
    print(f"Error opening PDF: {e}")
    sys.exit(1)

# Define the field labels we expect (as they appear exactly in the PDF)
field_labels = [
    "Relevance based on use case parametrization",
    "Evaluation requirement",
    "Evaluation principle",
    "Supportive guidance",
    "Evaluation method",
    "Evaluation tools",
    "Reference to EU AI Act"
]
field_set = set(field_labels)  # for quick lookup

# Collect all relevant lines from the PDF, cleaning out headers/footers and TOC lines
lines = []
for page in doc:
    text = page.get_text("text")
    for line in text.splitlines():
        if not line.strip():
            continue  # skip empty lines
        # Skip chapter headers and publication footers
        if line.strip().startswith(("CHAPTER", "Chapter")) or line.strip().startswith("Part "):
            continue
        if line.strip().startswith("Federal Office for Information Security"):
            continue
        # Skip table-of-contents style lines (criterion listings with page numbers)
        if re.match(r'^[A-Z]{2,}-\d{2}\s+-\s+.*\d+$', line.strip()):
            continue
        lines.append(line)

# Now parse the collected lines to extract criteria
criteria = []
i = 0
while i < len(lines):
    line = lines[i].strip()
    # Identify Criterion ID (format like "XYZ-01")
    if re.match(r'^[A-Z]{2,}-\d{2}$', line):
        # Start a new criterion entry
        current = {"Criterion ID": line}
        i += 1
        # 1. Capture Criterion Name (which may span multiple lines until a known field label appears)
        name_parts = []
        while i < len(lines):
            next_line = lines[i].strip()
            # Stop if we reach a new criterion ID or a field label, which means name is done
            if re.match(r'^[A-Z]{2,}-\d{2}$', next_line) or next_line in field_set:
                break
            name_parts.append(next_line)
            i += 1
        # Join the name lines, handling hyphenation and line breaks
        criterion_name = ""
        for part in name_parts:
            if criterion_name.endswith("-"):
                # Remove trailing hyphen and append directly (word continuation)
                criterion_name = criterion_name[:-1] + part
            elif criterion_name and criterion_name[-1].isalpha() and part and part[0].islower():
                # If the previous part ends with a letter and the next part starts with lowercase,
                # join without space (it was a line-break at a space in the PDF)
                criterion_name = criterion_name + part
            else:
                # Otherwise, add a space before the part (if not the first part)
                if criterion_name:
                    criterion_name += " "
                criterion_name += part
        current["Criterion name"] = criterion_name

        # 2. Extract all fields for this criterion until the next criterion ID is encountered
        current_field = None
        while i < len(lines):
            line = lines[i].strip()
            # If we hit another criterion ID, break to outer loop (this criterion finished)
            if re.match(r'^[A-Z]{2,}-\d{2}$', line):
                break
            # If line is a known field label, start a new field
            if line in field_set:
                current_field = line
                current[current_field] = ""  # initialize field content
                i += 1
                continue
            # If it's content for the current field, append it
            if current_field:
                content_line = lines[i]
                # Handle hyphenated word breaks and line continuation for field content
                if current[current_field].endswith("-"):
                    # Remove hyphen and concatenate without newline
                    current[current_field] = current[current_field][:-1] + content_line.strip()
                elif current[current_field] and current[current_field][-1].isalpha() and content_line.strip() and content_line.strip()[0].islower():
                    # Continue the sentence on the same line (remove newline)
                    current[current_field] = current[current_field].rstrip("\n") + content_line.strip()
                else:
                    # Normal new line in content (preserve line break in output)
                    if current[current_field]:
                        current[current_field] += "\n" + content_line
                    else:
                        current[current_field] = content_line
            # If we encounter a line that is not a field label and no current_field is set (should not happen in structured content), skip it.
            i += 1

        # Add the completed criterion to the list
        criteria.append(current)
    else:
        # If the line is not a criterion ID (e.g., a stray line outside criteria), skip it.
        i += 1

# Write the results to a CSV file
output_file = "criteria_catalogue.csv"
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Criterion ID", "Criterion name"] + field_labels)
    writer.writeheader()
    for crit in criteria:
        writer.writerow(crit)

print(f"Extracted {len(criteria)} criteria. Data saved to {output_file}.")
print("Field statistics:")
for field in field_labels:
    field_count = sum(1 for crit in criteria if field in crit and crit[field].strip())
    print(f"  - {field}: {field_count}/{len(criteria)}")