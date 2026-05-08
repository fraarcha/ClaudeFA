# SPECTER Watch Face — Publishing Guide

**Cybernetic Noir for Wear OS**
Package: `com.specter.watchface` | WFF v1 | API 33+ (Wear OS 4)

---

## Prerequisites

| Tool | Version | Notes |
|------|---------|-------|
| Android Studio | Hedgehog (2023.1.1)+ | Ladybug or Meerkat preferred |
| JDK | 17 | Bundled with Android Studio |
| Wear OS device / emulator | API 33 (Wear OS 4)+ | For testing |
| Google Play Developer account | Any | One-time $25 registration |

---

## 1. Clone / Open Project

```bash
git clone https://github.com/fraarcha/claudefa.git
cd claudefa/specter-watchface
```

Open in Android Studio: **File → Open** → select `specter-watchface/`.

Android Studio will sync Gradle automatically. If it asks to upgrade AGP, accept.

---

## 2. Validate the Watch Face XML

The WFF validator catches schema errors before building.

```bash
# Option A — Android Studio built-in
# Open res/raw/watchface.xml → the editor shows WFF warnings inline

# Option B — CLI validator (requires WFF tools)
java -jar wff-validator.jar app/src/main/res/raw/watchface.xml
```

Common errors to watch for:
- `ComplicationSlot` must contain `DefaultProviderPolicy` and `BoundingRectangle` before `Complication` children
- Color expressions `[CONFIGURATION.id.N]` are 0-indexed
- Arithmetic in dimension attributes: no parentheses, use `226 - [BATTERY_PERCENT_INT] * 2.26`

---

## 3. Create a Release Keystore

> **Do this once** and keep the `.jks` file and passwords somewhere safe.
> Losing the keystore = losing the ability to update the app on Play.

```bash
keytool -genkeypair \
  -alias specter-key \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000 \
  -keystore specter-release.jks \
  -storepass YOUR_STORE_PASSWORD \
  -keypass  YOUR_KEY_PASSWORD \
  -dname "CN=Your Name, OU=, O=Your Company, L=City, ST=State, C=US"
```

Add to `specter-watchface/keystore.properties` (already in `.gitignore`):

```properties
storeFile=../specter-release.jks
storePassword=YOUR_STORE_PASSWORD
keyAlias=specter-key
keyPassword=YOUR_KEY_PASSWORD
```

Wire it up in `app/build.gradle` `android { }` block:

```gradle
def keystoreProps = new Properties()
keystoreProps.load(new FileInputStream(rootProject.file("keystore.properties")))

signingConfigs {
    release {
        storeFile     file(keystoreProps['storeFile'])
        storePassword keystoreProps['storePassword']
        keyAlias      keystoreProps['keyAlias']
        keyPassword   keystoreProps['keyPassword']
    }
}
buildTypes {
    release {
        signingConfig signingConfigs.release
        minifyEnabled false
    }
}
```

---

## 4. Build the Release AAB

```
Build → Generate Signed Bundle / APK → Android App Bundle → release
```

Or via command line:

```bash
./gradlew bundleRelease
```

Output: `app/build/outputs/bundle/release/app-release.aab`

The AAB is a **resource-only bundle** (~200 KB). No code, no permissions requested.

---

## 5. Test on a Wear OS Device

```bash
# Install directly to a paired watch (USB debugging or ADB over Bluetooth)
adb install app/build/outputs/apk/release/app-release.apk

# Or sideload via Play Console internal testing track (recommended)
```

Verify:
- [ ] Watch face appears in the picker with the preview thumbnail
- [ ] All 4 neon themes selectable in watch face editor
- [ ] Time updates every second (check against phone)
- [ ] Battery bar moves as you drain / charge
- [ ] Tapping complication slots opens their configuration
- [ ] Ambient mode activates (lower wrist / cover screen) — time remains legible
- [ ] No crash in watch face picker or after theme switch

---

## 6. Prepare Play Store Assets

### App Icon
Use `renders/specter_renders.svg` — export a 512×512 PNG of one panel (CYBER CYAN recommended).

### Feature Graphic
Export `renders/specter_renders.svg` at full 1060×600, save as `feature_graphic.png`.

### Screenshots (required: min 2, Wear OS circular 384×384 or 450×450)
Export each of the 4 watch panels from the renders SVG as individual 450×450 PNGs:
- `screenshot_cyber_cyan.png`
- `screenshot_ghost_crimson.png`
- `screenshot_matrix_green.png`
- `screenshot_synth_violet.png`

If you have a physical Wear OS device, take on-device screenshots via:
```bash
adb exec-out screencap -p > screenshot.png
```

### Short Description (80 chars max)
```
Cybernetic noir Wear OS watch face. Neon HUD. 4 dark themes.
```

### Full Description (copy-paste ready)
```
SPECTER — CYBERNETIC NOIR WATCH FACE

Darkness. Neon. Identity.

Inspired by cyberpunk cinema, SPECTER turns your wrist into a hacker's
HUD. A hooded figure watches from the shadows. A city skyline pulses
below. Scan lines bleed through the void. And in neon that bleeds
through the dark — your time.

── DESIGN ──────────────────────────────────────────────────
• Moody noir atmosphere with city silhouette and scan-line texture
• Hooded figure with reactive chest glow
• Angular HUD corner brackets frame the display
• RPG-style vertical battery bar at the edge — always know your power
• STEPS and HEART RATE data panels in tactical angular frames

── 4 NEON THEMES ────────────────────────────────────────────
• CYBER CYAN    — electric teal, the original hacker aesthetic
• GHOST CRIMSON — deep red, for operatives who work in blood
• MATRIX GREEN  — acid green, straight from the source code
• SYNTH VIOLET  — purple magenta for synthwave nights

── LIVE DATA ────────────────────────────────────────────────
• Real-time hours, minutes, seconds
• Day of week + date + month
• Live battery percentage (vertical bar + numeric)
• Step count complication (bottom left panel)
• Heart rate complication (bottom right panel)
• Swappable complications — configure for your fitness goals

── TECHNICAL ────────────────────────────────────────────────
• Built on Watch Face Format v1 (Google's official XML standard)
• Wear OS 4+ (API 33 and above)
• Pixel Watch 2 / 3, Galaxy Watch 6/7 and all Wear OS 4 devices
• OLED-optimised ambient mode — minimal pixel activation
• No permissions required — zero data collection

Perfect for developers, cyberpunk fans, sci-fi enthusiasts, and anyone
who wants a watch face that looks like it came from another dimension.
```

---

## 7. Create Play Console Listing

1. Go to [play.google.com/console](https://play.google.com/console)
2. **Create app** → App → `com.specter.watchface`
3. **App category**: Tools (or Personalization if available for Wear)
4. Upload AAB to **Internal testing** first
5. Fill Store listing → paste description above
6. Upload graphic assets (see §6)
7. Set **Content rating** → complete questionnaire → likely PEGI 3 / Everyone
8. **Pricing**: $1.99 (see §8)
9. Submit for review

---

## 8. Pricing Strategy

### Recommended: $1.99

| Tier | Price | Rationale |
|------|-------|-----------|
| Impulse buy | $0.99 | High volume, low barrier, race to bottom |
| **Premium digital** | **$1.99** | Sweet spot for watch faces; feels intentional |
| Boutique | $2.99–$3.99 | Defensible with strong brand / press coverage |
| Luxury | $4.99+ | Requires established reputation or IP |

**Why $1.99:**
- Google Play's best-selling watch face tier is $1.49–$2.49
- Below $2 psychological barrier → impulse purchase
- Above $0.99 signals quality and filters bot reviews
- With a distinctive cyberpunk niche, $1.99 captures enthusiast buyers
- Once rated 4.5+ with 100+ reviews, consider A/B testing $2.49

### Revenue projection (conservative)
```
100 purchases/month × $1.99 × 0.70 (Play 30% cut) = $139/month
500 purchases/month                                 = $697/month
```

Watch faces with strong visual identity and niche appeal (cyberpunk, anime, etc.)
routinely reach 200–500 organic downloads/month within 3 months of good ASO.

---

## 9. ASO (App Store Optimisation)

**Keywords to target** (add to title / description naturally):
- cyberpunk watch face
- neon watch face wear os
- pixel watch dark theme
- hacker watch face
- sci-fi watch face
- dark digital watch

**Title**: `SPECTER: Cyberpunk Watch Face`
(60 char limit — keep it tight)

**Localisations to add early** (high cyberpunk fan density):
- Japanese (ja) — strong sci-fi watch market
- Korean (ko) — Galaxy Watch + cyberpunk aesthetic
- German (de) — large Wear OS user base
- French (fr)

---

## 10. Post-Launch Checklist

- [ ] Reply to every review in the first 2 weeks
- [ ] Share screenshots on r/WearOS and r/Cyberpunk
- [ ] Post video walkthrough on Instagram Reels / TikTok (15s loop showing theme switching)
- [ ] List on [facer.io](https://www.facer.io) (different platform, different audience, free cross-promotion)
- [ ] Monitor crash reports in Play Console → Android Vitals
- [ ] Add 2 more themes in v1.1 (e.g., BLOOD MOON red-orange, GLITCH rainbow)
- [ ] Consider a free "lite" version with only CYBER CYAN to drive paid conversions

---

## 11. Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Watch face not appearing in picker | `watch_face_info.xml` missing or malformed | Validate XML; ensure `<Preview value="@drawable/preview"/>` exists |
| Complications not loading | `DefaultProviderPolicy` missing `defaultSystemProviderType` | Add `defaultSystemProviderType="SHORT_TEXT"` attribute |
| Battery bar not animating | Expression syntax error in `height` attribute | No parentheses; use `226 - [BATTERY_PERCENT_INT] * 2.26` |
| Theme colours not switching | `ColorConfiguration` id mismatch | Confirm `[CONFIGURATION.neonStyle.0]` matches `id="neonStyle"` |
| Build fails: "namespace not set" | `app/build.gradle` missing `namespace` | Add `namespace 'com.specter.watchface'` |
| `hasCode="false"` warning | Ignored — WFF requires this | Leave as-is, it is correct |
| Ambient mode too bright | No `Variant` on decorative elements | Add `<Variant mode="AMBIENT" target="alpha" value="0"/>` inside scan-line PartDraw elements |
| AAB too large (>50MB) | Unexpected assets | Verify no image assets included; VectorDrawable only |

---

## 12. File Inventory

```
specter-watchface/
├── settings.gradle
├── build.gradle
├── gradle.properties
├── .gitignore
└── app/
    ├── build.gradle
    └── src/main/
        ├── AndroidManifest.xml
        └── res/
            ├── raw/
            │   └── watchface.xml          ← THE WATCH FACE
            ├── xml/
            │   └── watch_face_info.xml
            ├── values/
            │   └── strings.xml
            └── drawable/
                └── preview.xml            ← Picker thumbnail (vector)

renders/
├── specter_renders.svg                    ← 4-theme showcase board
└── specter_ambient.svg                    ← Active vs ambient comparison
```

---

*Built with Watch Face Format v1 · Wear OS 4+ · SPECTER Watch Face*
