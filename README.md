# python-projects

## Structure du projet

```plaintext

crypto/

- config.py          # global defaults for every crypto sub-project

- functions/         # shared helper routines

- projects/

--- spot_analysis/
------- config.py      # spot-specific defaults
------- run.py         # SpotAnalysis class

--- volatility/
------- config.py      # volatility-specific defaults
------- run.py
