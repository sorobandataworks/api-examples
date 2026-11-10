"""Japanese business-day calculations: is a date a business day, and how
many business days are there between two dates? Weekends and Japanese
national holidays are handled by the API.

API: Japan Business Days API (Soroban Data Works) on RapidAPI
     https://rapidapi.com/sorobandataworks/api/japan-business-days-api

Setup: export RAPIDAPI_KEY="your-key"
Run:   python3 business_days.py
"""
import json, os, urllib.request

HOST = "japan-business-days-api.p.rapidapi.com"

def call(path: str) -> dict:
    req = urllib.request.Request(
        f"https://{HOST}{path}",
        headers={"X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"], "X-RapidAPI-Host": HOST,
                 "User-Agent": "soroban-api-examples/1.0 (+https://github.com/sorobandataworks/api-examples)"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def main() -> None:
    # 2026-11-03 is Culture Day (a national holiday).
    print("2026-11-03:", call("/v1/jp/is-business-day?date=2026-11-03"))
    print("2026-11-04:", call("/v1/jp/is-business-day?date=2026-11-04"))
    # Business days across the year-end / New Year period.
    print("2026-12-28 -> 2027-01-05:",
          call("/v1/jp/business-days?start=2026-12-28&end=2027-01-05"))
    # National holidays of 2026 (free endpoint).
    holidays = call("/v1/jp/holidays?year=2026")
    print("Holidays in 2026:", len(holidays.get("holidays", holidays)))

if __name__ == "__main__":
    main()
