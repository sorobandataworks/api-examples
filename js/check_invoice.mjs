// Check a Japanese company against BOTH official registries in one call:
// the Corporate Number registry and the Qualified Invoice registry.
//
// API: Japan Corporate Invoice Check API (Soroban Data Works) on RapidAPI
//   https://rapidapi.com/sorobandataworks/api/japan-corporate-invoice-check-api
//
// Setup: export RAPIDAPI_KEY="your-key"
// Run:   node check_invoice.mjs 1030001158338
const HOST = "japan-corporate-invoice-check-api.p.rapidapi.com";
const number = process.argv[2] ?? "1030001158338";

const res = await fetch(`https://${HOST}/v1/check?id=${encodeURIComponent(number)}`, {
  headers: { "X-RapidAPI-Key": process.env.RAPIDAPI_KEY, "X-RapidAPI-Host": HOST },
});
if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
const r = await res.json();

console.log("Corporate number    :", r.bangou);
console.log("Invoice (T) no.     :", r.t_number);
console.log("In corporate registry:", r.houjin.found);
if (r.houjin.found) console.log("  Name (registry)   :", r.houjin.record.name);
console.log("Invoice registered  :", r.invoice.registered, `(status: ${r.invoice.status})`);
if (r.invoice.registered) console.log("  Registered on     :", r.invoice.registration_date);
console.log("Names match         :", r.name_match);
console.log("Data as of          :", JSON.stringify(r.data_as_of));
