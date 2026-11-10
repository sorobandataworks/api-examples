// Japanese business-day calculations (weekends + national holidays handled).
// API: Japan Business Days API (Soroban Data Works) on RapidAPI
//   https://rapidapi.com/sorobandataworks/api/japan-business-days-api
// Setup: export RAPIDAPI_KEY="your-key"   Run: node business_days.mjs
const HOST = "japan-business-days-api.p.rapidapi.com";
async function call(path) {
  const res = await fetch(`https://${HOST}${path}`, {
    headers: { "X-RapidAPI-Key": process.env.RAPIDAPI_KEY, "X-RapidAPI-Host": HOST },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  return res.json();
}
console.log("2026-11-03:", await call("/v1/jp/is-business-day?date=2026-11-03")); // Culture Day
console.log("2026-11-04:", await call("/v1/jp/is-business-day?date=2026-11-04"));
console.log("2026-12-28 -> 2027-01-05:",
  await call("/v1/jp/business-days?start=2026-12-28&end=2027-01-05"));
