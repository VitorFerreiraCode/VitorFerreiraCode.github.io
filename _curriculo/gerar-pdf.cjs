// Gera os PDFs do currículo: node _curriculo/gerar-pdf.cjs (precisa de playwright-core e do Chromium do cache).
const path = require("path");
const { chromium } = require(process.env.PW);
(async () => {
  const b = await chromium.launch({ executablePath: process.env.HOME + "/.cache/ms-playwright/chromium-1248/chrome-linux64/chrome" });
  const page = await b.newPage();
  for (const [html, pdf] of [["curriculo-pt.html", "curriculo-vitor-ferreira-viana-pt.pdf"], ["curriculo-en.html", "resume-vitor-ferreira-viana-en.pdf"]]) {
    await page.goto("file://" + path.join(__dirname, html), { waitUntil: "networkidle" });
    await page.pdf({ path: path.join(__dirname, "..", "assets", "curriculo", pdf), format: "A4", printBackground: true, preferCSSPageSize: true });
    console.log("gerado", pdf);
  }
  await b.close();
})();
