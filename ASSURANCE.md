# Assurance boundaries

- Written proof: internal analytic review covered the matrix reduction, uniform
  exponent Taylor remainder, differentiated parameter remainders, endpoint
  localization and family-versus-unrestricted scope. Internal review is not
  external specialist refereeing or a journal decision.
- Exact computation: two scripts each check three selected rational projector
  instances. This is finite exact arithmetic, not formal verification of the
  universally quantified claims.
- Numerical computation: 72 and 25 direct SVD cases, Decimal and mpmath tables,
  and five stationary-point computations support implementation consistency.
  High precision is not interval certification; stationary roots alone do not
  establish global optimality or uniqueness.
- Robustness: both scripts and 12 intended-error negative controls passed a
  bounded isolated repair replay in normal and optimized Python modes. A final
  frozen-archive replay is a distinct gate, not inferred from that run.
- Historical originality: bounded source comparison is documented in SOURCES.md.
  It does not exclude unindexed prior work or establish absolute priority.
- External assurance: unaffiliated rerun, independent reimplementation,
  proof-assistant checking and editorial peer review have not been established.

Availability and scientific correctness are different questions. A DOI or public
repository, once available, does not strengthen the mathematical evidence by itself.
