# Music Practice II

This small python program to practice bass exercises.

You can choose the material and time to focus on each exercise by editing the `bass.json` file. Then simply cd into your folder and run `python make_exercises.py`

It generates scales, chords, triads for you from a random scale (from any of major, melodic minor or harmonic minor) with a random key. You can set certain keys or modes to focus on if you wish.

Next features to be implemented:

# Features

- Log finished exercises to Postgres db
- Implement simple Flask server
- Use jython to show notated triads, scales etc in browser
- Option to allow user save the schedule for practice later in the day
