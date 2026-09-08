# AVA portal testing shell

Andrew authorized deployment for internal testing on September 8, 2026. This dedicated preview repository is not the M-Testco employee production application.

- Sample-data UI testing: https://himsafx.github.io/mtestco-customer-portal-preview/demo/
- Existing isolated preview sign-in: https://himsafx.github.io/mtestco-customer-portal-preview/
- Build receipt: testing-build.json

Application source: 60e978586dc693e337b1cdc1661d74ddaf2f17f7. Verified build: 81cc80be9f4af27391b690490627ebaec18b9dba. Private source PR 50 remains draft and unmerged.

The shell loads versioned, integrity-pinned JS and CSS through the existing static hosting function on isolated project zwgnrlvxvthdsdkeuimn. Sign-in and existing role permissions are unchanged. The sample view makes no database calls and does not persist changes. Source maps, artifacts containing internal evidence, secrets and real customer records are not published here.

Previous shell commit ce247d18ce5afe4c3d55171dc882b7ef8c4532a4 is retained in Git for rollback; old static hosting paths are unchanged. Publishing this test shell does not mean all features are complete or authorize a customer rollout.
