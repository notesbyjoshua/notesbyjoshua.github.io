---
title: "Invariants, Coloring, and Games"
status: developing
progress: 68
sidebar:
  order: 6
description: "Competition math notes on parity, invariants, monovariants, board colorings, and game strategies with worked impossibility and winning arguments."
---

## Invariants and Impossibility

An **invariant** is a quantity that stays unchanged after every legal move. To prove a target is unreachable, find an invariant whose starting and target values differ. Parity, remainders, sums, and products are useful first candidates.

The invariant must be preserved by every allowed move, not just by the moves you happen to try.

<div class="theorem-box">

**Example.** A row contains seven coins, all showing heads. A move flips exactly two coins. Can all seven coins be changed to tails?

The parity of the number of tails is invariant. Flipping two heads adds two tails, flipping two tails removes two, and flipping one of each leaves the count unchanged. Initially the number of tails is zero, which is even; the target has seven tails, which is odd. The target is impossible.

</div>

An invariant can rule out a configuration without telling us which configurations are reachable. Matching the invariant is necessary, but it need not be sufficient.

---

## Coloring Boards

A coloring turns a geometric move into an algebraic constraint. On a checkerboard, each domino covers one black and one white square. Any domino-tileable region must therefore have equal numbers of black and white squares.

<div class="theorem-box">

**Example.** Two opposite corner squares are removed from an $$8\times8$$ chessboard. Can the remaining board be tiled by $$1\times2$$ dominoes?

Opposite corners have the same color. The original board has $$32$$ squares of each color; removing the corners leaves $$30$$ of one color and $$32$$ of the other. Each domino covers one of each, so no tiling exists.

</div>

When ordinary black-and-white coloring gives no obstruction, try coloring by the remainder of a row or column index. A three-color pattern can help with length-three tiles, for example. The useful coloring depends on what every legal piece must cover.

---

## Monovariants and Termination

A **monovariant** always moves in one direction. A strictly decreasing nonnegative integer cannot decrease forever, so it proves that a process terminates. A decreasing positive real number need not do this: $$1,1/2,1/4,\ldots$$ continues indefinitely.

<div class="theorem-box">

**Example.** A finite row of zeros and ones is repeatedly changed by replacing an adjacent $$10$$ with $$01$$. Prove the process stops and describe the final row.

Count **inversions**, pairs of positions $$i<j$$ containing a one followed by a zero. An adjacent swap $$10\to01$$ removes exactly their mutual inversion; all other pairs retain their order. Thus each move decreases the inversion count by one.

The count is a nonnegative integer, so the process terminates. At termination no adjacent $$10$$ remains, which means every zero is before every one. The final row consists of all the zeros followed by all the ones.

</div>

A useful potential often measures disorder: inversions, total distance from a target, or the sum of squares of pile sizes. Check its change under one general move before relying on it.

---

## Winning and Losing Positions

For a finite impartial game with normal play, both players have the same legal moves, and a player with no move loses. Classify positions backward:

- A **losing position** has no move to a losing position; every available move leads to a winning position.
- A **winning position** has at least one move to a losing position.

The terminal position is losing. The finite-game assumption lets this recursion reach every position without unresolved loops.

<div class="theorem-box">

**Example.** A pile contains $$23$$ stones. Each player removes $$1$$, $$2$$, or $$3$$ stones, and the player taking the last stone wins. Find a winning first move.

With zero stones, the player to move loses. Positions with $$1,2,3$$ stones are winning; $$4$$ is losing because every move leaves a winning position. Continuing gives losing positions at multiples of four.

Remove three stones to leave $$20$$. Whenever the opponent removes $$r\in\{1,2,3\}$$ stones, remove $$4-r$$. Each pair of turns removes four stones, so we take the last stone.

</div>

The response rule proves the whole pattern rather than merely guessing it from a small table.

---

## Pairing Strategies

A pairing strategy answers each opponent move with its partner. The pairs must be disjoint, and the response must remain legal.

<div class="theorem-box">

**Example.** Players alternately choose an unused square of a $$2\times n$$ board, with no additional restrictions. A player unable to move loses. Give a winning strategy for the second player.

Pair the two squares in each column. Whenever the first player chooses a square, the second chooses its partner in the same column. At the start of each round, every column is either untouched or completely used, so the response is always available. After $$n$$ rounds the board is exhausted, and the first player has no move. Thus the second player wins.

</div>

A pairing must preserve legality and control the actual winning condition. Merely finding pairs with a convenient sum is insufficient if the game's score depends on each player's own accumulated total.

---

## Strategy Stealing

A **strategy-stealing argument** proves that a player has a winning strategy by assuming the opponent has one and showing how to borrow it after a harmless extra move. It may prove existence without giving a practical rule.

<div class="theorem-box">

**Example.** In Chomp on a rectangular board with at least two rows and two columns, the lower-left square is poisoned. Choosing a square removes it and all squares above and to its right; eating the poison loses. Prove the first player has a winning strategy.

Assume instead that the second player can always win. The first player removes only the upper-right square. The assumed strategy supplies a winning response at some square $$s$$ other than the poison. Choosing $$s$$ also removes the upper-right square, so the position after those two moves could have been obtained by choosing $$s$$ on the very first move.

The first player could therefore play $$s$$ immediately and leave the opponent that same losing position, contradicting the assumed second-player win. Since the finite game has no draws, the first player has a winning strategy.

</div>

:::strategy
For transformations, test parity and small moduli before searching for a complicated invariant. For termination, look for an integer measure of disorder. For games, compute small positions, state the proposed losing positions, and prove both that moves leave them and that other positions can reach them.
:::

## Modular and Weighted Invariants

Parity is arithmetic modulo two. If parity does not distinguish the starting and target positions, try another modulus or a weighted sum. Assigning different weights to positions can make a move's total change cancel even when the unweighted count changes.

The right invariant depends on the move, so analyze a general move first. For a board operation, write its contribution to the proposed sum. For a replacement rule on numbers, calculate the new sum or product in terms of the old entries. An attractive expression that survives a few examples is only a conjecture until the general calculation is checked.

<div class="theorem-box">

**Example.** An $$8\times8$$ board has its lower-left corner removed. Can the remaining squares be tiled by straight $$1\times3$$ pieces placed horizontally or vertically?

Label a square with coordinates $$(i,j)$$, where $$0\le i,j\le7$$, by the residue of $$i+j$$ modulo three. Every allowed piece covers exactly one square of each label.

Among the coordinate values, residues zero and one each occur three times, and residue two occurs twice. Counting sums of residue pairs gives twenty-one squares labeled zero, twenty-two labeled one, and twenty-one labeled two. The removed corner has label zero, leaving counts twenty, twenty-two, and twenty-one.

These counts are unequal, so a tiling is impossible. Area alone would not detect the obstruction: sixty-three is divisible by three.

</div>

A weighted coloring can replace literal colors by numbers, including negative weights. The requirement is that each tile or move has a predictable total weight. If every tile has weight zero but the region has nonzero weight, no tiling exists.

---

## From Necessary Conditions to a Reachability Proof

An invariant usually gives only a necessary condition. To prove sufficiency, supply a construction or a reduction algorithm that reaches the target whenever the invariant agrees.

<div class="theorem-box">

**Example.** A rectangular board of lamps starts entirely off. A move toggles the four lamps in any adjacent $$2\times2$$ block. Prove that a target configuration is reachable exactly when every row and every column contains an even number of lit lamps.

Every move toggles two lamps in each affected row and column, preserving all row and column parities. The evenness condition is therefore necessary.

For sufficiency, work backward from a target satisfying the condition. Scan all positions except the last row and last column, from left to right and top to bottom. Whenever the current lamp is on, toggle the block having that lamp as its upper-left corner. This turns it off without changing any previously cleared lamp.

After the scan, only the last row and column could contain lit lamps. Every earlier row already has all other entries off, so even row parity forces its last entry off. Then every column's parity forces the remaining last-row entry off as well. The board is now all off.

Reversing the finite sequence of toggles constructs the target from the initial board. Thus the parity conditions are sufficient.

</div>

The order of the scan is the key construction. A move may disturb lamps to the right and below, but those are precisely the ones not yet settled. This is a common pattern in constructive invariance problems: eliminate one coordinate at a time while preserving completed work.

---

## Energy and Smoothing Processes

Sums of squares are useful monovariants when a move transfers units from a larger quantity to a smaller one. They measure imbalance while the ordinary sum remains fixed.

<div class="theorem-box">

**Example.** Ten identical stones are distributed among three piles. A move transfers one stone from a pile of size $$a$$ to one of size $$b$$ whenever $$a\ge b+2$$. Prove the process stops and identify the final pile sizes.

The total remains ten. Let the energy be the sum of the squares of the pile sizes. A move changes it by

$$
(a-1)^2+(b+1)^2-a^2-b^2=-2(a-b-1)\le-2.
$$

The energy is a nonnegative integer, so only finitely many moves occur. At termination, no two pile sizes differ by two or more. Three nonnegative integers totaling ten with that property must be $$3,3,4$$ in some order.

</div>

This proof does not assert that every sequence of moves visits the same intermediate configurations. It identifies a common terminal multiset because the invariant total and terminal inequality determine it uniquely. If those conditions allowed several terminal multisets, termination alone would not prove uniqueness.

---

## Normal-Play Nim and Binary XOR

In **Nim**, a move removes any positive number of stones from exactly one pile. Under normal play, the player taking the last stone wins. The losing positions are precisely those whose pile sizes have binary XOR zero.

XOR adds each binary digit modulo two, without carrying. Thus $$a\oplus a=0$$ and $$a\oplus0=a$$. If a move changes a pile from $$a$$ to $$b\ne a$$, the total XOR changes from $$S$$ to $$S\oplus a\oplus b$$. From a zero-XOR position, this cannot remain zero.

Conversely, if $$S\ne0$$, choose its highest nonzero binary digit. Some pile $$a$$ has that digit set. Replacing it by $$b=a\oplus S$$ clears that highest differing digit, so $$b<a$$ and the move is legal. The new total XOR is zero.

These two facts prove the strategy: every move from a losing position leaves it, while every other position can move to one.

<div class="theorem-box">

**Example.** Three Nim piles have sizes seven, eleven, and thirteen. Find a winning move.

In binary, the sizes are $$0111,1011,1101$$. Their XOR is $$0001$$. Replace the last pile by $$13\oplus1=12$$, removing one stone. The new XOR is

$$
7\oplus11\oplus12=0.
$$

After every opponent move, use the same highest-bit construction to restore XOR zero. Since the game is finite, this strategy wins.

</div>

Do not replace XOR by ordinary addition or parity of the total. A position can have an even total and still have nonzero XOR. The invariant describes the chosen strategy's target positions; arbitrary legal moves do not preserve it.

---

## Misère Play Changes the Endgame

Under **misère** rules, taking the last stone loses. For Nim, the ordinary XOR strategy works while at least two piles have size greater than one. The special endgame occurs when all piles have size one, or when only one larger pile remains.

If all piles have size one, an odd number is losing: each move removes exactly one pile, so the player facing an odd count takes the final stone. With exactly one larger pile, reduce it so the opponent receives an odd number of unit piles. This may mean removing the large pile entirely or reducing it to one.

<div class="theorem-box">

**Example.** In misère Nim, the piles are one, one, and seven. Find a winning move.

Reduce the seven-stone pile to one. The opponent receives three unit piles, an odd count. Play then has no choices about move size, and the opponent eventually takes the last stone.

Removing the seven-stone pile entirely would leave two unit piles and give the opponent a win. The normal-play instinct to make XOR zero is wrong in this special endgame.

</div>

When at least two large piles exist, a move to zero XOR cannot leave exactly one large pile, since unit piles affect only the lowest bit and cannot cancel a larger pile's higher bits. This explains why the normal strategy remains valid until the controlled transition to the unit-pile endgame.

---

## Combining Independent Games

A game can consist of several components, with each move changing exactly one component. Winning one component in isolation does not automatically tell us how their sum behaves, because players may choose which component to move in.

For a finite impartial normal-play game, assign each position its **Grundy number**: the smallest nonnegative integer absent from the Grundy numbers of its legal followers. This operation is called mex. A terminal position has number zero. For independent components, the combined Grundy number is their XOR.

For a pile where a move removes one or two stones, the Grundy values repeat $$0,1,2$$, so the value of a pile of size $$n$$ is $$n\bmod3$$. Two such piles of sizes four and eight have values one and two, whose XOR is three. Reducing the second pile from eight to seven gives values one and one, hence a losing combined position.

The distinction from unrestricted Nim matters: use the XOR of the components' Grundy values, not automatically the XOR of their raw sizes. The legal move set determines the values.

:::strategy
For transformations, prove one move preserves the proposed invariant. For termination, require a quantity that cannot decrease indefinitely. For games, identify the play convention and prove both directions of a losing-position characterization. A strategy must include a legal response, not merely a desirable pattern.
:::

---

## Key Relations

:::equations
| Method | What must be proved |
| --- | --- |
| Invariant | $$I(\text{after})=I(\text{before})$$ for every legal move |
| Integer monovariant | $$M\ge0$$ and $$M(\text{after})<M(\text{before})$$ |
| Domino coloring | Covered black count equals covered white count |
| Remove $$1,\ldots,k$$ stones | Losing pile sizes are $$0\pmod{k+1}$$ under normal play |
| Pairing | Each response is unused, legal, and preserves the required position |
| Smoothing energy change | $$(a-1)^2+(b+1)^2-a^2-b^2=-2(a-b-1)$$ |
| Nim losing condition | $$a_1\oplus\cdots\oplus a_k=0$$ under normal play |
| Nim move | Change $$a$$ to $$a\oplus S<a$$ using a highest set bit of nonzero total XOR $$S$$ |
| Grundy recursion | $$g(P)=\operatorname{mex}\{g(Q):P\to Q\}$$ for finite impartial normal play |
| Independent game sum | $$g(P+Q)=g(P)\oplus g(Q)$$ |
:::
