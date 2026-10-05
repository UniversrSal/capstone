<img width="632" height="97" alt="image" src="https://github.com/user-attachments/assets/08457828-2774-4ac0-a94f-95de2e8a6900" />

> **Core Research Question:** [Q2. What explains geographic differences in AI adoption?]

---

```bibtex
@misc{handa2025economictasksperformedai,
  title={Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations}, 
  author={Kunal Handa and Alex Tamkin and Miles McCain and Saffron Huang and Esin Durmus and Sarah Heck and Jared Mueller and Jerry Hong and Stuart Ritchie and Tim Belonax and Kevin K. Troy and Da[...]
  year={2025},
  eprint={2503.04761},
  archivePrefix={arXiv},
  primaryClass={cs.CY}
}
```

---

<img width="115" height="51" alt="image" src="https://github.com/user-attachments/assets/7f6c5522-4f08-4b4f-b3fa-cdea3c3cd70d" />

This repository contains the data pipelines, statistical models, and visualization tools for analyzing global patterns in AI adoption using the **Anthropic Economic Index** dataset (available via [...]

By mapping high-volume platform interaction metrics across regions, this project investigates whether economic prosperity ($GDP\ per\ capita$) is the primary explanatory driver of AI usage intensi[...]

<img width="291" height="47" alt="image" src="https://github.com/user-attachments/assets/b827e37a-29a5-4129-a833-e4eb81704059" />

* **Geospatial Mapping:** Visualize global and regional distributions of AI task usage (e.g., technical writing, software engineering, business automation vs. augmentation) using real-world platfo[...]
* **Econometric Modeling:** Quantify the relationship between national economic metrics—primarily $GDP\ per\ capita$—and regional AI adoption rates derived from the Anthropic Economic Index.
* **Disparity & Driver Analysis:** Identify geographic "adoption gaps" or "outlier regions" and test whether differences are explained by labor market demographics, wage distribution, or internet/[...]

<img width="137" height="42" alt="image" src="https://github.com/user-attachments/assets/9b41b58d-15a6-4d5f-a572-340f19247340" />

* **Primary Dataset:** [`Anthropic/EconomicIndex`](https://huggingface.co/datasets/Anthropic/EconomicIndex) — Privacy-preserved dataset of anonymized real-world interactions categorized by task [...]
* **Methodological Foundation:** *Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations* ([arXiv:2503.04761](https://arxiv.org/abs/2503.04761)).
* **Supplementary Data:** World Bank Open Data (National $GDP\ per\ capita$, Broadband Access, Labor Force Participation).

---

<img width="120" height="27" alt="image" src="https://github.com/user-attachments/assets/34787a49-deb6-4e46-86a5-54d07fa2fbdd" />

```text
├── data/           # Datasets and processing scripts
├── notebooks/      # Exploratory data analysis and prototyping
├── src/            # Core source code and implementation modules
├── tests/          # Unit and integration test suites
├── README.md
├── PROFILE.md      # visualization of datasets
```

## Findings

- **The United States** has the most overall AI usage globally.
- **Israel** has the highest AI adoption rate in 2025.

## Recent Changes

October 5, 2026: Added key findings on AI usage and adoption rates; documented that the United States leads in overall AI usage while Israel demonstrates the highest adoption rate in 2025. Added GDP and AI investment focus comparison visualizations for the United States and Israel, including a PNG export workflow for notebook-ready presentation and repo documentation.

September 21, 2026: Updated project documentation by adding a changelog, introducing PROFILE.md, and refactoring the README.md for better clarity; also removed obsolete files and replaced interact[...]

September 14, 2026: Refactored geographic data visualizations by splitting them into separate country and state breakdown charts with complete code listings, updating image links in PROFILE.md, re[...]

September 13, 2026: Created the repository with the initial commits and added Git dataset analytics capabilities.
