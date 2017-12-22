import xml.dom.minidom as md
from metadata import Schema, Constraint, Domain, Field, Index, Table

def xml_to_ram(xml):
    schema = Schema()
    for attr_name, attr_value in xml.documentElement.attributes.items():
        if attr_name.lower() == "fulltext_engine":
            schema.fulltext_engine = attr_value
        if attr_name.lower() == "version":
            schema.version = attr_value
        if attr_name.lower() == "name":
            schema.name = attr_value
        if attr_name.lower() == "description":
            schema.description = attr_value
    schema.domains = getDomains(xml)
    schema.tables = getTables(xml)
    return schema

def getDomains(xml):
    domains = []
    for xmlDomain in xml.getElementsByTagName("domain"):
        domain = Domain()
        for attr_name, attr_value in xmlDomain.attributes.items():
            if attr_name.lower() == "name":
                domain.name = attr_value
            elif attr_name.lower() == "description":
                domain.description = attr_value
            elif attr_name.lower() == "type":
                domain.type = attr_value
            elif attr_name.lower() == "align":
                domain.align = attr_value
            elif attr_name.lower() == "width":
                domain.width = attr_value
            elif attr_name.lower() == "precision":
                domain.precision = attr_value
            elif attr_name.lower() == "props":
                for prop in attr_value.split(", "):
                    if prop == "show_null":
                        domain.show_null = True
                    elif prop == "summable":
                        domain.summable = True
                    elif prop == "case_sensitive":
                        domain.case_sensitive = True
                    elif prop == "show_lead_nulls":
                        domain.show_lead_nulls = True
                    elif prop == "thousands_separator":
                        domain.thousands_separator = True
                    else:
                        raise ValueError("Invalid format of props string: {}".format(attr_value))
            elif attr_name.lower() == "char_length":
                domain.char_length = attr_value
            elif attr_name.lower() == "length":
                domain.length = attr_value
            elif attr_name.lower() == "scale":
                domain.scale = attr_value
            else:
                raise ValueError("In tag \"{}\" Invalid attribute name \"{}\"".format(domain, attr_name))
        domains.append(domain)
    return domains

def getTables(xml):
    tables = []
    for xml_table in xml.getElementsByTagName("table"):
        table = Table()
        for attr_name, attr_value in xml_table.attributes.items():

            if attr_name.lower() == "name":
                table.name = attr_value
            elif attr_name.lower() == "description":
                table.description = attr_value
            elif attr_name.lower() == "props":
                for prop in attr_value.split(", "):
                    if prop == "add":
                        table.add = True
                    elif prop == "edit":
                        table.edit = True
                    elif prop == "delete":
                        table.delete = True
                    else:
                        raise ValueError("Invalid format of props string in domains: {}".format(attr_value))
            else:
                raise ValueError("In tag \"{}\" Invalid attribute name in domains \"{}\"".format(table, attr_name))

        table.fields = GetFields(xml_table)
        table.constraints = GetConstraints(xml_table)
        table.indexes = GetIndexes(xml_table)

        tables.append(table)
    return tables

def GetFields(xml):
    fields = []
    for xml_field in xml.getElementsByTagName("field"):
        field = Field()
        for attr_name, attr_value in xml_field.attributes.items():
            if attr_name.lower() == "name":
                field.name = attr_value
            elif attr_name.lower() == "rname":
                field.rname = attr_value
            elif attr_name.lower() == "domain":
                field.domain = attr_value
            elif attr_name.lower() == "description":
                field.description = attr_value
            elif attr_name.lower() == "props":
                for prop in attr_value.split(", "):
                    if prop == "input":
                        field.input = True
                    elif prop == "edit":
                        field.edit = True
                    elif prop == "show_in_grid":
                        field.show_in_grid = True
                    elif prop == "show_in_details":
                        field.show_in_details = True
                    elif prop == "is_mean":
                        field.is_mean = True
                    elif prop == "autocalculated":
                        field.autocalculated = True
                    elif prop == "required":
                        field.required = True
                    else:
                        raise ValueError("Invalid format of props string in constraints: {}".format(attr_value))
            else:
                raise ValueError("In tag \"{}\" Invalid attribute name \"{}\"".format(field, attr_name))
        fields.append(field)
    return fields

def GetConstraints(xml):
    constraints = []
    for xml_constraint in xml.getElementsByTagName("constraint"):
        constraint = Constraint()
        for attr_name, attr_value in xml_constraint.attributes.items():

            if attr_name.lower() == "name":
                constraint.name = attr_value
            elif attr_name.lower() == "kind":
                constraint.kind = attr_value
            elif attr_name.lower() == "items":
                constraint.items = attr_value
            elif attr_name.lower() == "reference_type":
                constraint.reference_type = attr_value
            elif attr_name.lower() == "reference":
                constraint.reference = attr_value
            elif attr_name.lower() == "props":
                for prop in attr_value.split(", "):
                    if prop == "has_value_edit":
                        constraint.has_value_edit = True
                    elif prop == "cascading_delete":
                        constraint.cascading_delete = True
                    elif prop == "full_cascading_delete":
                        constraint.full_cascading_delete = True
                    else:
                        raise ValueError("Invalid format of props string in constraints: {}".format(attr_value))
            else:
                raise ValueError("In tag \"{}\" Invalid attribute name\"{}\"".format(constraint, attr_name))
        constraints.append(constraint)
    return constraints

def GetIndexes(xml):
    indexes = []
    for xml_index in xml.getElementsByTagName("index"):
        index = Index()
        for attr_name, attr_value in xml_index.attributes.items():
            if attr_name.lower() == "name":
                index.name = attr_value
            elif attr_name.lower() == "field":
                index.fields = attr_value
            elif attr_name.lower() == "props":
                for prop in attr_value.split(", "):
                    if prop == "fulltext":
                        index.fulltext = True
                    elif prop == "uniqueness":
                        index.uniqueness = True
                    else:
                        raise ValueError("Invalid format of props string in indexes: {}".format(attr_value))
            else:
                raise ValueError("In tag \"{}\" Invalid attribute name in indexes\"{}\"".format(index, attr_name))
        indexes.append(index)
    return indexes