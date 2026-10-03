# Fixed-Income Research Lab

Government-bond and corporate-credit research, with a **runnable, offline bond-pricing example** and a separate archive of dated research inputs.

**Xavier Chen · Fordham MS Finance**  
**Status:** Educational research workspace, not a live dashboard or trading service.

## Start with the working example

[Source code](bond_demo.py) · [Expected output](examples/expected_scenarios.csv) · [Tests](tests/test_bond_demo.py) · [Validation record](docs/VALIDATION.md)

Explore how the price of a fictional five-year, 5% coupon bond changes when its yield changes. The example calculates price, Macaulay duration, modified duration, and convexity, then compares exact repricing with the first-order duration approximation.

All inputs are synthetic. No data-provider account, API key, download, or private workbook is needed.

## Tech stack and installation

Python standard library only. Tested locally with Python **3.13.5**; no `pip install` step is needed for the example.

```bash
git clone https://github.com/Xiaowen-CHEN-Learner/Headhunt_FixedIncome.git
cd Headhunt_FixedIncome
python bond_demo.py
python -m unittest discover -s tests -v
```

## Usage

Use decimal rates (`0.05` means 5%). Default face value is 100, maturity is five years, and coupons are semiannual.

```bash
python bond_demo.py --coupon 0.05 --yield-rate 0.05 --years 5 --frequency 2
python bond_demo.py --output output/scenarios.csv
```

| Yield shock | Yield | Price per 100 | Exact price change |
| ---: | ---: | ---: | ---: |
| -100 basis points | 4.00% | 104.491293 | +4.491293% |
| -50 basis points | 4.50% | 102.216554 | +2.216554% |
| 0 | 5.00% | 100.000000 | 0.000000% |
| +50 basis points | 5.50% | 97.839981 | -2.160019% |
| +100 basis points | 6.00% | 95.734899 | -4.265101% |

These are calculated educational examples, not market quotations, forecasts, or investment returns.

## Methodology and limits

The price is the sum of discounted coupon and principal cash flows. Valuation is exactly on a coupon date; maturity must span whole coupon periods. Annual nominal yield is compounded at the coupon frequency. Duration and convexity are derived from the same cash flows.

There is no accrued interest, default, call feature, term structure, tax, fee, or liquidity adjustment. The example therefore does not replace a production bond-pricing or credit-risk system.

**Validation:** 15 local unit tests passed on October 3, 2026. See the [validation record](docs/VALIDATION.md) for the scope. Passing example tests does not validate the historical data archive or a trading strategy.

## Existing research archive

The [October 1, 2026 snapshot](Fixed%20income%20data%20as%20of%20Oct%201%202026/) contains Excel workbooks, PNG charts, and an HTML spreadsheet export. The folder date is a collection date; individual observations may differ.

| Area | Files present |
| --- | --- |
| Government bonds | US Treasury charts and a US 10-year workbook; Japan/China curve images |
| Corporate credit | Workbooks labelled Oracle, NVIDIA, Meta, Microsoft, Google, Blackstone, BlackRock, and Blue Owl; selected spread files |
| Macroeconomics | US, Japan, and China activity, inflation, and labour-market workbooks |
| Cross-market reference | World bond, curve, and spread workbooks |

This inventory does not establish accuracy or redistribution permissions. Inspect sources, instruments, units, dates, missing values, and external workbook connections before use. Do not redistribute restricted provider or institutional data. Use permitted samples or acquisition instructions where necessary.

## Next development steps

Document archive sources and usage rights; add a field dictionary; extend the analytical example only after validating settlement and instrument conventions. Government-bond dashboards, corporate-credit workflows, and reusable AI research skills remain development goals, not shipped features.

## Attribution, contributions, and contact

The offline example and tests were added with AI assistance during an October 2026 portfolio improvement session. They are intended for study, review, and extension; they are not presented as prior professional work. Existing research materials are preserved.

Open an issue with a reproducible problem or suggested improvement. Do not attach confidential information or restricted datasets.

[Xavier Chen on LinkedIn](https://www.linkedin.com/in/xiaowen-chen/) · [GitHub portfolio](https://github.com/Xiaowen-CHEN-Learner)

## License

No project-wide license has been added. Third-party data retain their applicable rights and restrictions.

---

Educational research only. Not investment advice.
