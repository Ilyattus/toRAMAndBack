class Schema:
    def __init__(self):
        self.fulltext_engine = None
        self.version = None
        self.name = None
        self.description = None
        self.domains = []
        self.tables = []

class Domain:
    def __init__(self):
        self.name = None
        self.description = None
        self.type = None
        self.align = None
        self.width = None
        self.precision = None
        self.show_null = False
        self.summable = False
        self.case_sensitive = False
        self.show_lead_nulls = False
        self.thousands_separator = False
        self.char_length = None
        self.length = None
        self.scale = None

class Table:
    def __init__(self):
        self.name = None
        self.description = None
        self.add = False
        self.edit = False
        self.delete = False
        self.fields = []
        self.constraints = []
        self.indexes = []

class Field:
    def __init__(self):
        self.name = None
        self.rname = None
        self.domain = None
        self.description = None
        self.input = False
        self.edit = False
        self.show_in_grid = False
        self.show_in_details = False
        self.is_mean = False
        self.autocalculated = False
        self.required = False

class Constraint:
    def __init__(self):
        self.name = None
        self.kind = None
        self.items = None
        self.reference_type = None
        self.reference = None
        self.has_value_edit = False
        self.cascading_delete = False
        self.full_cascading_delete = False

class Index:
    def __init__(self):
        self.name = None
        self.fulltext = False
        self.uniqueness = False
        self.fields = []

