"""Check a Japanese company against BOTH official registries in one call:
the Corporate Number registry and the Qualified Invoice (適格請求書) registry.

API: Japan Corporate Invoice Check API (Soroban Data Works) on RapidAPI
     https://rapidapi.com/sorobandataworks/api/japan-corporate-invoice-check-api

Setup: get a free key on the API page, then
    export RAPIDAPI_KEY="your-key"
Run:  python3 check_invoice.py 1030001158338
      python3 check_invoice.py T1030001158338   # the T-number form works too
"""
import json, os, sys, urllib.request

HOST = "japan-corporate-invoice-check-api.p.rapidapi.com"

def call(path: str) -> dict:
    req = urllib.request.Request(
        f"https://{HOST}{path}",
        headers={"X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"], "X-RapidAPI-Host": HOST,
                 "User-Agent": "soroban-api-examples/1.0 (+https://github.com/sorobandataworks/api-examples)"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def main() -> None:
    number = sys.argv[1] if len(sys.argv) > 1 else "1030001158338"
    result = call(f"/v1/check?id={number}")
    print("Corporate number :", result["bangou"])
    print("Invoice (T) no.  :", result["t_number"])
    print("In corporate registry:", result["houjin"]["found"])
    if result["houjin"]["found"]:
        print("  Name (registry)  :", result["houjin"]["record"]["name"])
    inv = result["invoice"]
    print("Invoice registered   :", inv["registered"], f'(status: {inv["status"]})')
    if inv["registered"]:
        print("  Registered on    :", inv["registration_date"])
    print("Names match          :", result["name_match"])
    print("Data as of           :", result["data_as_of"])

if __name__ == "__main__":
    main()
