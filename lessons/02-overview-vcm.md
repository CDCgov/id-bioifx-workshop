---
layout: page
title: Training Overview - Influenza Vaccine Composition
nav_order: 2
---

<style>
.activity:first-of-type .activity-body,
.activity:first-of-type .activity-overview {
  background-color: #ffffff;
}
</style>

{% capture section_overview_1 %}
Introductions, Course Objectives, and a Review of the Influenza Vaccine Composition Cycle.
{% endcapture %}

{% capture section_body_1 %}
## **Training Overview**

Introductions, Course Objectives, and a Review of the Influenza Vaccine Composition Cycle.

![Training Overview Icon]({{ site.baseurl }}/assets/images/overview-vcm-img02.png){: width="25%" .img-center}

### Disclaimer


### Faculty

![Faculty 3]({{ site.baseurl }}/assets/images/overview-vcm-img01.png){: width="25%" .img-center}
![Faculty 3]({{ site.baseurl }}/assets/images/overview-vcm-img06.png){: width="25%" .img-center}
![Faculty 4]({{ site.baseurl }}/assets/images/overview-vcm-img07.png){: width="25%" .img-center}
{% endcapture %}

{% capture section_overview_2 %}
Key learning goals for trainees covering data submission, genomic surveillance, informatic analyses, and command-line skills.
{% endcapture %}

{% capture section_body_2 %}
## **Training Objectives**

- Trainees should be able to **productionalize submission of timely, high-quality data** to GISAID, NCBI.
- Trainees should be able to **produce genomic surveillance reports** describing circulating subtypes and clades in their country.
- Trainees should be able to **produce informatic analyses** like phylogenetic trees and amino acid mutations of sequenced influenza samples.
- At the end of the flu season, trainees should have enough high-quality data and analyses to **write a report or manuscript of publication-quality**.
- Trainees should be **confident in command-line navigation**, NGS file manipulation, ad hoc analyses and troubleshooting.
- Trainees should be able to **describe applications and limitations** of using genomic data for public health decision-making.


![Training Objectives - Publication]({{ site.baseurl }}/assets/images/overview-vcm-img11.png){: width="25%" .img-left} 
![Training Objectives - Public Health]({{ site.baseurl }}/assets/images/overview-vcm-img13.png){: width="25%" .img-right}
{% endcapture %}

{% capture section_overview_3 %}
A brief overview of influenza virus characteristics relevant to bioinformatics analysis.
{% endcapture %}

{% capture section_body_3 %}
## **Influenza Bioinformatics**

- **Influenza A and B**
- **8 segments**
- **Influenza A** — HA NA subtypes, Zoonotic
- **Influenza B** — human
- **Highly variable virus**
- Influenza circulates year-round globally with alternating peaks in NH and SH flu seasons

![Influenza Global Circulation]({{ site.baseurl }}/assets/images/overview-vcm-img15.png){: width="50%" .img-center}
{% endcapture %}

{% capture section_overview_4 %}
Understanding the timeline and process for updating the seasonal influenza vaccine, including CVV development and manufacturing.
{% endcapture %}

{% capture section_body_4 %}
## **Vaccine Composition**

Vaccine antigen must be updated most years.

| | | | |
|---|---|---|---|
| A(H3N2) | A(H1N1) | B/Victoria | B/Yamagata |

*Source and thanks: Dr. J. McCauley*

![Vaccine Antigen Changes]({{ site.baseurl }}/assets/images/overview-vcm-img17.png){: width="100%"}

### Year-Round Global Influenza Surveillance Critical to Vaccine Antigen Updates

- 7 WHO Collaborating Centers for Influenza
- 4 Essential Reference Laboratories
- 13 WHO H5 Reference Laboratories
- Two annual VCM Consultations (Feb and Sept)
- Review, analyze and summarize data and make recommendation within 3 days
- Epidemic/endemic influenza A and B viruses
- Zoonotic influenza viruses (avian H5, H7, H9; H1 and H3 swine origin ("variant viruses"))
- Communicate to Industry for vaccine manufacturing

*Source: https://www.nature.com/articles/s41467-022-29402-5/figures/2*

![Global Surveillance Map]({{ site.baseurl }}/assets/images/overview-vcm-img19.png){: width="100%"}

### Key Questions to Answer for VCM

- Are there significant epidemics and where were they?
- What are the genetic subclades (variants) that have emerged in our population?
- Are the new emerging variants spreading geographically?
- Are emerging variant viruses antigenically distinct from prior or contemporary viruses?
- What is the proportion of the new group(s) and what group(s) is/are likely to predominate?
- Do current vaccines induce antibodies in humans that protect against co-circulating viruses and/or emerging variants?
- For each type/subtype/lineage?
- Is the current vaccine virus likely to provide the best protection, or is a new prototype needed?

![Key Questions 2]({{ site.baseurl }}/assets/images/overview-vcm-img21.png){: width="25%" .img-center}

### VCM Timelines

Timelines for 2021/2022 influenza season (NH):

| October | November | December | January | February | March |
|---------|----------|----------|---------|----------|-------|

- Vaccine Composition Meeting 22nd to 26th February 2021
- Continuous genetic and phenotypic characterization
- Typical European NH influenza season

*Source and thanks: Dr. J. McCauley*
*Data from ECDC/WHO EURO Flu News Europe. Available from: https://fluNewseurope.org/*


### Pre-VCM Timelines: CVVs

Due to genetic characterization runtimes, there are multiple data cut-offs of specimens collected prior to a VCM.

- Genetic characterization
- 1-way antigenic characterization
- 2-way antigenic characterization

To be able to name a prototype in February it must have been selected, amongst others, and further characterized by December. Thereby a choice of CVV options is available in February.

*Modified from: Dr. J. McCauley*

Multiple CVVs from each emerging subclade/group are concurrently generated and down selected through the process to rapidly identify optimal CVVs.

**Ideal properties:**
- Elicit antibodies that react strongly to a virus that is the representative prototype for a particular group or clade.
- Needed to pass a two-way antigenic reactivity test.
- Represent an emerging clade that is likely to circulate in the future and/or will give rise to future viruses.
- Elicit antibodies that cross-react with viruses outside of their own group.
- Can be propagated/grown efficiently and/or the protein is stable under storage conditions.

![Pre-VCM CVV Development]({{ site.baseurl }}/assets/images/overview-vcm-img23.png){: width="100%"}

### Post-VCM Timelines: Vaccine Manufacturing

Influenza vaccine manufacturing timelines (for NH).

*Source and thanks: Dr. J. McCauley*

{% endcapture %}

{% capture section_overview_5 %}
Data quality considerations, timeliness requirements, and importance of original specimens for CVV development.
{% endcapture %}

{% capture section_body_5 %}
## **Timeliness and Quality**

- CDC performs year-round risk assessment to begin early CVV development on several potential clades.
- Genetic analysis to see change in clade dynamics and substitutions emerging in HA and NA proteins.
- Integrated genetic and antigenic analysis to identify substitution conferring antigenic change.
- Clades are then selected – and data analysis of available original specimens for CT values and NGS for polymorphism in HA and NA.
- CT <25, no amino acid polymorphisms >5% and sufficient volume.
- CVV development, qualification of stocks and characterization can take several months.
- In order to update the vaccine composition fully characterized CVVs for cell- and egg-based platforms are needed.

![Timeliness and Quality 2]({{ site.baseurl }}/assets/images/overview-vcm-img26.png){: width="25%" .img-center}

### Importance of Original Specimens

- **Timely and reliable CVV development:** Direct access to original specimens allows CDC to rapidly isolate representative viruses and generate high-quality candidate vaccine viruses (CVVs) that are well matched to circulating strains, reducing delays and uncertainty in the vaccine strain selection process.
- **Global vaccine preparedness and public health protection:** Receiving original specimens strengthens CDC's role in global influenza surveillance and risk assessment, supporting evidence-based recommendations for VCM and manufacturers and ultimately improving the effectiveness of seasonal and pandemic influenza vaccines.
- **CONTINUE SHIPPING SPECIMENS TO CDC IN ADDITION TO SEQUENCING DISTINCT SAMPLES**

{% endcapture %}

{% capture section_overview_6 %}
US influenza surveillance data, vaccine composition recommendations, and sequencing guidance.
{% endcapture %}

{% capture section_body_6 %}
## **US 2024-2025 National Surveillance**

- **A(H1N1)pdm09** – 5a.2a and 5a.2a.1 co-circulated; change in HA subclade over the season
- **A(H3N2)** – Nearly all HA clade 2a.3a.1, subclade J.2 (New vaccine)
- **B/Victoria lineage** – Nearly all C.5; co-circulation of different subclades

![US Surveillance H3N2]({{ site.baseurl }}/assets/images/overview-vcm-img29.png){: width="100%"}
![US Surveillance B/Victoria]({{ site.baseurl }}/assets/images/overview-vcm-img30.png){: width="100%"}
![US Surveillance Overview]({{ site.baseurl }}/assets/images/overview-vcm-img31.png){: width="100%"}

### Influenza Vaccine Composition for the 2025-2026 NH Season

**Trivalent egg-based Vaccines:**
- an A/Victoria/4897/2022 (H1N1)pdm09-like virus antigen;
- an A/Croatia/10136RV/2023 (H3N2)-like virus antigen*; and
- a B/Austria/1359417/2021 (B/Victoria lineage)-like virus.

**Trivalent cell- or recombinant-based Vaccines:**
- an A/Wisconsin/67/2022 (H1N1)pdm09-like virus antigen;
- an A/District of Columbia/27/2023 (H3N2)-like virus antigen*; and
- a B/Austria/1359417/2021 (B/Victoria lineage)-like virus antigen.

For more information: [Influenza Vaccine Composition for the 2025-2026 U.S. Influenza Season - FDA](https://www.fda.gov/)


### Sample Selection Review

- Appropriate sample types for influenza should have **Ct values less than 28** (determined by molecular diagnostic testing)
- Respiratory samples (nasal/throat swabs, nasopharyngeal swabs, sputum, bronchial lavage fluid) = High quantity of viral RNA
- Lung autopsy, tissue samples = variable quantity of viral RNA
- Viral isolate from clinical sample = High quantity of viral RNA but may have passage induced mutation

![Sample Selection 2]({{ site.baseurl }}/assets/images/overview-vcm-img38.png){: width="25%" .img-center}
{% endcapture %}

{% capture section_overview_7 %}
Sequencing guidance, power analyses for detecting rare viruses, establishing predominance, and identifying changes in proportion.
{% endcapture %}

{% capture section_body_7 %}
## **Sequencing Guidance and Power Analyses**


### Key Assumptions

- Our samples are completely random; e.g., an individual within each lineage has an equal probability of being sampled (which implies that each lineage causes similar symptoms)
- Sequencing is unbiased & error-free
- Sampling is uniform over time
- Each individual is infected with only a single variant

![Power Analyses Assumptions 2]({{ site.baseurl }}/assets/images/overview-vcm-img35.png){: width="25%" .img-center}

### Three Examples

1. **Detect rare groups of viruses** — What is the minimum proportion we are likely (i.e., confidence = 95%) to detect with a given sample size?
2. **Identify a group as > 50% ("predominance")** — What is the minimum proportion we can reliably (i.e., power = 90%; confidence = 95%) distinguish as being > 50% with a given sample size?
3. **Detect a change in proportion** — What is the minimum proportion for which we could reliably (power = 90%; confidence = 95%) identify an increase in proportion given the observed sample size in a time period, assuming the true proportion of the group doubles from the 1st to the 2nd time period and we sample the same number during a 2nd (imaginary) time period.


### US Sequencing Guidance

If influenza specimens are available in PHL to meet submission guidance:
- 4 B/Vic / state / 2 wks
- 4 H1N1 / state / 2 wks
- 6 H3N2 / state / 2 wks

**National Totals (assuming 50 PHL and 33 weeks/Season):**
- B/Vic = 100/wk = 3,300/season
- H1N1 = 100/wk = 3,300/season
- H3N2 = 150/wk = 4,950/season
- **Total = 350/wk = 11,550/season**

![US Sequencing Guidance 2]({{ site.baseurl }}/assets/images/overview-vcm-img40.png){: width="100%"}

### Observed US Sample Size

Dotted lines represent submission guidance.

![Observed US Sample Size 2]({{ site.baseurl }}/assets/images/overview-vcm-img42.jpg){: width="100%"}

### Detecting Rare Viruses

**Guidance:** What is the minimum proportion we are likely (i.e., confidence = 95%) to detect with a given sample size?

If Submission Goals are met – at the National Level:
- **Monthly** – variants circulating at 1% would be sequenced at least once.
- **In a season** – variants circulating at ~0.1% would be sequenced at least once.
- **Summer** – variants circulating at ~0.15% would be sequenced at least once.

![Guidance Detect Rare Viruses 2]({{ site.baseurl }}/assets/images/overview-vcm-img44.jpg){: width="100%"}

**Observed Sample Sizes:**

![Observed Detect Rare Viruses 2]({{ site.baseurl }}/assets/images/overview-vcm-img46.jpg){: width="100%"}

### Determining Predominance

**Guidance:** What is the minimum proportion we can reliably (i.e., power = 90%; confidence = 95%) distinguish as being > 50% with a given sample size? What virus/clade/subclade/HA was responsible for the majority of infections?

![Guidance Predominance 2]({{ site.baseurl }}/assets/images/overview-vcm-img48.jpg){: width="100%"}

**Observed Sample Sizes:**

![Observed Predominance 2]({{ site.baseurl }}/assets/images/overview-vcm-img50.jpg){: width="100%"}

### Detecting Change in Proportion

**Guidance:** What is the minimum proportion for which we could reliably (power = 90%; confidence = 95%) identify an increase in proportion given the observed sample size in a time period, assuming:
- The true proportion of the group doubles from the 1st to the 2nd time period
- We sample the same number during a 2nd (imaginary) time period

*The calculations on the ability to detect changes in proportion are not ideal. A better method for assessing growth would be to use logistic regression on data from many time periods.*

![Guidance Detect Change 2]({{ site.baseurl }}/assets/images/overview-vcm-img52.jpg){: width="100%"}

**Observed Sample Sizes:**

![Observed Detect Change 2]({{ site.baseurl }}/assets/images/overview-vcm-img54.jpg){: width="100%"}

### Can We Reliably Identify the Predominant Group in the U.S. in the 2024-2025 Season?

**National** — Based on the sample size of the observed data, if a subgroup constitutes more than 50% of the total in the observed data, can we reliably conclude that it is the predominant group?

| | H1 | H3 | B/VIC |
|---|---|---|---|
| **Clade level** | YES – 5a.2a.1 (63%) | YES – 2a.3a.1 (99.8%) | YES – 3a.2 (100%) |
| **Subclade level** | NO — D.3 (50.3%) does not reach the minimal proportion for predominancy determination | YES – J.2 (91%) | YES – C.5 (C.5 together with its subclades) (96%) |
| **AA group level** | NO HA subgroup >50% | NO HA subgroup >50% | NO HA subgroup >50% |

### Can We Reliably Identify the Predominant Group in the U.S. During Any Month of the Season?

**National** — Based on the sample size of the observed data, if a subgroup constitutes more than 50% of the total in a month, can we reliably conclude that it is the predominant group in that month?

**H1:** National HA clade predominance changed in the US over the season. HA clade 5a.2a predominated in November 2024 while clade 5a.2a.1 subclade D.3 became predominant in February and March 2025.

| | H1 | H3 | B/VIC |
|---|---|---|---|
| **Clade level** | YES in some months | YES – 2a.3a.1 in every month | YES – 3a.2 in every month |
| **Subclade level** | YES in some months | YES – J.2 in every month | YES – C.5 (C.5 together with its subclades) in every month |
| **AA group level** | NO HA subgroup >50% in any month | NO HA subgroup >50% in any month | NO HA subgroup >50% in any month |

![Monthly Predominance Analysis]({{ site.baseurl }}/assets/images/overview-vcm-img55.png){: width="100%"}
{% endcapture %}

{% capture section_overview_8 %}
A summary of key takeaways from the training.
{% endcapture %}

{% capture section_body_8 %}
## **Key Takeaways**

- This training will provide **valuable skills** for influenza bioinformatics.
- Sample selection should be **random, Ct < 28**.
- **Routine, timely, high-quality sequences** are essential for powerful analyses like predominance and vaccine selection.
- **Original specimens** are necessary for characterization, CVV development.

![Key Takeaways 2]({{ site.baseurl }}/assets/images/overview-vcm-img57.png){: width="25%" .img-center}
{% endcapture %}

{% include activity.html variant="1" title="Training Overview" overview=section_overview_1 content=section_body_1 %}
{% include activity.html variant="2" title="Training Objectives" overview=section_overview_2 content=section_body_2 %}
{% include activity.html variant="3" title="Influenza Bioinformatics" overview=section_overview_3 content=section_body_3 %}
{% include activity.html variant="1" title="Vaccine Composition Process" overview=section_overview_4 content=section_body_4 %}
{% include activity.html variant="2" title="Timeliness, Quality & Specimens" overview=section_overview_5 content=section_body_5 %}
{% include activity.html variant="3" title="US Surveillance & Vaccine" overview=section_overview_6 content=section_body_6 %}
{% include activity.html variant="1" title="Sequencing Guidance & Power Analyses" overview=section_overview_7 content=section_body_7 %}
{% include activity.html variant="2" title="Key Takeaways" overview=section_overview_8 content=section_body_8 %}
