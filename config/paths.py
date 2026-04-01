from chincheron_util import file_util

ROOT = file_util.find_repository_root()

DATA = ROOT / "data"
DATA_RAW = DATA / "raw"
DATA_INTERIM = DATA / "interim"
DATA_PIPELINE = DATA / "pipeline"
DATA_FINAL = DATA / "final"

RESULTS = ROOT / "results"
RESULTS_FIGURES = RESULTS / "figures"
RESULTS_TABLES = RESULTS / "tables"
RESULTS_PUBLICATIONS = RESULTS / "publications"

SCRIPTS = ROOT / "scripts/"

DOC = ROOT / "doc"

SRC = ROOT / "src"