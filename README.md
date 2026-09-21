<img width="632" height="97" alt="image" src="https://github.com/user-attachments/assets/08457828-2774-4ac0-a94f-95de2e8a6900" />


> **Core Research Question:** [Q2. What explains geographic differences in AI adoption?]

---
>@misc{handa2025economictasksperformedai,
  title={Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations}, 
  author={Kunal Handa and Alex Tamkin and Miles McCain and Saffron Huang and Esin Durmus and Sarah Heck and Jared Mueller and Jerry Hong and Stuart Ritchie and Tim Belonax and Kevin K. Troy and Dario Amodei and Jared Kaplan and Jack Clark and Deep Ganguli},
  year={2025},
  eprint={2503.04761},
  archivePrefix={arXiv},
  primaryClass={cs.CY}
}



<img width="115" height="51" alt="image" src="https://github.com/user-attachments/assets/7f6c5522-4f08-4b4f-b3fa-cdea3c3cd70d" />


This repository contains the data pipelines, statistical models, and visualization tools for analyzing global patterns in AI adoption using the **Anthropic Economic Index** dataset (available via Hugging Face) alongside findings from arXiv:2503.04761. 

By mapping high-volume platform interaction metrics across regions, this project investigates whether economic prosperity ($GDP\ per\ capita$) is the primary explanatory driver of AI usage intensity, or if geographic disparities are better accounted for by factors such as digital infrastructure, occupational labor composition, localized AI policy, or wage structures.

<img width="291" height="47" alt="image" src="https://github.com/user-attachments/assets/b827e37a-29a5-4129-a833-e4eb81704059" />


* **Geospatial Mapping:** Visualize global and regional distributions of AI task usage (e.g., technical writing, software engineering, business automation vs. augmentation) using real-world platform data.
* **Econometric Modeling:** Quantify the relationship between national economic metrics—primarily $GDP\ per\ capita$—and regional AI adoption rates derived from the Anthropic Economic Index.
* **Disparity & Driver Analysis:** Identify geographic "adoption gaps" or "outlier regions" and test whether differences are explained by labor market demographics, wage distribution, or internet/compute access.

<img width="137" height="42" alt="image" src="https://github.com/user-attachments/assets/9b41b58d-15a6-4d5f-a572-340f19247340" />


* **Primary Dataset:** [`Anthropic/EconomicIndex`](https://huggingface.co/datasets/Anthropic/EconomicIndex) — Privacy-preserved dataset of anonymized real-world interactions categorized by task and geographic indicators.
* **Methodological Foundation:** *Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations* ([arXiv:2503.04761](https://arxiv.org/abs/2503.04761)).
* **Supplementary Data:** World Bank Open Data (National $GDP\ per\ capita$, Broadband Access, Labor Force Participation).
---
<img width="120" height="27" alt="image" src="https://github.com/user-attachments/assets/34787a49-deb6-4e46-86a5-54d07fa2fbdd" />

<!-- CHANGELOG:START -->
**2026-09-21**
- `aa23e20` add changelog
- `2bd90b7` updated readme.md
- `fc00794` updated readme.md
- `00d7677` remove old files
- `a10d74a` Turn html charts into pngs
- `1c454c6` Add geographic AI usage charts as PNGs
- `e84d926` Add geographic AI usage charts and fix usage totals

**2026-09-14**
- `a596afc` Add top country and top US state charts
- `cd388d4` Remove obsolete top_geography.png
- `4d9c208` Fix PROFILE.MD image links after splitting geography chart
- `363a3e7` Split geography into country/state breakdowns with full code listings
- `824e7ea` Dataset Provenance

**2026-09-13**
- `132eff6` git dataset analytics
- `2617b9c` first commit
- `ae65dfc` Initial commit
<!-- CHANGELOG:END -->

```text
├── data/           # Datasets and processing scripts
├── notebooks/      # Exploratory data analysis and prototyping
├── src/            # Core source code and implementation modules
├── tests/          # Unit and integration test suites
├── README.md
├── PROFILE.md      # visualization of datasets

