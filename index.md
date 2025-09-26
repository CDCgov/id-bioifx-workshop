---
layout: page
title: Influenza Bioinformatics Workshop
nav_order: 0
---
<!-- filepath: /Users/nbx0/repos/id-bioifx-workshop/index.md -->

<!-- This chunk of code creates a modal popup warning that the site is under development. -->
<div id="dev-warning-modal" style="display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.5);">
    <div style="background-color: #fefefe; margin: 15% auto; padding: 20px; border: 1px solid #888; width: 300px; border-radius: 5px; text-align: center;">
        <h3 style="color: #ff6b35;">⚠️ Under Development</h3>
        <p>This site is currently under development.</p>
        <button onclick="document.getElementById('dev-warning-modal').style.display='none'" style="background-color: #007cba; color: white; border: none; padding: 10px 20px; border-radius: 3px; cursor: pointer;">OK</button>
    </div>
</div>
<script>
window.onload = function() {
    document.getElementById('dev-warning-modal').style.display = 'block';
}
</script>
<!-- End of modal popup code -->

Introduction text here

## Contributors
- [US CDC Influenza Division](https://www.cdc.gov/ncird/divisions-offices/flu.html)
    - Kristine Lacek
    - Mandy Sullivan
    - GAT peeps
    - Becky Kondor
    - [Ben Rambo-Martin](https://github.com/nbx0)
- [Association of Public Health Laboratories (APHL)](https://www.aphl.org)
    - Alisa Bochnowski
    - Logan Fink
    - Kristen Knipe
    - Eugene Yeboah

---
# Examples for developers:

## Code Snippets

```bash
Throughout the lessons, you will encounter code snippets 
that you can easily copy to your clipboard. Look for the 
copy button next to the code blocks to facilitate this process.
```

## Expandable Section
<details class="collapsible">
    <summary>Click to see how this works!</summary>
This is an example of an expandable section. You can click on the summary above to expand or collapse this content. This feature allows you to focus on the main content while still having access to supplementary material when needed.
</details>

## Check your work

We should include knowledge checks. These can include more complicated answers that the Student will determine on their local machine over the course of real file manipulation.

{% include qa.html id="list_ls_human" %}

{% include qa.html id="print_working_directory" %}