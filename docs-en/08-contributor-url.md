# Creating a Contributor URL

For Community Influencer activities, add your Student Ambassadors Contributor ID to a Microsoft content URL so visits from your link can be tracked. This guide explains how to turn an original content URL into a Contributor URL for sharing.

> This guide is for Community Influencer content sharing. For Community Skiller, see [Add a Contributor ID to a plan link](06-community-skiller.md#how-do-i-add-my-contributor-id-to-a-plan-link).

## 1. Find your Contributor ID

Use the **Student Ambassadors Contributor ID** sent by email 3–5 days after registration. The general format is:

```text
?wt.mc_id=studentamb_######
```

The `######` portion is replaced by your unique number. Do not confuse this with the **Learn Contributor ID** shown in your Learn profile settings.

## 2. Add a Contributor ID to a clean URL

If the URL does not contain a question mark (`?`), append your Contributor ID directly to the end.

1. Open an eligible Microsoft content page to share.
2. Remove the language-region code such as `/en-us/` or `/ko-kr/`. For example, change `https://learn.microsoft.com/en-us/copilot` to `https://learn.microsoft.com/copilot`.
3. Append `?wt.mc_id=studentamb_######` to the URL.

```text
Original: https://learn.microsoft.com/en-us/copilot
Updated:  https://learn.microsoft.com/copilot?wt.mc_id=studentamb_######
```

## 3. Update a URL with existing parameters

If the original URL already contains `?`, do not add a second question mark. Keep the existing parameters and add `&wt.mc_id=studentamb_######` at the end.

```text
Original: https://learn.microsoft.com/en-us/copilot?WT.mc_id=academic
Updated:  https://learn.microsoft.com/copilot?WT.mc_id=academic&wt.mc_id=studentamb_######
```

If the URL already contains another Contributor ID, keep it and add your Student Ambassadors Contributor ID after `&`.

## 4. Update a URL with a fragment (`#`)

If the URL contains a fragment that starts with `#`, do not append the Contributor ID after it. Add the ID to the query string before the fragment.

```text
Original: https://learn.microsoft.com/copilot#overview
Updated:  https://learn.microsoft.com/copilot?wt.mc_id=studentamb_123456#overview
```

If the URL already has both a query string and a fragment, update it like this:

```text
Original: https://learn.microsoft.com/copilot?view=latest#overview
Updated:  https://learn.microsoft.com/copilot?view=latest&wt.mc_id=studentamb_123456#overview
```

## 5. Final check before sharing

- [ ] Are you using your Student Ambassadors Contributor ID?
- [ ] Did you remove a language-region code such as `learn.microsoft.com/en-us/`?
- [ ] If the URL already has `?`, did you use `&wt.mc_id=...`?
- [ ] If the URL has a fragment, did you put the Contributor ID before it?
- [ ] Is the content an eligible Microsoft URL for Community Influencer?
- [ ] Is it specific, useful content rather than a Microsoft homepage?
- [ ] Did you avoid third-party URL shorteners such as Bitly?
- [ ] Are you sharing it on a public social network with a curated explanation?

After creating the link, paste the full URL into your browser to confirm that the content opens correctly. Preferred Visitor counts are reflected in the weekly reporting email and Progression Board rather than immediately, and processing may take up to 48 hours.

## Links that should not be used

- Microsoft Learn Plans cannot be used for the Community Influencer Preferred Visitor count. See the [Community Skiller guide](06-community-skiller.md) for Learn Plans.
- A path outside the eligible list may not count even when it includes a Contributor ID. Check the latest eligible URL list in the [Community Influencer guide](05-community-influencer.md) before sharing.
- Avoid spammy click requests, automated traffic, and third-party URL shorteners such as Bitly. Share the link with an explanation that is genuinely useful to your community.
