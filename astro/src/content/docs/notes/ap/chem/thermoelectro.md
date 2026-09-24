---
title: "Unit 9: Thermodynamics and Electrochemistry"
description: "AP Chemistry notes on thermodynamics, entropy, Gibbs free energy, electrochemistry, galvanic cells, and electrolysis."
next: false
sidebar:
  order: 9
---

## Spontaneity and Thermodynamic favorability

A **spontaneous** process is one that occurs *without continuous external intervention* once the required conditions are present. Spontaneous does not mean fast. Iron rusting is thermodynamically favored under ordinary conditions, but it is slow because its pathway has kinetic barriers.

A process is **thermodynamically favored** when it is spontaneous under the stated conditions. A process can be thermodynamically favored but **kinetically controlled** if it happens slowly because the activation energy is high or the reaction mechanism is difficult.

<div class="theorem-box">

**Example.** A mixture remains unchanged until sparked, then reacts vigorously. Can the reaction have been thermodynamically favorable before the spark?

Yes. Favorability describes a decrease in free energy under the stated conditions, while the activation barrier controls how readily reaction starts. A spark can help the mixture cross that barrier. It does not establish the sign of the free-energy change by itself.

</div>

---

## The Second law and Entropy

The **Second Law of Thermodynamics** says that for any spontaneous process, the entropy of the universe increases:

$$
\Delta S_{\text{universe}} > 0.
$$

- **Entropy** $$S$$ is a measure of *energy dispersal* and the number of possible microscopic arrangements available to a system. A common shorthand is "chaos," but the more precise AP idea is that higher entropy means more accessible **microstates**.
- **Microstates** are the *possible arrangements of particles and energy* that produce the same macroscopic state. More particles, more volume, more freedom of motion, and more possible energy distributions usually mean more microstates and therefore higher entropy.

The entropy change for the universe is

$$
\Delta S_{\text{universe}} = \Delta S_{\text{system}} + \Delta S_{\text{surroundings}}.
$$

Use this sign test:


| Condition                          | Meaning                                              |
| ---------------------------------- | ---------------------------------------------------- |
| $$\Delta S_{\text{universe}} > 0$$ | Spontaneous in the forward direction                 |
| $$\Delta S_{\text{universe}} = 0$$ | Equilibrium                                          |
| $$\Delta S_{\text{universe}} < 0$$ | Nonspontaneous forward; reverse direction is favored |


Heat leaving the system increases surrounding entropy; heat entering the system decreases surrounding entropy. At constant pressure and temperature, the surroundings contribution is often written as

$$
\Delta S_{\text{surroundings}} = -\frac{\Delta H_{\text{system}}}{T}.
$$

This equation explains why exothermic reactions often help spontaneity: if $$\Delta H_{\text{system}} < 0$$, then $$\Delta S_{\text{surroundings}} > 0$$.

<div class="theorem-box">

**Example.** At $$300\ K$$, a process has $$\Delta H=-6.00\ \mathrm{kJ}$$ and $$\Delta S_{sys}=-10.0\ \mathrm{J/K}$$. Determine whether the total entropy change is favorable.

The surroundings gain entropy $$-\Delta H/T=6000/300=20.0\ \mathrm{J/K}$$. Thus $$\Delta S_{univ}=-10.0+20.0=+10.0\ \mathrm{J/K}$$, favoring the process. The system can become more ordered if the surroundings' entropy increase is larger.

</div>

---

## Predicting entropy changes

To predict whether $$\Delta S_{\text{system}}$$ is positive or negative, compare particle freedom and the number of particles before and after the process.

Entropy usually increases when:

1. A substance changes to a more disordered phase: solid $$\rightarrow$$ liquid $$\rightarrow$$ gas.
2. The number of gas particles increases.
3. A solid or liquid dissolves into many aqueous ions or particles.
4. Temperature increases, because more energy states become accessible.
5. A larger, more complex molecule has more ways to vibrate, rotate, and arrange energy.

Entropy usually decreases when:

1. Gases become liquids or solids.
2. The number of gas particles decreases.
3. Separate particles combine into one more ordered product.
4. Ions or molecules crystallize from solution.

For aqueous ionic compounds, remember the **van't Hoff factor** idea from solutions: one formula unit can produce multiple dissolved particles. For example, dissolving $$\text{CaCl}_2$$ can produce three ions per formula unit, so the number of independently moving particles increases.

Some reactions look counterintuitive if you only inspect the system. For example, building biological polymers from smaller units can decrease system entropy, but the overall process can still be favored if heat release or coupled reactions increase the entropy of the surroundings enough.

<div class="theorem-box">

**Example.** Compare the likely entropy signs for liquid water vaporizing and two gas molecules combining into one gas molecule. Explain the particle-level basis.

Vaporization makes far more spatial arrangements accessible, giving positive system entropy change. Combining two gas molecules into one usually reduces translational arrangements, favoring a negative change. These are qualitative predictions; detailed molar-entropy data settle cases where other contributions compete.

</div>

---

## Standard molar entropy

**Standard molar entropy** $$S^\circ$$ is the absolute entropy of one mole of a substance in its *standard state*, usually reported at $$298\ \text{K}$$ and $$1\ \text{bar}$$ or approximately $$1\ \text{atm}$$.

The **Third Law of Thermodynamics** says that a perfect crystal at $$0\ \text{K}$$ has entropy equal to zero:

$$
S = 0 \quad \text{for a perfect crystal at } 0\ \text{K}.
$$

Unlike standard enthalpies of formation, standard molar entropies are not usually zero for elements at $$298\ \text{K}$$. Real substances have motion and energy distributions above absolute zero, so they have positive entropy.

For a reaction,

$$
\Delta S^\circ_{\text{rxn}} = \sum n_p S^\circ_{\text{products}} - \sum n_r S^\circ_{\text{reactants}},
$$

where $$n_p$$ and $$n_r$$ are the stoichiometric coefficients of products and reactants. Entropy is commonly tabulated in $$\text{J}/(\text{mol}\cdot\text{K})$$, not $$\text{kJ}/(\text{mol}\cdot\text{K})$$, so unit conversion matters when combining entropy with enthalpy or Gibbs free energy.

<div class="theorem-box">

**Example.** A student sets the standard molar entropy of oxygen gas to zero because its formation enthalpy is zero. Explain the distinction.

Standard molar entropy measures accessible energy arrangements at the stated temperature and is not assigned zero for ordinary elements at room temperature. Zero standard formation enthalpy is a reference convention. The third-law zero concerns a perfect crystal at zero kelvin, not a gas at room temperature.

</div>

---

## Gibbs free energy

**Gibbs free energy** $$G$$ is the thermodynamic quantity that predicts *maximum useful non-expansion work* at constant temperature and pressure. For a reaction,

$$
\Delta G = \Delta H - T\Delta S.
$$

Here $$T$$ must be in Kelvin. If $$\Delta H$$ is in $$\text{kJ/mol}$$, then $$T\Delta S$$ must also be in $$\text{kJ/mol}$$. Since $$\Delta S$$ is often given in joules, convert it:

$$
1\ \text{kJ} = 1000\ \text{J}.
$$



The sign of $$\Delta G$$ determines thermodynamic favorability:


| $$\Delta G$$     | Meaning                         |
| ---------------- | ------------------------------- |
| $$\Delta G < 0$$ | Spontaneous forward reaction    |
| $$\Delta G = 0$$ | Equilibrium                     |
| $$\Delta G > 0$$ | Nonspontaneous forward reaction |


### Enthalpy and entropy drivers

A reaction is **enthalpy-driven** when a large negative $$\Delta H$$ dominates the $$-T\Delta S$$ term. A reaction is **entropy-driven** when a large positive $$\Delta S$$ makes $$-T\Delta S$$ very negative, especially at high temperature.


| $$\Delta H$$ | $$\Delta S$$ | Spontaneity                        |
| ------------ | ------------ | ---------------------------------- |
| Negative     | Positive     | Spontaneous at all temperatures    |
| Positive     | Negative     | Nonspontaneous at all temperatures |
| Negative     | Negative     | Spontaneous at low temperature     |
| Positive     | Positive     | Spontaneous at high temperature    |


When $$\Delta G = 0$$, the threshold temperature is

$$
T = \frac{\Delta H}{\Delta S},
$$

as long as units match.

<div class="theorem-box">

**Example.** A reaction has $$\Delta H=+40.0\ \mathrm{kJ/mol}$$ and $$\Delta S=+100.\ \mathrm{J/(mol\,K)}$$. Find its crossover temperature and predict favorability at $$500\ K$$, assuming these quantities are constant.

Convert entropy to $$0.100\ \mathrm{kJ/(mol\,K)}$$. Then $$T=\Delta H/\Delta S=400\ K$$ and $$\Delta G(500)=40.0-500(0.100)=-10.0\ \mathrm{kJ/mol}$$. Above 400 K the favorable entropy term outweighs the positive enthalpy change.

</div>

---

## Standard and nonstandard free energy

**Standard Gibbs free energy change** $$\Delta G^\circ$$ is the free energy change when all reactants and products are in their standard states.

You can calculate it from standard free energies of formation:

$$
\Delta G^\circ_{\text{rxn}} = \sum n_p \Delta G_f^\circ(\text{products}) - \sum n_r \Delta G_f^\circ(\text{reactants}).
$$

Elements in their standard states have $$\Delta G_f^\circ = 0$$.

Free energy also connects directly to equilibrium:

$$
\Delta G^\circ = -RT\ln K.
$$

Under nonstandard conditions,

$$
\Delta G = \Delta G^\circ + RT\ln Q.
$$

Combining the equations gives

$$
\Delta G = RT\ln\left(\frac{Q}{K}\right).
$$

If $$Q < K$$, then $$\Delta G < 0$$ and the reaction proceeds forward. If $$Q > K$$, then $$\Delta G > 0$$ and the reverse direction is favored. At equilibrium, $$Q = K$$ and $$\Delta G = 0$$.

<div class="theorem-box">

**Example.** At fixed temperature, a reaction has $$K=100$$ but the prepared mixture has $$Q=1000$$. Predict the sign of actual free-energy change despite its negative standard value.

$$\Delta G=RT\ln(Q/K)=RT\ln10>0$$, so the forward direction is unfavorable in that mixture. The reverse direction reduces Q toward K. Standard free energy describes a reference composition; actual direction requires the current reaction quotient.

</div>

---

## Coupled reactions

**Coupled reactions** combine a thermodynamically unfavorable process with a favorable process so the net $$\Delta G$$ is negative. The reactions usually share a common intermediate or occur through a linked mechanism.

Because $$G$$ is a state function, Gibbs free energy changes add like Hess's law:

$$
\Delta G_{\text{net}} = \Delta G_1 + \Delta G_2 + \cdots
$$

The coupled process is thermodynamically favored when

$$
\Delta G_{\text{net}} < 0.
$$

This is how many biological and industrial processes drive unfavorable steps: the system "pays" for them using a more favorable reaction.

<div class="theorem-box">

**Example.** An uphill step has $$\Delta G=+25\ \mathrm{kJ/mol}$$ and a linked downhill step has $$-40\ \mathrm{kJ/mol}$$. Does their sum establish that simply mixing separate reactants will force the uphill step?

The linked net reaction has $$\Delta G=-15\ \mathrm{kJ/mol}$$ and is favorable. But an actual mechanism must couple the processes, for example by consuming a shared intermediate. An unrelated exergonic reaction occurring nearby does not automatically drive the uphill chemistry.

</div>

---

## Electrochemistry overview

**Electrochemistry** studies *electron-transfer reactions* and the conversion between chemical energy and electrical work. Electrochemical cells are built from two half-reactions:

1. **Oxidation**: loss of electrons.
2. **Reduction**: gain of electrons.

Remember:

- **ANOX**: oxidation occurs at the anode.
- **REDCAT**: reduction occurs at the cathode.

Electrons flow through the external wire from anode to cathode. Ions move through the solution or salt bridge to maintain charge balance.

<div class="theorem-box">

**Example.** A student proposes that electrons leave the anode through the salt bridge and return through the wire. Explain which charge carriers move in each path.

Electrons travel through the metallic external circuit from oxidation to reduction. Ions migrate through the electrolyte and salt bridge to prevent charge buildup. Both paths complete the circuit, but ionic migration is not electron conduction through the salt solution.

</div>

---

## Galvanic cells

A **galvanic cell** converts a *spontaneous redox reaction* into electrical work by separating oxidation and reduction into different compartments. A battery is one or more galvanic cells connected to provide power. A **fuel cell** is a galvanic cell where reactants are continuously supplied; unlike a sealed battery, it can keep operating as long as fuel and oxidant are replenished. All galvanic cells involve having two *separate* compartments, with the cathode (reduction site) in one compartment and the anode (oxidation site) in the other. The two are connected with a salt bridge, which maintains neutrality.

In a galvanic cell:


| Part            | Role                                                                 |
| --------------- | -------------------------------------------------------------------- |
| **Anode**       | Site of *oxidation*; produces electrons; negative in a galvanic cell |
| **Cathode**     | Site of *reduction*; consumes electrons; positive in a galvanic cell |
| **Salt bridge** | Allows ion flow to maintain charge neutrality                        |
| External wire   | Allows electron flow from anode to cathode                           |


The **salt bridge** is usually a U-shaped tube or porous barrier containing inert ions. Without it, charge buildup stops electron flow. Anions migrate toward the anode to balance newly produced cations, and cations migrate toward the cathode to replace cations being reduced.

<div class="theorem-box">

**Example.** The salt bridge is removed from an operating Zn/Cu cell while the wire remains connected. Explain why sustained current stops although both electrodes remain present.

Zinc oxidation leaves excess positive charge in its compartment; copper-ion reduction removes positive charge from the other. Without ion migration, this charge separation rapidly opposes further electron transfer. Keeping a wire connected cannot replace the missing ionic path.

</div>

---

## Cell potential and electrical work

**Cell potential** $$E_{\text{cell}}$$ is the *electrical potential difference* of a cell, measured in volts. It reflects the thermodynamic tendency for electrons to move through the external circuit. The ideal thermodynamic cell potential is measured for an open circuit, or with negligible current, so the cell is not being significantly drained while it is measured.

Charge is

$$
q = nF = It,
$$

where $$n$$ is moles of electrons, $$F = 96485\ \text{C/mol e}^-$$ is **Faraday's constant**, $$I$$ is current in amperes, and $$t$$ is time in seconds.

Electrical work and cell potential are related by

$$
w_{\text{max}} = -qE_{\text{cell}}.
$$

For a redox reaction,

$$
\Delta G = -nFE_{\text{cell}}.
$$

Important sign connection:


| Condition               | Meaning                                     |
| ----------------------- | ------------------------------------------- |
| $$E_{\text{cell}} > 0$$ | $$\Delta G < 0$$, spontaneous as written    |
| $$E_{\text{cell}} = 0$$ | $$\Delta G = 0$$, equilibrium               |
| $$E_{\text{cell}} < 0$$ | $$\Delta G > 0$$, nonspontaneous as written |


Cell potential is an **intensive property**, so it does not get multiplied by stoichiometric coefficients. If a half-reaction is doubled, $$\Delta G$$ doubles because $$n$$ doubles, but $$E^\circ$$ stays the same.

The percent efficiency of a cell can be estimated by

$$
\text{efficiency} = \frac{\text{actual work}}{\text{theoretical maximum work}} \times 100
$$

<div class="theorem-box">

**Example.** A balanced cell reaction is doubled. Determine the changes in n, standard free energy, and standard voltage.

Electron stoichiometry n doubles, and the free energy for the doubled reaction doubles. Since $$E^\circ=-\Delta G^\circ/(nF)$$, their ratio stays fixed. Voltage is energy per unit charge, not the total amount of energy available.

</div>

---

## Standard reduction potentials

**Standard reduction potential** $$E^\circ$$ is the *cell potential contribution for a half-reaction written as a reduction* under standard conditions. Tables list reductions by convention.

The standard hydrogen electrode is assigned

$$
2\text{H}^+(aq) + 2e^- \longrightarrow \text{H}_2(g), \qquad E^\circ = 0.00\ \text{V}.
$$

The more positive the standard reduction potential, the easier the species is to reduce and the stronger it is as an oxidizing agent. The more negative the value, the more the reverse oxidation is favored and the stronger the reduced species is as a reducing agent.

For a galvanic cell,

$$
E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}},
$$

where both values are read from a reduction potential table. The cathode usually has the more positive reduction potential.

Do not change the sign of the tabulated anode value before using the subtraction form. If instead you write

$$
E^\circ_{\text{cell}} = E^\circ_{\text{red}} + E^\circ_{\text{ox}},
$$

then you must reverse the anode half-reaction and change its sign.

Under standard galvanic conditions, electrons flow from the anode with the lower reduction potential to the cathode with the higher reduction potential. Voltage measures energy per unit charge, not the number of electrons present.

<div class="theorem-box">

**Example.** Half-cell reductions have potentials $$+0.80$$ and $$-0.40\ V$$. Determine the spontaneous cathode and voltage, and explain whether multiplying one half-reaction by three multiplies its potential.

The more positive reduction runs at the cathode, giving $$E^\circ=0.80-(-0.40)=1.20\ V$$. Balancing electron counts changes amounts, not energy per charge, so no tabulated potential is multiplied by three. Electrons flow from the lower-reduction-potential anode toward the cathode.

</div>

---

## Line notation

**Line notation** is a compact way to represent an electrochemical cell. For a galvanic cell, the anode is written on the left and the cathode on the right:

$$
\text{anode} \mid \text{anode solution} \parallel \text{cathode solution} \mid \text{cathode}.
$$

Single vertical lines $$\mid$$ mark phase boundaries. The double vertical line $$\parallel$$ represents the salt bridge.

Example:

$$
\text{Zn}(s)\mid \text{Zn}^{2+}(aq)\parallel \text{Cu}^{2+}(aq)\mid \text{Cu}(s).
$$

This describes a cell where zinc is oxidized at the anode and copper ions are reduced at the cathode.

<div class="theorem-box">

**Example.** Interpret $$\mathrm{Pt(s)\mid Fe^{2+}(aq),Fe^{3+}(aq)\parallel Ag^+(aq)\mid Ag(s)}$$ with the left side as anode. Explain the role of Pt.

Iron(II) is oxidized to iron(III), and silver ions are reduced to silver metal. Both iron species are dissolved, so an inert conductor is needed to exchange electrons with the wire. Platinum supplies that conducting surface without appearing in the net reaction.

</div>

---

## The Nernst equation

The **Nernst equation** relates cell potential to *nonstandard concentrations or pressures*:

$$
E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{RT}{nF}\ln Q.
$$

At $$25^\circ\text{C}$$, this becomes

$$
E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{0.0592}{n}\log Q.
$$

As a galvanic cell runs, reactants are consumed and products form, so $$Q$$ increases and $$E_{\text{cell}}$$ usually decreases. At equilibrium,

$$
E_{\text{cell}} = 0.
$$

Combining Nernst with equilibrium gives

$$
E^\circ_{\text{cell}} = \frac{RT}{nF}\ln K
$$

or at $$25^\circ\text{C}$$,

$$
E^\circ_{\text{cell}} = \frac{0.0592}{n}\log K.
$$

<div class="theorem-box">

**Example.** For a two-electron cell at $$25^\circ\mathrm{C}$$, Q increases by a factor of 100. Determine the voltage change without knowing its initial value.

Subtracting two Nernst equations gives $$\Delta E=-(0.0592/2)\log100=-0.0592\ V$$. The standard potential cancels. Increasing the product-to-reactant activity ratio reduces the forward driving force.

</div>

---

## Concentration cells and ion-selective electrodes

A **concentration cell** uses the same redox couple in both half-cells but at different concentrations. Because the electrodes and species are chemically the same, $$E^\circ_{\text{cell}} = 0$$, and the voltage comes entirely from the concentration difference.

The spontaneous direction reduces the concentration difference. Electrons flow from the dilute side to the concentrated side for a metal-ion concentration cell, so metal tends to oxidize on the dilute side and plate onto the concentrated side.

An **ion-selective electrode** is an electrode that responds selectively to a particular ion concentration. Its potential follows Nernst-type behavior, so it can be used to measure ion activity, such as $$\text{H}^+$$ in a pH electrode or $$\text{F}^-$$ in a fluoride electrode.

<div class="theorem-box">

**Example.** A copper concentration cell has $$[Cu^{2+}]=0.010\ M$$ on the left and $$1.0\ M$$ on the right. Identify the anode and explain how discharge reduces the concentration difference.

Oxidation occurs on the dilute left side, adding copper ions. Reduction occurs on the concentrated right side, removing them. Electrons flow left to right. Standard cell potential is zero, but the concentration difference gives a positive actual potential.

</div>

---

## Corrosion

**Corrosion** is an electrochemical process where different parts of a metal surface act as anodes and cathodes. At anodic sites, metal atoms oxidize:

$$
\text{M}(s) \longrightarrow \text{M}^{n+}(aq) + ne^-.
$$

Electrons travel through the metal to cathodic sites, where a reduction reaction occurs, often involving oxygen and water. Rusting of iron is a common example.

Corrosion can be slowed by:

1. Coating the metal to block water and oxygen.
2. Alloying to form a more resistant material.
3. Adding corrosion inhibitors.
4. Using **cathodic protection**.

In cathodic protection, a more easily oxidized metal acts as a **sacrificial anode**. It oxidizes instead of the protected metal, keeping the protected metal as the cathode.

<div class="theorem-box">

**Example.** A scratched iron object is electrically connected to a more easily oxidized sacrificial metal. Explain why protection can continue despite the scratch.

The sacrificial metal supplies electrons as it oxidizes, keeping iron cathodic and suppressing its oxidation. Protection depends on electrical contact and an ionic path, not an intact surface barrier. Once the sacrificial metal is consumed, that protection is lost.

</div>

---

## Electrolytic cells

An **electrolytic cell** uses *external electrical energy* to drive a nonspontaneous redox reaction. Electrolytic cells are used in electroplating, metal purification, and production of elements from molten salts or aqueous ions.

Oxidation still occurs at the anode and reduction still occurs at the cathode. The sign of the electrodes changes compared with galvanic cells:

| Cell type    | Anode    | Cathode  | Spontaneity                            |
| ------------ | -------- | -------- | -------------------------------------- |
| Galvanic     | Negative | Positive | Spontaneous                            |
| Electrolytic | Positive | Negative | Nonspontaneous; driven by power source |

If both electrodes are in the same compartment and an external battery is driving the reaction, the setup is usually electrolytic. The absence of a salt bridge can also suggest a simple electrolytic setup, though some galvanic cells use porous barriers instead of classic U-shaped bridges. Basically, electrolytics cells are like galvanic cells but reversed.

<div class="theorem-box">

**Example.** A rechargeable cell is driven in reverse by an external source. Do the physical electrodes retain their discharge labels anode and cathode?

No. Labels follow the reactions: the electrode now undergoing oxidation is the anode, and the one now undergoing reduction is the cathode. Reversing the chemistry exchanges those roles. The definitions do not depend on a permanent label stamped on the metal.

</div>

---

## Electrolysis of salts

### Electrolysis of molten salts

Often, we want to derive the individual solid metal components from a compound. One method that is used is the **electrolysis of molten salts**, when molten, liquid, *non-aqueous* ionic salts are electrolyzed into their elemental forms. The anions will react at the anode, while the cations will react at the cathode. For example, in the electrolysis of $$PbBr_2$$:

At the anode: $$2 Br^{-} (l) \longrightarrow Br_2 (l) + 2 e^{-}$$

At the cathode: $$Pb^{2+} (l) + 2 e^{-} \longrightarrow Pb(s)$$

Since no water is present, it can't react! The metals/liquids should then form onto an **inert electrode** (like platinum and graphite). However, the electrolysis of molten salts is not very practical because it takes hundreds and even thousands of degrees to get the salts into molten form!

<div class="theorem-box">

**Example.** For molten $$\mathrm{MgCl_2}$$, a student predicts chlorine at the cathode because chloride is negative. Correct the electrode assignments and find the mole ratio of products.

Cations migrate toward the negative cathode, where $$\mathrm{Mg^{2+}+2e^-\rightarrow Mg}$$. Chloride migrates toward the positive anode, where $$\mathrm{2Cl^-\rightarrow Cl_2+2e^-}$$. Equal electron transfer gives one mole of magnesium per mole of chlorine gas. The charge of an ion predicts which electrode attracts it, while reduction or oxidation determines the product formed there.

</div>

### Electrolysis of aqueous solutions

More commonly, electrolysis is done on *aqueous solutions* to generate the elemental form of elements from compounds. It is similar to the molten salt electrolysis, expect water is present and could react at either, both, or neither electrode. Usually, the half-reaction with a *higher potential* (whether oxidation or reduction) will be favored at an electrode (with the exception of the comparison of $$Cl_2$$ and water).

At the anode: Compare the oxidation of anion vs. water ($$-1.23 V$$). If water was oxidized, gas is produced, and the solution should be acidic.

At the cathode: Compare the reduction of cation vs. water ($$-0.83 V$$). If water was reduced, gas is produced, and the solution should be basic.

Note that the reduction and oxidation of water have DIFFERENT magnitudes! They are two separate reactions and have different voltages!

Below are some common observations that would occur if certain elements formed:

| Element   | Observations        |
| ----------| ------------------- |
| $$Br_2$$ (l) | Yellow liquid, clear in starch |
| $$I_2$$ (l) | Yellow liquid, dark blue in starch|
| $$Cl_2$$ (g) | Gas that discolors green dye |
| $$Cu$$ (s) | Orange-colored solid forming on electrode |
| $$Co$$ (s) | Silver-colored solid forming on electrode |
| $$H_2$$ (g) | Bubbling gas with small, fast-rising bubbles |
| $$O_2$$ (g) | Bubbling gas with large, slow-rising bubbles |
| $$OH^{-}$$ (aq) | Blue in bromothymol blue, pink in phenolphthalein|
| $$H^{+}$$ (aq) | Yellow in bromothymol blue, clear in phenolphthalein |

<div class="theorem-box">

**Example.** Explain why molten NaCl can yield sodium metal but aqueous NaCl normally produces hydrogen at the cathode.

The melt contains sodium and chloride ions without water competing. In aqueous solution, water is reduced more readily than sodium ions under ordinary conditions, producing hydrogen and hydroxide. Listing the dissolved cation alone is therefore insufficient for predicting aqueous products.

</div>

---

## Electroplating and competing reactions

**Electroplating** deposits a thin layer of metal onto an object by reducing metal ions at the cathode:

$$
\text{M}^{n+}(aq) + ne^- \longrightarrow \text{M}(s).
$$

In aqueous electrolysis, water can compete with dissolved ions. Whether water or an ion is oxidized/reduced depends on reduction potentials, concentration, electrode material, and overpotential. AP problems often simplify this by giving the relevant half-reactions or asking you to compare standard potentials.

<div class="theorem-box">

**Example.** A copper-plating experiment deposits only 80% of the mass predicted from charge passed. Explain how hydrogen evolution could account for the shortfall.

The theoretical mass assumes every electron reduces copper ions. If some electrons reduce water or acid to hydrogen instead, less charge is available for copper deposition. An 80% current efficiency would multiply the ideal copper mass by 0.80; it does not mean charge disappeared.

</div>

---

## Faraday's law

**Faraday's law** says that the amount of substance produced or consumed at an electrode is *directly proportional to the total charge passed through the cell*.

Use this unit pathway:

$$
\text{current} \times \text{time} \rightarrow \text{coulombs} \rightarrow \text{mol e}^- \rightarrow \text{mol substance} \rightarrow \text{mass}.
$$

Because $$q = It$$ and $$1\ \text{mol e}^- = F\ \text{C}$$,

$$
\text{mol e}^- = \frac{It}{F}.
$$

If $$n$$ electrons produce one formula unit or atom of the substance, then

$$
m = \frac{MIt}{nF},
$$

where $$m$$ is mass, $$M$$ is molar mass, $$I$$ is current, $$t$$ is time, $$n$$ is moles of electrons per mole of product, and $$F$$ is Faraday's constant.

For example, plating $$\text{Cu}(s)$$ from $$\text{Cu}^{2+}$$ requires two electrons per copper atom:

$$
\text{Cu}^{2+} + 2e^- \longrightarrow \text{Cu}(s).
$$

So $$n = 2$$ in the mass equation.

---

:::checklist
1. Decide whether the question is about thermodynamics, electrochemistry, or both.
2. For entropy, compare phases, gas moles, dissolved particles, and temperature.
3. For Gibbs free energy, keep units consistent: $$\Delta H$$ and $$T\Delta S$$ must match.
4. Use $$\Delta G < 0$$, $$E_{\text{cell}} > 0$$, and $$K > 1$$ as equivalent signs of a favored forward reaction under standard conditions.
5. In galvanic cells, anode is oxidation, cathode is reduction, and electrons flow anode $$\rightarrow$$ cathode.
6. Use reduction potential tables carefully: values are intensive, and tabulated half-reactions are written as reductions.
7. For nonstandard cells, write $$Q$$ correctly before using the Nernst equation.
8. For electrolysis, convert current and time into charge, then into moles of electrons.
:::

---

:::equations
| Idea                                       | Equation                                                                                                                 |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Entropy of universe                        | $$\Delta S_{\text{universe}} = \Delta S_{\text{system}} + \Delta S_{\text{surroundings}}$$                               |
| Surroundings entropy                       | $$\Delta S_{\text{surroundings}} = -\Delta H_{\text{system}}/T$$                                                         |
| Standard reaction entropy                  | $$\Delta S^\circ_{\text{rxn}} = \sum n_p S^\circ_{\text{products}} - \sum n_r S^\circ_{\text{reactants}}$$               |
| Gibbs free energy                          | $$\Delta G = \Delta H - T\Delta S$$                                                                                      |
| Standard free energy from formation values | $$\Delta G^\circ_{\text{rxn}} = \sum n_p\Delta G_f^\circ(\text{products}) - \sum n_r\Delta G_f^\circ(\text{reactants})$$ |
| Free energy and equilibrium                | $$\Delta G^\circ = -RT\ln K$$                                                                                            |
| Nonstandard free energy                    | $$\Delta G = \Delta G^\circ + RT\ln Q$$                                                                                  |
| Free energy and cell potential             | $$\Delta G = -nFE_{\text{cell}}$$                                                                                        |
| Standard cell potential                    | $$E^\circ_{\text{cell}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}$$                                            |
| Nernst equation                            | $$E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{RT}{nF}\ln Q$$                                                         |
| Nernst at $$25^\circ\text{C}$$             | $$E_{\text{cell}} = E^\circ_{\text{cell}} - \frac{0.0592}{n}\log Q$$                                                     |
| Charge                                     | $$q = nF = It$$                                                                                                          |
| Faraday's law mass form                    | $$m = \frac{MIt}{nF}$$                                                                                                   |
:::

<div class="theorem-box">

**Example.** Equal charge passes through silver-ion and copper(II)-ion plating cells. Using molar masses 107.9 and $$63.55\ \mathrm{g/mol}$$, compare deposited masses.

Silver needs one electron per atom and copper needs two. Thus $$m_{Ag}/m_{Cu}=(107.9/1)/(63.55/2)=3.40$$. Equal charge means equal electron amounts, not equal metal moles or equal masses.

</div>

---


## Practice

### MCQ

::::problem
1. A reaction has $$\Delta H^\circ=+60.0\ \mathrm{kJ/mol}$$ and $$\Delta S^\circ=+150\ \mathrm{J/(mol\,K)}$$. Assuming both are constant, when is the standard reaction favorable?

   (A) Below 400 K<br>
   (B) Above 400 K<br>
   (C) At every temperature<br>
   (D) At no temperature

:::solution
Convert entropy to 0.150 kJ/(mol K). The crossover is $$60.0/0.150=400\ K$$. Above it, $$T\Delta S^\circ$$ exceeds $$\Delta H^\circ$$ and standard free energy is negative.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
2. For a two-electron cell at $$25^\circ C$$, $$E^\circ=1.10\ V$$ and $$Q=100$$. Find its actual potential.

   (A) $$1.1592\ V$$<br>
   (B) $$1.1000\ V$$<br>
   (C) $$1.0408\ V$$<br>
   (D) $$0.9816\ V$$

:::solution
$$E=1.10-(0.0592/2)\log100=1.0408\ V$$. Both the electron coefficient and the base-ten logarithm matter; product enrichment reduces forward voltage.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
3. Doubling a balanced redox equation changes which quantities?

   (A) E doubles but n stays fixed<br>
   (B) E and standard free energy both stay fixed<br>
   (C) E doubles and standard free energy halves<br>
   (D) n and standard free energy double, but E stays fixed

:::solution
Standard free energy scales with the reaction amount and n scales with electrons transferred. Their ratio $$-\Delta G^\circ/(nF)$$ is unchanged, so voltage remains fixed.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
4. Exactly $$0.100\ \mathrm{mol}$$ electrons passes through a copper-plating cell, but only 80.0% reduces copper(II). Use molar mass $$63.55\ \mathrm{g/mol}$$. What mass plates?

   (A) $$2.54\ g$$<br>
   (B) $$3.18\ g$$<br>
   (C) $$5.08\ g$$<br>
   (D) $$6.36\ g$$

:::solution
Effective electron amount is 0.0800 mol. Two electrons plate one Cu, giving 0.0400 mol Cu and $$0.0400(63.55)=2.54\ g$$. Efficiency applies to useful charge before the electron-to-metal conversion.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
5. An operating Zn/Cu galvanic cell uses an inert salt bridge. Which description of charge flow is correct?

   (A) Electrons cross the bridge toward zinc<br>
   (B) Anions migrate toward the zinc compartment as zinc ions form<br>
   (C) Cations migrate toward zinc to increase its positive charge<br>
   (D) Electrons move through solution from copper to zinc

:::solution
Zinc oxidation adds cations to its compartment, requiring anion migration for charge balance. Electrons flow through the external wire from zinc toward copper, not through the salt bridge.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
6. A cell has positive standard voltage but actual reaction quotient larger than K. Which conclusion follows?

   (A) Its forward reaction is favorable because standard voltage is positive<br>
   (B) A catalyst will increase K until discharge resumes<br>
   (C) Its actual forward voltage is negative<br>
   (D) Its standard free energy becomes zero

:::solution
$$\Delta G=RT\ln(Q/K)>0$$, so $$E=-\Delta G/(nF)<0$$ for the written forward reaction. Standard voltage remains a reference property; actual composition can reverse the favorable direction.

$$
\boxed{\text{C}}.
$$
:::
::::

### FRQ

::::frq{id=chem-thermoelectro-1}
7. A galvanic cell is based on the reaction

$$
\text{Zn}(s)+\text{Cu}^{2+}(aq)\rightarrow\text{Zn}^{2+}(aq)+\text{Cu}(s).
$$

Use $$E^\circ_{\text{red}}(\text{Cu}^{2+}/\text{Cu})=+0.34\ \text{V}$$ and $$E^\circ_{\text{red}}(\text{Zn}^{2+}/\text{Zn})=-0.76\ \text{V}$$.

   $$(A)$$ Identify the anode and cathode.

   $$(B)$$ Calculate $$E^\circ_{\text{cell}}$$.

   $$(C)$$ Calculate $$\Delta G^\circ$$ for the reaction.

   $$(D)$$ Explain the direction of electron flow in the external circuit.

   $$(E)$$ **Original extension.** At $$25^\circ\text{C}$$, let $$[\text{Zn}^{2+}]=1.00\ M$$ and $$[\text{Cu}^{2+}]=0.0100\ M$$. Calculate the cell potential and explain why its change from the standard value agrees with the reaction quotient.

:::solution
$$(A)$$ Zinc is oxidized:

$$
\text{Zn}(s)\rightarrow\text{Zn}^{2+}(aq)+2e^-,
$$

so zinc is the anode. Copper(II) is reduced at the cathode:

$$
\text{Cu}^{2+}(aq)+2e^-\rightarrow\text{Cu}(s).
$$

This follows the rule that oxidation occurs at the anode and reduction occurs at the cathode.

$$(B)$$

$$
E^\circ_{\text{cell}}=E^\circ_{\text{cathode}}-E^\circ_{\text{anode}}
$$

$$
E^\circ_{\text{cell}}=0.34-(-0.76)=1.10\ \text{V}.
$$

The positive cell potential is consistent with the reaction being spontaneous as a galvanic cell under standard conditions.

$$(C)$$ Here $$n=2$$.

$$
\Delta G^\circ=-nFE^\circ_{\text{cell}}
$$

$$
\Delta G^\circ=-(2)(96485)(1.10)=-2.12\times10^5\ \text{J/mol rxn}.
$$

So

$$
\boxed{\Delta G^\circ=-212\ \text{kJ/mol rxn}}.
$$

$$(D)$$ Electrons are produced at the zinc anode and consumed at the copper cathode, so electrons flow from Zn to Cu through the external circuit. Ions move through the salt bridge to maintain charge balance, but electrons do not travel through the salt bridge.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,patterns,decorations.pathmorphing,angles,quotes}
\begin{tikzpicture}[>=Stealth, font=\small]
\draw (-4,-1.4) rectangle (-1,1.2); \draw (1,-1.4) rectangle (4,1.2);
\draw[fill=gray!20] (-3.2,-1.1) rectangle (-2.9,0.9); \node at (-3.05,1.45) {Zn anode};
\draw[fill=orange!30] (2.9,-1.1) rectangle (3.2,0.9); \node at (3.05,1.45) {Cu cathode};
\draw[thick] (-3.05,0.9) -- (-3.05,2.2) -- (3.05,2.2) -- (3.05,0.9);
\draw[->, very thick, blue] (-2.4,2.45) -- (2.4,2.45) node[midway, above] {electron flow};
\draw[rounded corners, fill=yellow!20] (-1.2,0.8) -- (-0.5,1.45) -- (0.5,1.45) -- (1.2,0.8) -- (0.8,0.65) -- (0.35,1.05) -- (-0.35,1.05) -- (-0.8,0.65) -- cycle;
\node at (0,1.75) {salt bridge};
\end{tikzpicture}
```

$$(E)$$ For $$\text{Zn}(s)+\text{Cu}^{2+}(aq)\rightarrow\text{Zn}^{2+}(aq)+\text{Cu}(s)$$, $$Q=[\text{Zn}^{2+}]/[\text{Cu}^{2+}]=100$$; the solids are excluded. The Nernst equation gives $$E=1.10-(0.0592/2)\log(100)=1.04\ \text{V}$$. Relative to standard conditions, the mixture has a larger product-to-reactant ratio, reducing the forward driving force and voltage. The voltage is still positive, so the forward reaction remains thermodynamically favorable under these conditions.
:::
::::

::::frq{id=chem-thermoelectro-2}
8. The 2024 AP Chemistry exam included electroplating and nonspontaneous electrochemistry in a sterling silver context. (Adapted from College Board, [2024 AP Chemistry FRQ 3](https://apcentral.collegeboard.org/media/pdf/ap24-frq-chemistry.pdf).)

   $$(A)$$ Explain why an electrolytic plating process requires an external power source.

   $$(B)$$ Calculate the time required to plate $$1.00\ \text{g}$$ of $$\text{Cu}(s)$$ from $$\text{Cu}^{2+}$$ using a current of $$2.00\ \text{A}$$.

   $$(C)$$ Identify whether reduction or oxidation occurs at the object being plated.

   $$(D)$$ **Original extension.** Only $$80.0\%$$ of the current deposits copper; the rest drives a competing reaction. Recalculate the time to deposit the same mass and explain whether the copper half-reaction's electron coefficient changes.

:::solution
$$(A)$$ Electroplating is nonspontaneous as written, so an external power source is needed to drive electron flow and force reduction of metal ions onto the object. In other words, electrical energy is used to make a thermodynamically unfavorable redox process occur.

$$(B)$$ Moles of copper plated:

$$
n_{\text{Cu}}=\frac{1.00\ \text{g}}{63.55\ \text{g/mol}}=0.0157\ \text{mol}.
$$

For $$\text{Cu}^{2+}+2e^-\rightarrow\text{Cu}(s)$$,

$$
n_{e^-}=2(0.0157)=0.0315\ \text{mol e}^-.
$$

Charge required:

$$
q=nF=(0.0315)(96485)=3.04\times10^3\ \text{C}.
$$

Since $$q=It$$,

$$
t=\frac{3.04\times10^3\ \text{C}}{2.00\ \text{C/s}}=1.52\times10^3\ \text{s}.
$$

This is about $$25.3\ \text{min}$$ if converted to minutes.

$$(C)$$ Metal ions gain electrons and become solid metal on the object, so reduction occurs at the object being plated. The object being plated acts as the cathode in the electrolytic cell.

$$(D)$$ The useful deposition current is $$0.800(2.00)=1.60\ \text{A}$$. Equivalently, the required total charge is the ideal deposition charge divided by $$0.800$$. Thus $$t=t_{\text{ideal}}/0.800\approx1.90\times10^3\ \text{s}$$, or $$31.6\ \text{min}$$. The reaction remains $$\text{Cu}^{2+}+2e^-\rightarrow\text{Cu}$$: two electrons are still required per copper atom. Lower efficiency changes how much of the supplied charge reaches that reaction, not its stoichiometry.
:::
::::
