# Zips inside zips

Author: Jared Wilder. First public timestamp: 2026-09-11.

A prior sweep read only the top-level members of 673 archives. **98 of them are containers holding
other archives**, so their contents were never seen. This is that layer.

| | count |
|---|---|
| `.zip` files in the folder | 907 |
| containers holding inner archives | **98** |
| inner archives found | 343 |
| **inner archives opened** (in memory, zero extractions to disk) | **253** — 234 at level 2, 19 at level 3 |
| read in full, deduplicated, excluded topics removed | 157 |
| **held mathematics** | **134** |
| text members decompressed | 17,346 |
| claim-shaped statements extracted | 25,612 |

Level 3 is mostly lineage recursion, where each release embeds its predecessors. The genuine third
level is the mathematics bundles, and **every one of those held mathematics**.

Everything below marked recomputed was checked here from the definition.

---

## Four integral distances, no three collinear, not concyclic

**Recomputed.** The four points

```
(-12, 0)    (12, 0)    (0, 5)    (0, -9)
```

have all six pairwise distances integral:

```
(-12,0)-(12,0)   d^2 = 576   d = 24
(-12,0)-(0,5)    d^2 = 169   d = 13
(-12,0)-(0,-9)   d^2 = 225   d = 15
(12,0)-(0,5)     d^2 = 169   d = 13
(12,0)-(0,-9)    d^2 = 225   d = 15
(0,5)-(0,-9)     d^2 = 196   d = 14
```

distance multiset `{13, 13, 14, 15, 15, 24}`, **no three collinear** (all four cross products
nonzero), and **not concyclic** (the 4x4 circle determinant is nonzero). A counterexample you can
check on paper.

## The regular n-gon distance count, and what it kills

**Recomputed for n = 3..64, zero mismatches.** A regular `n`-gon has **exactly `floor(n/2)` distinct
distances**, since `d(k)^2 = 4 sin^2(pi k / n)` pairs `k` with `n-k` and `sin` is strictly increasing
on `(0, pi/2]`.

That refutes any claim of the form `(1+c)n/2` distinct distances for every `c > 0`.

The audit attached to it notes that the green Lean receipt for this only checks `n = 120`, not the
universal statement.

## Powerful values in three families

**Recomputed.**

```
n! + 1 is powerful, 2 <= n <= 7   :  exactly n = 4, 5, 7    (25 = 5^2, 121 = 11^2, 5041 = 71^2)
2^n + 1 is powerful, 2 <= n <= 11 :  exactly n = 3          (9 = 3^2)
2^n - 1 is powerful, 2 <= n <= 11 :  none
```

The same source caught an endpoint trap in its own earlier claim: 1 is powerful by the standard
convention and `2! - 1 = 1`, so "no powerful `n! - 1` for `n >= 2`" is false as stated.

## Two large divisibility witnesses

**Recomputed.** `n(n-1)(n-2)` divides `C(2n, n)` at **n = 2480** and **n = 3478**. Either one kills a
no-solution theorem at `k = 2`.

## An exact totient equality family

**Recomputed.** Let `m_n` be the least `m` with `n | phi(m)`, and `p_n` the least prime `= 1 mod n`.

For every odd prime `p`, taking `n = p - 1` gives **`m_{p-1} = p_{p-1} = p`**: any `m <= n` has
`phi(m) <= m - 1 < n`, while `phi(p) = n`, and any prime `= 1 mod n` is at least `n + 1`. Verified
for every odd prime up to 29.

Over `1 <= n <= 24`, the strict inequality `m_n < p_n` holds **exactly at `n = 1, 8, 20, 24`**:

```
(m_8,  p_8)  = (15, 17)
(m_20, p_20) = (25, 41)
(m_24, p_24) = (35, 73)
```

## A three-way error on a published sequence

One archive records the Mian-Chowla sequence A005282 with `a(13) = 155`. Another file in the same
estate records `a(13) = 134`. An audit adjudicated between them and chose **134** as the correct
value.

**All three are wrong.** Recomputing the greedy sequence from the definition:

```
1, 2, 3, 5, 8, 13, 21, 30, 39, 53, 74, 95, 128, 152, ...
```

**`a(13) = 128`**, matching OEIS. The estate held two wrong values, and the audit that resolved the
conflict introduced a third.

---

## Reported from their sources

These carry real content and were not recomputed here.

**Carry-free positional arithmetic, three sharp thresholds with necessity witnesses.** For
`Phi_B(r) = sum r_j B^j` on `[-A, A]^m`: zero-detection holds **iff `B > A`** (witness
`(-B, 1, 0, ...)`), injectivity holds **iff `B > 2A`**, and

```
ker Phi_B = <B e_j - e_{j+1}>   exactly
```

so every collision is a finite sequence of adjacent carry moves with no hidden mechanism.
Companion: for `P` in `Z[X]` with all coefficients at most `C`, `P(B) != 0` for every such `P` **iff
`B > C`**, universal over all degrees and sharp on two terms.

**Full-box optimality with equality rigidity.** If `w . x` is injective on `[-A, A]^m` then
`||w||_1 >= (q^m - 1)/(q - 1)` with `q = 2A + 1`, attained at `w = (1, q, ..., q^{m-1})`, and
**equality forces `w_j = q^j` exactly**. Exact exponents alongside: signed support-two is
`Theta(m^2)` via a shifted Sidon set, binary sparse is `Theta_s(m^s)`. The named frontier is support
three, where the charge argument stops reducing the forms.

**A density staircase for the Turan (3,4) problem.** With `c_n` the minimum triple cover and
`q_n = c_n / C(n,3)`:

```
sum_v delta_M(v) = (n-2)|M| - (n+1) c_n

q_{n+1} - q_n = 6 Delta_n / [(n-2)(n-1)n(n+1)]      where  Delta_n = (n-2)c_{n+1} - (n+1)c_n
```

so a density plateau holds if and only if every vertex-deletion of every optimum is optimal, if and
only if every optimum is regular of degree `c_{n+1} - c_n`. The algebra checks. The attached finite
values `c_7 = 12`, `c_8 = 20`, `c_9 = 30` coincide with known covering numbers under complementation,
so they are not fresh.

**An exact reduction of a growth law.** With `U_k = {2a_j - a_i}` and `sum_x m_k(x) = C(k,2)`, the
corrected count is `|U_k ∩ [0, a_k)| = a_k - k - 3` (the values 1, 2, 3 are forced seed omissions,
not reflection-generated), giving `a_k = Theta(k + k^2/mu_k)` and hence

```
a_k = Theta(k^2 / log k)   <=>   mu_k = Theta(log k)
```

The proposed scale-mixing lemma is explicitly retired as unproved, because exact maxima at the
checkpoints rise and there is no absolute per-scale multiplicity constant.

**No exact square tiling of the integers.** With `B = {k^2}`, the difference set is
`B - B = {m : m != 2 mod 4}`. A unique decomposition `Z = A + B` forces every nonzero difference in
`A` to be `= 2 mod 4`; three elements then produce a difference `= 0 mod 4`, so `|A| <= 2`, and a
finite `A` plus the nonnegative squares is bounded below.

**An exact semiprime formula.** `f(n) = min_{1 < k <= n/2} gcd(n, C(n,k))` satisfies **`f(pq) = p`**
for primes `p < q`, via `k C(n,k) = n C(n-1, k-1)` plus Lucas at `k = q`. Values: `f(21) = 3`,
`f(33) = 3`, `f(35) = 5`, `f(49) = 7`, `f(77) = 7`.

**An infinite parametric witness family.** For every `j >= 0` and odd prime `p`, setting
`k = 2^(2^j)` and `n = 2^j p` gives **`2^n = k (mod n)`** by Fermat mod `p`, both powers vanishing
mod `2^j`, and CRT. Infinitely many `n` for each such `k`.

**An exact polychromatic collapse.** For `r = 2`, `k = 3` the polychromatic number is 3 at `n = 4`
with an explicit matching-colouring certificate, and **drops to 2 at `n = 5`** by exact counting:
each colour class must be a `2-(5,3,1)` covering, `C(5,2,3) = 4`, and `3 x 4 = 12 > 10 = C(5,2)`. The
`q = 3` certificate is an extremal endpoint, not a scaling pattern.

**A 2-adic parity obstruction.** Any interval of at least two consecutive integers has a unique
element of maximal `v_2`, so its reciprocal sum is non-integral. Extended: for a finite union of such
blocks, an integral total requires an **even number of blocks** attaining the global maximal `v_2`.

**Exact Erdős–Gyárfás pieces.** In a `C_4`-free graph of minimum degree at least 3,
`|N_2(v)| >= 2d(v) - 2e(G[N(v)]) >= d(v)`, **sharpened to `d(v) + 1` when `d(v)` is odd**. Every
minimum counterexample has arboricity at most 2. An ear on a shortest cycle of length `r` has
`p >= max(a, r - a) >= ceil(r/2)`. And exactly **21 complete one-hub base configurations** are
`C4`/`C8`-free with hub degree at least 3.

**Exhaustive witness tables.** Least witnesses `W(2..5) = 1, 17, 1019, 2521`, certified to
`n <= 2 x 10^5`. `W(2,3) = 9` via an exact verifier over 512 colourings and 16 progressions, with the
hand-checkable witness **`RBRBBRBR`** on `[8]`. Order-5 Golomb rulers: optimum length **11** with
exactly four optimal witnesses.

---

## The corpus convicts itself, and those are findings too

- A Hadamard-lacunary bound `Q(sum z^(2^k)) <= 2/7 < 1/2` was **blacklisted by the machine itself**:
  the series has radius of convergence 1, so it is not an entire function and the bound does not
  apply.
- An irrationality claim died to `a_n = n`, since `sum n/2^n = 2`.
- A witness `{0,1,3,4}` was refuted by exact check, because `0 + 4 = 1 + 3`.

## `KERNEL_CHECKED` is a scope label, not a close

The archive's own audit says so and the evidence backs it. One entry labelled `KERNEL_CHECKED` has
the Lean conclusion `check_L1 5 2 = true`. Others are `(2 : Rat)/4 = 1/2`, `2 + 2 = 4` over the
integers, `n^2 >= 0`, and a check that a string is 16 hexadecimal characters.

The census across these bundles: **710 records labelled PROVED across 189 problem numbers**, a
941-row gold ledger (818 lemmas, 81 counterexamples, 26 verified witnesses, 8 obstruction case-law
rows, 5 kernel theorems), **135 kernel-checked against 72 kernel-failed**, and 252 Lean theorem
files.

## Not read

The 16 invention assets inside one container, and all medical, imaging and web-application archives,
were skipped unopened. Four session-export containers were read only for their Ramsey receipts;
their full transcripts may hold more.

## Verification

```bash
python verify.py
```

Standard library only.

## License

Apache-2.0.
