import { chromium } from 'playwright';
const [src, out, footer] = process.argv.slice(2);
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file:///' + src.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
await p.pdf({ path: out, format: 'A4', printBackground: true,
  displayHeaderFooter: true, headerTemplate: '<div></div>',
  footerTemplate: footer,
  margin: { top: '18mm', bottom: '20mm', left: '0mm', right: '0mm' } });
await b.close();
