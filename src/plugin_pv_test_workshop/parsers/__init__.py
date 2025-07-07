from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from plugin_pv_test_workshop.parsers.parser import NewParser

        return NewParser(**self.model_dump())


class FAIRmatTESTExperimentParserEntryPoint(ParserEntryPoint):

    def load(self):
        from plugin_pv_test_workshop.parsers.FAIRmatTEST_batch_parser import FAIRmatTESTExperimentParser

        return FAIRmatTESTExperimentParser(**self.model_dump())


class FAIRmatTESTParserEntryPoint(ParserEntryPoint):

    def load(self):
        from plugin_pv_test_workshop.parsers.FAIRmatTEST_measurement_parser import FAIRmatTESTParser

        return FAIRmatTESTParser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


FAIRmatTEST_experiment_parser_entry_point = FAIRmatTESTExperimentParserEntryPoint(
    name='FAIRmatTESTExperimentParserEntryPoint',
    description='FAIRmatTEST experiment parser entry point configuration.',
    mainfile_name_re='^(.+\.xlsx)$',
    mainfile_mime_re='(application|text|image)/.*',
)


FAIRmatTEST_parser_entry_point = FAIRmatTESTParserEntryPoint(
    name='FAIRmatTESTParserEntryPoint',
    description='FAIRmatTEST parser entry point configuration.',
    mainfile_name_re='^.+\.?.+\.((eqe|jv|mppt)\..{1,4})$',
    mainfile_mime_re='(application|text|image)/.*',
)
