# DAAA – Alger FIR Squawk Generator

## 1. Purpose
This software automatically assigns a SSR (squawk) code to an aircraft operating in the Alger FIR.  

It helps ATC radar operation where the controller assigns a code ( IVAO AND VATSIM ONLY) :

**Example:** `DAH2701 squawk 4234`  

The program ensures:  
- Each code is unique  
- Codes fall within official ranges  
- No duplicates are assigned  

---

## 2. Interface

### Radar Panel (Left)
- Displays distance circles  
- Radar sweep  
- Radar center: ALGER RADAR  

Currently, the radar display is visual only.  

### Input Panel
- **CALLSIGN:** Flight identifier.  
  Examples: `DAH2701`, `AFR1234`, `TAR451`, `DLH6AB`  
- **AIRCRAFT:** Type of aircraft.  
  Examples: `B738`, `A320`, `A21N`, `B77W`, `C172`  
- **AIRPORT / SECTOR:** Control area.  
  Examples: `DAAG`, `DAAS`, `DAAE`, `SECTOR ALGER`, `SECTOR EAST`, `SECTOR WEST`, `SECTOR SAHARA`  
- **TYPE (Mission):** Depends on selected airport/sector.  
  - Airports: `DEP`, `ARR`, `APP`, `VFR`  
  - FIR Sectors: `OVERFLIGHT`, `TRANSIT`, `LOCAL`, `LOCAL FLIGHT`  

### Activate Flight
- Automatically assigns an available squawk code  
- Code appears in large format below the form and in the flight list on the right  

---

## 3. Flight Table

| Column | Description |
|--------|-------------|
| CS     | Callsign |
| AC     | Aircraft |
| SQK    | Squawk |
| AP     | Airport / Sector |
| TYPE   | Mission |
| TIME   | Assignment time |

---

## 4. Squawk Allocation
Follows Algiers ACC series:

- **Series 42 (4201–4277):**  
  Used for international flights, departures from FIR, or flights not from neighboring FIRs  
- **Series 44 (4401–4437):**  
  Used for some international flights and ACC coordination  
- **Reserve Series (4440–4477):**  
  Reserved for ATC allocation  

**VFR Flights:**  
- Series: 1601–1677, 2601–2677, 3201–3277  

**Local Flights:**  
- Series: 0000, 0060–0067  
- Used for training, local traffic, or short flights  

---

## 5. Assignment Logic
When a flight is activated:  
1. Program checks the mission type  
2. Selects the corresponding squawk range  
3. Checks which codes are already in use  
4. Assigns a free code randomly  

---

## 6. Example

**Input:**  

CALLSIGN: DAH2701
AIRCRAFT: B738
AIRPORT: DAAG
TYPE: DEP


**Output:**  
SQUAWK: 4235


The flight appears in the flight list.  

---

## 7. FAQ

**Can a squawk be assigned twice?**  
- No. The program checks existing codes.  

**Why do some codes never appear?**  
- They are outside the selected range  
- They are already in use  

**Why 7500 / 7600 / 7700 are not assigned?**  
- These are international emergency codes defined by ICAO:

| Code | Meaning        |
|------|----------------|
| 7500 | Hijacking      |
| 7600 | Radio failure  |
| 7700 | Emergency      |

**Can the same callsign be used twice?**  
- Yes, but not recommended. Real ATC assigns unique callsigns to each active flight.  

**Why does the radar not show aircraft?**  
- Radar is graphical only. It simulates the radar screen but does not track positions.  

**Is the software realistic?**  
- Yes, for squawk assignment, ATC logic, radar interface  
- Does not simulate aircraft position, altitude, speed, or trajectories  

---

## 8. Usage Tips
- **DEP:** Flights departing an Algerian airport  
- **ARR:** Flights arriving at an airport  
- **OVERFLIGHT:** Flights crossing the FIR  
- **TRANSIT:** Flights between sectors  
- **VFR:** General aviation  

---

## 9. Troubleshooting
- **Empty Airport List:** Restart the program  
- **No Squawk Generated:** Check that airport and mission are selected  
- **Interface Frozen:** Close and reopen the program
