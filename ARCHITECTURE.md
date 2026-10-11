# ArabSea Frontend Architecture

## Structure

- `assets/css/core.css` provides shared responsive layout, focus, notification, mobile navigation, and search styles.
- `assets/js/core/i18n.js` contains exact-string translations and language/RTL-LTR switching. Dictionaries can be extended through `ArabSeaI18n.extend(lang, entries)`.
- `assets/js/core/app.js` bootstraps the common application layer on all 114 HTML pages. It provides search, common table behavior, local forms, workflow state, audit and notification views, permissions, and page-aware delegated actions.
- Existing role directories, page layouts, and inline page scripts remain the information architecture and can continue to supply page-specific behavior.
- `scripts/qa_audit.py` scans local targets, duplicate IDs, shared script coverage, static text coverage, and button labels. `scripts/build_interaction_audit.py` writes a page-by-page interaction inventory. Their label-based classifications are review aids, not proof of correct behavior.

## Localization

Arabic is the default. The language selector persists the choice in local storage, updates the document language and direction, and translates exact dictionary matches in page text, labels, titles, placeholders, and options. Unmatched Arabic remains Arabic in English mode. See `QA_VALIDATION.md` and `V2_IMPLEMENTATION_REPORT.md` for the current measured gap; the translation pass is not complete.

## Shared UI and interactions

The shared core adds workspace search over portal links/current-page rows, live search, basic select filtering, sortable table headings, paging for tables longer than ten rows, CSV export, print, responsive sidebar controls, feedback, and native form validation. Common page-aware actions cover the implemented demo flows documented in the interaction audit. Controls outside those mappings may still receive a generic page-context response; use the inventory to identify those that require semantic implementation.

## State model

`ArabSea.storage` namespaces browser storage keys with `arabsea:`. Demo state includes:

- `workflow:<id>`: current status and an ordered transition history.
- `audit-trail`: bounded local action entries with page, role, timestamp, and event details.
- `notifications`: locally generated items and read state.
- `users:<page>`: user rows for the administration demo.
- Feature keys for requests, risks, meeting attendance and votes, audit workpapers, report filters, settings, and communications.

Table hydration reapplies saved row values/statuses when the same page loads again in the same browser. Local data is not shared between users or devices. Fields that could contain passwords, secrets, or tokens are redacted on generic form submission; uploaded file contents are not persisted.

## Roles and permissions

`ArabSea.permissions.can(action)` provides a centralized frontend role policy inferred from the portal path. It can hide or refuse selected demo actions. It is not an authorization boundary: production APIs must authenticate the user and enforce all permissions server-side for every operation.

## Workflow, audit, and notifications

`ArabSea.workflow.transition(id, status, comment)` appends a local history event and records an audit event. User actions may update the visible row, dashboard count, and local notification list. These records are editable browser storage, not a regulated or immutable audit trail. Real workflow rules, delegation, approval routing, thresholds, identity, SLAs, and cross-user notifications require backend policy and persistence.

## API integration and deployment

The repository remains static HTML/CSS/JavaScript and requires no build step. Replace or wrap the local storage adapter with authenticated APIs for users, requests, documents, approvals, notifications, financial data, and audit events. Do not use hidden controls or local state to enforce security. Existing Tailwind and Font Awesome CDN assets still require network access.
