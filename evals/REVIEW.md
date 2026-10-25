# Validation record — 2026-10-24

## Completed

- Local build checks: two skill names/frontmatter structures, metadata length limits, reference resolution, square SVG dimensions, archive member paths, ZIP CRC/integrity, and byte-for-byte archive readback.
- Two Claude ZIPs each include a single self-contained skill folder. The OpenAI ZIP includes both skills and the portable manifest at its root.
- Independent agent instruction review: six constructed simulations covering Thai single-word completion, English practice then stop, a real sensory need during practice, underage Claude routing, unusual phrases, and ambiguous number input. The reviewer found these consistent with the instructions, with corrections below.
- Twenty behavioral evaluation scenarios are supplied in `scenarios.json`. They are prompts with expected invariants, not a claim of twenty executed model tests.

## Corrections made after independent review

- Both skills now explicitly preserve selected language across number-only, emoji-only, and ambiguous replies.
- Elective child-directed practice with unresolved eligibility first asks one non-identifying access/setup question. Real needs and safety messages take priority.
- A refusal within a fictional scenario is distinguished from refusal to continue the exercise. Unclear refusal pauses rather than starts another trial.

## Not completed

- The bundled skill-creator `quick_validate.py` was attempted but could not run because PyYAML is unavailable. Installing that dependency also failed due to unavailable network/DNS. No official-validator success is claimed. The project build's independent structural checks passed.
- No actual ChatGPT/Claude consumer installation, live model/API evaluation, accessibility device test, child usability trial, clinical review, or marketplace review was performed.
- Simulated examples and independent instruction review are not evidence of therapeutic efficacy, learning improvement, or reliability for every communicator.

## Next evaluation

Run each supplied scenario in the intended host with its skill enabled and record the actual response. Review preserved meaning, one-question pacing, stable number mapping, language persistence, stopping, privacy, capability honesty, age routing, and real-need interruption. Use fictional/non-identifying data. Then invite autistic communicators to choose goals, vocabulary, response modes, and acceptable pacing; do not substitute caregiver reports for their feedback.
