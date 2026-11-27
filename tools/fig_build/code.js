/* BP-2128 Component Builder — builds variables, text styles and 7 component sets
   with event_type variants from the embedded SPEC. Colors -> variables,
   text -> text styles, text areas -> auto layout. */
const SPEC = {
 "colors": {
  "color.brand.primary.700": "#144536",
  "color.brand.primary.600": "#1D5C46",
  "color.brand.primary.500": "#27795F",
  "color.brand.accent.gold.500": "#C9A227",
  "color.neutral.900": "#1C2126",
  "color.neutral.700": "#3D444C",
  "color.neutral.500": "#6B7480",
  "color.neutral.100": "#EEF1F4",
  "color.neutral.0": "#FFFFFF",
  "color.badge.public.bg": "#166534",
  "color.badge.public.text": "#FFFFFF",
  "color.badge.member-only.bg": "#854D0E",
  "color.badge.member-only.text": "#FFFFFF",
  "color.badge.closed-door.bg": "#1F2937",
  "color.badge.closed-door.text": "#FFFFFF"
 },
 "textStyles": {
  "display-poster": {
   "weight": 700,
   "size": 88.0,
   "lh": 120
  },
  "display-square": {
   "weight": 700,
   "size": 80.0,
   "lh": 120
  },
  "display-wide": {
   "weight": 700,
   "size": 52.0,
   "lh": 120
  },
  "display-oa": {
   "weight": 700,
   "size": 32.0,
   "lh": 120
  },
  "display-thumb": {
   "weight": 700,
   "size": 24.0,
   "lh": 110
  },
  "display-mp": {
   "weight": 700,
   "size": 36.0,
   "lh": 120
  },
  "display-podcast": {
   "weight": 700,
   "size": 220.0,
   "lh": 120
  },
  "subtitle-lg": {
   "weight": 400,
   "size": 28.0,
   "lh": 150
  },
  "subtitle-md": {
   "weight": 400,
   "size": 24.0,
   "lh": 140
  },
  "subtitle-sm": {
   "weight": 400,
   "size": 16.0,
   "lh": 140
  },
  "subtitle-mp": {
   "weight": 400,
   "size": 18.0,
   "lh": 130
  },
  "subtitle-podcast": {
   "weight": 400,
   "size": 72.0,
   "lh": 140
  },
  "meta": {
   "weight": 400,
   "size": 24.0,
   "lh": 150
  },
  "meta-square": {
   "weight": 400,
   "size": 20.0,
   "lh": 150
  },
  "meta-sm": {
   "weight": 400,
   "size": 22.0,
   "lh": 160
  },
  "meta-podcast": {
   "weight": 400,
   "size": 48.0,
   "lh": 150
  },
  "badge-xl": {
   "weight": 700,
   "size": 56.0,
   "lh": 100
  },
  "badge-lg": {
   "weight": 700,
   "size": 28.0,
   "lh": 100
  },
  "badge-md": {
   "weight": 700,
   "size": 24.0,
   "lh": 100
  },
  "badge-sm": {
   "weight": 700,
   "size": 20.0,
   "lh": 100
  },
  "badge-xs": {
   "weight": 700,
   "size": 14.0,
   "lh": 100
  },
  "logo-xl": {
   "weight": 400,
   "size": 44.0,
   "lh": 120
  },
  "logo-lg": {
   "weight": 400,
   "size": 26.0,
   "lh": 120
  },
  "logo-md": {
   "weight": 400,
   "size": 22.0,
   "lh": 120
  },
  "logo-sm": {
   "weight": 400,
   "size": 16.0,
   "lh": 120
  },
  "logo-xs": {
   "weight": 400,
   "size": 14.0,
   "lh": 120
  },
  "caption": {
   "weight": 400,
   "size": 18.0,
   "lh": 130
  }
 },
 "fontFamily": "Noto Sans SC",
 "badgeLabels": {
  "public": "公开活动",
  "member-only": "会员专享",
  "closed-door": "闭门会"
 },
 "eventTypes": [
  {
   "key": "public",
   "value": "公开"
  },
  {
   "key": "member-only",
   "value": "会员专享"
  },
  {
   "key": "closed-door",
   "value": "闭门会"
  }
 ],
 "templates": {
  "poster_vertical_1080x1920": {
   "w": 1080,
   "h": 1920,
   "hero": [
    80,
    80,
    920,
    980
   ],
   "heroRadius": 24,
   "deco1": 320,
   "deco2": 180,
   "deco3": 420,
   "decoBorder": 8,
   "decoRadius": 64,
   "decoPos": [
    560,
    120,
    700,
    620,
    180,
    660
   ],
   "badge": [
    104,
    104
   ],
   "badgePad": [
    12,
    24
   ],
   "badgeStyle": "badge-lg",
   "titleWrap": [
    80,
    1100,
    920,
    330
   ],
   "titleStyle": "display-poster",
   "titleClamp": 3,
   "subtitleWrap": [
    80,
    1450,
    640,
    96
   ],
   "subtitleStyle": "subtitle-lg",
   "meta": [
    80,
    1560,
    620,
    90
   ],
   "metaStyle": "meta",
   "metaBold": "2027-03-18 14:00",
   "metaRest": "示例城市 · 示例园区国际会议中心",
   "qr": [
    760,
    1480,
    240,
    240
   ],
   "qrLabelStyle": "caption",
   "qrLabelOff": 26,
   "logo": [
    80,
    1780,
    400,
    100
   ],
   "logoStyle": "logo-lg",
   "logoMark": 56,
   "logoMarkRadius": 14
  },
  "poster_square_1080x1080": {
   "w": 1080,
   "h": 1080,
   "hero": [
    72,
    72,
    936,
    420
   ],
   "heroRadius": 24,
   "deco1": 180,
   "deco2": 110,
   "deco3": 220,
   "decoBorder": 6,
   "decoRadius": 40,
   "decoPos": [
    600,
    60,
    740,
    240,
    140,
    220
   ],
   "badge": [
    92,
    92
   ],
   "badgePad": [
    10,
    20
   ],
   "badgeStyle": "badge-md",
   "titleWrap": [
    72,
    532,
    936,
    300
   ],
   "titleStyle": "display-square",
   "titleClamp": 3,
   "subtitleWrap": [
    72,
    852,
    640,
    84
   ],
   "subtitleStyle": "subtitle-md",
   "meta": [
    72,
    956,
    640,
    44
   ],
   "metaStyle": "meta-square",
   "metaBold": "2027-03-18 14:00",
   "metaRest": "示例园区国际会议中心",
   "qr": [
    788,
    838,
    220,
    220
   ],
   "qrLabelStyle": "caption",
   "qrLabelOff": 26,
   "logo": [
    72,
    1000,
    300,
    60
   ],
   "logoStyle": "logo-sm",
   "logoMark": 40,
   "logoMarkRadius": 10
  },
  "poster_horizontal_1920x1080": {
   "w": 1920,
   "h": 1080,
   "hero": [
    0,
    0,
    1120,
    1080
   ],
   "heroRadius": 0,
   "deco1": 340,
   "deco2": 200,
   "deco3": 460,
   "decoBorder": 8,
   "decoRadius": 64,
   "decoPos": [
    640,
    100,
    820,
    620,
    200,
    160
   ],
   "badge": [
    1184,
    64
   ],
   "badgePad": [
    10,
    20
   ],
   "badgeStyle": "badge-md",
   "titleWrap": [
    1184,
    150,
    672,
    200
   ],
   "titleStyle": "display-wide",
   "titleClamp": 3,
   "subtitleWrap": [
    1184,
    370,
    672,
    96
   ],
   "subtitleStyle": "subtitle-md",
   "meta": [
    1184,
    486,
    672,
    120
   ],
   "metaStyle": "meta-sm",
   "metaBold": "2027-03-18 14:00",
   "metaRest": "示例城市 · 示例园区国际会议中心\n主办方：示例空间",
   "qr": [
    1184,
    660,
    240,
    240
   ],
   "qrLabelStyle": "caption",
   "qrLabelOff": 26,
   "logo": [
    1184,
    940,
    400,
    80
   ],
   "logoStyle": "logo-md",
   "logoMark": 44,
   "logoMarkRadius": 12
  },
  "oa_cover_first_900x383": {
   "w": 900,
   "h": 383,
   "hero": [
    258,
    40,
    383,
    120
   ],
   "heroRadius": 24,
   "deco1": 64,
   "deco2": 40,
   "deco3": 80,
   "decoBorder": 4,
   "decoRadius": 20,
   "decoPos": [
    210,
    -14,
    40,
    40,
    120,
    10
   ],
   "badge": [
    258,
    170
   ],
   "badgePad": [
    6,
    14
   ],
   "badgeStyle": "badge-sm",
   "titleWrap": [
    258,
    214,
    383,
    116
   ],
   "titleStyle": "display-oa",
   "titleClamp": 3,
   "subtitleWrap": [
    258,
    334,
    383,
    46
   ],
   "subtitleStyle": "subtitle-sm",
   "meta": null,
   "metaStyle": "meta",
   "metaBold": "",
   "metaRest": "",
   "qr": [
    660,
    151,
    200,
    200
   ],
   "qrLabelStyle": "caption",
   "qrLabelOff": 26,
   "logo": [
    20,
    320,
    220,
    44
   ],
   "logoStyle": "logo-sm",
   "logoMark": 32,
   "logoMarkRadius": 8
  },
  "oa_cover_second_200x200": {
   "w": 200,
   "h": 200,
   "hero": [
    0,
    0,
    200,
    48
   ],
   "heroRadius": 0,
   "deco1": 26,
   "deco2": 16,
   "deco3": 34,
   "decoBorder": 3,
   "decoRadius": 10,
   "decoPos": [
    130,
    -10,
    30,
    6,
    60,
    4
   ],
   "badge": [
    10,
    10
   ],
   "badgePad": [
    4,
    8
   ],
   "badgeStyle": "badge-xs",
   "titleWrap": [
    16,
    56,
    168,
    134
   ],
   "titleStyle": "display-thumb",
   "titleClamp": 5,
   "subtitleWrap": null,
   "subtitleStyle": "subtitle-md",
   "meta": null,
   "metaStyle": "meta",
   "metaBold": "",
   "metaRest": "",
   "qr": null,
   "qrLabelStyle": "caption",
   "qrLabelOff": 26,
   "logo": null,
   "logoStyle": "logo-md",
   "logoMark": 44,
   "logoMarkRadius": 12
  },
  "mp_cover_750x420": {
   "w": 750,
   "h": 420,
   "hero": [
    0,
    0,
    750,
    160
   ],
   "heroRadius": 0,
   "deco1": 80,
   "deco2": 48,
   "deco3": 100,
   "decoBorder": 4,
   "decoRadius": 24,
   "decoPos": [
    500,
    -18,
    600,
    60,
    300,
    20
   ],
   "badge": [
    40,
    36
   ],
   "badgePad": [
    6,
    14
   ],
   "badgeStyle": "badge-sm",
   "titleWrap": [
    40,
    184,
    430,
    140
   ],
   "titleStyle": "display-mp",
   "titleClamp": 3,
   "subtitleWrap": [
    40,
    332,
    430,
    48
   ],
   "subtitleStyle": "subtitle-mp",
   "meta": null,
   "metaStyle": "meta",
   "metaBold": "",
   "metaRest": "",
   "qr": [
    500,
    176,
    200,
    200
   ],
   "qrLabelStyle": "caption",
   "qrLabelOff": 26,
   "logo": [
    40,
    388,
    200,
    28
   ],
   "logoStyle": "logo-xs",
   "logoMark": 20,
   "logoMarkRadius": 6
  },
  "podcast_cover_3000x3000": {
   "w": 3000,
   "h": 3000,
   "hero": [
    300,
    300,
    2400,
    780
   ],
   "heroRadius": 24,
   "deco1": 520,
   "deco2": 300,
   "deco3": 640,
   "decoBorder": 14,
   "decoRadius": 96,
   "decoPos": [
    1560,
    60,
    1900,
    420,
    400,
    120
   ],
   "badge": [
    300,
    1140
   ],
   "badgePad": [
    20,
    44
   ],
   "badgeStyle": "badge-xl",
   "titleWrap": [
    300,
    1320,
    2400,
    840
   ],
   "titleStyle": "display-podcast",
   "titleClamp": 3,
   "subtitleWrap": [
    300,
    2220,
    2400,
    220
   ],
   "subtitleStyle": "subtitle-podcast",
   "meta": [
    300,
    2500,
    1900,
    90
   ],
   "metaStyle": "meta-podcast",
   "metaBold": "",
   "metaRest": "示例主理人 · 对话示例产业合伙人",
   "qr": [
    2460,
    2500,
    400,
    400
   ],
   "qrLabelStyle": "meta-podcast",
   "qrLabelOff": 40,
   "logo": [
    300,
    2860,
    600,
    100
   ],
   "logoStyle": "logo-xl",
   "logoMark": 80,
   "logoMarkRadius": 20
  }
 }
};

function hexToRgb(hex) {
  const h = hex.replace('#', '');
  return {
    r: parseInt(h.slice(0, 2), 16) / 255,
    g: parseInt(h.slice(2, 4), 16) / 255,
    b: parseInt(h.slice(4, 6), 16) / 255,
  };
}

function log(msg) { try { figma.ui.postMessage({ type: 'log', msg }); } catch (e) {} }
function done(payload) { try { figma.ui.postMessage({ type: 'done', payload }); } catch (e) {} }
function fail(msg) { try { figma.ui.postMessage({ type: 'fail', msg }); } catch (e) {} }
let __gradBound = true;

async function main() {
  log('loading fonts…');
  const fam = SPEC.fontFamily;
  await figma.loadFontAsync({ family: fam, style: 'Regular' });
  await figma.loadFontAsync({ family: fam, style: 'Bold' });

  // ---------- variables ----------
  const buildErrors = [];
  await figma.loadFontAsync({ family: 'Inter', style: 'Regular' });
  const reportPage = figma.createPage();
  reportPage.name = 'Build Report';
  const rep = figma.createText();
  rep.fontName = { family: 'Inter', style: 'Regular' };
  rep.fontSize = 24;
  const NL = String.fromCharCode(10);
  const repLines = ['BP-2128 BUILD REPORT v11 (live)', 'started ' + new Date().toISOString()];
  rep.characters = repLines.join(NL);
  reportPage.appendChild(rep);
  function updateRep(extra) {
    try {
      const ls = ['BP-2128 BUILD REPORT v11 (live)', 'started ' + new Date().toISOString(), 'stage: ' + (extra || ''), 'build_errors (' + buildErrors.length + '): ' + (buildErrors.slice(-6).join(' | ') || 'NONE')];
      rep.characters = ls.join(NL);
    } catch (e) {}
  }
  updateRep('variables done');

  // ---------- CLEANUP PHASE (crash-proof, keeps live report page) ----------
  try {
    log('cleanup: removing previous collections/styles/pages…');
    for (const c of figma.variables.getLocalVariableCollections()) {
      try { c.remove(); } catch (e) { buildErrors.push('cleanup collection: ' + e); }
    }
    for (const s of figma.getLocalTextStyles()) {
      try { s.remove(); } catch (e) { buildErrors.push('cleanup style: ' + e); }
    }
    try {
      figma.currentPage = figma.root.children[0];
      const keep = figma.currentPage;
      for (const child of [...keep.children]) child.remove();
      for (const p of [...figma.root.children]) {
        if (p.id !== keep.id && p.id !== reportPage.id) p.remove();
      }
      keep.name = 'Brand Components';
    } catch (e) { buildErrors.push('cleanup pages: ' + e); }
    updateRep('cleanup done');
  } catch (e) {
    buildErrors.push('cleanup fatal: ' + String(e));
    updateRep('cleanup fatal: ' + String(e));
  }

  log('creating variable collection…');
  const col = figma.variables.createVariableCollection('Brand Tokens');
  const mode = col.modes[0].modeId;
  const varIds = {};
  const varName = {}; // css-path -> variable name
  for (const path in SPEC.colors) {
    const vname = path.split('.').join('/');
    const v = figma.variables.createVariable(vname, col, 'COLOR');
    v.setValueForMode(mode, hexToRgb(SPEC.colors[path]));
    varIds[path] = v.id;
    varName[path] = vname;
  }

  const bindable = (path) => ({ type: 'VARIABLE_ALIAS', id: varIds[path] });
  const varObj = {};
  for (const v of figma.variables.getLocalVariables('COLOR')) varObj[v.id] = v;
  function solidFill(path, opacity) {
    const p = { type: 'SOLID', color: hexToRgb(SPEC.colors[path]) };
    if (opacity !== undefined) p.opacity = opacity;
    try {
      const bound = figma.variables.setBoundVariableForPaint(p, 'color', varObj[varIds[path]]);
      return bound;
    } catch (e) {
      buildErrors.push('solidFill ' + path + ': ' + e);
      p.boundVariables = { color: bindable(path) };
      return p;
    }
  }

  // ---------- text styles ----------
  log('creating text styles…');
  const styleIds = {};
  for (const name in SPEC.textStyles) {
    const t = SPEC.textStyles[name];
    const s = figma.createTextStyle();
    s.name = name;
    s.fontName = { family: fam, style: t.weight >= 700 ? 'Bold' : 'Regular' };
    s.fontSize = t.size;
    s.lineHeight = { value: t.lh, unit: 'PERCENT' };
    styleIds[name] = s.id;
  }
  log('text styles: ' + Object.keys(styleIds).length);

  // ---------- helpers ----------
  function withTimeout(p, ms) {
    return Promise.race([p, new Promise(res => setTimeout(() => res('TIMEOUT'), ms))]);
  }
  async function safeSetStyle(t, styleName) {
    const sid = styleIds[styleName];
    try {
      const r = await withTimeout(t.setTextStyleIdAsync(sid), 3000);
      if (r === 'TIMEOUT') {
        try { t.textStyleId = sid; } catch (e2) { buildErrors.push('style sync fallback ' + styleName + ': ' + e2); }
      }
    } catch (e) {
      buildErrors.push('style ' + styleName + ': ' + e);
    }
  }
  async function makeText(chars, styleName, colorPath, opts) {
    opts = opts || {};
    const t = figma.createText();
    t.fontName = { family: fam, style: SPEC.textStyles[styleName].weight >= 700 ? 'Bold' : 'Regular' };
    t.characters = chars;
    t.fontSize = SPEC.textStyles[styleName].size;
    await safeSetStyle(t, styleName);
    t.fills = [solidFill(colorPath)];
    if (opts.letterSpacing) t.letterSpacing = { unit: 'PIXELS', value: opts.letterSpacing };
    if (opts.maxLines) { t.textTruncation = 'ENDING'; t.maxLines = opts.maxLines; }
    if (opts.name) t.name = opts.name;
    if (opts.textAutoResize) t.textAutoResize = opts.textAutoResize;
    return t;
  }

  function autoWrap(x, y, w, h, name) {
    const f = figma.createFrame();
    f.name = name;
    f.layoutMode = 'VERTICAL';
    f.primaryAxisAlignItems = 'CENTER';
    f.counterAxisAlignItems = 'MIN';
    f.fills = [];
    f.x = x; f.y = y;
    f.resize(w, h);
    f.primaryAxisSizingMode = 'FIXED';
    f.counterAxisSizingMode = 'FIXED';
    return f;
  }

  async function buildVariant(tpl, eventKey, eventValue) {
    figma.notify('building variant ' + eventValue, {timeout: 800});
    const comp = figma.createComponent();
    comp.name = 'event_type=' + eventValue;
    comp.resizeWithoutConstraints(tpl.w, tpl.h);
    comp.clipsContent = true;
    comp.fills = [solidFill('color.neutral.0')];
    comp.description = 'BP-2128 ' + tpl.name + ' (' + tpl.w + 'x' + tpl.h + ')';

    // hero + deco
    const hero = figma.createFrame();
    hero.name = 'hero';
    hero.x = tpl.hero[0]; hero.y = tpl.hero[1];
    hero.resizeWithoutConstraints(tpl.hero[2], tpl.hero[3]);
    hero.cornerRadius = tpl.heroRadius;
    hero.clipsContent = true;
    const [hx, hy, hw, hh] = tpl.hero;
    const g = {
      type: 'GRADIENT_LINEAR',
      gradientTransform: [[0.5, 0.5, 0], [-0.5, 0.5, 0.5]],
      gradientStops: [
        { position: 0, color: Object.assign({ a: 1 }, hexToRgb(SPEC.colors['color.brand.primary.700'])) },
        { position: 0.62, color: Object.assign({ a: 1 }, hexToRgb(SPEC.colors['color.brand.primary.600'])) },
        { position: 1, color: Object.assign({ a: 1 }, hexToRgb(SPEC.colors['color.brand.primary.500'])) },
      ],
    };
    // try to bind gradient stops to variables; fall back to raw stop colors
    let bound = true;
    try {
      g.gradientStops[0].boundVariables = { color: bindable('color.brand.primary.700') };
      g.gradientStops[1].boundVariables = { color: bindable('color.brand.primary.600') };
      g.gradientStops[2].boundVariables = { color: bindable('color.brand.primary.500') };
      hero.fills = [g];
      // read back: if binding silently dropped, detect
      bound = !!(hero.fills[0].gradientStops[0].boundVariables && hero.fills[0].gradientStops[0].boundVariables.color);
    } catch (e) { bound = false; }
    if (!bound) {
      __gradBound = false;
      log('gradient stop binding unsupported — stops use token values verbatim');
      hero.fills = [g];
    }
    comp.appendChild(hero);

    const d1 = figma.createEllipse();
    d1.name = 'deco-1';
    d1.resizeWithoutConstraints(tpl.deco1, tpl.deco1);
    d1.x = tpl.decoPos[0]; d1.y = tpl.decoPos[1];
    d1.fills = [];
    d1.strokes = [solidFill('color.brand.accent.gold.500')];
    d1.strokeWeight = tpl.decoBorder;
    d1.strokeAlign = 'INSIDE';
    d1.opacity = 0.55;
    hero.appendChild(d1);

    const d2 = figma.createEllipse();
    d2.name = 'deco-2';
    d2.resizeWithoutConstraints(tpl.deco2, tpl.deco2);
    d2.x = tpl.decoPos[2]; d2.y = tpl.decoPos[3];
    d2.fills = [solidFill('color.brand.primary.500')];
    d2.opacity = 0.35;
    hero.appendChild(d2);

    const d3 = figma.createRectangle();
    d3.name = 'deco-3';
    d3.resizeWithoutConstraints(tpl.deco3, tpl.deco3);
    d3.x = tpl.decoPos[4]; d3.y = tpl.decoPos[5];
    d3.cornerRadius = tpl.decoRadius;
    d3.fills = [solidFill('color.neutral.0')];
    d3.opacity = 0.08;
    hero.appendChild(d3);

    // badge (variant-driven)
    const badge = figma.createFrame();
    badge.name = 'badge';
    badge.layoutMode = 'HORIZONTAL';
    badge.primaryAxisSizingMode = 'AUTO';
    badge.counterAxisSizingMode = 'AUTO';
    badge.primaryAxisAlignItems = 'CENTER';
    badge.counterAxisAlignItems = 'CENTER';
    badge.paddingTop = tpl.badgePad[0]; badge.paddingBottom = tpl.badgePad[0];
    badge.paddingLeft = tpl.badgePad[1]; badge.paddingRight = tpl.badgePad[1];
    badge.cornerRadius = 999;
    badge.fills = [solidFill('color.badge.' + eventKey + '.bg')];
    const btxt = await makeText(SPEC.badgeLabels[eventKey], tpl.badgeStyle, 'color.badge.' + eventKey + '.text', { letterSpacing: 2, textAutoResize: 'WIDTH_AND_HEIGHT' });
    badge.appendChild(btxt);
    badge.x = tpl.badge[0]; badge.y = tpl.badge[1];
    comp.appendChild(badge);

    // title
    const tw = tpl.titleWrap;
    const wrap = autoWrap(tw[0], tw[1], tw[2], tw[3], 'title-wrap');
    const title = await makeText('示例产业沙龙', tpl.titleStyle, 'color.neutral.900', { maxLines: tpl.titleClamp, textAutoResize: 'HEIGHT', name: 'title' });
    wrap.appendChild(title);
    title.layoutAlign = 'STRETCH';
    comp.appendChild(wrap);

    // subtitle
    if (tpl.subtitleWrap) {
      const sw = tpl.subtitleWrap;
      const swrap = autoWrap(sw[0], sw[1], sw[2], sw[3], 'subtitle-wrap');
      const sub = await makeText('面向会员企业代表的产业资源对接与商务合作交流活动', tpl.subtitleStyle, 'color.neutral.700', { maxLines: 2, textAutoResize: 'HEIGHT', name: 'subtitle' });
      swrap.appendChild(sub);
      sub.layoutAlign = 'STRETCH';
      comp.appendChild(swrap);
    }

    // meta
    if (tpl.meta) {
      const m = tpl.meta;
      let chars = (tpl.metaBold ? tpl.metaBold : '') + tpl.metaRest;
      if (tpl.metaBold && tpl.metaRest) {
        if (tpl.metaBr) chars = tpl.metaBold + '\n' + tpl.metaRest;
        else if (!chars.includes('\n')) chars = tpl.metaBold + ' · ' + tpl.metaRest;
      }
      const meta = figma.createText();
      meta.fontName = { family: fam, style: 'Regular' };
      meta.fontSize = SPEC.textStyles[tpl.metaStyle].size;
      meta.characters = chars;
      await safeSetStyle(meta, tpl.metaStyle);
      meta.fills = [solidFill('color.neutral.700')];
      meta.name = 'meta';
      if (tpl.metaBold) {
        const n = tpl.metaBold.length;
        meta.setRangeFontName(0, n, { family: fam, style: 'Bold' });
        meta.setRangeFills(0, n, [solidFill('color.brand.primary.700')]);
      }
      meta.x = m[0]; meta.y = m[1];
      meta.resize(m[2], m[3]);
      meta.textAutoResize = 'HEIGHT';
      comp.appendChild(meta);
    }

    // qr slot
    if (tpl.qr) {
      const q = tpl.qr;
      const qr = figma.createFrame();
      qr.name = 'qr-slot';
      qr.x = q[0]; qr.y = q[1];
      qr.resizeWithoutConstraints(q[2], q[3]);
      qr.cornerRadius = 16;
      qr.fills = [solidFill('color.neutral.100')];
      qr.strokes = [solidFill('color.neutral.500')];
      qr.strokeWeight = 2;
      qr.dashPattern = [6, 6];
      qr.layoutMode = 'HORIZONTAL';
      qr.primaryAxisAlignItems = 'CENTER';
      qr.counterAxisAlignItems = 'CENTER';
      const inner = Math.round(Math.min(q[2], q[3]) * (tpl.qrInner || 78) / 100);
      const qi = figma.createRectangle();
      qi.name = 'qr-inner';
      qi.resizeWithoutConstraints(inner, inner);
      qi.cornerRadius = 8;
      qi.fills = [solidFill('color.neutral.900', 0.85)];
      qr.appendChild(qi);
      comp.appendChild(qr);
      const label = await makeText('扫码报名', tpl.qrLabelStyle, 'color.neutral.500', { textAutoResize: 'HEIGHT', name: 'qr-label' });
      label.textAlignHorizontal = 'CENTER';
      label.x = q[0]; label.y = q[1] + q[3] + 6;
      label.resize(q[2], 30);
      comp.appendChild(label);
    }

    // logo safe area
    if (tpl.logo) {
      const l = tpl.logo;
      const logo = figma.createFrame();
      logo.name = 'logo-safe';
      logo.layoutMode = 'HORIZONTAL';
      logo.primaryAxisSizingMode = 'FIXED';
      logo.counterAxisSizingMode = 'AUTO';
      logo.counterAxisAlignItems = 'CENTER';
      logo.itemSpacing = 12;
      logo.fills = [];
      logo.x = l[0]; logo.y = l[1];
      logo.resize(l[2], l[3]);
      const mark = figma.createFrame();
      mark.name = 'logo-mark';
      mark.resizeWithoutConstraints(tpl.logoMark, tpl.logoMark);
      mark.cornerRadius = tpl.logoMarkRadius;
      mark.fills = [solidFill('color.brand.primary.600')];
      const dot = figma.createEllipse();
      const ins = Math.round(tpl.logoMark * 0.3);
      dot.resizeWithoutConstraints(tpl.logoMark - 2 * ins, tpl.logoMark - 2 * ins);
      dot.x = ins; dot.y = ins;
      dot.fills = [solidFill('color.brand.accent.gold.500')];
      mark.appendChild(dot);
      logo.appendChild(mark);
      const brand = await makeText('示例空间', tpl.logoStyle, 'color.neutral.500', { letterSpacing: 3, textAutoResize: 'WIDTH_AND_HEIGHT', name: 'logo-text' });
      logo.appendChild(brand);
      comp.appendChild(logo);
    }
    return comp;
  }

  // ---------- build component sets ----------
  const page = figma.currentPage;
  page.name = 'Brand Components v5';

  const sets = [];
  let ox = 0;
  const names = Object.keys(SPEC.templates);
  let rowY = 0;
  let rowH = 0;
  const GAP = 200;
  for (const name of names) {
    const tpl = SPEC.templates[name];
    const variants = [];
    for (const et of SPEC.eventTypes) {
      try {
        const c = await buildVariant(tpl, et.key, et.value);
        page.appendChild(c);
        variants.push(c);
      } catch (e) {
        buildErrors.push('build ' + name + '/' + et.value + ': ' + String(e));
        updateRep('ERR build ' + name + '/' + et.value);
        figma.notify('ERROR building ' + name + '/' + et.value, {timeout: 3000});
      }
    }
    let set;
    try {
      set = figma.combineAsVariants(variants, page);
    } catch (e) {
      buildErrors.push('combine ' + name + ': ' + String(e));
      updateRep('ERR combine ' + name);
      figma.notify('ERROR combine ' + name, {timeout: 3000});
      continue;
    }
    set.name = name;
    set.description = 'event_type variant property: 公开 / 会员专享 / 闭门会. Colors bound to variable collection "Brand Tokens"; text bound to text styles named after tokens.';
    // layout the set on canvas
    const insetPad = 60;
    set.x = ox + insetPad;
    set.y = rowY + insetPad;
    const totalW = set.width;
    if (totalW > 1600) { ox = 0; rowY += set.height + GAP; set.x = 0 + insetPad; set.y = rowY + insetPad; }
    else ox += totalW + GAP;
    rowH = Math.max(rowH, set.height);
    sets.push(set);
    updateRep('set ' + name + ' done, errors=' + buildErrors.length);
    log('built component set: ' + name + ' (3 variants)');
  }

  figma.viewport.scrollAndZoomIntoView(sets);

  // ---------- export renders into a "Variant Renders" page (no downloads) ----------
  log('exporting variant renders…');
  const renderPage = figma.createPage();
  renderPage.name = 'Variant Renders';
  const labelMap = { '公开': 'public', '会员专享': 'member-only', '闭门会': 'closed-door' };
  let rx = 0, ry = 0, rowMaxH = 0;
  const RGAP = 120;
  for (const set of sets) {
    for (const child of set.children) {
      if (child.type !== 'COMPONENT') continue;
      const val = (child.name.split('event_type=')[1] || '').trim();
      const fname = set.name + '_v_' + (labelMap[val] || val) + '.png';
      const escale = Math.min(1, 1400 / Math.max(child.width, child.height));
      updateRep('render ' + fname + ' @' + escale.toFixed(2));
      let bytes;
      const er = await withTimeout(child.exportAsync({ format: 'PNG', constraint: { type: 'SCALE', value: escale } }), 60000);
      if (er === 'TIMEOUT') { buildErrors.push('export timeout ' + fname); continue; }
      bytes = er;
      const img = figma.createImage(bytes);
      const rect = figma.createRectangle();
      rect.name = fname;
      rect.resizeWithoutConstraints(child.width, child.height);
      rect.fills = [{ type: 'IMAGE', imageHash: img.hash, scaleMode: 'FILL' }];
      if (rx + rect.width > 32000) { rx = 0; ry += rowMaxH + RGAP; rowMaxH = 0; }
      rect.x = rx; rect.y = ry;
      rx += rect.width + RGAP;
      rowMaxH = Math.max(rowMaxH, rect.height);
      renderPage.appendChild(rect);
      log('rendered ' + fname);
    }
  }

  // ---------- final report update ----------
  const allVars = figma.variables.getLocalVariables('COLOR');
  const stylesN = figma.getLocalTextStyles().length;
  const finalText = 'BP-2128 FINAL collections=' + figma.variables.getLocalVariableCollections().length +
    ' vars=' + allVars.length + '/' + Object.keys(SPEC.colors).length +
    ' styles=' + stylesN + '/' + Object.keys(SPEC.textStyles).length +
    ' sets=' + sets.length + '/7 | ' +
    sets.map(s => s.name + '[' + s.children.filter(c => c.type === 'COMPONENT').length + 'v]').join(' ') +
    ' || ERRORS(' + buildErrors.length + '): ' + (buildErrors.join(' || ') || 'NONE');
  try { figma.ui.postMessage({ type: 'clipboard', text: finalText }); } catch (e) {}
  updateRep('FINAL done, errors=' + buildErrors.length);
  log('report written');
  done({});
  figma.closePlugin();
}

figma.showUI(__html__, { visible: false });
main().catch(e => { fail(String(e && e.stack || e)); });
