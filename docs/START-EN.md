# Start using Easy Communication

This prototype offers two skills: real-message support and optional communication practice. Thai, English, and opt-in bilingual output are supported. It has not been trialled with children or clinically validated.

## Choose the eligible route

ChatGPT under 13: an adult conducts the interaction. Ages 13–17: parental consent is required. Claude consumer services: 18+ only; adults may prepare materials to use offline with younger learners. Do not hand an adult account to a child. Adults 18+ may use either service subject to its rules and feature availability.

Learner-led practice means choosing responses, topics, pacing, and stopping; it does not promise unsupported or unsupervised use for every learner.

## Claude installation for adults

1. Run `python3 scripts/build_release.py`, or use the supplied files in `dist/`.
2. Enable Code execution and file creation as required by Claude.
3. Open Customize → Skills → + Create skill → Upload a skill.
4. Upload the two `claude-…-0.1.0.zip` files separately and enable them.
5. Start a fresh chat: “Help me communicate in English” or “I choose to practice asking for help.” Check the current official guide if menu labels differ.

## ChatGPT installation or preview

`openai-easy-communication-0.1.0.zip` is a skills-only plugin package for supported installation/submission routes. Attaching a ZIP to a normal chat does not install a persistent skill. Public directory submission needs a verified developer identity and review.

For an immediate text-only preview on an account without plugin installation, open the desired SKILL.md, copy the body below its YAML frontmatter into a new conversation as instructions, and add your starter request. This is a one-chat prompt preview, not a verified skill installation. Review output before use. Reference examples are optional; essential behavior is in each SKILL.md.

## Adult setup example

“ChatGPT; learner age 13–17; parental consent obtained; English; two choices at a time; learner chooses the responses; goal: asking for a break.” Do not include birth date, legal name, school, diagnosis records, pictures, or recordings. If setup is absent, the skill uses short text and does not assume independent child use is permitted.

Switch languages with `ไทย`, `English`, or `both`. Enter a number, word, emoji, or your own message. `pause`, `stop`, `done`, `edit`, `repeat`, `skip`, and `easier` control the session. Choices are numbered text lines, not clickable buttons. Speech and image features depend on the host application; the skill does not add a visual AAC board, microphone, or automatic read-aloud.

## Offline practice

An adult can prepare one card at a time: “Let's pretend you want water. What would you say?” Offer “Water”, “I want water”, or the learner's own message. Accept speech, pointing, writing, existing AAC, and refusal. A single word is enough. If they actually need water, address the real need immediately rather than continue the exercise.

Keep established AAC available. Invite the learner's preferences; caregiver reports do not replace them. No forced repetition, withholding of essentials, streaks, or required politeness. A stopped session remains stopped until the learner asks to restart.
