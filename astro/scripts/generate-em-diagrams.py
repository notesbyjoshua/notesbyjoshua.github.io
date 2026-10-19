from html import escape
from math import cos, sin, pi, exp, log10, tanh, sqrt
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "public/assets/physics/usapho/em-original"
OUT.mkdir(parents=True, exist_ok=True)
BLUE, RED, GREEN, GRAY = "#1769aa", "#b73535", "#147d64", "#516173"


def text(x, y, value, size=18, color="#172b40", anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(value)}</text>'


def line(x1, y1, x2, y2, color=GRAY, arrow=False, dash=False, width=2):
    marker = f' marker-end="url(#{color[1:]})"' if arrow else ""
    dashed = ' stroke-dasharray="6 5"' if dash else ""
    return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{width}" fill="none"{marker}{dashed}/>'


def path(d, color=BLUE, width=3, fill="none"):
    return f'<path d="{d}" stroke="{color}" stroke-width="{width}" fill="{fill}"/>'


def rect(x, y, w, h, fill="#edf4fa", stroke=GRAY):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'


def circle(x, y, r, color=BLUE, fill="none"):
    return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="{color}" fill="{fill}" stroke-width="2"/>'


def symbol(x, y, outward=True):
    return circle(x, y, 8) + (circle(x, y, 2, BLUE, BLUE) if outward else
           line(x-5, y-5, x+5, y+5, BLUE) + line(x-5, y+5, x+5, y-5, BLUE))


def curve(points, color=BLUE):
    return path("M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in points), color)


def save(name, title, body, height=360):
    defs = "".join(f'<marker id="{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{c}"/></marker>' for c in [BLUE, RED, GREEN, GRAY])
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 {height}" role="img"><title>{escape(title)}</title><defs>{defs}</defs><rect width="720" height="{height}" rx="12" fill="#fff"/><g font-family="Arial, sans-serif">{text(24,32,title,22)}{body}</g></svg>\n'
    (OUT / f"{name}.svg").write_text(svg)


b = line(70,265,580,265,GRAY,True) + text(586,272,"wire")
b += line(160,265,240,265,RED,True,width=5) + text(158,300,"I dℓ →",20,RED)
b += line(190,265,430,100,GREEN,True) + text(300,165,"R",22,GREEN)
b += symbol(430,100) + text(450,95,"P: dB out of page",18,BLUE)
b += path("M250 265 A60 60 0 0 0 239 231",GRAY,2) + text(255,244,"θ")
b += text(70,335,"Point R from the source element to the observation point.")
save("biot-savart", "Field of a current element", b)

b = ""
for x in range(120,610,55):
    b += symbol(x,105,True) + symbol(x,245,False)
b += line(90,175,635,175,BLUE,True,width=3) + text(320,158,"B inside →",20,BLUE)
b += path("M155 175 L155 65 L550 65 L550 175 Z",GREEN,2)
b += line(280,65,225,65,GREEN,True) + line(315,175,370,175,GREEN,True)
b += text(270,56,"Amperian loop",17,GREEN) + text(120,285,"Dots: current out     Crosses: current in",18)
b += text(120,325,"Inside: B = μ₀nI       Outside: B ≈ 0 (long-solenoid model)")
save("solenoid", "Solenoid, viewed in axial cross-section", b)

b = line(90,160,630,160,BLUE,True) + text(615,145,"B",22,BLUE)
b += line(215,160,505,160,GRAY,width=5) + symbol(215,160) + symbol(505,160,False)
b += line(215,160,215,75,RED,True,width=3) + text(170,65,"F ↑",20,RED)
b += line(505,160,505,245,RED,True,width=3) + text(520,240,"F ↓",20,RED)
b += circle(360,160,5,GRAY,GRAY) + text(340,192,"pivot")
b += line(215,280,505,280) + text(350,303,"a")
b += text(60,335,"Edge-on loop: forces cancel, but their torques add.")
save("loop-torque", "A force pair turns the current loop", b)

b = rect(45,110,70,100,"#ffe9e9",RED) + text(80,170,"N",28,RED,"middle")
b += rect(605,110,70,100,"#e5f0ff",BLUE) + text(640,170,"S",28,BLUE,"middle")
b += line(135,85,585,85,BLUE,True) + text(345,73,"B →",20,BLUE)
b += path("M345 215 L260 215 L260 115 L460 115 L460 215 L375 215",GRAY,2)
b += line(345,215,345,258,RED) + line(375,215,375,258,BLUE) + line(260,195,260,130,RED,True)
b += line(460,135,460,200,RED,True) + text(228,165,"I",20,RED)
b += text(478,165,"I",20,RED) + line(360,100,360,248,GRAY,dash=True)
b += path("M345 258 A23 23 0 0 0 345 300",RED,8) + path("M375 258 A23 23 0 0 1 375 300",BLUE,8)
b += line(260,280,323,280,GRAY,width=6) + line(397,280,460,280,GRAY,width=6)
b += text(190,312,"brush",16) + text(450,312,"brush",16)
b += text(280,340,"split-ring commutator",17) + text(60,385,"Reversing the coil current each half-turn keeps torque driving rotation.",17)
save("dc-motor", "DC motor: coil and split-ring commutator", b,410)

b = ""
for panel, caption in enumerate(["Unmagnetized", "Applied field →", "Remanence (hard magnet)"]):
    x0 = 35 + panel*235
    b += rect(x0,90,190,155) + text(x0+95,280,caption,16,anchor="middle")
    for row in range(3):
        for col in range(3):
            angle = ([0,pi/2,pi, -pi/2,pi,0,pi/2,0,pi][row*3+col] if panel==0 else
                     (0 if panel==1 or (row+col)%3 else pi/3))
            x, y = x0+35+col*60, 120+row*48
            b += line(x-15*cos(angle), y+15*sin(angle), x+15*cos(angle), y-15*sin(angle),RED,True)
b += text(45,325,"Arrows represent domain magnetization, not individual electron paths.",17)
save("domains", "Domains and retained magnetization", b)

b = circle(360,190,70,GRAY,"#eef2f6") + text(360,195,"B ≈ 0",22,anchor="middle")
for offset in [-145,-105,-55,55,105,145]:
    sign = 1 if offset>0 else -1
    x, mid = 360+offset, 360+sign*max(abs(offset),100)
    b += path(f"M{x} 320 C{x} 270 {mid} 260 {mid} 190 C{mid} 120 {x} 100 {x} 65",BLUE,2)
    b += line(x,83,x,64,BLUE,True)
b += text(35,345,"Meissner state: screening currents exclude flux from the bulk.",18)
save("meissner", "Magnetic flux bends around a superconductor", b,375)

b = line(100,185,640,185,GRAY,True) + line(360,310,360,65,GRAY,True)
b += text(650,190,"H",20) + text(370,70,"M",20)
for shift in [-0.75,0.75]:
    b += curve([(360+80*x,185-95*tanh(1.25*(x-shift))) for x in [i/30 for i in range(-90,91)]],RED)
b += text(372,118,"remanence",16,RED) + text(270,213,"−Hc",17) + text(408,213,"Hc",17)
b += text(75,345,"Different paths on increasing and decreasing H retain magnetic history.",17)
save("hysteresis", "Magnetization hysteresis (schematic)", b,375)

b = ""
for x in range(180,600,70):
    for y in [105,175,245]:
        b += symbol(x,y,False)
b += path("M110 100 L110 140 L100 150 L120 165 L100 180 L120 195 L110 210 L110 260 L570 260",GRAY)
b += line(110,100,570,100) + line(465,80,465,280,RED,width=8)
b += line(465,205,465,140,GREEN,True,width=3) + text(485,160,"I ↑",20,GREEN)
b += line(490,70,600,70,RED,True) + text(615,76,"v",22,RED)
b += line(450,305,340,305,BLUE,True) + text(325,312,"magnetic drag",18,BLUE,"end")
b += text(75,180,"R",22) + text(620,180,"ℓ",22) + text(475,95,"+",22,RED)
b += text(475,280,"−",22,RED) + text(150,350,"Increasing inward flux → counterclockwise induced current.",18)
save("sliding-rod", "Motional emf: mechanical input, electrical output", b,380)

b = circle(280,190,80,BLUE,"#eef6ff")
for x,y in [(250,160),(310,160),(250,220),(310,220),(280,190)]:
    b += symbol(x,y)
for r in [50,125]:
    b += circle(280,190,r,RED) + line(280+r,175,280+r,205,RED,True)
b += text(440,125,"B out of page",20,BLUE) + text(440,155,"and increasing",20,BLUE)
b += text(440,215,"E circulates clockwise",19,RED) + text(440,245,"even outside the field",17,RED)
b += line(280,190,360,190,BLUE) + text(365,194,"R",18,BLUE)
save("induced-field", "Changing flux creates a circulating electric field", b,370)

b = line(90,285,650,285,GRAY,True) + line(90,285,90,65,GRAY,True)
b += text(650,310,"t / τ",18) + text(30,65,"I / Iref",16)
b += line(90,95,630,95,GRAY,dash=True) + text(58,100,"1")
b += curve([(90+100*t,285-190*(1-exp(-t))) for t in [i/40 for i in range(211)]],BLUE)
b += curve([(90+100*t,285-190*exp(-t)) for t in [i/40 for i in range(211)]],RED)
b += line(190,285,190,75,GRAY,dash=True) + text(186,310,"1")
b += text(350,125,"growth: 1 − exp(−t/τ)",18,BLUE) + text(350,260,"decay: exp(−t/τ)",18,RED)
b += text(205,175,"0.632",16,BLUE) + text(205,220,"0.368",16,RED)
b += text(150,345,"τ = L/R; Iref is the final (growth) or initial (decay) current.",17)
save("rl-response", "RL current approaches its steady value gradually", b,375)

b = text(445,65,"voltage",17,BLUE) + text(550,65,"current",17,RED)
for row, (label,phase) in enumerate([("R: in phase",0),("C: current leads",pi/2),("L: current lags",-pi/2)]):
    cy = 130+row*140
    b += text(25,cy,label,17) + line(220,cy,680,cy,GRAY)
    for shift,color in [(0,BLUE),(phase,RED)]:
        b += curve([(220+430*t/(2*pi),cy-42*cos(t+shift)) for t in [i*pi/100 for i in range(201)]],color)
b += text(240,510,"One full cycle →     (each waveform normalized to its own peak)",16)
save("ac-phase", "Phase is a shift in time, not a change in amplitude", b,540)

b = line(120,270,430,270,RED,True,width=3) + text(280,300,"VR (in phase with I)",18,RED)
b += line(120,270,120,75,BLUE,True,width=3) + text(90,66,"VL",19,BLUE)
b += line(120,270,120,345,GREEN,True,width=3) + text(90,365,"VC",19,GREEN)
b += line(430,270,430,150,GRAY,dash=True) + line(120,270,430,150,GRAY,True,width=3)
b += text(255,180,"Vtotal",20) + text(450,210,"VL − VC",18)
b += path("M190 270 A70 70 0 0 0 185 245",GRAY,2) + text(200,254,"φ",22)
b += text(235,350,"Inductive example: VL > VC",18)
save("rlc-phasor", "Series RLC: add voltage arrows, not their lengths", b,390)

b = rect(210,85,300,225,"#edf1f6") + rect(260,130,200,135,"white")
for x,color in [(210,RED),(510,BLUE)]:
    for y in range(135,260,24):
        b += path(f"M{x-25} {y} C{x+35} {y-15} {x+35} {y+15} {x-25} {y+12}",color,3)
b += text(80,205,"AC input V₁",18,RED) + text(540,205,"V₂ → load",18,BLUE)
b += text(160,295,"N₁ turns",18,RED) + text(525,295,"N₂ turns",18,BLUE)
b += line(290,110,425,110,GREEN,True) + text(345,180,"shared flux Φ",18,GREEN,"middle")
b += text(130,350,"V₂ / V₁ = N₂ / N₁        I₂ / I₁ = N₁ / N₂",20)
save("transformer", "Transformer: both coils link the same changing flux", b,380)

b = line(75,285,665,285,GRAY,True)
raw, smooth, previous = [], [], 0
for k in range(601):
    t = k*3*pi/600
    v = abs(sin(t))
    previous = max(v,previous*exp(-(3*pi/600)/5))
    raw.append((75+580*k/600,285-180*v))
    smooth.append((75+580*k/600,285-180*previous))
b += curve(raw,BLUE) + curve(smooth,RED)
b += text(80,70,"Rectified input",18,BLUE) + text(330,70,"Capacitor-smoothed output",18,RED)
b += text(200,335,"Capacitor charges near peaks and supplies the load between them.",16)
save("rectifier", "A smoothing capacitor reduces, but does not remove, ripple", b,365)

b = text(60,75,"Low-pass: output across C",18,BLUE) + text(380,75,"High-pass: output across R",18,RED)
b += line(55,110,95,110) + rect(95,100,55,20,"white") + text(115,94,"R",15)
b += line(150,110,270,110) + line(220,110,220,145) + line(200,145,240,145)
b += line(200,155,240,155) + line(220,155,220,185) + line(55,185,270,185)
b += text(245,154,"C",15) + text(275,115,"out",15)
b += line(385,110,430,110) + line(430,90,430,130) + line(440,90,440,130)
b += text(425,82,"C",15) + line(440,110,650,110) + line(600,110,600,135)
b += rect(590,135,20,30,"white") + line(600,165,600,185) + line(385,185,650,185)
b += text(620,154,"R",15) + text(655,115,"out",15)
b += line(90,450,660,450,GRAY,True) + line(90,450,90,245,GRAY,True)
b += text(30,245,"gain",18) + text(570,485,"ωRC (log scale)",16)
b += text(64,275,"1",16) + text(64,455,"0",16)
for v,label in [(0.01,"0.01"),(0.1,"0.1"),(1,"1"),(10,"10"),(100,"100")]:
    x=90+140*(log10(v)+2)
    b += text(x,472,label,15,anchor="middle")
for high,color in [(False,BLUE),(True,RED)]:
    pts=[]
    for k in range(301):
        z=-2+4*k/300
        w=10**z
        gain=(w if high else 1)/sqrt(1+w*w)
        pts.append((90+140*(z+2),450-180*gain))
    b += curve(pts,color)
b += line(370,450,370,265,GRAY,dash=True) + text(390,330,"cutoff: gain = 1/√2",17)
save("filters", "Output location determines what frequencies pass", b,510)

print(f"Generated {len(list(OUT.glob('*.svg')))} original SVG diagrams in {OUT}")
