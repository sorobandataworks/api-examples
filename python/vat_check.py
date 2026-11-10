"""Validate the FORMAT and CHECK DIGIT of an EU VAT number for 11 countries.

Important scope note: this checks that the number is well-formed and its
check digit is consistent. It does NOT check whether the number is
registered to a business (that is a VIES lookup, which this API does not
do). Responses say so explicitly: registration_status is "not_checked".

API: EU VAT Number Format & Checksum Checker (Soroban Data Works)
     https://rapidapi.com/sorobandataworks/api/eu-vat-number-format-checksum-checker

Setup: export RAPIDAPI_KEY="your-key"
Run:   python3 vat_check.py DE 136695976
"""
import json, os, sys, urllib.request

HOST = "eu-vat-number-format-checksum-checker.p.rapidapi.com"

def validate(country: str, vat: str) -> dict:
    body = json.dumps({"country": country, "vat": vat}).encode()
    req = urllib.request.Request(
        f"https://{HOST}/validate", data=body, method="POST",
        headers={"X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
                 "X-RapidAPI-Host": HOST, "Content-Type": "application/json",
                 "User-Agent": "soroban-api-examples/1.0 (+https://github.com/sorobandataworks/api-examples)"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def main() -> None:
    country = sys.argv[1] if len(sys.argv) > 1 else "DE"
    vat = sys.argv[2] if len(sys.argv) > 2 else "136695976"
    result = validate(country, vat)
    print("Country          :", result["country"])
    print("Normalized number:", result["normalized"])
    print("Format valid     :", result["format_valid"])
    print("Checksum valid   :", result["checksum_valid"])  # None for DK (no check digit)
    print("Registration     :", result["registration_status"], "(not a VIES check)")

if __name__ == "__main__":
    main()
