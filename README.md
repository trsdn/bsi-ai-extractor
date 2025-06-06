# BSI AI Extractor

A Python tool for extracting and structuring AI evaluation criteria from BSI (Federal Office for Information Security) PDF documents. This tool parses the "AI-Finance Test Criteria" PDF and converts the criteria into structured CSV format for easier analysis and processing.

## About the Document

The **AI-Finance Test Criteria** document is published by the German Federal Office for Information Security (BSI) as part of their comprehensive framework for evaluating artificial intelligence systems in the financial sector. This document provides:

- **Regulatory Compliance Guidelines**: Criteria aligned with the EU AI Act requirements for financial AI applications
- **Risk Assessment Framework**: Systematic evaluation methods for AI systems used in banking, insurance, and financial services
- **Technical Standards**: Detailed evaluation principles covering data quality, model transparency, algorithmic fairness, and robustness
- **Implementation Guidance**: Practical instructions for financial institutions to assess their AI systems
- **Use Case Categorization**: Specific criteria based on different AI application scenarios in finance

The document contains 95 distinct evaluation criteria organized into categories such as:
- **Explainability (EX)**: Requirements for AI system transparency and interpretability
- **Trustworthiness (TR)**: Criteria for reliable and dependable AI operations
- **Data Quality (DQ)**: Standards for training and operational data management
- **Robustness (RO)**: Requirements for AI system resilience and stability
- **Fairness (FA)**: Guidelines for preventing bias and ensuring equitable outcomes

This extraction tool helps financial institutions, compliance officers, and AI developers to systematically work with these criteria by converting the PDF format into structured, searchable, and processable data.

## Overview

The BSI AI Extractor processes PDF documents containing AI evaluation criteria and extracts:
- Criterion IDs and names
- Relevance based on use case parametrization
- Evaluation requirements
- Evaluation principles
- Supportive guidance
- Evaluation methods
- Evaluation tools
- References to EU AI Act

## Features

- **Automated PDF parsing**: Extracts text from multi-page PDF documents
- **Intelligent text processing**: Handles hyphenated words, line breaks, and formatting issues
- **Structured data output**: Generates clean CSV files with all criteria fields
- **Error handling**: Robust error handling and validation
- **Statistics reporting**: Provides extraction statistics and field completion rates

## Requirements

- Python 3.7+
- PyMuPDF (fitz) library for PDF processing

## Installation

### Quick Setup (Recommended)

Run the automated setup script:
```bash
git clone https://github.com/trsdn/bsi-ai-extractor.git
cd bsi-ai-extractor
./setup.sh
```

### Manual Setup

1. Clone this repository:
```bash
git clone https://github.com/trsdn/bsi-ai-extractor.git
cd bsi-ai-extractor
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

   Or install manually:
```bash
pip install PyMuPDF
```

## Usage

1. Place your BSI PDF document in the project directory and name it `AI-Finance_Test-Criteria.pdf`

2. Run the extraction script:
```bash
python script.py
```

3. The extracted data will be saved to `criteria_catalogue.csv`

## Output Format

The generated CSV file contains the following columns:
- **Criterion ID**: Unique identifier (e.g., EX-01, TR-02)
- **Criterion name**: Descriptive name of the criterion
- **Relevance based on use case parametrization**: Applicability filters
- **Evaluation requirement**: Description of what the criterion evaluates
- **Evaluation principle**: Document-based or test-based classification
- **Supportive guidance**: Additional explanations and examples
- **Evaluation method**: Testing and evaluation instructions
- **Evaluation tools**: Suggested tools and methods
- **Reference to EU AI Act**: Corresponding EU AI Act articles

## Example Output

The tool successfully processes complex PDF structures and handles:
- Multi-line criterion names
- Hyphenated word breaks across lines
- Various text formatting inconsistencies
- Field content spanning multiple paragraphs

Sample extraction statistics:
```
Extracted 95 criteria. Data saved to criteria_catalogue.csv.
Field statistics:
  - Relevance based on use case parametrization: 95/95
  - Evaluation requirement: 95/95
  - Evaluation principle: 95/95
  - Supportive guidance: 95/95
  - Evaluation method: 95/95
  - Evaluation tools: 95/95
  - Reference to EU AI Act: 95/95
```

## File Structure

```
bsi-ai-extractor/
├── script.py                    # Main extraction script
├── setup.sh                     # Automated setup script
├── requirements.txt             # Python dependencies
├── AI-Finance_Test-Criteria.pdf # Input PDF document
├── criteria_catalogue.csv       # Generated output file
├── README.md                    # This file
├── LICENSE                      # License information
└── venv/                        # Virtual environment (created after setup)
```

## Technical Details

The extraction process:
1. Opens and reads the PDF document page by page
2. Filters out headers, footers, and table of contents
3. Identifies criterion IDs using regex patterns
4. Extracts multi-line criterion names with intelligent text joining
5. Parses structured field content for each criterion
6. Handles text formatting issues (hyphenation, line breaks)
7. Outputs structured data to CSV format

## Troubleshooting

**PDF not found error**: Ensure the PDF file is named exactly `AI-Finance_Test-Criteria.pdf` and is in the project root directory.

**Import error for fitz**: Install PyMuPDF using `pip install PyMuPDF` in your virtual environment.

**Permission errors**: Make sure you have write permissions in the project directory.

**Empty output**: Check that the PDF contains the expected criterion format (e.g., "XYZ-01" style IDs).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the terms specified in the LICENSE file.

## Acknowledgments

- Federal Office for Information Security (BSI) for the AI evaluation criteria framework
- PyMuPDF library for robust PDF processing capabilities