Release checklist & instructions

Steps to prepare a release:

1. Ensure branch `ci/notebook-ci` has all changes merged or create a release branch from it.
2. Confirm CI passes on the branch (import checks, pytest, notebook execution).
3. Build the Docker image locally or via the `docker-build` workflow and verify the artifact:

   - Workflow: `.github/workflows/docker-build.yml` (runs on push or manual dispatch)
   - After run: download `docker-image-tar` artifact and test locally: `docker load -i <tar>`

4. Update `CHANGELOG.md` or release notes with user-facing changes.
5. Tag the commit (semantic version): `git tag -a vX.Y.Z -m "Release vX.Y.Z"` and push tags.
6. Create the GitHub Release (Draft) and attach artifacts if desired.
7. Optionally publish container to GitHub Container Registry or Docker Hub (requires credentials and GH Action secrets):

   - Create a GH secret `CR_PAT` or `DOCKERHUB_TOKEN` and configure push in a workflow.

8. Announce the release and monitor user feedback/bug reports.

Minimal release checklist (quick):
- [ ] CI passing
- [ ] Tests passing locally and in CI
- [ ] Notebook executes end-to-end
- [ ] Docker image built and smoke-checked
- [ ] Release created on GitHub
