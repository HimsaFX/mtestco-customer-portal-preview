# AVA portal testing shell

Andrew authorized deployment for internal testing on September 8, 2026. This dedicated preview repository is not the M-Testco employee production application.

- Sample-data UI testing: https://himsafx.github.io/mtestco-customer-portal-preview/demo/
- Existing isolated preview sign-in: https://himsafx.github.io/mtestco-customer-portal-preview/
- Build receipt: testing-build.json

Application source and verified build: 4f8403e372a07ea7aa8f8dcec9b8f9ad47f94033. Private source PR 50 remains draft and unmerged. This testing update separates responsible branch from current job site in asset profiles. Active project assignments come from the existing authorized project snapshot; unavailable or limited visibility is explicit. Transfer inspections, safer save/cancel handling, and custody CSV export are retained.

The shell loads versioned, integrity-pinned JS and CSS through the existing static hosting function on isolated project zwgnrlvxvthdsdkeuimn. Sign-in and existing role permissions are unchanged. The sample view makes no database calls and does not persist changes. Source maps, artifacts containing internal evidence, secrets and real customer records are not published here.

Previous shell commit e2ea18fb482234999315d4fb11b26c701cb79b68 is retained in Git for rollback; old static hosting paths are unchanged. Publishing this test shell does not mean all features are complete or authorize a customer rollout. The signed-in branch-to-project-to-branch custody journey passed on the preceding build; final live location-display verification is tracked separately.

The exact artifacts from verification run 34299505570 were downloaded and checked against GitHub's archive hashes and the authenticated build receipt. All six release workflows passed, including 473 portal tests. All four versioned assets were uploaded with fixed path, length and checksum restrictions and independently fetched through the existing serving function to verify decoded hashes. The temporary publication helper was closed after upload. No source maps or internal browser evidence were published.
