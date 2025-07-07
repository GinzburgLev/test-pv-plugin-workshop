from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from plugin_pv_test_workshop.schema_packages.schema_package import m_package

        return m_package


class FAIRmatTESTPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from plugin_pv_test_workshop.schema_packages.FAIRmatTEST_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)


FAIRmatTEST_schema_package_entry_point = FAIRmatTESTPackageEntryPoint(
    name='FAIRmatTESTPackage',
    description='FAIRmatTEST package entry point configuration.',
)
