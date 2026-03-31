---
layout: default
title: Electric Fields and Forces
parent: AP Physics C E&M
permalink: /notes/physics/electrostatics/
---

# Electric Forces and Fields

This is also sometimes called electrostatics

---

## Electric Charge

Electric charge is a fundamental property of matter.

- Protons carry positive charge  
- Electrons carry negative charge  
- Magnitude of charge: $$e = 1.60 \times 10^{-19} \, \text{C}$$ (Take positive charge for proton, negative charge for electron)

---

### Key Ideas

- Charge is **transferred via electrons** (protons are NEVER transferred)
- Positive charge = lack of electrons  
- Negative charge = excess electrons

---

### Quantization of Charge

Max Planck correctly formulated that energy was quantized. Later, experimenters like Robert Millikan (and his infamous oil drop experiment) proved that charge comes in discrete units, with the fundamental unit of charge being the charge of an electron. So, all charged objects have charge:

$$
q = ne, \quad n \in \mathbb{Z}
$$

You can never have a fractional multiple smaller than $e$. Charge always comes in integer amounts in relation to $e$!

---

## Conservation of Charge

Total charge in an isolated system is constant:

- Charge cannot be created or destroyed  
- Only transferred between objects  

This is one of the most important conservation laws in physics, and can be used to derive many of the formulas that come up later.

---

## Electroscopes

Electroscopes detect charge using metal leaves that repel each other. (INSERT PICTURE)

---

### Grounding

Grounding connects an object to the Earth:

- Excess charge flows to/from Earth  
- Object becomes neutral  

The Earth can be treated infinite charge reservoir, and will always replenish/take the necessary amounts of electrons to make the object neutral.

---

### Charging by Conduction

1. Touch charged object to electroscope (originally neutral) 
2. Charge transfers directly  
3. By Conservation of Charge, both objects end with **same sign**

### Charging by Induction (EXPLAIN MORE)

1. Bring charged object nearby  
2. Ground the electroscope  
3. Remove ground, then remove object  
4. The electroscope ends with **opposite charge**

---

## Polarization

A charged object can rearrange charges in a neutral object.

Example:
- Negative balloon near wall  
- Electrons in wall move away  
- Positive side faces balloon  

👉 This causes **attraction without net charge**

---

## Coulomb's Law

Force between two point charges is given by:

$$
\vec{F} = k \frac{q_1 q_2}{r^2} \hat{r}
$$, 

where $$k = 8.99 \times 10^9 \, \text{N} \cdot \text{m}^2 / \text{C}^2$$

A positive force (like charges) indicates repulsion, while a negative force (opposite charges) indicates attraction. The Coulombic force follow very similarly like the Law of Universal Gravitation, and follows the inverse-square law.

---

## Permittivity of Free Space

We have $$k = \frac{1}{4\pi \varepsilon_0}$$, meaning that $$\varepsilon_0 = 8.85 \times 10^{-12}$$. $$\varepsilon_0$$ represents the permittivity of free space, a measure of how easily electric fields form in vacuum.

---

## Superposition Principle

For multiple charges: Forces can add like vectors.

$$
\vec{F}_{\text{net}} = \sum \vec{F}_i
$$

Strategy:
- Draw vectors  
- Break into components if needed

---

## Electric Field

Electric field describes how a charge affects space around it.

$$
\vec{E} = \frac{\vec{F}}{q}
$$ (Units: N/C)

For a point charge:

$$
\vec{E} = \frac{1}{4\pi \varepsilon_0} \frac{Q}{r^2} \hat{r}
$$

This field exists independently of a second charge (called test charge). It's direction is marked by the direction of force on a positive test charge, so if a negative test charge is placed in the field, the force will be pointing the opposite direction of the field.

---

### Continuous Charge Distributions

For a continuous charge distribution, there are 3 types, each applicable to different objects/surfaces:

- Linear charge density:$$\lambda = \frac{q}{L}
- Area charge density: $$\sigma = \frac{q}{A}$$, 
- Volume charge density: $$\rho = \frac{q}{V}$$

For a continuous charge distribution, instead of sums, use integrals to calculate electric fields:

$$
\vec{E} = k \int \frac{dq}{r^2}
$$

A more useful rewrite of this is:

$$
dE = \frac{k dq}{r^2}
$$,

where you take a small $$dr$$ on your object and calculate $$dE$$ based on how much charge is in that $$dr$$ (Usually it will be in the form of $$\lambda dr$$, $$\sigma dA$$, etc.)

---

## Electric Field Lines

Visual representation of fields:

- Start at positive charges  
- End at negative charges  
- Density = field strength  

💡 Field lines never cross

---

## Gauss's Law and Electric Flux

Electric flux measures how much field passes through a surface. If you increase area, you get more flux, and a perpindicular field generates the maximum flux possible at a set area. The equation is given by:

$$
\Phi_E = \vec{E} \cdot \vec{A} = EA \cos \theta
$$

For any surface, it can be modeled by:

$$
\Phi_E = \oint \vec{E} \cdot d\vec{A}
$$

In addition, Gauss's Law states that for any closed surface,

$$\Phi_E = \oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}$$

This equation related electric fields to enclosed charges.

---

### When to Use Gauss’s Law

Works best for cases of high symmetry:

- Spheres  
- Cylinders  
- Infinite planes

For any surface, you can draw a Gaussian surface (Sphere, Cylinder, etc.), which is a surface where the flux is easily calculated from (Usually, you choose one where $E$ is constant). You enclose a section of the surface inside the surface, and use Gauss's Law to solve for the flux/electric field generated from the target surface. 