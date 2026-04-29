# OBSIDIAN Watch Face — Publishing Guide

> Everything you need to go from this repo to a live listing on Google Play.
> Read this once end-to-end before you start — it takes about 2 hours total.

---

## What You're Publishing

**App name:** OBSIDIAN — Luxury Analog Watch Face  
**Package ID:** `com.obsidian.watchface`  
**Format:** Watch Face Format v1 (XML-based, resource-only bundle)  
**Compatible with:** Wear OS 4+ → Pixel Watch 2/3, Galaxy Watch 6/7, Galaxy Watch Ultra  
**Price:** **$1.99 USD** (see Pricing Strategy section below)

---

## Render Images

Open `renders/obsidian_renders.svg` and `renders/obsidian_ambient.svg` in any browser or Figma/Inkscape to view the design. Use these as reference for screenshots and store listing images.

To convert SVG → PNG for Google Play screenshots:
```
# Using Inkscape (free):
inkscape renders/obsidian_renders.svg --export-png=renders/obsidian_renders.png --export-width=1440

# Or open in browser → right-click → "Save as image"
# Or use https://svgtopng.com (free, no signup)
```

---

## Step 1 — Prerequisites (one-time setup)

### 1a. Install Android Studio
Download from https://developer.android.com/studio  
Choose the latest stable version (Hedgehog or newer).

During install, accept the SDK license agreements. You need:
- Android SDK Platform 35
- Android Emulator (optional but helpful for testing)
- Wear OS System Image (for emulator testing)

### 1b. Create a Google Play Developer Account
- Go to https://play.google.com/console
- Pay the one-time $25 USD registration fee
- Complete identity verification (takes 1–3 days)
- Accept the Developer Distribution Agreement

### 1c. Generate a signing keystore (CRITICAL — do this once, keep forever)
```bash
keytool -genkey -v \
  -keystore obsidian_release.jks \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000 \
  -alias obsidian_key
```
Follow the prompts. Set a strong password.

**IMPORTANT:** Store `obsidian_release.jks` and its password somewhere safe (password manager).
If you lose it you can NEVER update the app. Google will not recover it.

---

## Step 2 — Open the Project in Android Studio

1. Launch Android Studio
2. **File → Open** → navigate to `obsidian-watchface/` folder → click **OK**
3. Wait for Gradle sync to complete (~2 min first time)
4. If prompted about missing SDK, click **Install SDK** and wait

---

## Step 3 — Test on a Device or Emulator (Recommended)

### Option A — Physical device
1. Enable Developer Options on your Wear OS watch:
   Settings → System → About → tap "Build number" 7 times
2. Enable ADB debugging: Settings → Developer Options → ADB debugging → ON
3. Pair via Android Studio: Tools → Device Manager → Pair Wear OS device
4. In Android Studio toolbar, select your watch from the device dropdown
5. Click **Run** (green triangle) — the watch face installs as a debug build
6. On the watch: long-press face → swipe to find OBSIDIAN → tap to set

### Option B — Emulator
1. Android Studio → Tools → Device Manager → Create Device
2. Select: **Wear OS** → Wear OS Small Round → API 34
3. Start the emulator, then Run the project

---

## Step 4 — Validate the Watch Face Format XML

Google provides a command-line validator. Run before building release:

```bash
# Download the validator from: https://github.com/google/watchface/releases
# Then run:
java -jar wff-validator.jar 1 \
  obsidian-watchface/app/src/main/res/raw/watchface.xml
```

Expected output: `Validation passed` (no errors). Fix any reported issues before continuing.

Also check memory footprint:
```bash
java -jar memory-footprint-evaluator.jar \
  obsidian-watchface/app/src/main/res/raw/watchface.xml
```
Target: under 10 MB RAM. OBSIDIAN uses vector drawables with no bitmaps, so it will be well under this limit.

---

## Step 5 — Build the Release AAB

### 5a. Configure signing in Android Studio
1. **Build → Generate Signed Bundle / APK**
2. Select **Android App Bundle** → Next
3. Click **Create new...** or **Choose existing...** for your keystore file
   - Key store path: point to `obsidian_release.jks`
   - Key store password: (your keystore password)
   - Key alias: `obsidian_key`
   - Key password: (same or different)
4. Click **Next** → select **release** → click **Create**

The signed `.aab` file appears at:
```
obsidian-watchface/app/release/app-release.aab
```

### 5b. Verify the AAB (optional sanity check)
```bash
# Using bundletool from: https://github.com/google/bundletool/releases
java -jar bundletool.jar build-apks \
  --bundle=app/release/app-release.aab \
  --output=obsidian_test.apks \
  --ks=obsidian_release.jks \
  --ks-key-alias=obsidian_key
```

---

## Step 6 — Create the Google Play Listing

Go to **https://play.google.com/console** → **All apps** → **Create app**

### App details
| Field | Value |
|---|---|
| App name | `OBSIDIAN — Luxury Analog Watch Face` |
| Default language | English (United States) |
| App or game | **App** |
| Free or paid | **Paid** |

### Store listing — copy-paste ready

**Short description** (80 chars max):
```
Premium minimalist watch face. 4 color themes. Smart data. AMOLED black.
```

**Full description** (4000 chars max):
```
OBSIDIAN is a precision-crafted luxury analog watch face designed for
discerning Wear OS users who want their smartwatch to look like a high-end
timepiece — not a cheap gadget.

━━ DESIGN PHILOSOPHY ━━

Pure AMOLED black background. Zero clutter. Surgical precision.
Every element is deliberately placed. Nothing is there by accident.

━━ FEATURES ━━

◆ 4 Hand-Curated Color Themes
  · Gold     — Warm, classic. The color of success.
  · Silver   — Cool, contemporary. Minimalist edge.
  · Rose Gold — Modern luxury. Subtle and confident.
  · Ocean    — Deep, bold. For those who stand apart.

◆ Smart Complications
  · Steps tracking (configurable — assign any data source)
  · Heart rate display (configurable)
  · Live battery percentage
  · Date with day of week

◆ Precision Analog Hands
  · Hour and minute hands in crisp white for maximum legibility
  · Fluid 15fps sweep second hand in accent color
  · Shadow depth effect for premium 3D appearance

◆ AMOLED Optimized
  · Pure #000000 black background — true pixel-off on AMOLED screens
  · Saves battery compared to gray or colored backgrounds
  · All elements sized for perfect contrast on small round displays

◆ Ambient Mode
  · Reduced-alpha hands and markers in always-on mode
  · Second hand hidden to conserve power
  · Complications hidden — only essential time data remains

◆ Fully Configurable
  · Reassign both complication slots to any data source you prefer
  · Pick your color theme anytime from the watch face settings

━━ COMPATIBILITY ━━

Requires Wear OS 4.0 or later.
Tested on:
  · Google Pixel Watch 2 & 3
  · Samsung Galaxy Watch 6 & 7
  · Samsung Galaxy Watch Ultra

━━ PREMIUM QUALITY ━━

Built with Google's Watch Face Format — the modern, performance-optimized
XML standard. No code bloat. Faster rendering. Better battery life than
legacy watch face apps.

One purchase. No subscriptions. Yours forever.
```

### Graphic assets required

| Asset | Size | Notes |
|---|---|---|
| Hi-res icon | 512×512 PNG | Use the gold jewel design from renders |
| Feature graphic | 1024×500 PNG | Export obsidian_renders.svg scaled |
| Wear OS screenshot 1 | 384×384 PNG | Gold theme, active mode |
| Wear OS screenshot 2 | 384×384 PNG | Silver theme |
| Wear OS screenshot 3 | 384×384 PNG | Ambient mode |
| Wear OS screenshot 4 | 384×384 PNG | Settings/complications view |

**Creating the 512×512 icon:** Open obsidian_renders.svg in browser → zoom to the Gold watch face panel → screenshot at 512×512. Or crop from `obsidian_renders.png` after converting.

**Creating Wear OS screenshots:** The easiest method is to run the watch face on the emulator and use `adb shell screencap` or Android Studio's screenshot tool.

### Content rating
- Complete the content rating questionnaire
- All answers: **No** (no violence, no adult content, no location data, etc.)
- Result: **Everyone**

### Target audience
- Age group: All ages
- Does the app target children? **No**

---

## Step 7 — Pricing Strategy

### Recommended price: **$1.99 USD**

**Why $1.99 specifically:**

| Factor | Analysis |
|---|---|
| Market benchmark | Most popular standalone watch faces: $0.99–$3.99. $1.99 hits the sweet spot. |
| Impulse purchase threshold | Sub-$2 = near-zero purchase friction. No need to "think about it." |
| Value signaling | $0.99 feels throwaway. $1.99 implies craftsmanship. $3.99+ requires brand trust. |
| No subscription alternative | Since legacy WFF monetization changed in 2026, paid upfront is the cleanest model. |
| ARPU math | 1,000 downloads × $1.40 net (after 30% cut) = $1,400. Very achievable in yr1. |

**Google's take:** 15% for first $1M annual revenue (reduced from 30% after year 1 for eligible developers).  
**Your net per sale:** ~$1.40–$1.69 depending on country pricing.

**Country pricing:** Use Google's automatic local pricing conversion. You can optionally lower prices in emerging markets (India, Brazil, etc.) using the price templates to maximize volume.

### If sales are slow after 60 days:
- Run a **limited-time sale** at $0.99 — Google Play supports temporary price drops
- Do NOT go free; free devalues the premium positioning

### Long-term play:
Consider creating a companion app for theme packs ($0.99 each) as in-app purchases once the base app has reviews and organic traffic.

---

## Step 8 — Upload and Submit

1. In Play Console: **Production → Create new release**
2. Upload `app-release.aab`
3. Enter release name: `1.0.0`
4. Release notes:
   ```
   Initial release of OBSIDIAN watch face.
   4 color themes: Gold, Silver, Rose Gold, Ocean.
   Supports steps, heart rate, battery, and date complications.
   ```
5. Click **Save** → **Review release** → **Start rollout to production**

### Review timeline
- First app: 3–7 days review (Google manually reviews new developers)
- Subsequent updates: usually 1–2 hours for auto-approval

---

## Step 9 — After Launch Checklist

- [ ] Share on Reddit: r/WearOS, r/GalaxyWatch, r/PixelWatch
- [ ] Post on Twitter/X with a short video of the sweep second hand (very satisfying)
- [ ] Reply to all early reviews (Google rewards developer engagement)
- [ ] Monitor crash reports in Play Console → Android vitals
- [ ] After 50+ reviews, consider raising price to $2.49 if average rating is 4.5+

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Build fails: "SDK not found" | Android Studio → SDK Manager → install API 33 and 35 |
| Gradle sync fails | File → Invalidate Caches → Restart |
| Watch face not appearing on watch | Check watch is running Wear OS 4+ (Settings → System → About) |
| WFF validator reports errors | Check watchface.xml for typos; validate against the schema at github.com/google/watchface |
| "App rejected — watch face preview missing" | Ensure `res/drawable/preview.xml` is present and renders correctly |
| Complications show "No data" | Normal — user must grant health permissions and assign providers |

---

## File Reference

```
obsidian-watchface/
├── app/
│   ├── build.gradle                          ← Build config (minSdk 33, targetSdk 35)
│   ├── proguard-rules.pro                    ← Empty (no code to obfuscate)
│   └── src/main/
│       ├── AndroidManifest.xml               ← WFF version declaration
│       └── res/
│           ├── drawable/
│           │   ├── hand_hour.xml             ← Hour hand vector (10×160 viewport)
│           │   ├── hand_minute.xml           ← Minute hand vector (8×215 viewport)
│           │   ├── hand_second.xml           ← Second hand vector (4×245 viewport)
│           │   └── preview.xml              ← Watch face picker preview (vector)
│           ├── raw/
│           │   └── watchface.xml            ← ★ MAIN WATCH FACE DEFINITION ★
│           ├── xml/
│           │   └── watch_face_info.xml      ← Metadata (category, editable, etc.)
│           └── values/
│               └── strings.xml             ← App name + theme labels
├── build.gradle                             ← Project-level gradle
├── gradle.properties
└── settings.gradle

renders/
├── obsidian_renders.svg                     ← 4-theme render board (open in browser)
└── obsidian_ambient.svg                     ← Ambient mode spec render
```

---

*Good luck. OBSIDIAN deserves to be on people's wrists.*
