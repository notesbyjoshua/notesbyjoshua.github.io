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

<div class="theorem-box">

**Example.** Equal charge passes through silver-ion and copper(II)-ion plating cells. Using molar masses 107.9 and $$63.55\ \mathrm{g/mol}$$, compare deposited masses.

Silver needs one electron per atom and copper needs two. Thus $$m_{Ag}/m_{Cu}=(107.9/1)/(63.55/2)=3.40$$. Equal charge means equal electron amounts, not equal metal moles or equal masses.

</div>

---

:::equations

| Idea | Equation | Conditions |
| --- | --- | --- |
| Total entropy | $$\Delta S_{univ}=\Delta S_{sys}+\Delta S_{surr}$$; $$\Delta S_{surr}=-\Delta H_{sys}/T$$ | Surroundings at fixed T; constant-pressure heat transfer, only pressure-volume work. |
| Standard entropy | $$\Delta S_{rxn}^\circ=\sum_p\nu_pS_p^\circ-\sum_r\nu_rS_r^\circ$$ | Standard molar entropies of elements are not generally zero. |
| Gibbs free energy | $$\Delta G=\Delta H-T\Delta S$$ | Compare states at the same T; negative change favors the written direction at fixed T and P. |
| Formation free energies | $$\Delta G_{rxn}^\circ=\sum_p\nu_p\Delta G_{f,p}^\circ-\sum_r\nu_r\Delta G_{f,r}^\circ$$ | Match stoichiometric coefficients and physical states. |
| Composition and equilibrium | $$\Delta G=\Delta G^\circ+RT\ln Q$$; $$\Delta G^\circ=-RT\ln K$$ | Use dimensionless activity ratios. |
| Cell energy | $$\Delta G=-nFE$$; $$E^\circ=E^\circ_{cathode}-E^\circ_{anode}$$ | n is electrons transferred per balanced reaction; tabulated potentials are reductions. |
| Nernst | $$E=E^\circ-\frac{RT}{nF}\ln Q$$ | Ideal dilute concentrations may approximate activities; omit pure solids. |
| Nernst at 25 degrees C | $$E=E^\circ-\frac{0.0592\ \mathrm{V}}n\log Q$$; $$\log K=nE^\circ/(0.0592\ \mathrm{V})$$ | Base-ten logarithms, potential in volts. |
| Charge | $$q=It=n_{e^-}F$$ | $$n_{e^-}$$ is moles of electrons, distinct from the reaction coefficient n. |
| Electrodeposition | $$m=\frac{M_{molar}\eta It}{zF}$$ | z electrons per deposited atom; $$\eta$$ is the useful-current fraction. |
| Electrical energy | $$E_{supplied}=qV_{applied}$$ | Constant applied voltage; actual energy can exceed desired reversible chemical work. |

:::

## Practice

### MCQ

::::problem
1. A two-electron cell has $$E^\circ=0.200\ V$$ at $$25^\circ\mathrm{C}$$. At what reaction quotient does its forward voltage become zero? Use the base-ten Nernst coefficient 0.0592 V.

   (A) $$2.4\times10^3$$<br>
   (B) $$5.7\times10^6$$<br>
   (C) $$1.7\times10^{-7}$$<br>
   (D) $$10^2$$

:::solution
At zero voltage, $$\log Q=nE^\circ/0.0592=0.400/0.0592=6.757$$. Thus $$Q=K\approx5.7\times10^6$$. Electron stoichiometry belongs in the numerator when solving for the logarithm, and zero voltage corresponds to equilibrium rather than necessarily equal concentrations.

$$
\boxed{\text{B}}.
$$
:::
::::

::::problem
2. For $$\mathrm{Zn+Cu^{2+}\rightarrow Zn^{2+}+Cu}$$, an operating cell has both solutions diluted tenfold without changing temperature or electrode materials. In the ideal dilute-solution model, how does its voltage change immediately?

   (A) Increases by 0.0592 V<br>
   (B) Decreases by 0.0296 V<br>
   (C) Becomes zero<br>
   (D) Stays unchanged because Q stays unchanged

:::solution
The quotient is $$[\mathrm{Zn^{2+}}]/[\mathrm{Cu^{2+}}]$$, so equal dilution factors cancel. The Nernst correction is unchanged. Dilution can change resistance and current under load, but the equilibrium cell potential in the stated ideal model depends on Q, not the two concentrations independently.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
3. The same total charge passes through silver(I) and copper(II) plating cells. Silver plates with 100% current efficiency and copper with 80.0%. Use molar masses 108 and 64.0. What is $$m_{Ag}/m_{Cu}$$?

   (A) $$4.22$$<br>
   (B) $$3.38$$<br>
   (C) $$2.70$$<br>
   (D) $$1.69$$

:::solution
Per mole of supplied electrons, silver deposits 108 g, whereas copper deposits $$0.800(64.0/2)=25.6\ \mathrm{g}$$. Their mass ratio is $$108/25.6=4.22$$. Equal charge is not equal deposited metal amount, and the inefficiency further lowers copper's mass.

$$
\boxed{\text{A}}.
$$
:::
::::

::::problem
4. A process at $$300\ K$$ has $$\Delta H=-9.00\ \mathrm{kJ}$$ and $$\Delta S_{sys}=-20.0\ \mathrm{J/K}$$. For constant-pressure heat transfer to surroundings at 300 K, which pair is correct?

   (A) $$\Delta S_{univ}=-50.0\ \mathrm{J/K}$$ and $$\Delta G=+15.0\ \mathrm{kJ}$$<br>
   (B) $$\Delta S_{univ}=+30.0\ \mathrm{J/K}$$ and $$\Delta G=-9.00\ \mathrm{kJ}$$<br>
   (C) $$\Delta S_{univ}=+10.0\ \mathrm{J/K}$$ and $$\Delta G=-3.00\ \mathrm{kJ}$$<br>
   (D) $$\Delta S_{univ}=-10.0\ \mathrm{J/K}$$ and $$\Delta G=+3.00\ \mathrm{kJ}$$

:::solution
The surroundings gain $$9000/300=30.0\ \mathrm{J/K}$$, making the universe change $$30.0-20.0=10.0\ \mathrm{J/K}$$. Independently, $$\Delta G=-9.00-300(-0.0200)=-3.00\ \mathrm{kJ}$$. The system's entropy can decrease while the total entropy increases.

$$
\boxed{\text{C}}.
$$
:::
::::

::::problem
5. Reduction potentials are $$E^\circ(\mathrm{M^{3+}/M^{2+}})=0.600\ V$$ and $$E^\circ(\mathrm{M^{2+}/M})=-0.300\ V$$. What is $$E^\circ$$ for $$\mathrm{M^{3+}+3e^-\rightarrow M}$$?

   (A) $$0.300\ V$$<br>
   (B) $$0.150\ V$$<br>
   (C) $$-0.300\ V$$<br>
   (D) $$0.000\ V$$

:::solution
Add free energies, not voltages. The one-electron step has $$\Delta G_1^\circ=-0.600F$$; the two-electron step has $$\Delta G_2^\circ=-2F(-0.300)=+0.600F$$. Their sum is zero, so $$E^\circ=-\Delta G^\circ/(3F)=0$$. An unweighted average would ignore the different electron amounts.

$$
\boxed{\text{D}}.
$$
:::
::::

::::problem
6. A reaction has $$\Delta H^\circ=+30.0\ \mathrm{kJ/mol}$$ and $$\Delta S^\circ=+50.0\ \mathrm{J/(mol\,K)}$$. At $$500\ K$$, what condition on Q makes the actual forward reaction favorable? Use $$R=8.314\ \mathrm{J/(mol\,K)}$$.

   (A) $$Q>3.33$$<br>
   (B) $$Q<0.300$$<br>
   (C) Every Q because entropy increases<br>
   (D) No Q because standard free energy is positive

:::solution
At 500 K, $$\Delta G^\circ=30.0-500(0.0500)=+5.00\ \mathrm{kJ/mol}$$. Favorability requires $$5000+RT\ln Q<0$$, or $$Q<e^{-5000/(8.314\times500)}=0.300$$. Positive standard free energy does not rule out a favorable nonstandard mixture.

$$
\boxed{\text{B}}.
$$
:::
::::

### FRQ

::::frq{id=chem-thermoelectro-challenge-1}
7. A galvanic cell follows $$\mathrm{Zn(s)+Cu^{2+}(aq)\rightarrow Zn^{2+}(aq)+Cu(s)}$$ with $$E^\circ=1.10\ V$$ at $$25^\circ\mathrm{C}$$. Initially each compartment has 1.00 L solution: $$[Zn^{2+}]=0.100\ M$$ and $$[Cu^{2+}]=0.500\ M$$. Use $$F=96485\ \mathrm{C/mol\ e^-}$$, a base-ten Nernst coefficient of 0.0592 V, and copper molar mass $$63.55\ \mathrm{g/mol}$$. Ignore volume change and competing reactions.

   $$(A)$$ Write both half-reactions, identify anode and cathode, and calculate the initial cell potential.

   $$(B)$$ After 0.100 mol copper has deposited, calculate both ion concentrations and the new cell potential.

   $$(C)$$ Find the charge passed and copper mass deposited during part B. Explain whether doubling electrode mass alone doubles voltage.

   $$(D)$$ Calculate the equilibrium constant and predict which salt-bridge ions move toward the zinc compartment during discharge.

:::solution
$$(A)$$ Zinc oxidation is $$\mathrm{Zn\rightarrow Zn^{2+}+2e^-}$$ at the anode. Copper reduction is $$\mathrm{Cu^{2+}+2e^-\rightarrow Cu}$$ at the cathode. Initially $$Q=0.100/0.500=0.200$$, so $$E=1.10-(0.0592/2)\log0.200=1.121\ V$$. The solids are excluded from Q, and electrons flow externally from zinc to copper.

$$(B)$$ Each mole of deposited copper consumes one mole copper ions and produces one mole zinc ions. The 1.00 L compartments therefore become 0.400 M copper(II) and 0.200 M zinc(II). Now $$Q=0.200/0.400=0.500$$ and $$E=1.10-(0.0592/2)\log0.500=1.109\ V$$. Discharge raises Q and lowers the forward voltage.

$$(C)$$ Depositing 0.100 mol Cu requires 0.200 mol electrons, giving $$q=0.200F=1.93\times10^4\ C$$. Copper mass is $$0.100(63.55)=6.36\ \mathrm{g}$$. Adding more of a pure solid electrode does not change its activity or Q, so voltage does not double. More electrode material can increase available reaction capacity without increasing energy per unit charge.

$$(D)$$ At equilibrium, $$0=E^\circ-(0.0592/2)\log K$$, giving $$\log K=2(1.10)/0.0592=37.16$$ and $$K\approx1.45\times10^{37}$$. Zinc oxidation adds positive ions to its compartment, so salt-bridge anions migrate toward it to maintain charge balance. Electrons travel through the wire, not through the salt bridge.
:::
::::

::::frq{id=chem-thermoelectro-challenge-2}
8. A copper-plating cell runs at 2.50 A. Only 75.0% of the charge reduces copper(II) to copper; all remaining cathodic charge produces hydrogen gas from acid. The target copper deposit is 3.00 g. Use $$M_{Cu}=63.55\ \mathrm{g/mol}$$, $$F=96485\ \mathrm{C/mol\ e^-}$$, and $$R=0.0821\ \mathrm{L\,atm/(mol\,K)}$$.

   $$(A)$$ Calculate the useful deposition charge, total charge, and operating time.

   $$(B)$$ Calculate the moles and dry volume of hydrogen produced at 298 K and 1.00 atm.

   $$(C)$$ If current is doubled but copper efficiency falls to 60.0%, calculate the new time for the same copper mass and compare it with the original time.

   $$(D)$$ An ideal reversible cell driving the desired reaction would require 0.300 V under its operating conditions. If the external source actually supplies 1.20 V throughout the original run, compare desired-reaction electrical work with total supplied energy.

:::solution
$$(A)$$ Copper moles are $$3.00/63.55=0.04721$$. The useful charge is $$q_{Cu}=2F(0.04721)=9.11\times10^3\ C$$. Because this is only 75.0% of supplied charge, $$q_{total}=q_{Cu}/0.750=1.21\times10^4\ C$$. Time is $$q_{total}/I=4.86\times10^3\ s$$, or 81.0 min. Efficiency reduces useful charge, not the two-electron requirement per copper atom.

$$(B)$$ Hydrogen receives $$0.250q_{total}=3.04\times10^3\ C$$. The half-reaction $$\mathrm{2H^++2e^-\rightarrow H_2}$$ requires two electrons per molecule, so $$n_{H_2}=q_{H_2}/(2F)=0.0157\ \mathrm{mol}$$. Its dry ideal-gas volume is $$nRT/P=0.0157(0.0821)(298)=0.385\ L$$. No water-vapor correction is needed because the requested gas is dry.

$$(C)$$ The useful charge remains fixed by the target mass. The original useful current is $$2.50(0.750)=1.875\ A$$, while the new useful current is $$5.00(0.600)=3.00\ A$$. Thus $$t_{new}/t_{old}=1.875/3.00=0.625$$ and $$t_{new}=3.04\times10^3\ s$$, about 50.6 min. Doubling total current does not halve time when efficiency also changes.

$$(D)$$ The reversible work for the copper amount is $$w_{desired}=q_{Cu}(0.300)=2.73\ \mathrm{kJ}$$. Actual source energy is $$q_{total}(1.20)=14.6\ \mathrm{kJ}$$. Their ratio is $$0.750(0.300/1.20)=0.1875$$, about 18.8%. Both competing reactions and operating above the reversible voltage reduce the fraction of supplied energy associated with the desired reversible chemical change.
:::
::::
