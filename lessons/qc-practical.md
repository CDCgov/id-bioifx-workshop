---
layout: page
title: "NGS QC Knowledge Check"
sidebar: workshop_sidebar
topnav: topnav
permalink: /lessons/qc-practical/
---

<style>
.quiz-question {
  border: 2px solid var(--c-border, #d1d5db);
  border-radius: 8px;
  background: var(--c-bg-alt, #f9fafb);
  padding: 1.25rem 1.25rem 1rem;
  margin: 1.5rem 0;
  font-size: 1.7rem;
}
.quiz-question h4 { margin-top: 0; font-size: 1.3rem; }
.quiz-question label {
  display: block;
  padding: 0.4rem 0.6rem;
  margin: 0.25rem 0;
  border-radius: 4px;
  cursor: pointer;
}
.quiz-question label:hover {
  background: rgba(1, 92, 174, 0.06);
}
.quiz-question input[type="radio"] {
  margin-right: 0.5rem;
}
.quiz-btn {
  background: var(--c-accent, #015CAE);
  color: #fff;
  border: none;
  padding: 0.55rem 0.9rem;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 0.5rem;
}
.quiz-btn:disabled {
  opacity: 0.5;
  cursor: default;
}
.quiz-feedback {
  margin-top: 0.75rem;
  font-weight: 600;
  min-height: 1.5em;
}
.quiz-explanation {
  margin-top: 0.5rem;
  font-size: 1.5rem;
  background: var(--c-muted-bg, #f3f4f6);
  border: 1px solid var(--c-border, #d1d5db);
  padding: 0.75rem 0.85rem;
  border-radius: 6px;
  display: none;
}
.quiz-correct { color: var(--c-success, #16a34a); }
.quiz-incorrect { color: var(--c-error, #dc2626); }
#quiz-score-box {
  border: 2px solid var(--c-accent, #015CAE);
  border-radius: 8px;
  padding: 1.25rem;
  margin: 2rem 0;
  text-align: center;
  display: none;
}
#quiz-score-box h3 { margin-top: 0; }
#quiz-progress {
  font-size: 0.9rem;
  color: var(--c-text-alt, #6b7280);
  margin-bottom: 1rem;
  text-align: right;
}
</style>

# NGS QC Knowledge Check

Test your understanding of NGS quality control concepts. Select an answer for each question and click **Check** to see if you're correct. Your total score will appear at the end after all questions are answered.

<div id="quiz-progress">Answered: <span id="progress-count">0</span> / 15</div>

<!-- Question 1 -->
<div class="quiz-question" data-correct="d" id="q1">
<h4>1. Why is Quality Control important in Next-Generation Sequencing?</h4>
<label><input type="radio" name="q1" value="a"> a. NGS is expensive, so it's good to ensure your data is useful in global analyses</label>
<label><input type="radio" name="q1" value="b"> b. Erroneous sequencing data can disrupt phylogenetic analyses</label>
<label><input type="radio" name="q1" value="c"> c. High quality data is needed to confidently identify novel mutations</label>
<label><input type="radio" name="q1" value="d"> d. All of the above</label>
<button class="quiz-btn" onclick="checkAnswer('q1')">Check</button>
<div class="quiz-feedback" id="q1-feedback"></div>
<div class="quiz-explanation" id="q1-explanation">All of these are valid reasons. QC ensures that expensive sequencing runs produce reliable data, prevents erroneous bases from distorting phylogenetic trees, and provides the confidence needed to call novel mutations accurately.</div>
</div>

<!-- Question 2 -->
<div class="quiz-question" data-correct="c" id="q2">
<h4>2. What does Phred score measure?</h4>
<label><input type="radio" name="q2" value="a"> a. Read length</label>
<label><input type="radio" name="q2" value="b"> b. Alignment quality</label>
<label><input type="radio" name="q2" value="c"> c. Base quality</label>
<label><input type="radio" name="q2" value="d"> d. Genome completeness</label>
<label><input type="radio" name="q2" value="e"> e. The number of reads aligned</label>
<button class="quiz-btn" onclick="checkAnswer('q2')">Check</button>
<div class="quiz-feedback" id="q2-feedback"></div>
<div class="quiz-explanation" id="q2-explanation">Phred scores represent the probability of an incorrect base call. A Phred score of 30 means a 1 in 1,000 chance of error (99.9% accuracy). Higher scores indicate more confident base calls.</div>
</div>

<!-- Question 3 -->
<div class="quiz-question" data-correct="b" id="q3">
<h4>3. What does coverage depth measure?</h4>
<label><input type="radio" name="q3" value="a"> a. Read length</label>
<label><input type="radio" name="q3" value="b"> b. The number of reads aligned to a given position</label>
<label><input type="radio" name="q3" value="c"> c. Genome completeness</label>
<label><input type="radio" name="q3" value="d"> d. Base quality</label>
<label><input type="radio" name="q3" value="e"> e. Alignment quality</label>
<button class="quiz-btn" onclick="checkAnswer('q3')">Check</button>
<div class="quiz-feedback" id="q3-feedback"></div>
<div class="quiz-explanation" id="q3-explanation">Coverage depth (or read depth) measures how many sequencing reads align to (cover) a given position in the reference genome. Higher depth provides more confidence in base calls and variant detection.</div>
</div>

<!-- Question 4 -->
<div class="quiz-question" data-correct="b" id="q4">
<h4>4. What metadata is mandatory for public database submission?</h4>
<label><input type="radio" name="q4" value="a"> a. Clade and Collection Date</label>
<label><input type="radio" name="q4" value="b"> b. Collection date and location</label>
<label><input type="radio" name="q4" value="c"> c. Patient age, sex, and location</label>
<label><input type="radio" name="q4" value="d"> d. There is no mandatory metadata</label>
<button class="quiz-btn" onclick="checkAnswer('q4')">Check</button>
<div class="quiz-feedback" id="q4-feedback"></div>
<div class="quiz-explanation" id="q4-explanation">Public databases like GISAID require collection date and geographic location as mandatory metadata. Patient-level data (age, sex) is encouraged but not required, and clade is typically assigned by the database itself.</div>
</div>

<!-- Question 5 -->
<div class="quiz-question" data-correct="a" id="q5">
<h4>5. What kinds of files are viewed in IGV (Integrative Genomics Viewer)?</h4>
<label><input type="radio" name="q5" value="a"> a. .bam files</label>
<label><input type="radio" name="q5" value="b"> b. .fastq files</label>
<label><input type="radio" name="q5" value="c"> c. .fasta files</label>
<label><input type="radio" name="q5" value="d"> d. .vcf files</label>
<button class="quiz-btn" onclick="checkAnswer('q5')">Check</button>
<div class="quiz-feedback" id="q5-feedback"></div>
<div class="quiz-explanation" id="q5-explanation">IGV is primarily used to visualize .bam files (aligned reads). BAM files contain read alignments mapped to a reference genome, allowing you to inspect coverage, variants, and read quality at specific genomic positions.</div>
</div>

<!-- Question 6 -->
<div class="quiz-question" data-correct="b" id="q6">
<h4>6. True or false: if there is amplicon drop-out in the laboratory, you can use complex bioinformatics methods to infer the missing read data from your sample.</h4>
<label><input type="radio" name="q6" value="a"> a. True</label>
<label><input type="radio" name="q6" value="b"> b. False</label>
<button class="quiz-btn" onclick="checkAnswer('q6')">Check</button>
<div class="quiz-feedback" id="q6-feedback"></div>
<div class="quiz-explanation" id="q6-explanation"><strong>False.</strong> Missing read data should be assembled as missing (N's), NOT reference-filled. Bioinformatics methods cannot invent data that was not sequenced. Reference-filling creates false consensus sequences that can mislead downstream analyses and introduce artificial similarity to the reference.</div>
</div>

<!-- Question 7 -->
<div class="quiz-question" data-correct="a" id="q7">
<h4>7. What kinds of influenza samples should be sequenced?</h4>
<label><input type="radio" name="q7" value="a"> a. Random sampling, Ct &lt; 28</label>
<label><input type="radio" name="q7" value="b"> b. Outbreak samples, Ct &lt; 32</label>
<label><input type="radio" name="q7" value="c"> c. Any influenza-like-illness samples</label>
<button class="quiz-btn" onclick="checkAnswer('q7')">Check</button>
<div class="quiz-feedback" id="q7-feedback"></div>
<div class="quiz-explanation" id="q7-explanation">For routine surveillance, random sampling with a Ct value below 28 ensures sufficient viral genetic material for high-quality sequencing. Higher Ct values (lower viral load) often result in incomplete genomes with poor coverage.</div>
</div>

<!-- Question 8 -->
<div class="quiz-question" data-correct="c" id="q8">
<h4>8. Why does MIRA check the total number of minor variants as a QC metric?</h4>
<label><input type="radio" name="q8" value="a"> a. To track super-flu mutations</label>
<label><input type="radio" name="q8" value="b"> b. To detect reassortants</label>
<label><input type="radio" name="q8" value="c"> c. To detect contamination/co-infection</label>
<label><input type="radio" name="q8" value="d"> d. To track vaccine efficacy</label>
<button class="quiz-btn" onclick="checkAnswer('q8')">Check</button>
<div class="quiz-feedback" id="q8-feedback"></div>
<div class="quiz-explanation" id="q8-explanation">An unusually high number of minor variants across multiple segments is a strong indicator of contamination or co-infection — meaning reads from two different viral populations are mixed in the same sample. This is flagged as a QC warning.</div>
</div>

<!-- Question 9 -->
<div class="quiz-question" data-correct="b" id="q9">
<h4>9. Which BLAST database would be more complete for Influenza samples?</h4>
<label><input type="radio" name="q9" value="a"> a. NCBI</label>
<label><input type="radio" name="q9" value="b"> b. GISAID</label>
<button class="quiz-btn" onclick="checkAnswer('q9')">Check</button>
<div class="quiz-feedback" id="q9-feedback"></div>
<div class="quiz-explanation" id="q9-explanation">GISAID contains a more comprehensive collection of influenza sequences because many submitters share data exclusively through GISAID before (or instead of) depositing in NCBI GenBank. This makes GISAID the preferred database for influenza BLAST searches.</div>
</div>

<!-- Question 10 -->
<div class="quiz-question" data-correct="b" id="q10">
<h4>10. An Influenza B sample was collected from a human in France in December 2025 and was sequenced in January 2026. Its identifier is sample number A123. How should it be named?</h4>
<label><input type="radio" name="q10" value="a"> a. A/France/A123/2025</label>
<label><input type="radio" name="q10" value="b"> b. B/France/A123/2025</label>
<label><input type="radio" name="q10" value="c"> c. B/human/France/A123/2026</label>
<label><input type="radio" name="q10" value="d"> d. B/human/France/A123/2025</label>
<button class="quiz-btn" onclick="checkAnswer('q10')">Check</button>
<div class="quiz-feedback" id="q10-feedback"></div>
<div class="quiz-explanation" id="q10-explanation">The correct influenza strain naming convention is: <strong>Type/Location/Identifier/Collection Year</strong>. For human samples, the host is <em>omitted</em> from the strain name. Since this is Influenza B collected from a human, it is B/France/A123/2025. The <em>collection</em> year (2025) is used, not the sequencing year (2026). The host field is only included for non-human isolates (e.g., swine, avian).</div>
</div>

<!-- Question 11 -->
<div class="quiz-question" data-correct="a" id="q11">
<h4>11. In your lab, you receive an Influenza sample that tests positive on RT-PCR for both Influenza A H3 and Influenza A H1. What would this sample be considered?</h4>
<label><input type="radio" name="q11" value="a"> a. Co-infection</label>
<label><input type="radio" name="q11" value="b"> b. Contamination</label>
<label><input type="radio" name="q11" value="c"> c. Reassortant</label>
<button class="quiz-btn" onclick="checkAnswer('q11')">Check</button>
<div class="quiz-feedback" id="q11-feedback"></div>
<div class="quiz-explanation" id="q11-explanation"><strong>Co-infection.</strong> The patient is infected with two different Influenza A subtypes simultaneously (H3 and H1). This is detected at the RT-PCR stage before sequencing. Do not proceed with sequencing this sample — mixed populations will produce uninterpretable assemblies.</div>
</div>

<!-- Question 12 -->
<div class="quiz-question" data-correct="b" id="q12">
<h4>12. In your lab, you receive an Influenza sample that tests positive on RT-PCR for Influenza A H3. Following NGS, it assembles as H3N1 with a high minor variant count in all internal segments. What would this sample be considered?</h4>
<label><input type="radio" name="q12" value="a"> a. Co-infection</label>
<label><input type="radio" name="q12" value="b"> b. Contamination</label>
<label><input type="radio" name="q12" value="c"> c. Reassortant</label>
<button class="quiz-btn" onclick="checkAnswer('q12')">Check</button>
<div class="quiz-feedback" id="q12-feedback"></div>
<div class="quiz-explanation" id="q12-explanation"><strong>Contamination.</strong> The RT-PCR only detected H3, but the assembly shows a mismatched neuraminidase (N1 instead of the expected N2) along with high minor variants across all internal segments. This pattern indicates laboratory contamination — reads from a different sample (likely H1N1) were mixed in during library preparation or sequencing. Do not submit this genome to GISAID!</div>
</div>

<!-- Question 13 -->
<div class="quiz-question" data-correct="c" id="q13">
<h4>13. In your lab, you receive an Influenza sample that tests positive on RT-PCR for Influenza A H3. Following NGS, it assembles as H3N1 with a small number of minor variants. All QC metrics pass in MIRA. You BLAST each segment and all are H3N2-like except for the NA segment, which is H1N1-like. You re-sequence the sample and get the same results. What would this sample be considered?</h4>
<label><input type="radio" name="q13" value="a"> a. Co-infection</label>
<label><input type="radio" name="q13" value="b"> b. Contamination</label>
<label><input type="radio" name="q13" value="c"> c. Reassortant</label>
<button class="quiz-btn" onclick="checkAnswer('q13')">Check</button>
<div class="quiz-feedback" id="q13-feedback"></div>
<div class="quiz-explanation" id="q13-explanation"><strong>Reassortant!</strong> Key indicators: (1) QC metrics pass with low minor variants (clean assembly from a single population), (2) only ONE segment is mismatched (NA is H1N1-like while all others are H3N2-like), and (3) re-sequencing reproduces the same result. This virus acquired its NA segment from an H1N1 lineage through reassortment — a biologically real event worth reporting.</div>
</div>

<!-- Question 14 -->
<div class="quiz-question" data-correct="e" id="q14">
<h4>14. What kind of pre-assembly QC does the MIRA pipeline perform for you?</h4>
<label><input type="radio" name="q14" value="a"> a. Primer trimming</label>
<label><input type="radio" name="q14" value="b"> b. Quality filtering</label>
<label><input type="radio" name="q14" value="c"> c. Read length filtering</label>
<label><input type="radio" name="q14" value="d"> d. Optional running of FastQC and MultiQC</label>
<label><input type="radio" name="q14" value="e"> e. All of the above</label>
<button class="quiz-btn" onclick="checkAnswer('q14')">Check</button>
<div class="quiz-feedback" id="q14-feedback"></div>
<div class="quiz-explanation" id="q14-explanation">MIRA performs all of these pre-assembly QC steps: it trims primer sequences, filters reads by quality score, removes reads that are too short, and can optionally generate FastQC/MultiQC reports for manual review of raw read quality.</div>
</div>

<!-- Question 15 -->
<div class="quiz-question" data-correct="e" id="q15">
<h4>15. What kind of post-assembly QC does the MIRA pipeline perform for you?</h4>
<label><input type="radio" name="q15" value="a"> a. Contamination checking</label>
<label><input type="radio" name="q15" value="b"> b. Coverage depth thresholds</label>
<label><input type="radio" name="q15" value="c"> c. Completeness thresholds</label>
<label><input type="radio" name="q15" value="d"> d. Premature stop codons</label>
<label><input type="radio" name="q15" value="e"> e. All of the above</label>
<button class="quiz-btn" onclick="checkAnswer('q15')">Check</button>
<div class="quiz-feedback" id="q15-feedback"></div>
<div class="quiz-explanation" id="q15-explanation">MIRA performs all of these post-assembly QC checks: it screens for contamination via minor variant counts, enforces minimum coverage depth thresholds, checks genome completeness, and scans coding regions for premature stop codons that may indicate assembly errors or pseudogenes.</div>
</div>

<!-- Score Box -->
<div id="quiz-score-box">
<h3>🎉 Quiz Complete!</h3>
<p id="quiz-score-text"></p>
<div id="quiz-score-bar-container" style="background:#e5e7eb;border-radius:6px;height:24px;margin:1rem auto;max-width:400px;overflow:hidden;">
<div id="quiz-score-bar" style="height:100%;border-radius:6px;transition:width 0.5s;"></div>
</div>
<p id="quiz-score-message" style="font-size:1.1rem;"></p>
<button class="quiz-btn" onclick="resetQuiz()" style="margin-top:0.5rem;">Retake Quiz</button>
</div>

<script>
(function(){
  const totalQuestions = 15;
  let answered = {};

  window.checkAnswer = function(qId) {
    const container = document.getElementById(qId);
    if (answered[qId] !== undefined) return; // already answered

    const selected = container.querySelector('input[type="radio"]:checked');
    const feedback = document.getElementById(qId + '-feedback');
    const explanation = document.getElementById(qId + '-explanation');

    if (!selected) {
      feedback.textContent = 'Please select an answer first.';
      feedback.className = 'quiz-feedback';
      return;
    }

    const correct = container.dataset.correct;
    const userAnswer = selected.value;

    // Disable all radios
    container.querySelectorAll('input[type="radio"]').forEach(function(r){ r.disabled = true; });
    container.querySelector('.quiz-btn').disabled = true;

    if (userAnswer === correct) {
      feedback.textContent = '✅ Correct!';
      feedback.className = 'quiz-feedback quiz-correct';
      answered[qId] = true;
    } else {
      feedback.textContent = '❌ Incorrect. The correct answer is ' + correct.toUpperCase() + '.';
      feedback.className = 'quiz-feedback quiz-incorrect';
      answered[qId] = false;
    }

    explanation.style.display = 'block';

    // Update progress
    var count = Object.keys(answered).length;
    document.getElementById('progress-count').textContent = count;

    // Show score if all done
    if (count === totalQuestions) {
      showScore();
    }
  };

  function showScore() {
    var correctCount = Object.values(answered).filter(function(v){ return v; }).length;
    var pct = Math.round((correctCount / totalQuestions) * 100);
    var scoreBox = document.getElementById('quiz-score-box');
    var scoreText = document.getElementById('quiz-score-text');
    var scoreBar = document.getElementById('quiz-score-bar');
    var scoreMsg = document.getElementById('quiz-score-message');

    scoreText.textContent = 'You scored ' + correctCount + ' out of ' + totalQuestions + ' (' + pct + '%)';

    var color = pct >= 80 ? '#16a34a' : pct >= 60 ? '#ca8a04' : '#dc2626';
    scoreBar.style.width = pct + '%';
    scoreBar.style.background = color;

    if (pct === 100) {
      scoreMsg.textContent = 'Perfect score! Excellent understanding of NGS QC concepts.';
    } else if (pct >= 80) {
      scoreMsg.textContent = 'Great job! You have a strong grasp of QC principles.';
    } else if (pct >= 60) {
      scoreMsg.textContent = 'Good effort! Review the explanations above for the questions you missed.';
    } else {
      scoreMsg.textContent = 'Consider reviewing the QC module materials and trying again.';
    }

    scoreBox.style.display = 'block';
    scoreBox.scrollIntoView({ behavior: 'smooth' });
  }

  window.resetQuiz = function() {
    answered = {};
    document.querySelectorAll('.quiz-question').forEach(function(q){
      q.querySelectorAll('input[type="radio"]').forEach(function(r){ r.disabled = false; r.checked = false; });
      q.querySelector('.quiz-btn').disabled = false;
    });
    document.querySelectorAll('.quiz-feedback').forEach(function(f){ f.textContent = ''; f.className = 'quiz-feedback'; });
    document.querySelectorAll('.quiz-explanation').forEach(function(e){ e.style.display = 'none'; });
    document.getElementById('progress-count').textContent = '0';
    document.getElementById('quiz-score-box').style.display = 'none';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };
})();
</script>