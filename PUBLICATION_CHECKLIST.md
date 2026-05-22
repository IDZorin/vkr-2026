# Publication Checklist

Use this checklist before pushing the bundle to a public Git repository.

1. Run the secret/path scan:

   ```bash
   rg -n "D:/|D:\\\\|OneDrive|Shadow|API_KEY|SECRET|PASSWORD|OPENAI|ANTHROPIC" . --glob '!README.md' --glob '!PUBLICATION_CHECKLIST.md'
   ```

2. Run the example check:

   ```bash
   python tools/check_entry.py examples/section_2_3_weighting
   python tools/check_entry.py demos/russian_law/data
   python tools/check_entry.py demos/draughts_64/data
   ```

3. Run the offline public demos:

   ```bash
   python demos/run_recorded_demo.py
   python -m unittest discover -s tests
   ```

4. Review `docs/thesis_artifact_mapping.md` and confirm every thesis-facing
   path points either to an included public artifact or to an explicitly marked
   template/private-source slot.

5. Decide on a license and add `LICENSE` if the repository is intended for reuse.

6. Review the example source text. If publication policy requires avoiding
   third-party excerpts, replace `examples/section_2_3_weighting/source.md`
   with a synthetic source fragment while keeping the A4V3 structure.

7. Verify attribution and publication terms for public demo source texts,
   especially any modern edition or federation rule text.

8. Do not add private run outputs, `.env`, virtual environments, or old
   experiment workspaces to the public repository.
