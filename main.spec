# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['ai21', 'aiofiles', 'aiohttp', 'aiosignal', 'aiosqlite', 'alabaster @ file:///home/ktietz/src/ci/alabaster_1611921544520/work
', 'altair', 'altgraph', 'anaconda-client', 'anaconda-navigator', 'anaconda-project @ file:///C:/Windows/TEMP/abs_91fu4tfkih/croots/recipe/anaconda-project_1660339890874/work
', 'anyio @ file:///C:/ci/anyio_1644481856696/work/dist
', 'appdirs', 'arabic-reshaper', 'argon2-cffi @ file:///opt/conda/conda-bld/argon2-cffi_1645000214183/work
', 'argon2-cffi-bindings @ file:///C:/ci/argon2-cffi-bindings_1644569876605/work
', 'arrow @ file:///C:/b/abs_cal7u12ktb/croot/arrow_1676588147908/work
', 'asn1crypto', 'astroid @ file:///C:/b/abs_d4lg3_taxn/croot/astroid_1676904351456/work
', 'astropy @ file:///C:/ci/astropy_1657719642921/work
', 'asttokens @ file:///opt/conda/conda-bld/asttokens_1646925590279/work
', 'async-timeout', 'asyncua', 'atomicwrites', 'attrs @ file:///C:/b/abs_09s3y775ra/croot/attrs_1668696195628/work
', 'auto-py-to-exe', 'Automat @ file:///tmp/build/80754af9/automat_1600298431173/work
', 'autopep8 @ file:///opt/conda/conda-bld/autopep8_1650463822033/work
', 'azure-common', 'azure-core', 'azure-identity', 'azure-search-documents', 'azure-storage-blob', 'Babel @ file:///C:/b/abs_a2shv_3tqi/croot/babel_1671782804377/work
', 'backcall @ file:///home/ktietz/src/ci/backcall_1611930011877/work
', 'backports.functools-lru-cache @ file:///tmp/build/80754af9/backports.functools_lru_cache_1618170165463/work
', 'backports.tempfile @ file:///home/linux1/recipes/ci/backports.tempfile_1610991236607/work
', 'backports.weakref', 'bcrypt @ file:///C:/Windows/Temp/abs_36kl66t_aw/croots/recipe/bcrypt_1659554334050/work
', 'beautifulsoup4 @ file:///C:/ci/beautifulsoup4_1650293028159/work
', 'binaryornot @ file:///tmp/build/80754af9/binaryornot_1617751525010/work
', 'black @ file:///C:/ci/black_1660221726201/work
', 'bleach @ file:///opt/conda/conda-bld/bleach_1641577558959/work
', 'blinker', 'bokeh @ file:///C:/Windows/TEMP/abs_4a259bc2-ed05-4a1f-808e-ac712cc0900cddqp8sp7/croots/recipe/bokeh_1658136660686/work
', 'bottle', 'bottle-websocket', 'Bottleneck @ file:///C:/Windows/Temp/abs_3198ca53-903d-42fd-87b4-03e6d03a8381yfwsuve8/croots/recipe/bottleneck_1657175565403/work
', 'breadability', 'Brotli', 'brotlipy', 'cachetools', 'certifi @ file:///C:/b/abs_85o_6fm0se/croot/certifi_1671487778835/work/certifi
', 'cffi @ file:///C:/b/abs_49n3v2hyhr/croot/cffi_1670423218144/work
', 'chardet @ file:///C:/ci_310/chardet_1642114080098/work
', 'charset-normalizer @ file:///tmp/build/80754af9/charset-normalizer_1630003229654/work
', 'Chroma', 'click', 'cloudpickle @ file:///tmp/build/80754af9/cloudpickle_1632508026186/work
', 'clr-loader', 'clyent', 'colorama @ file:///C:/b/abs_a9ozq0l032/croot/colorama_1672387194846/work
', 'colorcet @ file:///C:/b/abs_46vyu0rpdl/croot/colorcet_1668084513237/work
', 'comm @ file:///C:/b/abs_1419earm7u/croot/comm_1671231131638/work
', 'comtypes', 'conda', 'conda-build', 'conda-content-trust @ file:///C:/Windows/TEMP/abs_4589313d-fc62-4ccc-81c0-b801b4449e833j1ajrwu/croots/recipe/conda-content-trust_1658126379362/work
', 'conda-pack @ file:///tmp/build/80754af9/conda-pack_1611163042455/work
', 'conda-package-handling @ file:///C:/b/abs_fcga8w0uem/croot/conda-package-handling_1672865024290/work
', 'conda-repo-cli', 'conda-token @ file:///Users/paulyim/miniconda3/envs/c3i/conda-bld/conda-token_1662660369760/work
', 'conda-verify', 'conda_package_streaming @ file:///C:/b/abs_0e5n5hdal3/croot/conda-package-streaming_1670508162902/work
', 'config', 'constantly', 'contourpy @ file:///C:/b/abs_d5rpy288vc/croots/recipe/contourpy_1663827418189/work
', 'cookiecutter @ file:///opt/conda/conda-bld/cookiecutter_1649151442564/work
', 'cryptography', 'cssselect', 'cssselect2', 'cycler @ file:///tmp/build/80754af9/cycler_1637851556182/work
', 'cytoolz @ file:///C:/b/abs_61m9vzb4qh/croot/cytoolz_1667465938275/work
', 'daal4py', 'dash', 'dash-bootstrap-components', 'dash-core-components', 'dash-html-components', 'dash-table', 'dash_mantine_components', 'dask @ file:///C:/ci/dask-core_1658497112560/work
', 'dataclasses-json', 'datashader @ file:///C:/b/abs_e80f3d7ac0/croot/datashader_1676023254070/work
', 'datashape', 'debugpy @ file:///C:/ci_310/debugpy_1642079916595/work
', 'decorator @ file:///opt/conda/conda-bld/decorator_1643638310831/work
', 'defusedxml @ file:///tmp/build/80754af9/defusedxml_1615228127516/work
', 'diff-match-patch @ file:///Users/ktietz/demo/mc3/conda-bld/diff-match-patch_1630511840874/work
', 'dill @ file:///C:/b/abs_42h_07z1yj/croot/dill_1667919550096/work
', 'disease.py', 'distributed @ file:///C:/ci/distributed_1658523963030/work
', 'distro', 'docopt', 'docstring-to-markdown @ file:///C:/b/abs_cf10j8nr4q/croot/docstring-to-markdown_1673447652942/work
', 'docutils @ file:///C:/Windows/TEMP/abs_24e5e278-4d1c-47eb-97b9-f761d871f482dy2vg450/croots/recipe/docutils_1657175444608/work
', 'Eel', 'entrypoints @ file:///C:/ci/entrypoints_1649926676279/work
', 'et-xmlfile', 'executing @ file:///opt/conda/conda-bld/executing_1646925071911/work
', 'fastapi', 'fastjsonschema @ file:///C:/Users/BUILDE~1/AppData/Local/Temp/abs_ebruxzvd08/croots/recipe/python-fastjsonschema_1661376484940/work
', 'ffmpy', 'filelock @ file:///C:/b/abs_c7yrhs9uz2/croot/filelock_1672387617533/work
', 'fire', 'flake8 @ file:///C:/b/abs_9f6_n1jlpc/croot/flake8_1674581816810/work
', 'Flask @ file:///C:/b/abs_ef16l83sif/croot/flask_1671217367534/work
', 'flit_core @ file:///opt/conda/conda-bld/flit-core_1644941570762/work/source/flit_core
', 'fonttools', 'frozenlist', 'fsspec', 'fst-pso', 'future @ file:///C:/b/abs_3dcibf18zi/croot/future_1677599891380/work
', 'FuzzyTM', 'gensim @ file:///C:/b/abs_a5vat69tv8/croot/gensim_1674853640591/work
', 'getmac', 'gevent', 'gevent-websocket', 'gitdb', 'GitPython', 'glob2 @ file:///home/linux1/recipes/ci/glob2_1610991677669/work
', 'google-trans-new', 'gradio', 'gradio_client', 'greenlet @ file:///C:/b/abs_47lk_w2ajq/croot/greenlet_1670513248400/work
', 'h11', 'h5py @ file:///C:/ci/h5py_1659089830381/work
', 'HeapDict @ file:///Users/ktietz/demo/mc3/conda-bld/heapdict_1630598515714/work
', 'holoviews @ file:///C:/b/abs_bbf97_0kcd/croot/holoviews_1676372911083/work
', 'html5lib', 'httpcore', 'httpx', 'huggingface-hub', 'hvplot @ file:///C:/b/abs_13un17_4x_/croot/hvplot_1670508919193/work
', 'hyperlink @ file:///tmp/build/80754af9/hyperlink_1610130746837/work
', 'idna @ file:///C:/b/abs_bdhbebrioa/croot/idna_1666125572046/work
', 'imagecodecs @ file:///C:/b/abs_f0cr12h73p/croot/imagecodecs_1677576746499/work
', 'imageio @ file:///C:/b/abs_27kq2gy1us/croot/imageio_1677879918708/work
', 'imagesize @ file:///C:/Windows/TEMP/abs_3cecd249-3fc4-4bfc-b80b-bb227b0d701en12vqzot/croots/recipe/imagesize_1657179501304/work
', 'imbalanced-learn @ file:///C:/b/abs_1911ryuksz/croot/imbalanced-learn_1677191585237/work
', 'import-from-github-com', 'importlib-metadata @ file:///C:/ci/importlib-metadata_1648544469310/work
', 'incremental @ file:///tmp/build/80754af9/incremental_1636629750599/work
', 'inflection', 'iniconfig @ file:///home/linux1/recipes/ci/iniconfig_1610983019677/work
', 'install', 'intake @ file:///C:/b/abs_42yyb2lhwx/croot/intake_1676619887779/work
', 'intervaltree @ file:///Users/ktietz/demo/mc3/conda-bld/intervaltree_1630511889664/work
', 'ipykernel @ file:///C:/b/abs_b4f07tbsyd/croot/ipykernel_1672767104060/work
', 'ipython @ file:///C:/b/abs_d3h279dv3h/croot/ipython_1676582236558/work
', 'ipython-genutils @ file:///tmp/build/80754af9/ipython_genutils_1606773439826/work
', 'ipywidgets @ file:///tmp/build/80754af9/ipywidgets_1634143127070/work
', 'IronPdf', 'isodate', 'isort @ file:///tmp/build/80754af9/isort_1628603791788/work
', 'itemadapter @ file:///tmp/build/80754af9/itemadapter_1626442940632/work
', 'itemloaders @ file:///opt/conda/conda-bld/itemloaders_1646805235997/work
', 'itsdangerous @ file:///tmp/build/80754af9/itsdangerous_1621432558163/work
', 'jedi @ file:///C:/ci/jedi_1644315428305/work
', 'jellyfish @ file:///C:/ci/jellyfish_1647962737334/work
', 'Jinja2 @ file:///C:/b/abs_7cdis66kl9/croot/jinja2_1666908141852/work
', 'jinja2-time @ file:///opt/conda/conda-bld/jinja2-time_1649251842261/work
', 'jmespath @ file:///Users/ktietz/demo/mc3/conda-bld/jmespath_1630583964805/work
', 'joblib @ file:///C:/b/abs_e60_bwl1v6/croot/joblib_1666298845728/work
', 'JPype1', 'json5 @ file:///tmp/build/80754af9/json5_1624432770122/work
', 'jsonschema @ file:///C:/b/abs_6ccs97j_l8/croot/jsonschema_1676558690963/work
', 'jupyter @ file:///C:/Windows/TEMP/abs_56xfdi__li/croots/recipe/jupyter_1659349053177/work
', 'jupyter-console @ file:///C:/b/abs_68ttzd5p9c/croot/jupyter_console_1677674667636/work
', 'jupyter-server @ file:///C:/b/abs_1cfi3__jl8/croot/jupyter_server_1671707636383/work
', 'jupyter-ui-poll', 'jupyter_client @ file:///C:/ci/jupyter_client_1661834530766/work
', 'jupyter_core @ file:///C:/b/abs_bd7elvu3w2/croot/jupyter_core_1676538600510/work
', 'jupyterlab @ file:///C:/b/abs_513jt6yy74/croot/jupyterlab_1675354138043/work
', 'jupyterlab-pygments @ file:///tmp/build/80754af9/jupyterlab_pygments_1601490720602/work
', 'jupyterlab-widgets @ file:///tmp/build/80754af9/jupyterlab_widgets_1609884341231/work
', 'jupyterlab_server @ file:///C:/b/abs_d1z_g1swc8/croot/jupyterlab_server_1677153204814/work
', 'keyring @ file:///C:/ci_310/keyring_1642165564669/work
', 'kiwisolver @ file:///C:/b/abs_88mdhvtahm/croot/kiwisolver_1672387921783/work
', 'langchain', 'langchainplus-sdk', 'lazy-object-proxy @ file:///C:/ci_310/lazy-object-proxy_1642083437654/work
', 'libarchive-c @ file:///tmp/build/80754af9/python-libarchive-c_1617780486945/work
', 'linkify-it-py', 'llama-index', 'llvmlite', 'locket @ file:///C:/ci/locket_1652904090946/work
', 'lxml @ file:///C:/ci/lxml_1657527492694/work
', 'lz4 @ file:///C:/ci_310/lz4_1643300078932/work
', 'Markdown @ file:///C:/b/abs_98lv_ucina/croot/markdown_1671541919225/work
', 'markdown-it-py', 'MarkupSafe @ file:///C:/ci/markupsafe_1654508036328/work
', 'marshmallow', 'marshmallow-enum', 'matplotlib @ file:///C:/b/abs_b2d7uv90hg/croot/matplotlib-suite_1677674332463/work
', 'matplotlib-inline @ file:///C:/ci/matplotlib-inline_1661934094726/work
', 'mccabe @ file:///opt/conda/conda-bld/mccabe_1644221741721/work
', 'mdit-py-plugins', 'mdurl', 'menuinst @ file:///C:/Users/BUILDE~1/AppData/Local/Temp/abs_455sf5o0ct/croots/recipe/menuinst_1661805970842/work
', 'miniful', 'mistune @ file:///C:/ci_310/mistune_1642084168466/work
', 'mkl-fft', 'mkl-random @ file:///C:/ci_310/mkl_random_1643050563308/work
', 'mkl-service', 'mock @ file:///tmp/build/80754af9/mock_1607622725907/work
', 'mpmath', 'msal', 'msal-extensions', 'msgpack @ file:///C:/ci/msgpack-python_1652348582618/work
', 'msrest', 'multidict', 'multipledispatch @ file:///C:/ci_310/multipledispatch_1642084438481/work
', 'munkres', 'mypy-extensions', 'mysql-connector-python', 'navigator-updater', 'nbclassic @ file:///C:/b/abs_d0_ze5q0j2/croot/nbclassic_1676902914817/work
', 'nbclient @ file:///C:/ci/nbclient_1650308592199/work
', 'nbconvert @ file:///C:/b/abs_4av3q4okro/croot/nbconvert_1668450658054/work
', 'nbformat @ file:///C:/b/abs_85_3g7dkt4/croot/nbformat_1670352343720/work
', 'nest-asyncio @ file:///C:/b/abs_3a_4jsjlqu/croot/nest-asyncio_1672387322800/work
', 'networkx @ file:///C:/ci/networkx_1657716953747/work
', 'nltk @ file:///opt/conda/conda-bld/nltk_1645628263994/work
', 'notebook @ file:///C:/b/abs_ca13hqvuzw/croot/notebook_1668179888546/work
', 'notebook_shim @ file:///C:/b/abs_ebfczttg6x/croot/notebook-shim_1668160590914/work
', 'numba @ file:///C:/b/abs_e53pp2e4k7/croot/numba_1670258349527/work
', 'numexpr @ file:///C:/b/abs_a7kbak88hk/croot/numexpr_1668713882979/work
', 'numpy @ file:///C:/b/abs_datssh7cer/croot/numpy_and_numpy_base_1672336199388/work
', 'numpydoc @ file:///C:/b/abs_cfdd4zxbga/croot/numpydoc_1668085912100/work
', 'oauthlib', 'opcua', 'opcua-client', 'opcua-modeler', 'opcua-widgets', 'openai', 'openapi-schema-pydantic', 'opencv-python', 'openpyxl', 'orjson', 'oscrypto', 'packaging @ file:///C:/b/abs_cfsup8ur87/croot/packaging_1671697442297/work
', 'pandas @ file:///C:/b/abs_b9kefbuby2/croot/pandas_1677835593760/work
', 'pandocfilters @ file:///opt/conda/conda-bld/pandocfilters_1643405455980/work
', 'panel @ file:///C:/b/abs_55ujq2fpyh/croot/panel_1676379705003/work
', 'param @ file:///C:/b/abs_d799n8xz_7/croot/param_1671697759755/work
', 'paramiko @ file:///opt/conda/conda-bld/paramiko_1640109032755/work
', 'parsel @ file:///C:/ci/parsel_1646722035970/work
', 'parso @ file:///opt/conda/conda-bld/parso_1641458642106/work
', 'partd @ file:///opt/conda/conda-bld/partd_1647245470509/work
', 'pathspec @ file:///C:/b/abs_9cu5_2yb3i/croot/pathspec_1674681579249/work
', 'patsy', 'pdfkit', 'pefile', 'pep8', 'pexpect @ file:///tmp/build/80754af9/pexpect_1605563209008/work
', 'pickleshare @ file:///tmp/build/80754af9/pickleshare_1606932040724/work
', 'Pillow', 'pkginfo @ file:///C:/b/abs_d51wye6ned/croot/pkginfo_1666725041585/work
', 'platformdirs @ file:///C:/b/abs_73cc5cz_1u/croots/recipe/platformdirs_1662711386458/work
', 'plotly @ file:///C:/ci/plotly_1658160673416/work
', 'pluggy @ file:///C:/ci/pluggy_1648042746254/work
', 'ply', 'pocketsphinx', 'pooch @ file:///tmp/build/80754af9/pooch_1623324770023/work
', 'portalocker', 'powerbiclient', 'poyo @ file:///tmp/build/80754af9/poyo_1617751526755/work
', 'prometheus-client @ file:///C:/Windows/TEMP/abs_ab9nx8qb08/croots/recipe/prometheus_client_1659455104602/work
', 'prompt-toolkit @ file:///C:/b/abs_6coz5_9f2s/croot/prompt-toolkit_1672387908312/work
', 'Protego @ file:///tmp/build/80754af9/protego_1598657180827/work
', 'protobuf', 'psutil @ file:///C:/Windows/Temp/abs_b2c2fd7f-9fd5-4756-95ea-8aed74d0039flsd9qufz/croots/recipe/psutil_1656431277748/work
', 'ptyprocess @ file:///tmp/build/80754af9/ptyprocess_1609355006118/work/dist/ptyprocess-0.7.0-py2.py3-none-any.whl
', 'pure-eval @ file:///opt/conda/conda-bld/pure_eval_1646925070566/work
', 'py @ file:///opt/conda/conda-bld/py_1644396412707/work
', 'py4j', 'pyarrow', 'pyasn1 @ file:///Users/ktietz/demo/mc3/conda-bld/pyasn1_1629708007385/work
', 'pyasn1-modules', 'pycodestyle @ file:///C:/b/abs_d77nxvklcq/croot/pycodestyle_1674267231034/work
', 'pycosat @ file:///C:/b/abs_4b1rrw8pn9/croot/pycosat_1666807711599/work
', 'pycountry', 'pycparser @ file:///tmp/build/80754af9/pycparser_1636541352034/work
', 'pyct @ file:///C:/b/abs_92z17k7ig2/croot/pyct_1675450330889/work
', 'pycurl', 'pydantic', 'pydeck', 'PyDispatcher', 'pydocstyle @ file:///C:/b/abs_6dz687_5i3/croot/pydocstyle_1675221688656/work
', 'pydub', 'pydyf', 'pyerfa @ file:///C:/ci_310/pyerfa_1642088497201/work
', 'pyflakes @ file:///C:/b/abs_6dve6e13zh/croot/pyflakes_1674165143327/work
', 'pyFUME', 'pygame', 'Pygments', 'PyHamcrest @ file:///tmp/build/80754af9/pyhamcrest_1615748656804/work
', 'pyHanko', 'pyhanko-certvalidator', 'pyinstaller', 'pyinstaller-hooks-contrib', 'PyJWT @ file:///C:/ci/pyjwt_1657529477795/work
', 'pylint @ file:///C:/b/abs_83sq99jc8i/croot/pylint_1676919922167/work
', 'pylint-venv @ file:///C:/b/abs_bf0lepsbij/croot/pylint-venv_1673990138593/work
', 'pyls-spyder', 'pymodbus', 'pyModbusTCP', 'Pympler', 'PyMuPDF', 'PyMuPDFb', 'PyNaCl @ file:///C:/Windows/Temp/abs_d5c3ajcm87/croots/recipe/pynacl_1659620667490/work
', 'pyodbc @ file:///C:/Windows/Temp/abs_61e3jz3u05/croots/recipe/pyodbc_1659513801402/work
', 'pyOpenSSL', 'pyparsing @ file:///C:/Users/BUILDE~1/AppData/Local/Temp/abs_7f_7lba6rl/croots/recipe/pyparsing_1661452540662/work
', 'pypdf', 'PyPDF2', 'pyphen', 'pypiwin32', 'pypng', 'PyQt5', 'PyQt5-sip @ file:///C:/Windows/Temp/abs_d7gmd2jg8i/croots/recipe/pyqt-split_1659273064801/work/pyqt_sip
', 'PyQtWebEngine', 'pyrsistent @ file:///C:/ci_310/pyrsistent_1642117077485/work
', 'PySide6', 'PySide6-Addons', 'PySide6-Essentials', 'PySocks @ file:///C:/ci_310/pysocks_1642089375450/work
', 'pyspark', 'pytest', 'python-bidi', 'python-dateutil @ file:///tmp/build/80754af9/python-dateutil_1626374649649/work
', 'python-dotenv', 'python-lsp-black @ file:///C:/Users/BUILDE~1/AppData/Local/Temp/abs_dddk9lhpp1/croots/recipe/python-lsp-black_1661852041405/work
', 'python-lsp-jsonrpc', 'python-lsp-server @ file:///C:/b/abs_e44khh1wya/croot/python-lsp-server_1677296772730/work
', 'python-multipart', 'python-slugify @ file:///tmp/build/80754af9/python-slugify_1620405669636/work
', 'python-snap7', 'python-snappy @ file:///C:/b/abs_61b1fmzxcn/croot/python-snappy_1670943932513/work
', 'python-utils', 'pythonnet', 'pytoolconfig @ file:///C:/b/abs_18sf9z_iwl/croot/pytoolconfig_1676315065270/work
', 'pyttsx3', 'pytz @ file:///C:/b/abs_22fofvpn1x/croot/pytz_1671698059864/work
', 'pyviz-comms @ file:///tmp/build/80754af9/pyviz_comms_1623747165329/work
', 'PyWavelets @ file:///C:/b/abs_a8r4b1511a/croot/pywavelets_1670425185881/work
', 'pywin32', 'pywin32-ctypes', 'pywinpty @ file:///C:/b/abs_73vshmevwq/croot/pywinpty_1677609966356/work/target/wheels/pywinpty-2.0.10-cp310-none-win_amd64.whl
', 'PyYAML @ file:///C:/b/abs_d0g7dqt2xw/croot/pyyaml_1670514768165/work
', 'pyzmq @ file:///C:/ci/pyzmq_1657616000714/work
', 'QDarkStyle @ file:///tmp/build/80754af9/qdarkstyle_1617386714626/work
', 'qrcode', 'qstylizer @ file:///C:/b/abs_ef86cgllby/croot/qstylizer_1674008538857/work/dist/qstylizer-0.2.2-py2.py3-none-any.whl
', 'QtAwesome @ file:///C:/b/abs_c5evilj98g/croot/qtawesome_1674008690220/work
', 'qtconsole @ file:///C:/b/abs_5bap7f8n0t/croot/qtconsole_1674008444833/work
', 'QtPy @ file:///C:/ci/qtpy_1662015130233/work
', 'queuelib', 'regex @ file:///C:/ci/regex_1658258299320/work
', 'reportlab', 'requests', 'requests-file @ file:///Users/ktietz/demo/mc3/conda-bld/requests-file_1629455781986/work
', 'requests-oauthlib', 'retrying', 'rich', 'rope @ file:///C:/b/abs_55g_tm_6ff/croot/rope_1676675029164/work
', 'Rtree @ file:///C:/b/abs_e116ltblik/croot/rtree_1675157871717/work
', 'ruamel-yaml-conda @ file:///C:/b/abs_6ejaexx82s/croot/ruamel_yaml_1667489767827/work
', 'ruamel.yaml @ file:///C:/b/abs_30ee5qbthd/croot/ruamel.yaml_1666304562000/work
', 'ruamel.yaml.clib @ file:///C:/b/abs_aarblxbilo/croot/ruamel.yaml.clib_1666302270884/work
', 'scikit-image @ file:///C:/b/abs_63r0vmx78u/croot/scikit-image_1669241746873/work
', 'scikit-learn @ file:///C:/b/abs_7ck_bnw91r/croot/scikit-learn_1676911676133/work
', 'scikit-learn-intelex', 'scipy', 'Scrapy @ file:///C:/b/abs_9fn69i_d86/croot/scrapy_1677738199744/work
', 'seaborn @ file:///C:/b/abs_68ltdkoyoo/croot/seaborn_1673479199997/work
', 'semantic-version', 'semver', 'Send2Trash @ file:///tmp/build/80754af9/send2trash_1632406701022/work
', 'service-identity @ file:///Users/ktietz/demo/mc3/conda-bld/service_identity_1629460757137/work
', 'shiboken6', 'simpful', 'sip @ file:///C:/Windows/Temp/abs_b8fxd17m2u/croots/recipe/sip_1659012372737/work
', 'six @ file:///tmp/build/80754af9/six_1644875935023/work
', 'smart-open @ file:///C:/ci/smart_open_1651235038100/work
', 'smmap', 'sniffio @ file:///C:/ci_310/sniffio_1642092172680/work
', 'snowballstemmer @ file:///tmp/build/80754af9/snowballstemmer_1637937080595/work
', 'sortedcontainers @ file:///tmp/build/80754af9/sortedcontainers_1623949099177/work
', 'sounddevice', 'soupsieve @ file:///C:/b/abs_fasraqxhlv/croot/soupsieve_1666296394662/work
', 'speech-recognition-python', 'Sphinx @ file:///C:/ci/sphinx_1657617157451/work
', 'sphinxcontrib-applehelp @ file:///home/ktietz/src/ci/sphinxcontrib-applehelp_1611920841464/work
', 'sphinxcontrib-devhelp @ file:///home/ktietz/src/ci/sphinxcontrib-devhelp_1611920923094/work
', 'sphinxcontrib-htmlhelp @ file:///tmp/build/80754af9/sphinxcontrib-htmlhelp_1623945626792/work
', 'sphinxcontrib-jsmath @ file:///home/ktietz/src/ci/sphinxcontrib-jsmath_1611920942228/work
', 'sphinxcontrib-qthelp @ file:///home/ktietz/src/ci/sphinxcontrib-qthelp_1611921055322/work
', 'sphinxcontrib-serializinghtml @ file:///tmp/build/80754af9/sphinxcontrib-serializinghtml_1624451540180/work
', 'spyder @ file:///C:/b/abs_93s9xkw3pn/croot/spyder_1677776163871/work
', 'spyder-kernels @ file:///C:/b/abs_feh4xo1mrn/croot/spyder-kernels_1673292245176/work
', 'SQLAlchemy', 'stack-data @ file:///opt/conda/conda-bld/stack_data_1646927590127/work
', 'starlette', 'statsmodels @ file:///C:/b/abs_bdqo3zaryj/croot/statsmodels_1676646249859/work
', 'streamlit', 'sumy', 'svglib', 'sympy @ file:///C:/b/abs_95fbf1z7n6/croot/sympy_1668202411612/work
', 'tables', 'tabula', 'tabula-py', 'tabulate @ file:///C:/ci/tabulate_1657600805799/work
', 'TBB', 'tblib @ file:///Users/ktietz/demo/mc3/conda-bld/tblib_1629402031467/work
', 'tenacity', 'termcolor', 'terminado @ file:///C:/b/abs_25nakickad/croot/terminado_1671751845491/work
', 'text-unidecode @ file:///Users/ktietz/demo/mc3/conda-bld/text-unidecode_1629401354553/work
', 'textblob', 'textdistance @ file:///tmp/build/80754af9/textdistance_1612461398012/work
', 'threadpoolctl @ file:///Users/ktietz/demo/mc3/conda-bld/threadpoolctl_1629802263681/work
', 'three-merge @ file:///tmp/build/80754af9/three-merge_1607553261110/work
', 'tifffile @ file:///tmp/build/80754af9/tifffile_1627275862826/work
', 'tiktoken', 'timeloop', 'tinycss2', 'tkintertable', 'tldextract @ file:///opt/conda/conda-bld/tldextract_1646638314385/work
', 'tokenizers @ file:///C:/ci/tokenizers_1651821358528/work
', 'toml @ file:///tmp/build/80754af9/toml_1616166611790/work
', 'tomli @ file:///C:/Windows/TEMP/abs_ac109f85-a7b3-4b4d-bcfd-52622eceddf0hy332ojo/croots/recipe/tomli_1657175513137/work
', 'tomlkit @ file:///C:/Windows/TEMP/abs_3296qo9v6b/croots/recipe/tomlkit_1658946894808/work
', 'toolz @ file:///C:/b/abs_cfvk6rc40d/croot/toolz_1667464080130/work
', 'torch', 'torchvision', 'tornado @ file:///C:/ci_310/tornado_1642093111997/work
', 'tqdm @ file:///C:/b/abs_0axbz66qik/croots/recipe/tqdm_1664392691071/work
', 'traitlets @ file:///C:/b/abs_e5m_xjjl94/croot/traitlets_1671143896266/work
', 'transformers @ file:///C:/b/abs_8byf5_j714/croot/transformers_1667919454001/work
', 'Twisted @ file:///C:/Windows/Temp/abs_ccblv2rzfa/croots/recipe/twisted_1659592764512/work
', 'twisted-iocpsupport @ file:///C:/ci/twisted-iocpsupport_1646817083730/work
', 'typing-inspect', 'typing_extensions', 'tzdata', 'tzlocal', 'uc-micro-py', 'ujson @ file:///C:/ci/ujson_1657525893897/work
', 'Unidecode @ file:///tmp/build/80754af9/unidecode_1614712377438/work
', 'uritools', 'urllib3 @ file:///C:/b/abs_9bcwxczrvm/croot/urllib3_1673575521331/work
', 'utils', 'uvicorn', 'validators', 'w3lib @ file:///Users/ktietz/demo/mc3/conda-bld/w3lib_1629359764703/work
', 'watchdog @ file:///C:/ci_310/watchdog_1642113443984/work
', 'wcwidth @ file:///Users/ktietz/demo/mc3/conda-bld/wcwidth_1629357192024/work
', 'weasyprint', 'webencodings', 'websocket-client @ file:///C:/ci_310/websocket-client_1642093970919/work
', 'websockets', 'Werkzeug @ file:///C:/b/abs_17q5kgb8bo/croot/werkzeug_1671216014857/work
', 'whatthepatch @ file:///C:/Users/BUILDE~1/AppData/Local/Temp/abs_e7bihs8grh/croots/recipe/whatthepatch_1661796085215/work
', 'whichcraft', 'widgetsnbextension @ file:///C:/ci/widgetsnbextension_1645009839917/work
', 'win-inet-pton @ file:///C:/ci_310/win_inet_pton_1642658466512/work
', 'wincertstore', 'wrapt @ file:///C:/Windows/Temp/abs_7c3dd407-1390-477a-b542-fd15df6a24085_diwiza/croots/recipe/wrapt_1657814452175/work
', 'xarray @ file:///C:/b/abs_2fi_umrauo/croot/xarray_1668776806973/work
', 'xhtml2pdf', 'XlsxWriter', 'xlwings @ file:///C:/b/abs_1ejhh6s00l/croot/xlwings_1677024180629/work
', 'yapf @ file:///tmp/build/80754af9/yapf_1615749224965/work
', 'yarl', 'zict', 'zipp @ file:///C:/b/abs_b9jfdr908q/croot/zipp_1672387552360/work
', 'zope.event', 'zope.interface @ file:///C:/ci_310/zope.interface_1642113633904/work
', 'zopfli', 'zstandard'],

    hiddenimports=[],

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
