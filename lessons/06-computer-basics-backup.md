---
layout: page
title: Computer Basics
nav_order: 2
---

{% capture section_overview_1 %}

Understanding how computers work is essential for bioinformaticians who need to optimize pipelines, troubleshoot performance issues, and choose appropriate computational resources.

{% endcapture %}

{% capture section_body_1 %}

## **Why Computer Architecture Matters for Bioinformatics**

Bioinformatics workflows often involve:
- Processing **gigabytes to terabytes** of sequencing data
- Running computationally intensive algorithms (alignment, assembly, variant calling)
- Managing memory for large reference genomes and indices
- Parallelizing tasks across multiple CPU cores

Understanding the underlying hardware helps you:

| Scenario | Knowledge Applied |
|----------|-------------------|
| Pipeline runs slowly | Is it CPU-bound or I/O-bound? |
| "Out of memory" errors | How much RAM does the tool need? Can you use disk-based alternatives? |
| Choosing cloud instances | How many cores? How much memory? SSD vs HDD? |
| Optimizing tool parameters | Thread count, memory limits, temp directory location |

<div class="alert alert-info">
<strong>Key insight:</strong> Most bioinformatics bottlenecks come from either <strong>memory limitations</strong> (not enough RAM) or <strong>I/O bottlenecks</strong> (slow disk reads/writes), not CPU speed.
</div>

{% endcapture %}



{% capture section_overview_2 %}

A visual overview of how the major components of a computer system relate to each other.

{% endcapture %}

{% capture section_body_2 %}

## **Computer Architecture Overview**

The diagram below shows the main components of a computer and how they interact:

<style>
  /* ============================================================================
     Computer Architecture Diagram — scoped styles
     ============================================================================ */
  .diagram-wrap{
    position: relative;
    max-width: 1100px;
    margin: 0 auto;
    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #0b1b2b;
  }

  .diagram-computer{
    position: relative;
    background: #ECF5FF;
    border: 2px solid #032659;
    border-radius: 20px;
    box-shadow: 0 8px 18px rgba(3,38,89,0.10);
    padding: 24px;
  }

  .diagram-computer .d-title{
    font-weight: 800; color: #032659; margin: 0 0 16px; font-size: 18px;
  }

  /* OS pill — centered */
  .d-os-wrap{
    text-align: center;
    margin: 0 0 70px 0;
  }
  .d-os{
    display: inline-block;
    background: #3382CF; color: #fff; border: 2px solid #032659;
    border-radius: 14px; padding: 12px 24px; font-weight: 800;
    position: relative; z-index: 2;
  }

  /* 2-column grid */
  .d-layout{
    display: grid; grid-template-columns: 1.15fr 0.85fr;
    gap: 30px; align-items: start;
  }
  @media(max-width:920px){
    .d-layout{ grid-template-columns:1fr; }
    .d-core-grid{ grid-template-columns:1fr !important; }
  }

  /* Generic box */
  .d-box{ border-radius: 14px; padding: 18px; border: 2px solid transparent; background: #fff; }
  .d-label{ font-weight: 800; margin: 0 0 14px; font-size: 14px; }

  /* Hardware */
  .d-hardware{ background: #D5F7F9; border-color: #0081A1; color: #125261; }

  /* Firmware */
  .d-firmware{ background: #fff; border: 2px solid #47264F; border-radius: 14px; padding: 14px; margin-bottom: 24px; }
  .d-firmware .d-label{ color: #47264F; }
  .d-uefi{
    display: inline-block; padding: 10px 12px; border-radius: 12px;
    background: #8F4A8F; color: #fff; border: 2px solid #47264F; font-weight: 800;
    position: relative; z-index: 2;
  }

  /* Core compute */
  .d-core{ background: #fff; border: 2px solid #0081A1; border-radius: 14px; padding: 14px; }
  .d-core .d-label{ color: #125261; }
  .d-core-grid{ display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 36px; align-items: start; }

  /* CPU */
  .d-cpu{
    background: #00B1CE; color: #fff; border: 2px solid #125261;
    border-radius: 14px; padding: 12px; position: relative; z-index: 2;
  }
  .d-cpu .d-label{ color: #fff; margin-bottom: 8px; }
  .d-caches{ display: flex; flex-direction: column; gap: 6px; align-items: stretch; }
  .d-cache-row{ display: flex; align-items: center; gap: 6px; }
  .d-cache{
    background: #7DDEEC; color: #125261; border: 2px solid #0081A1;
    border-radius: 999px; padding: 6px 10px; font-weight: 800; font-size: 12px; white-space: nowrap;
    flex: 1; text-align: center;
  }
  .d-cache-arrow{
    font-weight: 900; opacity: .9; font-size: 16px; color: #125261; line-height: 1;
    text-align: center;
  }

  /* RAM */
  .d-ram{
    background: #AEECF2; border: 2px solid #0081A1; color: #125261;
    border-radius: 14px; padding: 12px; font-weight: 800; margin-bottom: 40px;
    position: relative; z-index: 2;
  }

  /* Disk */
  .d-disk{
    background: #D5F7F9; border: 2px solid #0081A1; color: #125261;
    border-radius: 14px; padding: 12px; position: relative; z-index: 2;
  }
  .d-disk .d-label{ color: #125261; }
  .d-disk-inner{ display: grid; gap: 14px; }
  .d-storage{
    background: #fff; border: 2px solid #0081A1; border-radius: 12px;
    padding: 10px 12px; font-weight: 800; color: #125261; position: relative; z-index: 2;
  }

  /* Peripherals */
  .d-peripherals{ background: #fff; border: 2px solid #975722; border-radius: 14px; padding: 18px; }
  .d-peripherals .d-label{ color: #975722; }
  .d-pgrid{ display: grid; gap: 16px; }
  .d-pitem{
    background: #FCCF85; border: 2px solid #975722; color: #975722;
    border-radius: 12px; padding: 10px 12px; font-weight: 900; position: relative; z-index: 2;
  }
  .d-pitem.d-network{
    background: #FF9C63; border-color: #944521; color: #944521;
  }

  /* USB Controller as a container with sub-devices */
  .d-usb-group{
    background: #FCCF85; border: 2px solid #975722; border-radius: 12px;
    padding: 12px; position: relative; z-index: 2;
  }
  .d-usb-group .d-usb-label{
    font-weight: 900; color: #975722; margin: 0 0 10px; font-size: 14px;
  }
  .d-usb-devices{
    display: grid; gap: 10px;
  }
  .d-usb-device{
    background: #FFF3DC; border: 2px solid #C8943A; color: #7A5B1E;
    border-radius: 10px; padding: 8px 12px; font-weight: 800; font-size: 13px;
    position: relative; z-index: 2;
  }

  /* SVG arrow canvas */
  .d-arrows{
    position: absolute;
    top: 0; left: 0;
    pointer-events: none;
    z-index: 1;
    overflow: visible;
  }

  /* Legend */
  .d-legend{
    margin-top: 14px; display: flex; flex-wrap: wrap; gap: 10px 14px;
    align-items: center; color: #032659; font-weight: 700; font-size: 12px;
  }
  .d-swatch{
    width: 14px; height: 14px; border-radius: 4px; border: 2px solid rgba(0,0,0,.15);
    display: inline-block; vertical-align: middle; margin-right: 6px;
  }
  .d-note{
    margin-top: 10px; color: #25425f; font-size: 12px; line-height: 1.35;
  }
</style>

<div class="diagram-wrap">
  <div class="diagram-computer" id="dia-computer">
    <div class="d-title">Computer</div>

    <div class="d-os-wrap">
      <div class="d-os" id="dia-os">Operating System</div>
    </div>

    <div class="d-layout">
      <!-- Hardware column -->
      <div class="d-box d-hardware">
        <div class="d-label">Hardware</div>

        <div class="d-firmware">
          <div class="d-label">Firmware</div>
          <div class="d-uefi" id="dia-uefi">UEFI / BIOS</div>
        </div>

        <div class="d-core">
          <div class="d-label">Core Compute Hardware</div>
          <div class="d-core-grid">
            <div>
              <div class="d-cpu" id="dia-cpu">
                <div class="d-label">CPU</div>
                <div class="d-caches">
                  <span class="d-cache">L1 Cache</span>
                  <div class="d-cache-arrow">↓</div>
                  <span class="d-cache">L2 Cache</span>
                  <div class="d-cache-arrow">↓</div>
                  <span class="d-cache" id="dia-l3">L3 Cache</span>
                </div>
              </div>
            </div>
            <div>
              <div class="d-ram" id="dia-ram">Physical RAM</div>
              <div class="d-disk" id="dia-disk">
                <div class="d-label">Hard Drive / SSD</div>
                <div class="d-disk-inner">
                  <div class="d-storage" id="dia-vmem">Virtual Memory</div>
                  <div class="d-storage" id="dia-pstore">Permanent Storage</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Peripherals column -->
      <div class="d-box d-peripherals">
        <div class="d-label">Peripherals</div>
        <div class="d-pgrid">
          <div class="d-pitem d-network" id="dia-net">Network</div>
          <div class="d-pitem" id="dia-mon">Monitor</div>
          <div class="d-usb-group" id="dia-usb">
            <div class="d-usb-label">USB Controller</div>
            <div class="d-usb-devices">
              <div class="d-usb-device" id="dia-kbd">⌨ Keyboard</div>
              <div class="d-usb-device" id="dia-mouse">🖱 Mouse</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="d-legend">
      <span><span class="d-swatch" style="background:#8F4A8F;border-color:#47264F"></span>Firmware</span>
      <span><span class="d-swatch" style="background:#3382CF;border-color:#032659"></span>Operating System</span>
      <span><span class="d-swatch" style="background:#D5F7F9;border-color:#0081A1"></span>Hardware</span>
      <span><span class="d-swatch" style="background:#FCCF85;border-color:#975722"></span>Peripherals</span>
      <span><span class="d-swatch" style="background:#FFF3DC;border-color:#C8943A"></span>USB Devices</span>
      <span><span class="d-swatch" style="background:#FF9C63;border-color:#944521"></span>Network</span>
    </div>

    <div class="d-note">
      Dashed arrows = boot-time initialization by firmware.
      Solid arrows = runtime control through the OS.
      ↔ = bidirectional data flow.
    </div>

    <!-- SVG canvas for connectors — dynamically sized by JS -->
    <svg class="d-arrows" id="dia-arrows" aria-hidden="true">
      <defs>
        <marker id="mk-blue" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="#032659"/></marker>
        <marker id="mk-teal" markerWidth="7" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6z" fill="#125261"/></marker>
        <marker id="mk-teal-rev" markerWidth="7" markerHeight="6" refX="1" refY="3" orient="auto"><path d="M7 0 L0 3 L7 6z" fill="#125261"/></marker>
        <marker id="mk-purple" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="#47264F"/></marker>
        <marker id="mk-orange" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="#975722"/></marker>
      </defs>
    </svg>
  </div>
</div>

<script>
(function(){
  var root = document.getElementById('dia-computer');
  var svg  = document.getElementById('dia-arrows');
  if(!root || !svg) return;

  function pos(id){
    var el = document.getElementById(id);
    if(!el) return null;
    var er = el.getBoundingClientRect();
    var rr = root.getBoundingClientRect();
    return { x: er.left - rr.left, y: er.top - rr.top, w: er.width, h: er.height };
  }

  function posEl(el){
    if(!el) return null;
    var er = el.getBoundingClientRect();
    var rr = root.getBoundingClientRect();
    return { x: er.left - rr.left, y: er.top - rr.top, w: er.width, h: er.height };
  }

  function edge(r, side, off){
    off = off || 0;
    var cx = r.x + r.w/2, cy = r.y + r.h/2;
    if(side==='top')    return {x: cx+off, y: r.y};
    if(side==='bottom') return {x: cx+off, y: r.y+r.h};
    if(side==='left')   return {x: r.x,    y: cy+off};
    if(side==='right')  return {x: r.x+r.w,y: cy+off};
  }

  function wpPath(pts){
    var d = 'M'+pts[0].x+' '+pts[0].y;
    for(var i=1; i<pts.length; i++) d += ' L'+pts[i].x+' '+pts[i].y;
    return d;
  }

  function mkPath(d, stroke, width, marker, dash, markerStart){
    var p = document.createElementNS('http://www.w3.org/2000/svg','path');
    p.setAttribute('d', d);
    p.setAttribute('fill', 'none');
    p.setAttribute('stroke', stroke);
    p.setAttribute('stroke-width', width||2);
    p.setAttribute('stroke-linecap', 'round');
    p.setAttribute('stroke-linejoin', 'round');
    if(dash) p.setAttribute('stroke-dasharray', dash);
    if(marker) p.setAttribute('marker-end', 'url(#'+marker+')');
    if(markerStart) p.setAttribute('marker-start', 'url(#'+markerStart+')');
    svg.appendChild(p);
  }

  function mkText(x, y, txt, color){
    var t = document.createElementNS('http://www.w3.org/2000/svg','text');
    t.setAttribute('x',x); t.setAttribute('y',y);
    t.setAttribute('fill', color||'#25425f');
    t.setAttribute('font-size','11'); t.setAttribute('font-weight','700');
    t.textContent = txt;
    svg.appendChild(t);
  }

  function drawLine(pts, cfg){
    var d = wpPath(pts);
    mkPath(d, cfg.color, cfg.w||2, cfg.mk, cfg.dash, cfg.mkStart);
    if(cfg.label){
      var segs = [], totalLen = 0;
      for(var i=1; i<pts.length; i++){
        var dx = pts[i].x - pts[i-1].x, dy = pts[i].y - pts[i-1].y;
        var len = Math.sqrt(dx*dx + dy*dy);
        segs.push({from:pts[i-1], to:pts[i], len:len});
        totalLen += len;
      }
      var half = totalLen / 2, accum = 0;
      for(var j=0; j<segs.length; j++){
        if(accum + segs[j].len >= half){
          var t = (half - accum) / segs[j].len;
          var mx = segs[j].from.x + t*(segs[j].to.x - segs[j].from.x);
          var my = segs[j].from.y + t*(segs[j].to.y - segs[j].from.y);
          mkText(mx + 6, my - 6, cfg.label, cfg.color);
          break;
        }
        accum += segs[j].len;
      }
    }
  }

  function render(){
    svg.querySelectorAll('path:not(defs path), text').forEach(function(n){ n.remove(); });
    var rr = root.getBoundingClientRect();
    svg.setAttribute('width',  rr.width);
    svg.setAttribute('height', rr.height);
    svg.setAttribute('viewBox','0 0 '+rr.width+' '+rr.height);

    var os   = pos('dia-os');
    var uefi = pos('dia-uefi');
    var cpu  = pos('dia-cpu');
    var l3   = pos('dia-l3');
    var ram  = pos('dia-ram');
    var disk = pos('dia-disk');
    var net  = pos('dia-net');
    var usb  = pos('dia-usb');
    var mon  = pos('dia-mon');
    if(!os||!uefi||!cpu||!l3||!ram||!disk||!net||!usb||!mon) return;

    var hwEl  = document.querySelector('.d-hardware');
    var perEl = document.querySelector('.d-peripherals');
    var hw    = hwEl  ? posEl(hwEl)  : null;
    var per   = perEl ? posEl(perEl) : null;
    if(!hw||!per) return;

    var BLUE='#032659', TEAL='#125261', PURPLE='#47264F', PAD=14;
    var chanY_cpu=hw.y-PAD, chanY_boot=hw.y-PAD-16, chanY_ram=hw.y-PAD-32, leftOfHw=hw.x-PAD;

    // Boot handoff
    var a=edge(uefi,'top'), b=edge(os,'bottom',5);
    drawLine([a,{x:a.x,y:chanY_boot},{x:b.x,y:chanY_boot},b],{color:PURPLE,mk:'mk-purple',dash:'6 4',w:2,label:'Boot handoff'});

    // Firmware → CPU, RAM
    a=edge(uefi,'bottom',-15); b=edge(cpu,'top',0);
    drawLine([a,{x:a.x,y:a.y+14},{x:b.x,y:a.y+14},b],{color:PURPLE,mk:'mk-purple',dash:'6 4',w:1.5});
    a=edge(uefi,'right'); b=edge(ram,'top',-20);
    drawLine([a,{x:b.x,y:a.y},b],{color:PURPLE,mk:'mk-purple',dash:'6 4',w:1.5});

    // OS → CPU
    a=edge(os,'bottom',-60); b=edge(cpu,'left',0);
    drawLine([a,{x:a.x,y:chanY_cpu},{x:leftOfHw,y:chanY_cpu},{x:leftOfHw,y:b.y},b],{color:BLUE,mk:'mk-blue',w:2});

    // OS → RAM
    a=edge(os,'bottom',-20); b=edge(ram,'top',20);
    drawLine([a,{x:a.x,y:chanY_ram},{x:b.x,y:chanY_ram},b],{color:BLUE,mk:'mk-blue',w:2});

    // OS → Peripherals
    var gapStart=hw.x+hw.w, gapEnd=per.x, gapW=gapEnd-gapStart;
    var gapX1=gapStart+gapW*0.2, gapX2=gapStart+gapW*0.5, gapX3=gapStart+gapW*0.8;
    a=edge(os,'right',-10); b=edge(net,'left');
    drawLine([a,{x:gapX1,y:a.y},{x:gapX1,y:b.y},b],{color:BLUE,mk:'mk-blue',w:2});
    a=edge(os,'right',0); b=edge(mon,'left');
    drawLine([a,{x:gapX2,y:a.y},{x:gapX2,y:b.y},b],{color:BLUE,mk:'mk-blue',w:2});
    a=edge(os,'right',10); b=edge(usb,'left');
    var gap=5;
    drawLine([{x:a.x,y:a.y-gap},{x:gapX3-4,y:a.y-gap},{x:gapX3-4,y:b.y-gap},{x:b.x,y:b.y-gap}],{color:BLUE,mk:'mk-blue',w:1.8});
    drawLine([{x:b.x,y:b.y+gap},{x:gapX3+4,y:b.y+gap},{x:gapX3+4,y:a.y+gap},{x:a.x,y:a.y+gap}],{color:BLUE,mk:'mk-blue',w:1.8});

    // CPU ↔ RAM
    a=edge(cpu,'right',0); b=edge(ram,'left',0);
    var gapMidX=(a.x+b.x)/2, cpuMidY=a.y, ramMidY=ram.y+ram.h/2;
    drawLine([a,{x:gapMidX-4,y:cpuMidY},{x:gapMidX-4,y:ramMidY-6},{x:b.x,y:ramMidY-6}],{color:TEAL,mk:'mk-teal',w:2});
    drawLine([{x:b.x,y:ramMidY+6},{x:gapMidX+4,y:ramMidY+6},{x:gapMidX+4,y:cpuMidY+12},{x:a.x,y:cpuMidY+12}],{color:TEAL,mk:'mk-teal',w:2});

    // RAM ↔ Disk
    a=edge(ram,'bottom',0); b=edge(disk,'top',0);
    var gapMidY=(a.y+b.y)/2, ramCX=ram.x+ram.w/2;
    drawLine([{x:ramCX-8,y:a.y},{x:ramCX-8,y:gapMidY-4},{x:ramCX-16,y:gapMidY-4},{x:ramCX-16,y:b.y}],{color:TEAL,mk:'mk-teal',w:2});
    drawLine([{x:ramCX+16,y:b.y},{x:ramCX+16,y:gapMidY+4},{x:ramCX+8,y:gapMidY+4},{x:ramCX+8,y:a.y}],{color:TEAL,mk:'mk-teal',w:2});
  }

  function go(){ requestAnimationFrame(render); }
  window.addEventListener('load', go);
  window.addEventListener('resize', go);
  if(typeof ResizeObserver !== 'undefined'){ new ResizeObserver(go).observe(root); }
  setTimeout(go, 200);
  setTimeout(go, 600);
})();
</script>

{% endcapture %}



{% capture section_overview_3 %}

The CPU is the "brain" of the computer. Understanding CPU architecture helps optimize multi-threaded bioinformatics tools.

{% endcapture %}

{% capture section_body_3 %}

## **The CPU (Central Processing Unit)**

### 3.1 What the CPU does

The CPU executes instructions — the fundamental operations that make up all software. For bioinformatics, this includes:
- Comparing nucleotide sequences character by character
- Calculating alignment scores
- Traversing suffix arrays and BWT indices
- Evaluating quality score thresholds

### 3.2 Cores and threads

Modern CPUs have multiple **cores** — independent processing units that can work in parallel:

| Term | Definition | Bioinformatics relevance |
|------|------------|-------------------------|
| **Core** | A physical processing unit | Each core can run one task at a time |
| **Thread** | A virtual execution stream | Hyperthreading gives 2 threads per core |
| **Multi-threading** | Using multiple threads | `-t 8` in BWA-MEM uses 8 threads |

<div class="alert alert-info">
<strong>Rule of thumb:</strong> Set thread count to the number of <em>physical cores</em>, not threads. On a 4-core/8-thread CPU, use <code>-t 4</code> for CPU-intensive tasks.
</div>

### 3.3 CPU cache hierarchy

Data must travel from RAM to the CPU to be processed. **CPU caches** are small, ultra-fast memory buffers that store frequently accessed data:

| Cache | Size (typical) | Speed | Purpose |
|-------|----------------|-------|---------|
| **L1** | 32-64 KB per core | Fastest | Currently executing instructions |
| **L2** | 256-512 KB per core | Very fast | Recent data per core |
| **L3** | 8-64 MB shared | Fast | Shared across all cores |
| **RAM** | 8-256+ GB | Slower | Main working memory |

The CPU automatically manages this hierarchy — when it needs data not in cache, it fetches it from RAM (a "cache miss"), which is slower.

<div class="alert alert-warning">
<strong>Bioinformatics insight:</strong> Tools that access data randomly (like hash tables) cause more cache misses than tools that process data sequentially (like streaming through a FASTQ file).
</div>

### 3.4 Checking your CPU

**Linux/WSL:**
```bash
# Number of cores
nproc

# Detailed CPU info
lscpu

# Or from /proc
cat /proc/cpuinfo | grep "model name" | head -1
cat /proc/cpuinfo | grep "cpu cores" | head -1
```

**macOS:**
```bash
sysctl -n hw.ncpu          # Total threads
sysctl -n hw.physicalcpu   # Physical cores
```

{% endcapture %}



{% capture section_overview_4 %}

RAM (Random Access Memory) is the computer's working memory. It's often the limiting factor for bioinformatics workflows.

{% endcapture %}

{% capture section_body_4 %}

## **Memory (RAM)**

### 4.1 What RAM does

RAM holds data that the CPU is actively working with:
- The genome sequence being aligned against
- Index structures (FM-index, hash tables)
- Reads currently being processed
- Intermediate results

When you load a reference genome into a tool like BWA, it gets loaded into RAM. The larger the reference or index, the more RAM required.

### 4.2 Common memory requirements

| Task | Typical RAM needed |
|------|-------------------|
| Aligning to human genome (BWA-MEM2) | 8-16 GB |
| *De novo* assembly (SPAdes, small genome) | 16-32 GB |
| *De novo* assembly (SPAdes, large genome) | 64-256+ GB |
| Variant calling (GATK) | 8-32 GB |
| Metagenomics classification (Kraken2) | 8-64 GB (depends on database) |

### 4.3 Virtual memory and swap

When RAM runs out, the operating system uses **virtual memory** — disk space that pretends to be RAM:

- Also called "swap" (Linux) or "page file" (Windows)
- **Much slower** than real RAM (100-1000x slower)
- Causes severe performance degradation ("thrashing")

<div class="alert alert-danger">
<strong>Warning:</strong> If your bioinformatics job starts using swap heavily, it may take 10-100x longer to complete. Either reduce memory usage or get more RAM.
</div>

### 4.4 Checking memory usage

**Linux/WSL:**
```bash
# Quick overview
free -h

# Detailed memory info
cat /proc/meminfo | head -10

# Watch memory in real-time
htop   # or: watch -n 1 free -h
```

**macOS:**
```bash
# Memory summary
vm_stat

# More readable
top -l 1 | head -n 10
```

### 4.5 Reducing memory usage

When RAM is limited:

1. **Use streaming algorithms** — Process reads one at a time instead of loading all into memory
2. **Reduce thread count** — Each thread may need its own memory buffer
3. **Use disk-based alternatives** — Some tools offer memory-efficient modes
4. **Split input files** — Process in chunks, merge results
5. **Use a cluster/cloud** — Rent machines with more RAM

{% endcapture %}



{% capture section_overview_5 %}

Storage holds data permanently, but speed varies dramatically between disk types.

{% endcapture %}

{% capture section_body_5 %}

## **Storage (Disk)**

### 5.1 Storage types

| Type | Speed | Cost | Use case |
|------|-------|------|----------|
| **NVMe SSD** | 3,000-7,000 MB/s | $$$ | Operating system, active projects |
| **SATA SSD** | 500-600 MB/s | $$ | General purpose, good balance |
| **HDD** | 100-200 MB/s | $ | Archival storage, backups |
| **Network storage** | Variable (1-1000 MB/s) | Variable | Shared data, depends on network |

### 5.2 Impact on bioinformatics

Many workflows are **I/O bound** — they spend more time reading/writing data than computing:

- Writing millions of SAM/BAM alignment records
- Reading large FASTQ files
- Sorting and indexing BAM files
- Building and querying databases

<div class="alert alert-info">
<strong>Tip:</strong> If possible, keep your working data on an SSD. The speed difference is dramatic for I/O-heavy operations like sorting BAM files.
</div>

### 5.3 Checking disk space and speed

**Linux/WSL:**
```bash
# Disk space
df -h

# Which disk a directory is on
df -h /path/to/directory

# Simple write speed test
dd if=/dev/zero of=testfile bs=1G count=1 oflag=direct 2>&1 | tail -1

# Clean up
rm testfile
```

### 5.4 Storage best practices

1. **Use SSDs for temp files** — Set `$TMPDIR` or tool-specific temp directories to SSD
2. **Compress when possible** — Gzipped FASTQ takes 3-4x less space and often processes faster
3. **Clean up intermediate files** — BAM files from failed runs, temp files, etc.
4. **Archive completed projects** — Move to cheaper HDD or tape storage

{% endcapture %}



{% capture section_overview_6 %}

The operating system manages hardware resources and provides the environment where bioinformatics tools run.

{% endcapture %}

{% capture section_body_6 %}

## **Operating System**

### 6.1 Role of the OS

The operating system:
- **Manages memory** — Allocates RAM to programs, handles virtual memory
- **Schedules CPU** — Decides which processes run on which cores
- **Handles I/O** — Coordinates disk reads/writes, network traffic
- **Provides interfaces** — File systems, command line, software installation

### 6.2 Linux dominance in bioinformatics

Most bioinformatics tools are designed for Linux:

| OS | Bioinformatics support |
|----|----------------------|
| **Linux (Ubuntu, CentOS, etc.)** | Excellent — most tools native |
| **macOS** | Good — Unix-based, most tools work |
| **Windows** | Limited — use WSL for Linux tools |

<div class="alert alert-info">
<strong>WSL (Windows Subsystem for Linux)</strong> lets you run a full Linux environment inside Windows, giving you access to the Linux bioinformatics ecosystem.
</div>

### 6.3 Key OS concepts

**File systems:**
- Linux uses paths like `/home/user/data/`
- Windows uses paths like `C:\Users\user\data\`
- WSL bridges both: `/mnt/c/Users/` accesses Windows files from Linux

**Environment variables:**
- `$PATH` — Where the shell looks for executables
- `$HOME` — Your home directory
- `$TMPDIR` — Where temporary files go

**Package managers:**
- **conda/mamba** — Cross-platform, recommended for bioinformatics
- **apt** (Ubuntu/Debian) — System packages
- **brew** (macOS) — macOS packages

### 6.4 Checking system info

```bash
# OS version
cat /etc/os-release    # Linux
sw_vers                 # macOS

# Kernel version
uname -r

# All system info summary
neofetch   # if installed, fun visualization
```

{% endcapture %}



{% capture section_overview_7 %}

Practical guidance for choosing hardware and computational resources for bioinformatics work.

{% endcapture %}

{% capture section_body_7 %}

## **Putting It All Together**

### 7.1 Minimum specs for bioinformatics

| Component | Minimum | Recommended | Heavy workloads |
|-----------|---------|-------------|-----------------|
| **CPU** | 4 cores | 8+ cores | 16-32+ cores |
| **RAM** | 8 GB | 32 GB | 64-256+ GB |
| **Storage** | 256 GB SSD | 1 TB SSD | 2+ TB NVMe SSD |

### 7.2 Diagnosing performance issues

When something runs slowly, ask:

1. **Is CPU at 100%?** → CPU-bound, consider more cores or faster algorithm
2. **Is RAM full / swapping?** → Memory-bound, reduce usage or get more RAM
3. **Is disk activity constant but CPU idle?** → I/O-bound, use faster storage
4. **Is network activity the bottleneck?** → Download data locally first

**Monitoring tools:**
```bash
htop          # Interactive process viewer (CPU, RAM per process)
iotop         # Disk I/O by process (requires sudo)
nmon          # All-in-one system monitor
```

### 7.3 When to use cloud/cluster

Consider external compute when:
- Job needs more RAM than your machine has
- Job would take days on your laptop
- You need to run many jobs in parallel
- You need specialized hardware (GPUs for ML)

Common platforms:
- **Institutional HPC clusters** — Often free for researchers
- **AWS, Google Cloud, Azure** — Pay per hour, flexible
- **Galaxy, Terra, DNAnexus** — Bioinformatics-specific platforms

### 7.4 Summary checklist

Before running a pipeline:

- [ ] Do I have enough **RAM** for the largest step?
- [ ] Do I have enough **disk space** for inputs, outputs, and temp files?
- [ ] Is my working directory on **fast storage** (SSD)?
- [ ] Have I set appropriate **thread counts** for my CPU?
- [ ] Do I know where **temp files** will be written?

{% endcapture %}

{% include activity.html variant="1" title="Part 1: Why This Matters" overview=section_overview_1 content=section_body_1 %}
{% include activity.html variant="2" title="Part 2: Architecture Overview" overview=section_overview_2 content=section_body_2 %}
{% include activity.html variant="3" title="Part 3: The CPU" overview=section_overview_3 content=section_body_3 %}
{% include activity.html variant="1" title="Part 4: Memory (RAM)" overview=section_overview_4 content=section_body_4 %}
{% include activity.html variant="2" title="Part 5: Storage" overview=section_overview_5 content=section_body_5 %}
{% include activity.html variant="3" title="Part 6: Operating System" overview=section_overview_6 content=section_body_6 %}
{% include activity.html variant="1" title="Part 7: Practical Applications" overview=section_overview_7 content=section_body_7 %}
