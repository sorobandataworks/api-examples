# Soroban Data Works — API Examples

Runnable Python and JavaScript examples for the public APIs of
[Soroban Data Works](https://sorobandataworks.com), a small data-API shop
in Shibuya, Tokyo. All three APIs are served through RapidAPI.

| Example | API | What it does |
|---|---|---|
| `python/check_invoice.py` · `js/check_invoice.mjs` | Japan Corporate Invoice Check API | Look up a Japanese company in **both** official registries at once: the Corporate Number registry and the Qualified Invoice (適格請求書) registry |
| `python/business_days.py` · `js/business_days.mjs` | Japan Business Days API | Is a date a Japanese business day? How many business days between two dates? (Weekends and national holidays handled) |
| `python/vat_check.py` · `js/vat_check.mjs` | EU VAT Number Format & Checksum Checker | Validate the **format and check digit** of an EU VAT number in 11 countries. Format/checksum only — this is **not** a registration (VIES) check, and the API says so in every response |

## Requirements

- Python 3.9+ (standard library only) or Node.js 18+ (built-in `fetch`)
- A free RapidAPI account and an API key (see below)

## Getting an API key

1. Open the API you want to use on RapidAPI and subscribe to the free
   **BASIC** plan:
   - [Japan Corporate Invoice Check API](https://rapidapi.com/sorobandataworks/api/japan-corporate-invoice-check-api)
   - [Japan Business Days API](https://rapidapi.com/sorobandataworks/api/japan-business-days-api)
   - [EU VAT Number Format & Checksum Checker](https://rapidapi.com/sorobandataworks/api/eu-vat-number-format-checksum-checker)
2. Your `X-RapidAPI-Key` is shown in the API's code-snippet panel on
   RapidAPI. Put it in an environment variable — the examples never
   hard-code a key:

   ```bash
   export RAPIDAPI_KEY="your-key-here"
   ```

## Running the examples

```bash
# Japan corporate / invoice cross-check (corporate number or T-number)
python3 python/check_invoice.py 1030001158338
node    js/check_invoice.mjs T1030001158338

# Japanese business days
python3 python/business_days.py
node    js/business_days.mjs

# EU VAT format & checksum (country code + number)
python3 python/vat_check.py DE 136695976
node    js/vat_check.mjs DE 136695976
```


## Pricing

Each API has a free BASIC plan; paid plans (higher monthly quotas) are
listed on the API pages linked above. The free tiers are enough to run
every example in this repository.

## Notes on the data

- Corporate and invoice data come from the National Tax Agency's public
  registries (Corporate Number Publication Site / Qualified Invoice
  Issuer Publication Site), used under the Public Data License (v1.0),
  and are refreshed daily.
- Japanese holidays are based on the Cabinet Office's official calendar.
- The VAT checker validates number structure and check digits only. It
  does not confirm that a number is registered to a business.
- **Rate limits:** Free-tier requests may be rate-limited (HTTP 429). If this occurs, wait before retrying and follow any Retry-After header or plan-specific limits.

## License

The examples are released under the [MIT License](LICENSE).
The APIs themselves are separate services with their own terms on RapidAPI.
