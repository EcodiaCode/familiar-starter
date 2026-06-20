---
name: travel-plan
description: Plan a trip end to end - flights, accommodation, ground transport, an itinerary, and the calendar holds - researched and laid out for your person to book. Use when they say "plan a trip to", "sort my travel for", or "book my flights".
triggers: ["plan a trip", "sort my travel", "book my flights", "travel to", "itinerary for", "going to", "plan my journey", "trip to"]
---

# travel-plan

A trip is a hundred small decisions that eat an afternoon. travel-plan does the research and the layout so your person makes the few choices that matter and books.

## When to use

- They are travelling and want the options researched and the itinerary built.
- A recurring trip where a prior plan is the template.

## When NOT to use

- To book and pay. Researching and laying out options is yours; spending money is theirs until they say otherwise.
- Where you cannot verify availability or price. Show options with the source and let them confirm at the point of booking; do not assert a fare from memory.

## Build the plan

1. Pin the brief: dates, origin and destination, budget, preferences (airline, seat, hotel area, must-dos). Ask the few that change everything before researching.
2. Read any prior trip notes in `knowledge/travel/` for their patterns: where they like to stay, how early they fly, what they always forget.
3. Research live: flights, accommodation, and ground transport. Drive the booking sites per the cdp-usage skill where there is no API. Quote real prices and times from the live page, marked with the source, since fares move by the hour.
4. Check the calendar so the trip does not collide with a commitment, and hold the travel days.

## The plan shape

- **Flights**: two or three real options with times, price, and source. Your recommendation and why.
- **Accommodation**: a short list that fits the budget and the area, with the trade-offs named.
- **Ground and logistics**: airport transfers, local transport, anything time-sensitive.
- **Day-by-day itinerary**: what is where on each day, with the fixed commitments anchored.
- **The book list**: exactly what they need to confirm, in order, so booking is fast.

## Hard rules

- Researching and laying out is yours; booking and paying is theirs until they grant standing authority.
- Prices and times are quoted live from the source and dated, never asserted from memory. A fare changes between research and booking; say so.
- Hold the calendar dates once the trip is real, and confirm the holds took.
- Save the trip notes to `knowledge/travel/` so the next trip starts ahead.
