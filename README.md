# EPC Project Controls

A browser-based project controls tool for EPC (engineering, procurement, construction) projects:
project registration, E/P/C progress updates, discipline and overall status reports, S-curves,
EVM (SPI/CPI), resource planning, crashing / fast-tracking / smoothing suggestions, L0–L5 schedules
with Microsoft Project XML export, 2-week / 1-month / 7-week look-aheads, delay analysis and a
time–chainage line diagram.

Live site: https://akhileshkmr2906-stack.github.io/Project-Management-Tool/

## Data storage
- Data is kept in the browser and, once connected, in one file (`EPC_Project_Controls_data.json`)
  in the signed-in user's Google Drive (scope `drive.file`: the app only sees files it created).
- The Google OAuth client ID is set in `index.html` (`window.EPC_CONFIG.googleClientId`) or by an
  admin on the Export page.
- Project data is not stored in this repository.

## Login
First sign-in: `admin` / `admin123`, then change the password under Users. Login is enforced in the
browser only; it is not server-side security.

## Build
`index.html` is generated: `python3 src/build.py src/starter_project.json index.html`
