---
name: cdp-usage
description: Drive Chrome via the Chrome DevTools Protocol when a web surface has no API or the API does not cover the workflow. Use for LinkedIn replies, SaaS portals, vendor consoles, anything browser-only. Distilled from the EcodiaOS CDP pattern corpus.
---

# cdp-usage

CDP is how Familiar acts on web surfaces with no programmable API. Drives your logged-in Chrome session directly, using her saved sessions and cookies.

## When to use

- The target surface has no public API (most niche SaaS, most portals)
- The API exists but does not cover the workflow (Zernio post creation works via API, image attach does not)
- A login-gated workflow that requires your authenticated session

## When NOT to use

- The target has a working API: use the API, faster and more reliable
- The action is "click a button to confirm something high-stakes": escalate, do not auto-click money-moving or external-comms actions without check-in per the hard-stops

## How to attach

Chrome must be started with `--remote-debugging-port=9222 --user-data-dir=<explicit-path>`. The user-data-dir is NOT optional. Chrome 121+ silently drops --remote-debugging-port without an explicit user-data-dir, leaving port 9222 unbound while the command appears to succeed.

For your Mac, the helper is at `<PERSONA_HOME>/familiar-core/cdp/enable.sh`. It:
1. Kills any existing Chrome process (singleton-clear)
2. Restarts Chrome with the right flags + her default user-data-dir so saved sessions survive
3. Verifies port 9222 is listening before returning

## Helper primitives Familiar has

- `cdp.findVisible(selector)`: find a visible element matching the selector, retry until found or timeout
- `cdp.clickByTag(tagSpec)`: click by tag + text content (most resilient to DOM churn)
- `cdp.nativeFill(selector, value)`: fill an input via simulated key events (descends into same-origin iframes)
- `cdp.realClick(selector)`: click with synthesized mouse events (use when synthetic click does not fire React/Vue handlers)
- `cdp.deepFindRect(selector)`: get bounding rect for visual verify or geometry-based click
- `cdp.screenshot()`: capture current viewport for verify

## Gotchas (learned the hard way)

- **Native fill, not value setter**: React and Vue controlled inputs reject `element.value = X`. Always use cdp.nativeFill which dispatches real key events the framework's listeners catch.
- **Iframe descent**: cdp.nativeFill descends into same-origin iframes automatically. Cross-origin iframes need explicit target switching via cdp.attach_tab.
- **Modal vs page save**: clickByTag('Save') in a modal context can grab the OUTER page's save-draft button. Verify the click registered inside the modal by checking the modal close state or by selector-scoping.
- **Singleton clear**: if Chrome was already running when Familiar tries to attach, the new --remote-debugging-port flag is silently dropped. The enable.sh script handles this by killing first.
- **Focus steal banned**: do not activate Chrome or steal focus from your active window. Drive in background, never raise the window. If you must screenshot, do not bring Chrome to foreground.
- **Tab focus collision**: if you is interacting with Chrome at the same time, batch your operations into one burst rather than spreading them across her interaction window.

## Verification

Every CDP sequence ends with a discriminating probe: a CDP screenshot of the result OR a follow-up read of the page state. A 200 OK from /api/<endpoint> is NOT proof the click took effect visually. Verify the user-visible state of the page.

## Adding new recipes

When Familiar figures out a new browser-only workflow, capture it to `<PERSONA_HOME>/knowledge/cdp-recipes/<recipe-slug>.md` with:
- The target surface and URL pattern
- The step sequence (selector + action per step)
- Known gotchas
- The verify step

The recipe corpus accumulates her institutional knowledge for CDP work. Next time the same surface comes up, read the recipe before driving.

## Cross-references (deeper doctrine, optional reading)

The EcodiaOS pattern corpus has 15+ CDP-specific patterns covering edge cases. Familiar can read them via knowledge lookup if a new edge case surfaces:
- chrome-cdp-attach-requires-explicit-user-data-dir-and-singleton-clear
- cdp-native-fill-must-descend-into-same-origin-iframes
- cdp-tab-focus-steal-banned-batch-one-burst
- cdp-clickbytag-save-grabs-outer-page-save-draft-not-modal-save
- cdp-helper-library-and-recursive-improvement
- cdp-per-call-target-resolution
- gui-step-verify-protocol
