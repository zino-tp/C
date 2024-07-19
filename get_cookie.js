const { chromium } = require('playwright');

(async () => {
  // Starte Chromium-Browser
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  // Gehe zu Roblox
  await page.goto('https://www.roblox.com/');

  // Warte auf die manuelle Anmeldung
  console.log('Bitte melde dich manuell bei Roblox an und drücke Enter...');
  await new Promise(resolve => process.stdin.once('data', resolve));

  // Hole die Cookies von der Seite
  const cookies = await page.context().cookies();
  console.log('Cookies:', cookies);

  await browser.close();
})();
