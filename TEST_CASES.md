# Co-founder Match Recommender - Manual Test Cases

This manual testing guide is designed to verify the functionality, responsiveness, UI/UX aesthetics, and error handling of the **Co-founder Match Recommender** dashboard. 

---

## 1. Introduction
Manual testing validates that the platform meets both its analytical requirements (accurate semantic profile matching) and its product requirements (premium AI SaaS UI/UX). This QA document details manual tests to ensure high visual quality and functional stability.

---

## 2. Test Environment
* **Backend Runtime**: FastAPI (Uvicorn server)
* **Frontend Runtime**: React + Vite (Local dev server)
* **Tested Browsers**: Google Chrome (Latest), Mozilla Firefox (Latest), Safari (Latest)
* **Operating System**: Windows 11 / Windows 10 / macOS

---

## 3. Manual Test Cases

| Test Case ID | Feature | Preconditions | Test Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|
| **TC-API-01** | Root Endpoint | Backend server running locally | Send a `GET` request to `http://127.0.0.1:8000/` | Returns HTTP 200 with a greeting JSON message | | |
| **TC-API-02** | Fetch Profiles list | Backend server running locally | Send a `GET` request to `http://127.0.0.1:8000/api/profiles` | Returns HTTP 200 with a list of 40 profile JSON objects (containing `id` and `name`) | | |
| **TC-API-03** | Retrieve Matches | Backend server running locally | Send a `GET` request to `http://127.0.0.1:8000/api/matches/1` | Returns HTTP 200 with a list of top 5 matches, each including `id`, `name`, `role`, `skills`, `interests`, `experience`, `availability`, `bio`, and `match_score` sorted descending | | |
| **TC-API-04** | Invalid Founder ID query | Backend server running locally | Send a `GET` request to `http://127.0.0.1:8000/api/matches/9999` | Returns HTTP 404 with a clear `"User not found"` detail message | | |
| **TC-API-05** | API Data Schema Check | Backend server running locally | Request matches and inspect JSON data keys | All profiles are mapped correctly; scores are returned as float values between `0.0` and `1.0` | | |
| **TC-FE-01** | First Load View | Backend and frontend running | Open `http://localhost:5173/` in the browser | Page loads without exceptions, showing the header, neural icon, selector panel, and "Ready to Match" placeholder | | |
| **TC-FE-02** | Dropdown Dynamic Options | Backend and frontend running | Open the dropdown selection menu | Dropdown list populates dynamically with the 40 real founder profiles fetched from the backend API | | |
| **TC-FE-03** | Dropdown Downward Opening | Dropdown is clicked | Click on "-- Select a Founder --" dropdown trigger | Options menu expands downward, keeping the hero section visible, and does not overlap headers | | |
| **TC-FE-04** | Dropdown Option Selection | Profiles loaded in menu | Select "Liam Davis" from the dropdown list | The trigger text updates to display "Liam Davis" and matches list is cleared if any matches were previously shown | | |
| **TC-FE-05** | Match Button State | No profile selected | Check the "Find Matches" button state | Button is greyed out and disabled; cursor displays as not-allowed | | |
| **TC-FE-06** | Query Execution | A profile is selected | Select "Liam Davis" and click the "Find Matches" button | The button highlights on click, triggers the matches request, and displays matches list upon completion | | |
| **TC-FE-07** | Loading Spinner | Click "Find Matches" button | Click "Find Matches" and observe screen before API responds | A clean loading spinner appears in the center of the dashboard; matches are cleared | | |
| **TC-FE-08** | Card Layout Rendering | Matches query completes | Inspect the returned cards layout | Each card displays a circular gradient initials avatar, founder name, role, compatibility score, skills, interests, details, and bio | | |
| **TC-FE-09** | Compatibility Score | Card details rendered | View the match score badge on a card | Score displays as a large percentage (e.g. `89% Compatibility`) inside a blue-purple gradient badge | | |
| **TC-FE-10** | Chip Custom Styling | Card details rendered | Compare Skills chips and Interests chips styles | Skills display with a subtle blue border and blue text; Interests display with a secondary purple border and purple text | | |
| **TC-FE-11** | Biography Line Clamping | Long founder bio loaded | Locate a card with a long biography paragraph | The biography text is clamped to exactly 2 lines, ending with a clean CSS-generated ellipsis (`...`) | | |
| **TC-FE-12** | Bottom Status Bar | Matches loaded successfully | Scroll to the bottom of the card grid | A premium dark status bar displays `✨ Showing top 5 compatible founders for [Active Founder] | 3 of 5 shown • Sorted by compatibility` | | |
| **TC-RESP-01**| Desktop Resolution | Browser width >= 1200px | Load matches and maximize browser window | Card grid displays exactly 3 columns per row; spacing margins are proportional and balanced | | |
| **TC-RESP-02**| Tablet Resolution | Browser width between 680px and 1199px | Resize the browser window to tablet scale | Card grid wraps to exactly 2 columns per row; no content overlaps or overlaps dropdown triggers | | |
| **TC-RESP-03**| Mobile Resolution | Browser width <= 679px | Resize the browser window to mobile scale | Card grid wraps to a single column (1 card per row); "Find Matches" button expands full-width | | |
| **TC-RESP-04**| Overflow Check | Drag viewport to minimum width | Resize viewport down to 320px | No horizontal scrolling occurs; elements scale and text clamps correctly without breaking container borders | | |
| **TC-UX-01**  | Card Hover Feedback | Matches cards rendered | Hover cursor over a founder profile card | Card lifts slightly (`translateY(-2px)`), card border glows brighter, and shadow opacity increases over a smooth 250ms transition | | |
| **TC-UX-02**  | Focus States | Keyboard navigation | Press `Tab` to navigate interactive controls | Selected inputs and buttons show visible glowing outlines to support keyboard accessibility | | |
| **TC-NEG-01** | Offline Connection | Shutdown backend server | Select a founder profile and click the "Find Matches" button | Frontend intercepts network failure, clears loading spinner, and displays a red error warning banner | | |
| **TC-NEG-02** | Bad Variable Configuration | Set VITE_API_BASE_URL to empty | Run local dev server with no `.env` | Frontend automatically falls back to `"http://localhost:8000"` and matches still query successfully | | |

---

## 4. Overall Expected Outcome
A successful test run must confirm that:
1. **0 static exceptions** are thrown in the developer tools console logs.
2. The user experience remains premium (no upward select popups overlapping titles, no broken column wrapping, and high readability contrast).
3. The offline state recovers cleanly when the server is restarted without requiring a browser refresh.