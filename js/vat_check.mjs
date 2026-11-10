// Validate the FORMAT and CHECK DIGIT of an EU VAT number (11 countries).
// Scope: format/checksum only — NOT a registration (VIES) check. Responses
// state this explicitly (registration_status: "not_checked").
// API: EU VAT Number Format & Checksum Checker (Soroban Data Works)
//   https://rapidapi.com/sorobandataworks/api/eu-vat-number-format-checksum-checker
// Setup: export RAPIDAPI_KEY="your-key"   Run: node vat_check.mjs DE 136695976
const HOST = "eu-vat-number-format-checksum-checker.p.rapidapi.com";
const [country = "DE", vat = "136695976"] = process.argv.slice(2);

const res = await fetch(`https://${HOST}/validate`, {
  method: "POST",
  headers: {
    "X-RapidAPI-Key": process.env.RAPIDAPI_KEY,
    "X-RapidAPI-Host": HOST,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ country, vat }),
});
if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
const r = await res.json();
console.log("Country          :", r.country);
console.log("Normalized number:", r.normalized);
console.log("Format valid     :", r.format_valid);
console.log("Checksum valid   :", r.checksum_valid); // null for DK (no check digit)
console.log("Registration     :", r.registration_status, "(not a VIES check)");
