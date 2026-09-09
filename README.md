# AVA portal testing shell

Andrew authorized deployment for internal testing on September 8, 2026. This dedicated preview repository is not the M-Testco employee production application.

- Sample-data UI testing: https://himsafx.github.io/mtestco-customer-portal-preview/demo/
- Existing isolated preview sign-in: https://himsafx.github.io/mtestco-customer-portal-preview/
- Build receipt: testing-build.json

Application source and verified build: 33f20ae9b457ce165a3a2767e4bf59c8d1151bbf. Private source PR 50 remains draft and unmerged. This testing update includes transfer inspections, safer save/cancel handling, and custody CSV export.

The shell loads versioned, integrity-pinned JS and CSS through the existing static hosting function on isolated project zwgnrlvxvthdsdkeuimn. Sign-in and existing role permissions are unchanged. The sample view makes no database calls and does not persist changes. Source maps, artifacts containing internal evidence, secrets and real customer records are not published here.

Previous shell commit 0a967ea144ab465187a53687f0101876c2d03280 is retained in Git for rollback; old static hosting paths are unchanged. Publishing this test shell does not mean all features are complete or authorize a customer rollout. Signed-in cross-screen custody acceptance remains pending.

The exact artifacts from verification run 34256572248 were downloaded and checked against GitHub's archive hashes and the authenticated build receipt. All four versioned assets were uploaded with fixed path, length and checksum restrictions and independently fetched through the existing serving function to verify decoded hashes. The temporary publication helper was closed after upload. No source maps or internal browser evidence were published.
