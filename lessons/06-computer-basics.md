---
layout: page
title: Computer Basics
nav_order: 2
---

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

  /* ---------- helpers ---------- */
  function pos(id){
    var el = document.getElementById(id);
    if(!el) return null;
    var er = el.getBoundingClientRect();
    var rr = root.getBoundingClientRect();
    return {
      x: er.left - rr.left,
      y: er.top  - rr.top,
      w: er.width,
      h: er.height
    };
  }

  /* Same as pos() but accepts a DOM element directly */
  function posEl(el){
    if(!el) return null;
    var er = el.getBoundingClientRect();
    var rr = root.getBoundingClientRect();
    return {
      x: er.left - rr.left,
      y: er.top  - rr.top,
      w: er.width,
      h: er.height
    };
  }

  /* ---- anchor point on a box edge, with optional offset along that edge ---- */
  function edge(r, side, off){
    off = off || 0;
    var cx = r.x + r.w/2, cy = r.y + r.h/2;
    if(side==='top')    return {x: cx+off, y: r.y};
    if(side==='bottom') return {x: cx+off, y: r.y+r.h};
    if(side==='left')   return {x: r.x,    y: cy+off};
    if(side==='right')  return {x: r.x+r.w,y: cy+off};
  }

  /* ---- build SVG path through explicit waypoints ---- */
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

  /* ---- draw a single waypoint arrow ---- */
  function drawLine(pts, cfg){
    var d = wpPath(pts);
    mkPath(d, cfg.color, cfg.w||2, cfg.mk, cfg.dash, cfg.mkStart);
    if(cfg.label){
      /* Place label at the actual midpoint of the total path length */
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

  /* ---- main render ---- */
  function render(){
    svg.querySelectorAll('path:not(defs path), text').forEach(function(n){ n.remove(); });

    var rr = root.getBoundingClientRect();
    svg.setAttribute('width',  rr.width);
    svg.setAttribute('height', rr.height);
    svg.setAttribute('viewBox','0 0 '+rr.width+' '+rr.height);

    /* ---- grab positions ---- */
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

    var hwEl   = document.querySelector('.d-hardware');
    var perEl  = document.querySelector('.d-peripherals');
    var hw     = hwEl  ? posEl(hwEl)  : null;
    var per    = perEl ? posEl(perEl) : null;
    if(!hw||!per) return;

    var BLUE   = '#032659';
    var TEAL   = '#125261';
    var PURPLE = '#47264F';
    var ORANGE = '#975722';
    var PAD    = 14;

    /* =========================================================
       Channel assignments for horizontal lines above the hw box.
       Each arrow gets its own Y-level so nothing overlaps.
         Channel 1 (closest to hw): OS → CPU    at hw.y - PAD
         Channel 2:                 Boot handoff at hw.y - PAD - 16
         Channel 3:                 OS → RAM     at hw.y - PAD - 32
         Channel 4 (highest):       OS → Disk    at hw.y - PAD - 48
       ========================================================= */
    var chanY_cpu  = hw.y - PAD;
    var chanY_boot = hw.y - PAD - 16;
    var chanY_ram  = hw.y - PAD - 32;
    var leftOfHw   = hw.x - PAD;

    /* =========================================================
       A) Boot handoff — UEFI ↑ OS  (dashed purple)
       UEFI.top → up to chanY_boot → left to under OS → up to OS.bottom
       ========================================================= */
    var a = edge(uefi,'top');
    var b = edge(os,'bottom', 5);
    drawLine([a, {x:a.x, y:chanY_boot}, {x:b.x, y:chanY_boot}, b],
      {color:PURPLE, mk:'mk-purple', dash:'6 4', w:2, label:'Boot handoff'});

    /* =========================================================
       B) Firmware → CPU, RAM  (dashed purple, internal)
       ========================================================= */
    a = edge(uefi,'bottom', -15);
    b = edge(cpu,'top', 0);
    drawLine([a, {x:a.x, y:a.y+14}, {x:b.x, y:a.y+14}, b],
      {color:PURPLE, mk:'mk-purple', dash:'6 4', w:1.5});

    a = edge(uefi,'right');
    b = edge(ram,'top', -20);
    drawLine([a, {x:b.x, y:a.y}, b],
      {color:PURPLE, mk:'mk-purple', dash:'6 4', w:1.5});

    /* =========================================================
       C) OS → Hardware components (solid blue)
       Each uses its own dedicated channel above the hw box.
       Exit points on OS bottom are well-spaced apart.
       Entry points on targets are offset from center to avoid
       colliding with firmware arrows.
       ========================================================= */

    /* OS → CPU: exit OS far left, travel to chanY_cpu, go left of hw, down to CPU.left */
    a = edge(os,'bottom', -60);
    b = edge(cpu,'left', 0);
    drawLine([
      a,
      {x:a.x, y:chanY_cpu},
      {x:leftOfHw, y:chanY_cpu},
      {x:leftOfHw, y:b.y},
      b
    ], {color:BLUE, mk:'mk-blue', w:2});

    /* OS → RAM: exit OS center-left, travel to chanY_ram, across to RAM.top
       Enter RAM at top+20 offset (UEFI→RAM enters at top-20) */
    a = edge(os,'bottom', -20);
    b = edge(ram,'top', 20);
    drawLine([
      a,
      {x:a.x, y:chanY_ram},
      {x:b.x, y:chanY_ram},
      b
    ], {color:BLUE, mk:'mk-blue', w:2});

    /* =========================================================
       D) OS → Peripherals (solid blue)
       Exit OS.right at well-spaced Y offsets.
       Route through distinct vertical channels in the gap.
       ========================================================= */
    var gapStart = hw.x + hw.w;
    var gapEnd   = per.x;
    var gapW     = gapEnd - gapStart;
    var gapX1    = gapStart + gapW * 0.2;
    var gapX2    = gapStart + gapW * 0.5;
    var gapX3    = gapStart + gapW * 0.8;

    /* OS → Network: exit OS.right near top */
    a = edge(os,'right', -10);
    b = edge(net,'left');
    drawLine([a, {x:gapX1, y:a.y}, {x:gapX1, y:b.y}, b],
      {color:BLUE, mk:'mk-blue', w:2});

    /* OS → Monitor: exit OS.right at center */
    a = edge(os,'right', 0);
    b = edge(mon,'left');
    drawLine([a, {x:gapX2, y:a.y}, {x:gapX2, y:b.y}, b],
      {color:BLUE, mk:'mk-blue', w:2});

    /* OS ↔ USB Controller: exit OS.right near bottom (bidirectional) */
    a = edge(os,'right', 10);
    b = edge(usb,'left');
    var gap = 5;
    /* forward arrow (OS → USB) */
    drawLine([
      {x:a.x, y:a.y - gap},
      {x:gapX3 - 4, y:a.y - gap},
      {x:gapX3 - 4, y:b.y - gap},
      {x:b.x, y:b.y - gap}
    ], {color:BLUE, mk:'mk-blue', w:1.8});
    /* return arrow (USB → OS) */
    drawLine([
      {x:b.x, y:b.y + gap},
      {x:gapX3 + 4, y:b.y + gap},
      {x:gapX3 + 4, y:a.y + gap},
      {x:a.x, y:a.y + gap}
    ], {color:BLUE, mk:'mk-blue', w:1.8});

    /* =========================================================
       E) Hardware data paths (teal, internal)
       ========================================================= */

    /* CPU ↔ Physical RAM (dog-leg so arrowheads don't overlap)
       Route: CPU.right → horizontal to gap midpoint → vertical jog → horizontal into RAM.left
       Two separate one-way arrows so heads are clearly separated. */
    a = edge(cpu,'right', 0);
    b = edge(ram,'left', 0);
    var gapMidX = (a.x + b.x) / 2;
    var cpuMidY = a.y;
    var ramMidY = ram.y + ram.h / 2;

    /* arrow 1: CPU → RAM (upper path) */
    drawLine([
      a,
      {x: gapMidX - 4, y: cpuMidY},
      {x: gapMidX - 4, y: ramMidY - 6},
      {x: b.x, y: ramMidY - 6}
    ], {color:TEAL, mk:'mk-teal', w:2});

    /* arrow 2: RAM → CPU (lower path) */
    drawLine([
      {x: b.x, y: ramMidY + 6},
      {x: gapMidX + 4, y: ramMidY + 6},
      {x: gapMidX + 4, y: cpuMidY + 12},
      {x: a.x, y: cpuMidY + 12}
    ], {color:TEAL, mk:'mk-teal', w:2});

    /* RAM ↔ Disk (dog-leg so arrowheads don't overlap)
       Two separate one-way arrows offset horizontally. */
    a = edge(ram,'bottom', 0);
    b = edge(disk,'top', 0);
    var gapMidY = (a.y + b.y) / 2;
    var ramCX = ram.x + ram.w / 2;

    /* arrow 1: RAM → Disk (left path) */
    drawLine([
      {x: ramCX - 8, y: a.y},
      {x: ramCX - 8, y: gapMidY - 4},
      {x: ramCX - 16, y: gapMidY - 4},
      {x: ramCX - 16, y: b.y}
    ], {color:TEAL, mk:'mk-teal', w:2});

    /* arrow 2: Disk → RAM (right path) */
    drawLine([
      {x: ramCX + 16, y: b.y},
      {x: ramCX + 16, y: gapMidY + 4},
      {x: ramCX + 8, y: gapMidY + 4},
      {x: ramCX + 8, y: a.y}
    ], {color:TEAL, mk:'mk-teal', w:2});
  }

  /* schedule renders after layout is stable */
  function go(){ requestAnimationFrame(render); }
  window.addEventListener('load', go);
  window.addEventListener('resize', go);
  if(typeof ResizeObserver !== 'undefined'){
    new ResizeObserver(go).observe(root);
  }
  setTimeout(go, 200);
  setTimeout(go, 600);
})();
</script>
