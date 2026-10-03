# Fixed-Income Research Lab

A research workspace for studying government bonds, corporate credit, macroeconomic indicators, and the design of AI-assisted fixed-income research workflows.

**Author:** Xavier Chen · MS Finance, Fordham University  
**Status:** Early-stage research workspace. The repository currently contains dated data exports and chart files, not an implemented dashboard or an automated research service.

## Project description

The goal is to connect macroeconomic developments and issuer-level information with questions about yields, yield curves, and credit spreads. The original repository name, `Headhunt_FixedIncome`, reflects the broader ambition to develop reusable research skills and fixed-income career preparation resources.

The distinction between **available materials** and **planned functionality** is intentional: the current files are inputs for analysis, not evidence of a tested trading strategy.

## Start here

Open the [October 1, 2026 research snapshot](Fixed%20income%20data%20as%20of%20Oct%201%202026/). The folder name records the collection date; individual series may have different observation dates and frequencies.

| Area | Existing materials |
| --- | --- |
| Government bonds | US Treasury chart files, a US 10-year index workbook, and Japan/China curve images |
| Corporate credit | Bond workbooks labelled Oracle, NVIDIA, Meta, Microsoft, Google, Blackstone, BlackRock, and Blue Owl; selected spread files |
| Macroeconomics | US, Japan, and China activity, inflation, and labour-market workbooks |
| Cross-market reference | World bond, curve, and spread workbooks |

This inventory describes the files present; it does not independently validate their contents, definitions, or redistribution permissions.

## Tech stack and formats

The current repository uses Excel workbooks (`.xlsx`), PNG charts, and an HTML spreadsheet export. No Python package, application entry point, or dependency manifest is included yet.

Planned analytical work may use Python and reusable Markdown research instructions. These are development goals, not current software features.

## Installation

No software installation is required to browse the repository. To obtain a local copy:

```bash
git clone https://github.com/Xiaowen-CHEN-Learner/Headhunt_FixedIncome.git
cd Headhunt_FixedIncome
```

Use a spreadsheet application to inspect the workbooks. Review any external data connections before refreshing them; access to an original data provider may be required.

## Usage

1. Select a workbook or chart from the dated snapshot folder.
2. Establish the source, instrument identifier, observation dates, frequency, units, and missing-value conventions before using the series.
3. Write a specific research question, such as how a yield-curve move relates to a macroeconomic release or how an issuer spread compares with a benchmark.
4. Record transformations and assumptions separately from observations. Distinguish a coincident event from an established cause.
5. Present conclusions with an as-of date, limitations, and links to the underlying permitted sources.

## Planned development

- A source and field dictionary, including access and redistribution conditions for each dataset.
- Government-bond and corporate-credit research workflows.
- US 10-year yield/event visualizations and a sourced fixed-income news workflow.
- Reproducible notebooks, a tested dependency specification, and permitted sample data.
- Documented validation of units, missing values, observation dates, and benchmark alignment.

## Data, limitations, and responsible use

Data snapshots are not a live feed. Definitions, accuracy, completeness, and availability must be checked before reuse. No performance results or investment recommendations are established by this repository.

Some market-data exports or screenshots may be subject to provider or institutional restrictions. Confirm the relevant permissions before redistributing them. Where redistribution is not permitted, use source links, acquisition instructions, or clearly labelled synthetic examples instead. Do not upload credentials, account identifiers, confidential research, or employer information.

## Contributing

Suggestions on data documentation, research design, and reproducibility are welcome through GitHub issues. Describe the problem, the affected file, and a proposed improvement. Do not attach restricted datasets.

## Author and contact

[Xavier Chen on LinkedIn](https://www.linkedin.com/in/xiaowen-chen/) · [GitHub portfolio](https://github.com/Xiaowen-CHEN-Learner)

## License

No project-wide license has been added. This README does not grant rights to third-party datasets or other materials.

---

Educational and research use only. Not investment advice.
