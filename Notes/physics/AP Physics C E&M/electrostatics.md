---
layout: default
title: Electric Fields and Forces
parent: Physics
permalink: /notes/physics/electrostatics/
---

# Electric Forces and Fields

Test text

---

## Electric Charge

Electric charge is a fundamental property of matter.

- Protons carry positive charge  
- Electrons carry negative charge  
- Magnitude of charge:

$$
e = 1.60 \times 10^{-19} \, \text{C}
$$

### Key Ideas

- Charge is **transferred via electrons**
- Positive charge = lack of electrons  
- Negative charge = excess electrons  

### Quantization of Charge

Charge comes in discrete units:

$$
q = ne, \quad n \in \mathbb{Z}
$$

👉 You can never have a fractional multiple smaller than $e$

---

## Conservation of Charge

Total charge in an isolated system is constant:

- Charge cannot be created or destroyed  
- Only transferred between objects  

👉 This is one of the most important conservation laws in physics

---

## Grounding

Grounding connects an object to the Earth:

- Excess charge flows to/from Earth  
- Object becomes neutral  

👉 The Earth acts as an **infinite charge reservoir**

---

## Electroscopes

Electroscopes detect charge using metal leaves that repel each other.

### Charging by Conduction

- Touch charged object to electroscope  
- Charge transfers directly  
- Both objects end with **same sign**

### Charging by Induction (VERY IMPORTANT)

1. Bring charged object nearby  
2. Ground the electroscope  
3. Remove ground, then remove object  

👉 Result: electroscope has **opposite charge**

💡 Key idea: **no direct contact needed**

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

Force between two point charges:

$$
\vec{F} = k \frac{q_1 q_2}{r^2} \hat{r}
$$

$$
k = 8.99 \times 10^9 \, \text{N} \cdot \text{m}^2 / \text{C}^2
$$

### Key Ideas

- Like charges → repel  
- Opposite charges → attract  
- Force follows **inverse-square law**  

👉 Doubling distance → force becomes $\frac{1}{4}$

---

### Permittivity of Free Space

$$
k = \frac{1}{4\pi \varepsilon_0}
$$

$$
\varepsilon_0 = 8.85 \times 10^{-12}
$$

👉 Measures how easily electric fields form in vacuum

---

## Superposition Principle

For multiple charges:

👉 **Add forces as vectors**

$$
\vec{F}_{\text{net}} = \sum \vec{F}_i
$$

💡 Strategy:
- Draw vectors  
- Break into components if needed  

---

## Electric Field

Electric field describes how a charge affects space around it.

$$
\vec{E} = \frac{\vec{F}}{q}
$$

For a point charge:

$$
\vec{E} = \frac{1}{4\pi \varepsilon_0} \frac{Q}{r^2} \hat{r}
$$

### Key Ideas

- Field exists **independently of test charge**
- Direction = force on a **positive test charge**
- Units: N/C  

---

### Continuous Charge Distributions

Instead of sums, use integrals:

$$
\vec{E} = k \int \frac{dq}{r^2}
$$

👉 Used for:
- rods  
- rings  
- disks  

---

## Electric Field Lines

Visual representation of fields:

- Start at positive charges  
- End at negative charges  
- Density = field strength  

💡 Field lines never cross

---

## Gauss's Law

One of the most powerful tools in electrostatics.

$$
\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}
$$

👉 Relates electric field to enclosed charge

---

### Charge Densities

$$
\lambda = \frac{q}{L}, \quad \sigma = \frac{q}{A}, \quad \rho = \frac{q}{V}
$$

---

### Electric Flux

$$
\Phi_E = \vec{E} \cdot \vec{A} = EA \cos \theta
$$

### Key Ideas

- Measures how much field passes through a surface  
- Larger area → more flux  
- Perpendicular field → maximum flux  

---

### When to Use Gauss’s Law

Works best for **high symmetry**:

- Spheres  
- Cylinders  
- Infinite planes  

👉 Trick: choose Gaussian surface so $E$ is constant

---