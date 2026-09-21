# Geographic Differences in AI Adoption

> **Core Research Question:** [Q2. What explains geographic differences in AI adoption?]

---

## Overview

This repository contains the data pipelines, statistical models, and visualization tools for analyzing global patterns in AI adoption using the **Anthropic Economic Index** dataset (available via Hugging Face) alongside findings from arXiv:2503.04761. 

By mapping high-volume platform interaction metrics across regions, this project investigates whether economic prosperity ($GDP\ per\ capita$) is the primary explanatory driver of AI usage intensity, or if geographic disparities are better accounted for by factors such as digital infrastructure, occupational labor composition, localized AI policy, or wage structures.

## Key Research Objectives

* **Geospatial Mapping:** Visualize global and regional distributions of AI task usage (e.g., technical writing, software engineering, business automation vs. augmentation) using real-world platform data.
* **Econometric Modeling:** Quantify the relationship between national economic metrics—primarily $GDP\ per\ capita$—and regional AI adoption rates derived from the Anthropic Economic Index.
* **Disparity & Driver Analysis:** Identify geographic "adoption gaps" or "outlier regions" and test whether differences are explained by labor market demographics, wage distribution, or internet/compute access.

## Data Sources

* **Primary Dataset:** [`Anthropic/EconomicIndex`](https://huggingface.co/datasets/Anthropic/EconomicIndex) — Privacy-preserved dataset of anonymized real-world interactions categorized by task and geographic indicators.
* **Methodological Foundation:** *Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations* ([arXiv:2503.04761](https://arxiv.org/abs/2503.04761)).
* **Supplementary Data:** World Bank Open Data (National $GDP\ per\ capita$, Broadband Access, Labor Force Participation).

## Repository Structure

```text
├── data/           # Datasets and processing scripts
├── notebooks/      # Exploratory data analysis and prototyping
├── src/            # Core source code and implementation modules
├── tests/          # Unit and integration test suites
├── README.md


@misc{handa2025economictasksperformedai,
  title={Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations}, 
  author={Kunal Handa and Alex Tamkin and Miles McCain and Saffron Huang and Esin Durmus and Sarah Heck and Jared Mueller and Jerry Hong and Stuart Ritchie and Tim Belonax and Kevin K. Troy and Dario Amodei and Jared Kaplan and Jack Clark and Deep Ganguli},
  year={2025},
  eprint={2503.04761},
  archivePrefix={arXiv},
  primaryClass={cs.CY}
}
