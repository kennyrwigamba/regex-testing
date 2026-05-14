# Regex SMS Matching

Simple Python scripts to extract transaction amounts from an SMS XML backup file using regular expressions.

## Files

- **matching.py**: finds both received and payment messages, then prints total received and total sent.
- **modified_sms_v2.xml**: input SMS file.

## How to run

From this folder:

```bash
python matching.py
```

## What this project demonstrates

- Reading XML with `xml.etree.ElementTree`
- Matching text patterns with `re`
- Summing extracted numeric values
