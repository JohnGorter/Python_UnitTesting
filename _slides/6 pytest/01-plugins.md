# pytest plugins

---
### Installing and Using plugins

Installing a third party plugin can be easily done with pip:

```
pip3 install pytest-NAME
pip3 uninstall pytest-NAME
```

If a plugin is installed, pytest automatically finds and integrates it, there is no need to activate it

---
### Popular plugins
Some popular plugins:

pytest-django: write tests for django apps, using pytest integration.
pytest-twisted: write tests for twisted apps, starting a reactor and processing deferreds from test functions.
pytest-cov: coverage reporting, compatible with distributed testing
pytest-xdist: to distribute tests to CPUs and remote hosts, to run in boxed mode which allows to survive segmentation faults, to run in looponfailing mode, automatically re-running failing tests on file changes.
pytest-instafail: to report failures while the test run is happening.
pytest-bdd and pytest-konira to write tests using behaviour-driven testing.
pytest-timeout: to timeout tests based on function marks or global definitions.
pytest-pep8: a --pep8 option to enable PEP8 compliance checking.
pytest-flakes: check source code with pyflakes.
oejskit: a plugin to run javascript unittests in live browsers.

more: http://plugincompat.herokuapp.com/

---
### Requiring/Loading plugins 

You can require plugins in a test module or a conftest file 
```
pytest_plugins = ("xdist",)
```

When the test module or conftest plugin is loaded the specified plugins will be loaded as well

---
### Listing the active plugins 
Get a list of active and registered plugins using
```
pytest --traceconfig
```
here is my output
```
PLUGIN registered: <_pytest.config.PytestPluginManager object at 0x102d8f588>
PLUGIN registered: <_pytest.config.Config object at 0x1023d1dd8>
PLUGIN registered: <module '_pytest.mark' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/mark/__init__.py'>
PLUGIN registered: <module '_pytest.main' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/main.py'>
PLUGIN registered: <module '_pytest.terminal' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/terminal.py'>
PLUGIN registered: <module '_pytest.runner' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/runner.py'>
PLUGIN registered: <module '_pytest.python' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/python.py'>
PLUGIN registered: <module '_pytest.fixtures' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/fixtures.py'>
PLUGIN registered: <module '_pytest.debugging' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/debugging.py'>
PLUGIN registered: <module '_pytest.unittest' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/unittest.py'>
PLUGIN registered: <module '_pytest.capture' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/capture.py'>
PLUGIN registered: <module '_pytest.skipping' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/skipping.py'>
PLUGIN registered: <module '_pytest.tmpdir' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/tmpdir.py'>
PLUGIN registered: <module '_pytest.monkeypatch' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/monkeypatch.py'>
PLUGIN registered: <module '_pytest.recwarn' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/recwarn.py'>
PLUGIN registered: <module '_pytest.pastebin' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/pastebin.py'>
PLUGIN registered: <module '_pytest.helpconfig' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/helpconfig.py'>
PLUGIN registered: <module '_pytest.nose' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/nose.py'>
PLUGIN registered: <module '_pytest.assertion' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/assertion/__init__.py'>
PLUGIN registered: <module '_pytest.junitxml' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/junitxml.py'>
PLUGIN registered: <module '_pytest.resultlog' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/resultlog.py'>
PLUGIN registered: <module '_pytest.doctest' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/doctest.py'>
PLUGIN registered: <module '_pytest.cacheprovider' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/cacheprovider.py'>
PLUGIN registered: <module '_pytest.freeze_support' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/freeze_support.py'>
PLUGIN registered: <module '_pytest.setuponly' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/setuponly.py'>
PLUGIN registered: <module '_pytest.setupplan' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/setupplan.py'>
PLUGIN registered: <module '_pytest.stepwise' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/stepwise.py'>
PLUGIN registered: <module '_pytest.warnings' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/warnings.py'>
PLUGIN registered: <module '_pytest.logging' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/logging.py'>
PLUGIN registered: <module '_pytest.reports' from '/usr/local/homebrew/lib/python3.7/site-packages/_pytest/reports.py'>
PLUGIN registered: <module 'xdist.plugin' from '/usr/local/homebrew/lib/python3.7/site-packages/xdist/plugin.py'>
PLUGIN registered: <module 'xdist.looponfail' from '/usr/local/homebrew/lib/python3.7/site-packages/xdist/looponfail.py'>
PLUGIN registered: <module 'pytest_forked' from '/usr/local/homebrew/lib/python3.7/site-packages/pytest_forked/__init__.py'>
PLUGIN registered: <CaptureManager _method='fd' _global_capturing=<MultiCapture out=<FDCapture 1 oldfd=5> err=<FDCapture 2 oldfd=6> in_=<FDCapture 0 oldfd=3>> _current_item=None>
PLUGIN registered: <module 'conftest' from '/Users/johngorter/Desktop/VueJs/_demos/6 pytest/demo 8 using plugins/conftest.py'>
PLUGIN registered: <Session demo 8 using plugins exitstatus=0 testsfailed=0 testscollected=0>
PLUGIN registered: <_pytest.cacheprovider.LFPlugin object at 0x1032e64e0>
PLUGIN registered: <_pytest.cacheprovider.NFPlugin object at 0x1032e6860>
PLUGIN registered: <_pytest.stepwise.StepwisePlugin object at 0x1032677f0>
PLUGIN registered: <_pytest.terminal.TerminalReporter object at 0x1032679b0>
PLUGIN registered: <_pytest.logging.LoggingPlugin object at 0x1032e9be0>
PLUGIN registered: <_pytest.fixtures.FixtureManager object at 0x103405080>
========================================================== test session starts ==========================================================
platform darwin -- Python 3.7.3, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
using: pytest-4.4.1 pylib-1.8.0
setuptools registered plugins:
  pytest-xdist-1.28.0 at /usr/local/homebrew/lib/python3.7/site-packages/xdist/plugin.py
  pytest-xdist-1.28.0 at /usr/local/homebrew/lib/python3.7/site-packages/xdist/looponfail.py
  pytest-forked-1.0.2 at /usr/local/homebrew/lib/python3.7/site-packages/pytest_forked/__init__.py
active plugins:
    4342740360          : <_pytest.config.PytestPluginManager object at 0x102d8f588>
    pytestconfig        : <_pytest.config.Config object at 0x1023d1dd8>
    mark                : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/mark/__init__.py
    main                : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/main.py
    terminal            : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/terminal.py
    runner              : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/runner.py
    python              : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/python.py
    fixtures            : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/fixtures.py
    debugging           : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/debugging.py
    unittest            : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/unittest.py
    capture             : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/capture.py
    skipping            : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/skipping.py
    tmpdir              : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/tmpdir.py
    monkeypatch         : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/monkeypatch.py
    recwarn             : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/recwarn.py
    pastebin            : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/pastebin.py
    helpconfig          : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/helpconfig.py
    nose                : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/nose.py
    assertion           : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/assertion/__init__.py
    junitxml            : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/junitxml.py
    resultlog           : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/resultlog.py
    doctest             : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/doctest.py
    cacheprovider       : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/cacheprovider.py
    freeze_support      : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/freeze_support.py
    setuponly           : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/setuponly.py
    setupplan           : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/setupplan.py
    stepwise            : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/stepwise.py
    warnings            : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/warnings.py
    logging             : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/logging.py
    reports             : /usr/local/homebrew/lib/python3.7/site-packages/_pytest/reports.py
    xdist               : /usr/local/homebrew/lib/python3.7/site-packages/xdist/plugin.py
    xdist.looponfail    : /usr/local/homebrew/lib/python3.7/site-packages/xdist/looponfail.py
    pytest_forked       : /usr/local/homebrew/lib/python3.7/site-packages/pytest_forked/__init__.py
    capturemanager      : <CaptureManager _method='fd' _global_capturing=<MultiCapture out=<FDCapture 1 oldfd=5> err=<FDCapture 2 oldfd=6> in_=<FDCapture 0 oldfd=3>> _current_item=None>
    /Users/johngorter/Desktop/VueJs/_demos/6 pytest/demo 8 using plugins/conftest.py: /Users/johngorter/Desktop/VueJs/_demos/6 pytest/demo 8 using plugins/conftest.py
    session             : <Session demo 8 using plugins exitstatus=0 testsfailed=0 testscollected=0>
    lfplugin            : <_pytest.cacheprovider.LFPlugin object at 0x1032e64e0>
    nfplugin            : <_pytest.cacheprovider.NFPlugin object at 0x1032e6860>
    stepwiseplugin      : <_pytest.stepwise.StepwisePlugin object at 0x1032677f0>
    terminalreporter    : <_pytest.terminal.TerminalReporter object at 0x1032679b0>
    logging-plugin      : <_pytest.logging.LoggingPlugin object at 0x1032e9be0>
    funcmanage          : <_pytest.fixtures.FixtureManager object at 0x103405080>
rootdir: /Users/johngorter/Desktop/VueJs/_demos/6 pytest/demo 8 using plugins
plugins: xdist-1.28.0, forked-1.0.2
collected 1 item                                                                                                                        

test_one.py .                                                                                                                     [100%]
```

---
### Deactivating / unregistering a plugin by name
You can prevent plugins from loading or unregister them:
```
pytest -p no:NAME
```
This means that any subsequent try to activate/load the named plugin will not work

