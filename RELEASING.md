Releasing a New Version
=======================

 * Update translations
   - `tx pull`
   - `tools/update-translations`
   - `virtaal po/fi.po`
   - `tools/check-translations`
   - `tx push -stf`
   - `git commit -a -m "Update translations for X.Y.Z."`
 * Do final quality checks
   - `python3 -Wd bin/nfoview`
   - `pyflakes3 bin/nfoview nfoview setup.py`
   - `py.test-3 --tb=no nfoview`
 * Bump version number
   - `nfoview/__init__.py`
 * Update `NEWS.md` and `TODO.md`
 * Check that installation works
   - `sudo python3 setup.py install --prefix=/usr/local`
   - `sudo python3 setup.py clean`
   - `/usr/local/bin/nfoview`
 * Commit changes
   - `git commit -a -m "RELEASE X.Y.Z"`
   - `git tag -s X.Y.Z`
   - `git push`
   - `git push --tags`
 * Add release notes on GitHub
 * Update web sites
   - <http://otsaloma.github.io/nfoview/>
   - <http://bugzilla.gnome.org/editproducts.cgi?action=edit&product=nfoview>